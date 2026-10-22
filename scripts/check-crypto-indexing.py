#!/usr/bin/env python3
"""Fail the site build if a Crypto article cannot be submitted for indexing."""

import json
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "sites/crypto/content/articles"
OUTPUT = ROOT / "dist/crypto"
BASE_URL = "https://crypto.ovzuno.com"


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.canonicals = []
        self.robots = []
        self.json_ld = []
        self._capture = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._capture = "title"
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self._capture = "script"
            self.json_ld.append("")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        elif tag == "meta":
            name = attrs.get("name", "").lower()
            if name == "description":
                self.description = attrs.get("content", "")
            elif name in {"robots", "googlebot"}:
                self.robots.append(attrs.get("content", ""))

    def handle_data(self, data):
        if self._capture == "title":
            self.title += data
        elif self._capture == "script":
            self.json_ld[-1] += data

    def handle_endtag(self, tag):
        if tag == self._capture:
            self._capture = None


def check():
    article_files = sorted(CONTENT.glob("*.md"))
    article_files = [path for path in article_files if path.name != "_index.md"]
    assert article_files, "Crypto article content is empty"
    sitemap = OUTPUT / "sitemap.xml"
    assert sitemap.is_file(), "Crypto sitemap is missing"
    assert sitemap.stat().st_size <= 50_000_000, "Crypto sitemap exceeds 50 MB"
    root = ElementTree.parse(sitemap).getroot()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text for node in root.findall("s:url/s:loc", namespace)]
    assert len(urls) <= 50_000, "Crypto sitemap exceeds 50,000 URLs"
    assert len(urls) == len(set(urls)), "Crypto sitemap contains duplicate URLs"
    dated_urls = {
        node.findtext("s:loc", namespaces=namespace): node.findtext("s:lastmod", namespaces=namespace)
        for node in root.findall("s:url", namespace)
        if node.find("s:lastmod", namespace) is not None
    }
    assert dated_urls == {f"{BASE_URL}/": "2026-10-22"}, (
        "Crypto sitemap must expose lastmod only for the updated homepage"
    )
    urls = set(urls)

    robots = (OUTPUT / "robots.txt").read_text()
    assert "Sitemap: https://crypto.ovzuno.com/sitemap.xml" in robots
    assert "Disallow:" not in robots, "Crypto robots.txt blocks crawling"
    headers = (OUTPUT / "_headers").read_text().lower()
    assert "x-robots-tag" not in headers, "Crypto response headers contain an indexing rule"
    homepage = (OUTPUT / "index.html").read_text()
    assert 'google-site-verification content="b7r3vC-jyKOhULZ_WRnsqyVdkwN0JgSI10dtLTYw248"' in homepage, (
        "Crypto homepage is missing its Search Console verification tag"
    )

    for source in article_files:
        slug = source.stem
        expected_url = f"{BASE_URL}/articles/{slug}/"
        raw = source.read_text()
        assert "noindex: true" not in raw, f"{slug}: page-level noindex"
        assert "sitemap: {disable: true}" not in raw, f"{slug}: excluded from sitemap"
        assert expected_url in urls, f"{slug}: absent from sitemap"
        page = OUTPUT / "articles" / slug / "index.html"
        assert page.is_file(), f"{slug}: rendered page missing"
        head = Head()
        head.feed(page.read_text())
        assert head.title.strip(), f"{slug}: title missing"
        assert head.description.strip(), f"{slug}: description missing"
        assert head.canonicals == [expected_url], f"{slug}: canonical mismatch"
        assert not any("noindex" in rule.lower() for rule in head.robots), f"{slug}: robots noindex"
        assert len(head.json_ld) == 1, f"{slug}: expected one JSON-LD block"
        graph = json.loads(head.json_ld[0])["@graph"]
        articles = [node for node in graph if node.get("@type") == "Article"]
        assert len(articles) == 1, f"{slug}: missing Article structured data"
        article = articles[0]
        assert article.get("url") == expected_url, f"{slug}: structured-data URL mismatch"
        assert article.get("headline") and article.get("datePublished") and article.get("author"), (
            f"{slug}: incomplete Article structured data"
        )

    for path, page_type in (("", "WebPage"), ("topics/", "CollectionPage"), ("about/", "AboutPage")):
        url = f"{BASE_URL}/{path}"
        page = OUTPUT / path / "index.html"
        assert page.is_file(), f"{path or 'home'}: rendered page missing"
        html = page.read_text()
        head = Head()
        head.feed(html)
        assert head.canonicals == [url], f"{path or 'home'}: canonical mismatch"
        assert not any("noindex" in rule.lower() for rule in head.robots), f"{path or 'home'}: robots noindex"
        assert len(head.json_ld) == 1, f"{path or 'home'}: expected one JSON-LD block"
        graph = json.loads(head.json_ld[0])["@graph"]
        pages = [node for node in graph if node.get("@type") == page_type]
        assert len(pages) == 1 and pages[0].get("url") == url, (
            f"{path or 'home'}: missing {page_type} structured data"
        )
        if path == "topics/":
            assert f"{len(article_files)} published articles" in html, "Topics article count is stale"
        if path == "about/":
            assert "first editorial collection is in development" not in html
            assert "not yet intended for search indexing" not in html

    print(f"Crypto indexing checks passed: {len(article_files)} articles and three publication pages.")


if __name__ == "__main__":
    check()
