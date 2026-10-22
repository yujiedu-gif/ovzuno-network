---
title: "near smart contract audit: scope, findings, and limitations"
description: "Learn what a near smart contract audit may examine, how to interpret findings and scope, and why an audit is not a guarantee of security."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "near smart contract audit"
owned_question: "What does a security audit of a smart contract on NEAR examine, and what can an audit report establish or leave unresolved?"
risk_level: "medium"
---

A NEAR smart contract audit is a bounded review of specified code and assumptions, not a certification that a contract or application is secure. To understand what an audit report supports, check what was examined, which code version it covered, what findings remain unresolved, and what was explicitly excluded. The evidence available here does not establish a NEAR-specific audit methodology or runtime checklist, so the discussion below stays at the level of general report interpretation and clearly bounded security concepts.

## What a NEAR smart contract audit covers

An audit report can support conclusions only about the scope it describes. The reviewed subject might be contract code, selected components, or a broader system; readers should not assume that a contract review also assessed a user interface, external service, operational control, or every dependency. The report’s scope and exclusions determine which of those areas were actually examined.

The audit label does not define a universal method. A report should be read as evidence about a particular review, not as proof that every possible vulnerability class was assessed. This limitation matters especially when a system relies on a bridge or oracle: bridge security depends materially on how source-chain events are verified, and oracle connections bring off-chain data or services into contract logic. Whether either component was reviewed must be confirmed in the report rather than inferred from the project description. [source](<https://ethereum.org/developers/docs/bridges>) [source](<https://docs.chain.link/getting-started/conceptual-overview>)

## How reviewers assess contract behavior

A useful review relates the code to its intended behavior: what state it changes, under what conditions, and what permissions or assumptions those changes rely on. But the evidence allowed for this article does not substantiate a specific checklist, test method, or NEAR runtime behavior. Those details should not be presented as mandatory or as necessarily performed in every audit.

Dependencies and upgrade mechanisms can affect the conclusions a reader draws. For example, proxy-based upgradeable contracts require initializer discipline and compatible storage layouts across implementations; this is a specific upgrade pattern, not a statement about all NEAR contracts. If a reviewed system uses an upgrade mechanism, the report’s scope should say whether that mechanism and its assumptions were assessed. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>)

Likewise, an audit of one component does not automatically establish the behavior or security of a separate integration. If the report discusses a bridge, oracle, or other dependency, check what the reviewers actually examined and which external assumptions remain. The existence of an integration in a system diagram is not evidence that it was part of the audit.

## Reading findings and stated scope

Start with the report’s identification of the reviewed code and components. Compare its stated version or revision with the code under consideration. Then read the scope, exclusions, and assumptions together: a conclusion about the inspected component does not extend automatically to omitted components or conditions the reviewers assumed.

Treat severity labels as report-specific unless the report defines a common standard and explains how it applied it. A label is a way to organize findings in that report; it is not, by itself, a universal measure of risk or a guarantee that all issues at that level were found. Similarly, a finding marked as fixed should be distinguished from one that remains unresolved, and remediation claims should be supported by the report or documented follow-up evidence.

Reports can also leave uncertainty visible. A finding may be unresolved, a component may be out of scope, or an assumption may not have been independently verified. Keep those categories separate: an issue identified by reviewers is not the same as a risk they did not assess, and neither should be silently converted into a claim that the system is safe or unsafe overall.

## What an audit cannot establish

An audit report is evidence about a bounded review, not proof that code contains no defects or that it will remain secure after changes. The report’s conclusions cannot be extended to a different code version, deployment, or unreviewed component without additional evidence showing that the relevant material matches.

Nor does an audit label establish the security of connected systems. If a contract depends on an oracle, the application must evaluate the oracle’s data sources, update policy, availability, and trust model. If it depends on a bridge, the verification model and its associated assumptions matter. These dependencies may be outside a contract audit’s scope even when the contract calls them. [source](<https://docs.chain.link/getting-started/conceptual-overview>) [source](<https://ethereum.org/developers/docs/bridges>)

An audit also does not establish a project’s regulatory standing, compliance, or suitability. Those are separate questions and should not be inferred from the existence of a technical report. This article makes no project-specific safety judgment and provides no legal, tax, or compliance conclusion.

## Evidence to verify before relying on a report

Use the report as a record of what was assessed, not as a substitute for checking the underlying evidence. A bounded review of the report can include these questions:

- Does the report identify the reviewed code or revision, and does that match the code under consideration?
- Which contracts, integrations, and other components are expressly in scope? What is excluded?
- What assumptions did reviewers make, and which claims or dependencies were not verified?
- Which findings remain unresolved, and what documented evidence supports any stated remediation?
- Does the report distinguish the assessed components from the broader application or protocol?

When a report discusses an upgradeable component, check whether its scope includes the relevant upgrade and storage-layout assumptions; the requirements described for proxy-based systems are pattern-specific. When it discusses an oracle or bridge, check whether the report identifies the data or event verification model and what assumptions remain. No single audit label answers these questions for every system. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>) [source](<https://docs.chain.link/getting-started/conceptual-overview>) [source](<https://ethereum.org/developers/docs/bridges>)

The L2BEAT Stages Framework offers a separate example of why labels need context: it measures rollup maturity in decentralization and trust minimization, not a complete security score. It is not a NEAR audit standard, and its stages should not be treated as an audit verdict. The broader lesson is to identify what a label measures before relying on it. [source](<https://l2beat.com/stages>)

A NEAR smart contract audit report can establish what reviewers say they examined and what findings they recorded, within its stated scope and assumptions. It can leave unresolved the security of excluded components, unverified dependencies, later code changes, and questions outside technical review. Read the report’s boundaries and evidence directly; do not treat the audit label as a guarantee.

## Sources and references

- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Smart Contract Overview](https://docs.chain.link/getting-started/conceptual-overview) — Chainlink Documentation; retrieved 2026-10-19.
