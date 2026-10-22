---
title: "DeFi Wealth Management: Wallet Custody and Operational Controls"
description: "Explore how wallet custody, transaction signing, and protocol access fit into DeFi wealth management, with operational risks and controls to assess."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["wallets_custody"]
tags: ["DeFi portfolio management", "wallet custody", "on-chain asset management"]
author: "editorial_team"
primary_keyword: "defi wealth management"
owned_question: "How do wallet custody, transaction signing, and protocol access fit together in DeFi wealth management, and what operational risks should a system design address?"
risk_level: "high"
---

DeFi wealth-management systems combine operational workflows with infrastructure that controls or interacts with digital assets. To assess one, trace who can authorize transactions, which systems prepare and submit them, and what the protocol does after a transaction is included. Do not treat an interface, a wallet, a smart contract, and an asset-management process as interchangeable.

## What DeFi wealth management means at the infrastructure layer

“Wealth management” describes the broader activities a person or organization may perform; the infrastructure layer is the set of technical components that supports particular interactions. This article focuses on that layer—not on selecting assets, designing a portfolio, or predicting outcomes.

One useful way to map a DeFi application is to distinguish its settlement, application, and interface layers. Settlement concerns the blockchain activity that records outcomes. Application logic determines how a particular service operates. The interface is the point through which a person or another system interacts with it. These layers have distinct dependencies, although a system may distribute or combine them differently. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

A broader application stack can include smart contracts and blockchain nodes alongside client libraries, wallets, front ends, data indexing, storage, and other off-chain services. A user-facing screen is therefore not necessarily the system that holds signing authority, and the contract that executes an operation is not necessarily the system that decides whether a user should request it.

The boundary matters operationally: a protocol can execute an authorized instruction, but its technical behavior does not explain who authorized that instruction, who operates the interface, or who is responsible for a particular business process. Document those responsibilities separately rather than describing the entire arrangement as one “DeFi platform.”

## Trace the wallet custody and transaction flow

A practical workflow map follows an instruction from request to outcome:

1. **Asset access:** Identify the arrangement that provides access to the assets and the keys or signing authority used for transactions.
2. **Transaction preparation:** Record which application or service constructs the proposed interaction and what information it presents for review.
3. **Authorization and signing:** Identify the person, wallet, or other authorized process that approves and signs the instruction. A signature is an authorization mechanism; it does not, by itself, establish the signer’s human or organizational identity.
4. **Submission and execution:** Determine which system submits the signed instruction and which protocol or contract processes it. In an AMM-based decentralized exchange, for example, trading can be implemented through smart contracts and liquidity pools, with transactions settled when included in a blockchain block. That example is not a description of every DeFi workflow. [source](<https://www.bis.org/publ/work1227.pdf>)
5. **Review of outcome:** Specify how the organization checks the result and records the relevant operational evidence. The review should distinguish what the system reports from what the protocol has recorded.

At the custody layer, self-custody and third-party custody describe different control arrangements. In the self-custody model, the user controls the private keys and recovery material needed to access the assets. In a third-party custody model, a custodian manages access to private keys on behalf of customers. These descriptions do not settle every question about legal rights, responsibility, or recovery; those depend on the specific arrangement and applicable context.

For system design, turn the distinction into explicit questions: who can initiate an instruction, who can approve it, who can produce a signature, and who can submit the signed transaction? Also document whether any one party can perform multiple steps. A workflow map that names only the wallet or application leaves these authority boundaries unclear.

Protocol access is another boundary. A user may retain control of assets while trades execute or settle through smart contracts, but a decentralized-exchange design can still depend on interfaces, relayers, administrators, or off-chain order components. The label “decentralized” is not a substitute for identifying the actual components and their roles.

## Compare signing and access-control models

Signing is the step that authorizes an instruction with a key or other permitted mechanism. Access control defines who may request, review, approve, or carry out the steps around that authorization. These functions should be mapped separately: application access does not automatically tell you who controls the signing authority, and protocol permissions do not by themselves explain an organization’s internal approval process.

For each proposed workflow, document the following:

- **Authorized actors:** Which people, services, or roles may propose and approve an action?
- **Approval conditions:** Does an instruction require one authorization or multiple approvals? If a threshold arrangement is used, specify what the threshold applies to and how it is enforced.
- **Role separation:** Can the same actor prepare, approve, sign, and submit an instruction? If roles are separated, describe the boundary and how it is maintained.
- **Transaction review:** What information is available to reviewers before authorization, and what checks must they complete? Do not assume that a screen’s summary is equivalent to an independent verification of the underlying instruction.
- **Protocol and application permissions:** Which permissions belong to the wallet, which belong to a connected contract or service, and which are managed by an application or provider?

Treat these as assessment questions, not as a recommendation for one signing model. Shared authorization, individual signing, or policy-based controls can only be evaluated in the context of their documented implementation. The available evidence here does not establish that a particular model is safer or suitable for a particular organization.

## Identify operational, security, and recovery risks

A useful risk review follows the workflow and asks what could fail at each boundary. Could an unauthorized party request an action? Could an authorized signer approve an instruction without understanding its destination or effect? Could preparation, approval, signing, or submission rely on a component whose role has not been documented? Could protocol execution differ from what the interface led a reviewer to expect? These are questions for system-specific analysis, not claims that a failure has occurred.

Review protocol dependencies as well as wallet controls. DeFi applications can be analyzed through settlement, application, and interface layers, but implementations may distribute or combine those layers differently. That means a security review should name the actual dependencies in the system under consideration rather than assume that one component’s controls cover the whole stack. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

Recovery deserves a separate written procedure. Specify who is permitted to initiate recovery, what evidence or approvals are required, which systems or parties must participate, and what actions become possible after recovery. State what happens if a required participant or component is unavailable. The evidence available for this article does not establish any general recovery capability, incident-response process, security guarantee, or recovery timeline; those claims require documentation for the specific implementation.

A practical control-and-evidence checklist is:

- Map the custody arrangement and identify the parties with access to signing authority.
- Trace instruction preparation, review, authorization, signing, submission, and outcome verification.
- Record role boundaries and approval conditions, including any threshold or policy mechanism.
- List application, interface, provider, contract, and protocol dependencies relevant to the workflow.
- Document recovery assumptions, authorized actors, prerequisites, and unresolved failure cases.
- Request implementation-specific evidence for security controls, incident handling, and recovery claims; do not infer guarantees from a product label or architecture description.

## Set evidence and jurisdiction boundaries before deployment

Separate technical facts from commercial, legal, tax, and investment claims. A description of how a transaction is authorized or settled does not establish that a service is available in a particular location, that a fee is charged at a particular level, that an asset or strategy will produce a return, or that a system meets a legal obligation. This article makes no such claims.

Where virtual-asset service providers fall under applicable FATF standards, those standards include preventive measures such as customer due diligence, record keeping, suspicious-transaction reporting, and originator and beneficiary information handling for applicable transfers. FATF standards are international standards; exact legal duties, thresholds, licensing, data handling, and permitted services depend on implementation in each jurisdiction. Do not treat this general description as a determination about whether a particular organization or system is covered. [source](<https://www.fatf-gafi.org/en/publications/Virtualassets/Virtual-assets-fatf-standards.html>)

Before a real deployment decision, verify any jurisdiction-specific compliance statement against current, applicable primary sources and the arrangement in question. Verify product availability, fees, service coverage, and any claimed security or recovery capability with direct documentation for the relevant system. Keep tax and investment conclusions outside an infrastructure map unless they are separately assessed for the appropriate jurisdiction and audience. The result should be a clear account of who controls access, who approves instructions, which components execute them, and what evidence supports the controls—without presenting technical architecture as a legal, financial, or operational assurance.

## Sources and references

- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
- [Virtual Assets](https://www.fatf-gafi.org/en/publications/Virtualassets/Virtual-assets-fatf-standards.html) — Financial Action Task Force; retrieved 2026-10-19.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
