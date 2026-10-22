---
title: "Solidity audit: scope, findings, and limitations"
description: "Learn what a solidity audit can examine, how findings are typically communicated, and why a completed review cannot guarantee that a smart contract is secure."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["smart contract security audit", "Solidity code review"]
author: "editorial_team"
primary_keyword: "solidity audit"
owned_question: "What does a Solidity audit examine, what can its findings establish, and what are its limits?"
risk_level: "high"
---

A Solidity audit is a scoped security review of specified smart-contract code and its assumptions. It can document issues found in the material examined and recommend changes, but it cannot establish that a contract is free of vulnerabilities or that its wider system is secure. To interpret a report, check exactly what code and dependencies it covered, what it excluded, and whether reported issues were addressed.

## What a Solidity audit is meant to assess

A smart contract is code and data deployed on a blockchain. An audit in this context examines contract code for security-relevant behavior within an agreed scope. It is not a general certification of the application, its operators, or every system connected to it. The reviewed code and the stated assumptions define what the conclusions can speak to.

A security review should also be distinguished from other forms of evaluation. Functional testing checks whether selected behavior matches expectations; a security review asks whether behavior or assumptions may create exploitable weaknesses. Formal verification is another distinct method, and legal review addresses questions outside code-security conclusions. These activities may complement one another, but one does not automatically substitute for another.

Even a focused code review may need to consider how contract components interact. Solidity’s checks-effects-interactions pattern, for example, orders logic by validating conditions, recording internal state changes, and only then interacting with external contracts. This reduces a class of reentrancy risk; it does not make arbitrary contract code safe. A report that discusses one pattern or vulnerability class should not be read as assessing every security property. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>)

## How code and threat assumptions shape the review

A review’s conclusions depend on what the reviewers were asked to examine and what information they received. Scope can specify particular contracts, versions, dependencies, or behavior. If a component or assumption is outside that scope, the report cannot be treated as evidence that it was reviewed.

Threat assumptions matter too. A reviewer may need to understand which accounts can change settings or perform privileged actions, how external components are called, and what the contract is expected to do. These questions help define which behaviors count as risks in the system under review. If the expected behavior or trust boundaries are undocumented, a report may be limited in what it can assess.

Review methods can vary. Manual inspection and automated analysis are possible approaches, but the available evidence here does not establish a universal method or required toolset for every audit. Do not infer that a particular technique was used unless the report says so. Likewise, do not assume an audit covered tests, deployed instances, operational practices, or dependencies merely because it reviewed Solidity source code.

Composability—the ability of contracts to call or reuse independent on-chain components through public interfaces—can make a contract’s behavior depend on other code. Each dependency adds behavior, upgrade, permission, availability, and economic assumptions. A report should therefore be read for its treatment of dependencies, not as proof that every component in an application stack was examined. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Changes after review create a separate boundary. Proxy-based upgradeable contracts, for example, require initializer discipline and compatible storage layout across implementations; an upgrade tool does not replace contract-specific review, testing, or governance analysis. A report on one implementation should not be assumed to cover later versions or upgrades unless those are explicitly included. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>)

## How to interpret audit findings

An audit report may describe issues, identify affected components, assign severity, and recommend remediation. The exact report format and severity conventions can differ, so treat the report’s own definitions as controlling. Severity labels are assessments within the report’s stated scope and assumptions, not universal measurements of a contract’s total risk.

A listed finding establishes that the report identified and described an issue in the reviewed material. It does not, by itself, show that a fix was implemented or verified. Look for the finding’s status, the response or remediation evidence, and any follow-up review. If the report does not document those details, the remediation status is not established by the report alone.

A report with no findings—or with findings marked resolved—also has limits. The absence of reported issues means only that no issues were reported under the review conditions; it is not proof that none exist. A maturity framework illustrates this distinction: the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization, rather than providing a complete security score. A framework label and an audit report answer different questions. [source](<https://l2beat.com/stages>)

## Why an audit is not a security guarantee

Review techniques can miss defects. Conclusions are bounded by the code and assumptions examined, the methods used, and the information available. An audit is evidence of a review, not a guarantee against exploitation or a statement that funds or systems are safe.

Risks may also arise outside the reviewed code. Integration behavior, operational controls, changes made after review, and dependencies may not be covered by a particular engagement. Even when a report examines contract logic carefully, that does not establish the safety of every application, wallet, service, or process interacting with it.

For this reason, separate claims should be evaluated separately. An audit of Solidity code does not by itself establish recovery outcomes, fees, yields, or legal or compliance status. Those questions require evidence specific to the relevant system and claim; they should not be inferred from a security report.

## What to confirm before relying on an audit report

Start by matching the report to the code in question. Check the reviewed version or commit, the contract components included, the stated scope, exclusions, and assumptions. If the deployed or currently proposed code differs, the report may not describe that code.

Then examine the findings and their status. Identify which components are affected, what remediation is described, and whether the report documents follow-up. Distinguish a recommendation from evidence that a change was made and checked.

Finally, note what the report does not claim to cover. A useful reading keeps the conclusion narrow: the report documents what its authors examined and found under stated conditions. It does not turn an incomplete scope into a complete assessment, and it does not replace separate evidence for matters outside code security.

## Sources and references

- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
