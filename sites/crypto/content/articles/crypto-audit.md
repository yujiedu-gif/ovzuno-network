---
title: "Crypto audit: scope, findings, and limitations"
description: "Learn what a crypto audit of smart contracts and dApps may examine, how to interpret reported findings, and why an audit cannot eliminate every risk."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["smart contract audit", "audit scope", "audit report", "audit findings"]
author: "editorial_team"
primary_keyword: "crypto audit"
owned_question: "What does a crypto audit of a smart contract or dApp examine, how should its findings be interpreted, and what limitations remain?"
risk_level: "medium"
---

A crypto audit is a review of specified smart-contract or decentralized-application (dApp) components, not a universal certification that a system is secure. To understand what an audit establishes, check which code and assumptions were in scope, what the report says about its work, and whether findings were addressed with evidence. Risks outside the review—including later changes and operational dependencies—remain separate questions.

## What a crypto audit means for smart contracts and dApps

A smart-contract audit, as used here, means a scoped examination of code and related system components. The word “audit” alone does not identify a uniform method, depth, or set of deliverables. The report and its scope define what was actually reviewed; do not infer that an entire dApp was covered just because its name appears in a report.

A dApp may include on-chain code and other components or dependencies. A review limited to particular contracts cannot by itself establish that every connected service, governance process, operational practice, or legal arrangement was examined. Treat each as a separate area unless the audit documentation explicitly includes it.

A maturity label or framework is not a substitute for review evidence. For example, the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization; it is not a complete security score. A label of this kind does not show that a particular contract or application is free of vulnerabilities. (claim_stages_not_security_score)

The term “audit” also does not mean that the reviewer issued a guarantee. Its useful meaning is bounded by the documented subject, methods, assumptions, and limitations. If the available documentation does not explain those boundaries, the reader cannot confidently determine what conclusions the review supports.

## How audit scope shapes what gets examined

Scope sets the boundaries of a review. Look for the identified contracts or other components, the code version or revision, assumptions on which the review depends, and explicit exclusions. Compare these boundaries with the system under consideration. If an integration or operational component is not listed, the report does not establish that it was reviewed.

Version matching matters. A report about one revision does not automatically apply to changed code. The report should identify the material examined, and the deployed code should be checked against that material. A change made after the review creates a gap unless the relevant change was assessed. The report’s existence is not evidence that every later modification was examined.

Do not assume an audit method from the word itself. Review the documentation for the methods it says were used and the limitations it states. If those details are absent or unclear, the documentation does not support a claim about the review’s depth. That is a limit on what can be concluded; it is not evidence that any particular method was or was not performed.

Scope includes assumptions and dependencies as well as code boundaries. A system may rely on components or processes outside the reviewed material. A finding about one component does not automatically establish the behavior or safety of an integration that was not assessed. Where the report refers to external assumptions, keep those assumptions attached to its conclusions rather than treating them as independently verified facts.

The same principle applies to specialized systems. A validity rollup, for example, updates canonical state after a base-layer verifier accepts a cryptographic validity proof for a proposed off-chain state transition. That mechanism describes one part of a system; it does not establish that a particular implementation, verifier, governance arrangement, or other dependency was covered by an audit. (claim_validity_proof)

## How to read an audit report and its findings

Start with the report’s scope, date, methods, and stated limitations. These details help answer what was reviewed and under what described conditions. Read findings in that context rather than treating a summary or headline as a certificate for the whole system.

Interpret severity terms and recommendations using the definitions in that report. The available evidence does not establish a universal severity scale, so labels from different reports should not be assumed to be directly comparable. A category communicates the report’s classification; by itself, it does not prove the likelihood or consequence of an issue in every deployment.

Next, inspect the status assigned to each finding. Reports may distinguish matters marked as fixed, accepted, unresolved, or outside scope, but the report’s terminology controls. A statement that an issue was fixed is a claim to verify, not a substitute for evidence connecting the change to the relevant reviewed or deployed code. An unresolved or accepted finding should not be silently treated as resolved.

Look for the basis of any remediation claim. A report may document a later review or other evidence, but do not infer that a correction was independently checked unless the documentation says so. If the status or supporting evidence is unclear, record it as unclear rather than assuming a favorable result. Remediation status is a separate question from whether the original review found an issue.

A report is also not an integrity guarantee. A cryptographic digest can support integrity verification only relative to a trusted digest and verification procedure; it does not establish the correctness or completeness of the underlying review. (claim_digest_external_trust) The relevant question is what evidence the report supplies for its conclusions and whether that evidence covers the version and components at issue.

## What an audit cannot establish on its own

An audit cannot prove that software has no vulnerabilities or guarantee future security. A scoped review supports conclusions only about the material and conditions it describes. It cannot establish conclusions about code changed later or components outside its scope.

Operational practices, dependencies, and governance may affect system behavior, and later code changes may alter the system that was reviewed. Do not extend a report to those areas unless it explicitly covers them. For proxy-based upgradeable contracts, initializer discipline and compatible storage layout across implementations are requirements to consider; an audit of an earlier implementation alone does not establish that later upgrades meet them. (claim_upgrade_constraints)

A review of a privacy application also has a limited evidentiary meaning. A zero-knowledge privacy application can separate private witness data and off-chain proof generation from a public commitment and an on-chain verifier that checks the proof. This architectural pattern does not, by itself, establish that a particular proof system, verifier, setup, data-availability arrangement, or implementation was reviewed or works as intended. (claim_private_proof_public_verify)

An audit report alone does not establish legal or regulatory compliance, and it does not guarantee recovery of lost assets. Those questions require separate, relevant evidence. Claims about fees, yields, availability, or tax consequences likewise cannot be inferred from a code review. This explanation makes no determination about such outcomes.

## Questions to resolve before relying on an audit

Before relying on an audit, check whether the reviewed code corresponds to what is deployed and whether material changes have been accounted for. Identify components, assumptions, and integrations that the report excludes. Confirm that the methods and limitations are described clearly enough to understand what the findings cover. If the report does not identify the reviewed material sufficiently, the relationship between its conclusions and the deployed system remains uncertain.

For each reported issue, establish its status using the report’s definitions. Look for evidence supporting claims that it was corrected, and determine whether that evidence addresses the relevant code and deployment. If the report does not document the basis for remediation, treat remediation as unconfirmed rather than complete. An issue marked outside scope should remain an open question, not be counted as a finding that the review resolved.

Then separate the report’s conclusions from other assurances. Security claims require evidence relevant to the current system and its dependencies. Claims about recovery, compliance, jurisdictional applicability, availability, fees, yields, and tax consequences require their own applicable evidence; an audit alone does not settle them. A report can inform those inquiries only to the extent its documented scope supports them.

The practical conclusion is narrow but useful: an audit tells readers what a stated review examined and what it reported, subject to its limitations. It does not automatically cover the full dApp, confirm every remediation, or remove residual risk. Where documentation leaves a gap, the accurate response is to identify that gap and seek evidence relevant to it rather than treating the audit label as a guarantee.

## Sources and references

- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Digest management - SQL Server](https://learn.microsoft.com/en-us/SQL/relational-databases/security/ledger/ledger-digest-management?view=sql-server-ver16) — Microsoft Learn; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
