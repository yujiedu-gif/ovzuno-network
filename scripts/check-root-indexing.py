#!/usr/bin/env python3
"""Check that every public OvZuno main-site page is indexable."""

from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "sites/root/content"
OUTPUT = ROOT / "dist/root"
BASE = "https://ovzuno.com"


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.robots = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag == "meta" and attrs.get("name", "").lower() in {"robots", "googlebot"}:
            self.robots.append(attrs.get("content", ""))


def check():
    pages = sorted(CONTENT.rglob("*.md"))
    assert len(pages) == 9, f"Expected 9 main-site pages, found {len(pages)}"
    expected = {f"{BASE}/" if page.name == "_index.md" else f"{BASE}/{page.parent.name}/" for page in pages}

    sitemap = OUTPUT / "sitemap.xml"
    assert sitemap.is_file(), "Main-site sitemap is missing"
    root = ElementTree.parse(sitemap).getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries = root.findall("s:url", ns)
    urls = [entry.findtext("s:loc", namespaces=ns) for entry in entries]
    assert len(urls) == len(set(urls)), "Main-site sitemap contains duplicate URLs"
    assert set(urls) == expected, "Main-site sitemap does not match the 9 public pages"
    assert not root.findall("s:url/s:lastmod", ns), "Main-site sitemap has unverified lastmod values"

    headers = (OUTPUT / "_headers").read_text().lower()
    assert "x-robots-tag" not in headers, "Main-site response headers contain an indexing rule"
    for url in expected:
        path = OUTPUT / url.removeprefix(f"{BASE}/") / "index.html"
        assert path.is_file(), f"Missing rendered page: {url}"
        head = Head()
        head.feed(path.read_text())
        assert head.canonicals == [url], f"Canonical mismatch: {url}"
        assert not any("noindex" in rule.lower() for rule in head.robots), f"Noindex page: {url}"

    print("Main-site indexing checks passed: 9 public pages.")


if __name__ == "__main__":
    check()
