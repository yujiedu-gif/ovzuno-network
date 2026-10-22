---
title: "Crypto audit companies: scope, methods, and limitations"
description: "Learn what crypto audit companies may review in smart contracts, how to assess an audit’s scope and report, and why an audit is not a security guarantee."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "crypto audit companies"
owned_question: "What do crypto audit companies review in smart contracts, and how can a project assess the scope and limitations of an audit?"
risk_level: "high"
---

Crypto audit companies review a defined set of smart-contract code and related assumptions, then communicate what their engagement found. A report is evidence about that review’s stated scope and timing—not proof that a contract or dApp is secure. To assess one, check exactly what was reviewed, what was excluded, how findings were handled, and whether the reviewed code matches the version in use.

## What crypto audit companies examine

A smart-contract review concerns specified code and the behavior it is intended to implement. The audit’s value as evidence depends on the boundary of that work: a report about particular contracts does not, by itself, establish the security of a broader application or of components outside the reviewed scope. In particular, bridge security depends materially on who or what verifies the source-chain event, and may involve external validators, oracles, connected-chain validators, light clients, or challenge mechanisms. A review of one contract should not be read as an assessment of every part of that verification system. ([source](<https://ethereum.org/developers/docs/bridges>))

The same boundary applies to dependencies and deployment arrangements. A report’s conclusions should be tied to the code and assumptions described in the engagement, not generalized to a whole product, protocol, or future release. Read the scope and exclusions alongside any summary label or overall conclusion.

## How an audit engagement is scoped

Before relying on a report, identify the exact codebase and version it covers. Look for repository or contract identifiers and a commit, release, or other reproducible reference. Then compare that reference with the code the project intends to deploy or currently operates. If the report does not make the reviewed version clear, ask the provider or project to clarify before treating its findings as relevant to that code.

Check which contracts and dependencies are included and which are expressly excluded. Also look for the stated assumptions, review approach, and any testing activities. These details define what the engagement can support; do not infer methods or coverage that the documents do not specify.

Changes after review need separate attention. For proxy-based upgradeable contracts, initializer discipline and compatible storage layout across implementations are necessary to avoid takeover or corrupted state. That is a specific design consideration, not a general claim that every audited contract is upgradeable. If an implementation, initializer, or related deployment configuration changed, ask whether the change was within the reviewed scope and whether it received further review. ([source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>))

## What an audit report can and cannot establish

Treat the report as a record of the work described in it. Read the individual findings, their stated status, and any remediation or verification evidence rather than relying only on an executive summary. A claim that an issue was fixed is stronger when the report or related documentation identifies the change and the follow-up check; if that evidence is absent, ask what was verified and against which version.

A report is not a guarantee that no vulnerability exists. Its conclusions are limited by its scope, assumptions, methods, and the code version it addresses. It also cannot establish that the same conclusions apply after relevant changes. Even a maturity framework should not be mistaken for a comprehensive security score: the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization, not complete security. That distinction illustrates why labels and ratings must be interpreted according to what they actually measure. ([source](<https://l2beat.com/stages>))

## Questions to ask when assessing an audit proposal

Use the proposal and report terms to get concrete answers to questions such as:

- Which repositories, contracts, commit or release, and dependencies are included? Which are excluded?
- What assumptions does the review make about external components, data, permissions, and deployment?
- What review and testing activities are explicitly included, and what are their limits?
- What deliverables will be provided, and how will findings and their status be documented?
- How are code changes during the engagement handled? What changes require additional review?
- What evidence will show that reported remediations were checked against the relevant code version?
- How are reviewer qualifications and potential conflicts disclosed, and what independently verifiable information is available?

Request a sample report structure or documented methodology if useful, but evaluate what the documents actually demonstrate. A polished format, a provider’s description of its process, or an assessment label is not, on its own, evidence that the proposed code and risks received the coverage your project needs.

## Security, recovery, and compliance boundaries

A contract audit does not automatically assess keys, front ends, infrastructure, governance, or operational response. Those are distinct parts of a system, and the proposal should say whether any are included. Similarly, an audit report does not itself provide recovery, insurance, or a remedy for losses. Do not treat the existence of a report as evidence of those protections.

A practical final check is to match three things: the code version in use, the scope recorded in the engagement, and the findings or follow-up evidence in the report. If any link is unclear, seek documentation rather than filling the gap with an assumed guarantee. For claims about regulation, tax, availability, fees, yields, security, recovery, or compliance, require current, jurisdiction-specific evidence; an audit report alone does not establish those matters. This article does not provide legal, tax, or compliance advice.

## Sources and references

- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
