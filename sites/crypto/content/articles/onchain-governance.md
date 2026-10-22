---
title: "Onchain governance: how proposals become protocol changes"
description: "Learn how onchain governance connects proposals, voting, and execution, and where implementation controls, offchain decisions, and operational risks shape outcomes."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["dao_governance"]
tags: ["on-chain voting", "governance proposal", "smart contract execution"]
author: "editorial_team"
primary_keyword: "onchain governance"
owned_question: "How does onchain governance move a decision from proposal and voting to execution, and what limitations or risks arise at each stage?"
risk_level: "medium"
---

Onchain governance moves a decision from proposal to an outcome recorded or acted on through blockchain transactions and smart contracts, but the exact path depends on each system’s rules. A recorded vote is not, by itself, proof that a change was executed, that every required offchain step occurred, or that the result establishes legal authority. To assess a particular process, follow its documented rules and verify the records for both the vote and any later implementation action.

## What onchain governance records—and what it does not

Onchain governance is a process in which some decision-related activity—such as a vote or an authorized contract action—is represented in blockchain records. A smart contract is code executed under a network’s rules. Participating blockchain nodes are expected to derive the same execution result, which is then recorded on the blockchain; the exact node set and consensus rules depend on the network. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

This description covers only the onchain portion. Discussion, proposal drafting, technical review, delegation, and coordination may occur outside the blockchain, or may be represented differently in different systems. A vote record therefore documents a particular onchain action under the system’s rules; it does not automatically capture all deliberation or establish that offchain procedures were completed.

Nor does a record alone prove that an approved change took effect. Some systems make a contract action follow a vote; others require a separate transaction or an operator’s action. The available evidence here does not specify a universal governance workflow, nor does it establish who has legal authority in any particular organization. Treat those as system- and context-specific questions.

## Onchain governance from proposal to execution

A useful way to trace a decision is to separate it into three stages: submission, decision, and implementation. The labels are a framework for examining a system, not a universal set of protocol rules.

**Submission.** Start with the proposal as recorded or described by the system. Check what the system’s own documentation says about who can submit, what information is required, and when a proposal becomes eligible for consideration. Do not assume that one system’s submission conditions apply elsewhere. If discussion or review occurs offchain, identify that separately from any proposal transaction or contract record.

**Decision.** Next, determine how the system records and evaluates votes. Review the documented voting period and the rules that define the outcome, rather than treating a displayed tally as self-explanatory. The evidence available for this article does not establish particular thresholds, quorum requirements, eligibility rules, or voting periods; these must be checked in the specific system’s current documentation and records.

**Implementation.** Finally, look for the action that carries the decision into effect. It may be a contract execution or another authorized transaction, or it may depend on a designated operator. A vote and an implementation action are distinct events unless the system’s documented mechanism connects them. Confirm whether there is a later transaction or other recorded execution step before describing a proposal as implemented.

This stage-by-stage view helps avoid a common interpretive error: treating approval as equivalent to execution. It also keeps the roles clear. The governance process records or determines an outcome according to its rules; the blockchain network processes valid transactions under its rules; and any separate operator or offchain participant performs responsibilities assigned to them by the particular arrangement.

## Voting and implementation mechanisms vary

Governance designs differ in how they connect a vote to an action. Some make contract execution part of the onchain process; others may record a preference or outcome that requires a later implementation step. Without primary documentation for a particular system, it is not safe to assume which model applies, or that a vote automatically triggers a change.

Participation rights can also be organized differently. Blockchain systems may be permissionless, with participation in block publication open, or permissioned, with authorized users maintaining the ledger; access to reading or submitting transactions can also be restricted. Real systems may combine open transaction submission with restricted validation or other controls. [source](<https://csrc.nist.gov/pubs/ir/8202/final>) This distinction concerns network participation, not a universal description of who may vote in a governance process. Check governance rules separately from network-access rules.

Thresholds, quorum, delegation, delays, and veto or emergency controls are likewise questions for system-specific documentation. Do not infer their existence or effect from the fact that a process is described as “onchain.” For an implementation that uses a contract, inspect the documented mechanism and the relevant contract evidence to establish what action it can perform and what permissions apply. The claims available here do not establish the controls or security properties of any particular governance contract.

Some decisions also rely on information or services outside the chain. An Ethereum smart contract cannot directly obtain offchain facts that are not present in deterministic blockchain state without an oracle or transaction mechanism. [source](<https://ethereum.org/developers/docs/smart-contracts/>) An oracle is a mechanism for bringing outside information into contract logic; its presence does not establish that the information is accurate or that the governance decision has been correctly interpreted. Determine what external inputs a process depends on and how they enter its decision path.

## Where the process can fail or concentrate control

A transparent vote record is not a guarantee of broad participation, correct interpretation, or successful implementation. Voters may coordinate unevenly; a proposal may be unclear; or participants may misunderstand the rules. These are practical assessment questions, not failures that can be diagnosed from a vote tally alone. Compare the proposal’s stated intent with the documented decision rule and any subsequent action.

Execution can introduce a separate set of dependencies. If a process needs a privileged operator or a separate authorized transaction, the outcome depends in part on that step being carried out. If a contract performs the action, its code and permissions matter. The evidence available here does not support a claim that any specific design is secure, free of defects, or immune to key-management or operator risks. Avoid converting visibility of a record into a broader security conclusion.

A system can also depend on external services or information. For example, an Ethereum contract’s inability to retrieve offchain facts directly means that a process requiring such facts needs a defined mechanism to supply them. [source](<https://ethereum.org/developers/docs/smart-contracts/>) Assess that dependency as part of the governance path rather than assuming the onchain record contains the complete basis for a decision.

## How to assess a governance process

For a specific proposal, trace the evidence in order:

1. Find the system’s primary documentation for proposal submission, voting, outcome determination, and implementation. Note which rules are explicitly documented and which steps happen offchain.
2. Locate the proposal and its recorded outcome in verifiable governance records. Confirm that the record corresponds to the proposal being assessed, rather than relying only on a summary or interface display.
3. Look for the later execution transaction or other documented implementation step. If none is available, describe the proposal as approved or recorded—not as implemented.
4. Compare any contract action or operator step with the documented permissions and process. Identify dependencies on external data or services, and distinguish those from actions recorded directly onchain.

This method establishes what the available documentation and records show; it does not settle legal authority or guarantee that every offchain obligation was met. The governing arrangement and applicable context may require separate review. Claims about security, recovery, fees, availability, compliance, or legal and tax consequences likewise require current, system-specific evidence and, where appropriate, qualified review.

The central distinction is simple: proposal, vote, and implementation are related but separate parts of a decision path. Follow each stage in the system’s own documentation and verifiable records, and state only what those records support.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
