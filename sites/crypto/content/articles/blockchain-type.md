---
title: "Blockchain type: how common architectures differ"
description: "Understand blockchain type distinctions by access, validation, and governance, and see how public, permissioned, and hybrid designs can affect payment systems."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["types of blockchain"]
author: "editorial_team"
primary_keyword: "blockchain type"
owned_question: "What does blockchain type mean, and how do common blockchain architectures differ in access, control, and transaction validation?"
risk_level: "medium"
---

A blockchain type describes an architecture’s approach to access, validation, and governance—not a separate underlying technology. To classify a system, ask who can read its records, submit transactions, and participate in validating them, then identify how its rules are governed. “Public,” “permissioned,” and “hybrid” are useful shorthand, but the labels alone do not establish how every function works or whether a system fits a particular payment need.

## What does blockchain type mean?

A blockchain is a tamper-evident and tamper-resistant digital ledger implemented in a distributed fashion. That is a broad technical definition, not a complete classification. Systems can differ in participation, consensus, privacy, finality, and governance, so the phrase “blockchain type” is best understood as a way to summarize design choices rather than a universal taxonomy. [source](<https://csrc.nist.gov/pubs/ir/8202/final>) [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Three dimensions help make the description more precise:

- **Access** concerns who can read data and who can submit transactions.
- **Validation** concerns who checks transactions or participates in maintaining an accepted ledger state.
- **Governance** concerns how operating rules are decided and changed.

These dimensions should be described separately. A system’s reading access does not, by itself, answer who may submit transactions. Transaction submission does not by itself establish who validates activity. And neither access nor validation alone explains how changes to rules are governed.

The terminology is not perfectly uniform across technical and business settings. Even the broader term “Web3,” which is sometimes used in discussions of public blockchain systems, has no single rigid definition. That is a reminder to state what a label means in the context at hand rather than assume that every organization uses it the same way. [source](<https://ethereum.org/web3/>)

## How do public, permissioned, and hybrid blockchains differ?

A **public blockchain** is commonly used to describe a system with some form of open participation or access. The label is incomplete unless the relevant role is specified: public reading, open transaction submission, and open validation are different properties. A precise description says which of them apply instead of implying that openness in one role guarantees openness in all others.

A **permissioned blockchain** uses controlled participation for one or more functions. The key question is what is controlled: access to read records, permission to submit transactions, participation in validation, or administrative authority. Permissioning is therefore not a single switch that defines every role. The label should be accompanied by a description of the relevant access boundaries.

A **hybrid blockchain** combines arrangements—for example, a design may treat different roles or kinds of access differently. “Hybrid” is a summary, not one standardized architecture. To make it useful, describe which functions are open, which are restricted, and how the parts relate.

| Label | What it can summarize | What to describe separately |
|---|---|---|
| Public | An open form of participation or access | Whether reading, submission, and validation are open |
| Permissioned | Controlled participation in one or more roles | Which roles require authorization and how access is bounded |
| Hybrid | A combination of open and restricted arrangements | Which functions use each arrangement |

The table is a vocabulary aid, not a guarantee that a system fits neatly into one column. A system can be described by more than one label when its functions have different access arrangements. The most informative classification names the role and the control attached to it.

Validation and governance must also remain distinct. Validation describes activity under the system’s rules; governance describes how those rules are set or changed. A label about access does not, by itself, tell a reader who can alter operating rules. That question requires information specific to the system rather than an inference from the architecture name.

## Which design choices matter for payment systems?

For a payment system, begin with the intended participants and responsibilities. Identify who needs to submit payment instructions, who needs access to records, and who participates in validating the activity. Then examine how the system’s rules are governed. This role-based review clarifies what the architecture allows without turning a label into a claim about commercial or operational suitability.

Architecture labels also do not say how a system divides its technical functions. One model distinguishes execution, settlement, consensus, and data availability. Data availability means that network participants can obtain the transaction data needed to verify summarized state changes; availability and long-term archival retrieval are related but distinct requirements. The function model is useful for asking where responsibilities sit, but it should not be treated as a guarantee that every system assigns them in the same way. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A payment-network assessment should consider the required transaction flow, confirmation and finality expectations, capacity, fee behavior, application integration, dependencies, and operational requirements. These are evaluation dimensions, not conclusions that follow from the words “public,” “permissioned,” or “hybrid.” The available evidence here does not establish comparative performance or suitability for any specific network.

Keep the protocol separate from surrounding services. A blockchain’s participation and validation arrangements describe features of its network design; they do not describe every application, operator, institution, or user involved in a payment process. When assessing a payment flow, identify those parties and their responsibilities rather than assuming that the architecture label accounts for the entire system.

## How should readers classify a blockchain?

Use a short role-by-role checklist:

1. **Reading:** Who can obtain the ledger data, and is access open or controlled?
2. **Submission:** Who can send transactions, and what authorization applies?
3. **Validation:** Who checks activity or participates in maintaining the accepted state? Do not infer this from submission rights.
4. **Governance:** How are operating rules decided or changed, and who participates in that process?
5. **Summary label:** Apply “public,” “permissioned,” or “hybrid” only after describing the roles. If arrangements differ by role, give the details alongside the summary.

This method reduces ambiguity. For example, saying that a system is public without specifying whether the statement refers to reading, transaction submission, or validation leaves important questions unanswered. A useful classification gives enough detail for another reader to understand which function the label describes.

## What the labels do not establish

An architecture category alone does not establish security, privacy, reliability, availability, or suitability. Nor does it establish fees, yields, recovery options, or compliance conditions. Those questions need evidence specific to the system and its operating context; they should not be answered by extending a broad category label beyond what it describes.

For payment-system evaluation, treat the label as an initial architectural description. Verify access, validation, and governance separately, then assess other requirements using system-specific information. Legal, regulatory, and tax conclusions are also outside what the architecture label can establish and are not addressed here.

The practical answer is simple: classify a blockchain by its actual access, validation, and governance arrangements, not by its name alone. Use public, permissioned, or hybrid as concise summaries only when the underlying roles and limits are clear.

## Sources and references

- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [What is Web3 and why is it important?](https://ethereum.org/web3/) — ethereum.org; retrieved 2026-10-19.
