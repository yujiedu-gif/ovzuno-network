---
title: "Certik smart contract audit: scope, findings, and limitations"
description: "Learn what a certik smart contract audit can examine, how to interpret reported findings, and why audit scope and remediation do not guarantee security."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["smart contract security audit", "audit findings", "audit report"]
author: "editorial_team"
primary_keyword: "certik smart contract audit"
owned_question: "What does a CertiK smart contract audit assess, and what can its report establish—and not establish—about a contract’s security?"
risk_level: "high"
---

A CertiK smart contract audit report can establish what a particular review examined and what findings it recorded, but only within the report’s documented scope. To interpret it, match the reviewed code and exclusions to the report, then check how findings and any claimed fixes are documented. The report is evidence about a bounded review—not proof that a contract or broader application is secure in every condition.

## What a smart contract audit examines

An audit is a review of specified code and materials, not an all-purpose assessment of every component connected to a project. The practical question is not just whether a report exists, but which contract, code version, and functions it covers. A report cannot establish more than its stated scope and the evidence it records.

On Ethereum, participating blockchain nodes must derive the same result when a smart contract executes, and the execution result is recorded on the blockchain. This deterministic behavior makes the contract’s code and state central to understanding what it does. But that does not mean a review of code automatically covers every dependency, input, or circumstance that can affect the application’s behavior.

For example, an Ethereum smart contract cannot directly obtain off-chain facts that are not already in deterministic blockchain state without an oracle or transaction mechanism. When reading an audit report, check whether relevant external inputs and connected components are within scope. If the report does not say that they were assessed, do not infer that they were.

A code review should also be distinguished from an assessment of the wider system. A report may focus on specified contracts without establishing the security of interfaces, operational processes, deployment arrangements, or economic design. Those boundaries are defined by the report’s scope and exclusions, not by a generic assumption about what every audit covers.

## How to read a CertiK audit report

Start with the report’s identity and boundaries. Locate the contract names and addresses, reviewed version or commit, review date, stated scope, and exclusions. Compare those details with the project’s corresponding source code. If the report does not identify the reviewed code clearly enough to match, the connection between the report and the code currently in use is uncertain. Do not assume they are identical.

Read each finding in context. Pay attention to the behavior described, the affected component, the supporting explanation, and any recommended action. If the report uses severity labels, treat them as the report’s categorization of recorded findings. A label does not independently establish that every significant problem was found, or that risks outside the reviewed scope were addressed. Use the report’s own definitions rather than importing assumptions about a provider’s terminology or methodology.

Look for the project’s response and the documented status of each finding. A recommendation is not evidence that an action was taken. A claim that an issue was fixed is not, by itself, evidence that the change was reviewed again. Check whether primary materials connect the change to a specific code version and whether the report or another documented review covers that version.

If the report describes follow-up work, identify precisely what it covers. A follow-up review of a change does not necessarily establish that unrelated code, integrations, or deployment conditions were assessed. Keep the conclusion as narrow as the evidence: which finding, which change, and which reviewed version?

## Findings, fixes, and unresolved risk

A finding records an issue identified during a particular review. A recommendation proposes an action; it does not prove completion. An exclusion or stated limitation marks an area for which the report does not establish coverage. Separating these categories helps prevent a short summary from obscuring unresolved findings or unreviewed areas.

When a project says an issue was fixed, connect that claim to the relevant code and report evidence. Check whether the change appears in the version identified by the project, whether the documented change addresses the described behavior, and whether a follow-up review is recorded for that version. If the materials do not support one of those links, describe the gap rather than treating remediation as confirmed.

Even a documented fix should be understood within its context. It establishes, at most, that the particular change and review are documented; it does not prove that no other issues remain. A new code version, an additional integration, or a different deployment configuration may introduce behavior not represented in the earlier review. The earlier report should not be assumed to cover those changes unless the documentation shows that it does.

This distinction also applies to dependencies. A contract can rely on other contracts or external information mechanisms. If such components are outside the stated scope, the audit report does not establish their security merely because they interact with reviewed code. The reader’s task is to map each conclusion to the component and version actually covered.

## What an audit does not guarantee

An audit is bounded by its scope, methods, timing, and available information. It can document findings in the materials reviewed, but it cannot prove that no vulnerabilities exist. A report with no listed findings is therefore not proof of absence, and its result should not be generalized beyond the covered code and conditions.

Nor does an audit report by itself establish ongoing security, operational reliability, regulatory compliance, or suitability for use. Those are broader conclusions than a bounded code review supports. The report should not be treated as an endorsement of a project or as an investment signal. Its value as evidence is limited to the review and findings it documents.

A report also does not automatically extend to later changes or to components that were excluded. If the project’s deployed code differs from the reviewed version, or if the application depends on systems not named in scope, the reader needs separate evidence to assess those differences. The report alone cannot fill those gaps.

## Evidence to verify before relying on a report

Use primary materials: the audit report and the project’s source code corresponding to the reviewed version. Check that the report identifies its scope, date, exclusions, findings, and any follow-up review. Compare those details with the code version the project says is relevant. If the available materials do not make the connection clear, the report’s applicability remains uncertain.

For each finding, look for a documented status and evidence of the corresponding change. Confirm whether a follow-up review is recorded and which version it covers. Do not infer that an unmentioned issue was tested, that a claimed fix was independently confirmed, or that a later version inherits the earlier review’s coverage.

Keep conclusions proportional to the evidence. A report can support statements about the work and findings it documents. It cannot, on its own, establish complete or continuing security, and it does not turn a bounded review into a general endorsement. For developers and project operators, that scope check is the practical basis for using an audit report responsibly.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
