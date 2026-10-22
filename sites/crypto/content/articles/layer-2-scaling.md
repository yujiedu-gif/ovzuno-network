---
title: "Layer 2 scaling: how blockchain systems process transactions"
description: "Learn how layer 2 scaling shifts blockchain transaction execution, how Layer 2 systems rely on a base chain, and which design trade-offs matter."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 scaling"
owned_question: "How does layer 2 scaling process transactions alongside a base blockchain, and what trade-offs follow from that design?"
risk_level: "medium"
---

Layer 2 scaling moves some transaction execution away from a base blockchain while using that base chain for specified functions, such as publishing data or settling results. The details vary: the label does not establish how a system verifies activity, where transaction data is available, or what happens if an operator or component fails. To understand a particular design, follow its transaction flow and identify exactly what the base chain checks and records.

## What layer 2 scaling means

A **base layer** is the underlying blockchain that provides a system with some combination of consensus, settlement, or data availability. A **Layer 2**, in common architectural terms, is a system that performs execution separately from that base layer and depends on it in defined ways. Layer 2 designs do not all share one architecture or the same security assumptions.

Execution means processing transactions to determine state changes: for example, which accounts or contracts have which updated values. In a rollup design, transactions execute outside Layer 1, while transaction data or commitments are posted to Layer 1 so the base layer can provide consensus and settlement for the published record. The posted material and verification path depend on the system.

Scaling work often aims to increase transaction speed and throughput without sacrificing decentralization or security. That is a design objective, not a guarantee that every system achieves all three or that the term “Layer 2” supplies a performance or security score. A useful distinction is between the *goal* of scaling and the specific mechanisms a system uses to pursue it.

## How a transaction moves through a Layer 2 system

A simplified flow helps separate the events that can otherwise be blurred together:

1. **Submission:** A user or application sends a transaction to the Layer 2 system. How the system accepts and orders it is design-dependent.
2. **Execution:** The Layer 2 processes transactions and derives state changes outside the base layer. A system may group many transactions into a batch.
3. **Publication:** The system posts transaction data, a commitment, or other specified information to the base chain. A rollup uses the base chain for consensus and settlement of the published record, but publication alone does not describe every verification or recovery rule.
4. **Verification and settlement:** Depending on the design, the base chain or its contracts may check a proof, allow challenges to a proposed result, or perform another defined role. The relevant rule is system-specific.

These steps explain why “included on Layer 2” and “settled on the base chain” should not automatically be treated as synonyms. Execution can occur on one layer, while a related record or result is later published or handled on another. The timing and meaning of settlement depend on the design’s rules; this overview does not establish a universal point at which every Layer 2 transaction becomes final.

The same caution applies to the word “batch.” Batching describes a way to group transactions for publication or processing, but it does not, by itself, tell a reader what data is available, what is verified, or how a disputed result can be addressed.

## How Layer 2 designs use the base chain

A central question is **data availability**: where can participants obtain the transaction data needed to verify summarized state changes? In one broad model, the base chain receives transaction data or commitments. The exact publication method matters because a commitment is not the same thing as publishing all underlying transaction data. The architecture should specify what is recorded and how participants can obtain the information needed for independent verification.

Another question is what the base chain verifies. Some designs use a validity-proof approach: a base-layer verifier accepts a cryptographic proof for a proposed offchain state transition. Other designs use an optimistic approach, accepting a proposed transition subject to a challenge period and a process for disputing incorrect execution. These are broad mechanism categories, not guarantees about a specific deployment. A system’s proof implementation, challenge process, data publication, upgrade controls, and exit mechanisms still require separate examination.

It can help to analyze a decentralized application in layers: settlement, application, and interface. A user-facing interface is not the settlement mechanism, and a Layer 2’s application logic is not the same as the base chain. A system may distribute or combine these components differently. Keep the roles distinct when evaluating a design: ask where transactions are executed, where relevant data is published, which component verifies or disputes results, and which parties control operational components.

## Rollups and other scaling approaches

A **rollup** is a broad scaling family that executes transactions outside a base layer and posts transaction data or commitments to that layer. Rollups can use different verification models. In a validity-proof design, a verifier contract accepts a cryptographic proof for a state transition. In an optimistic design, a proposed transition can be challenged through a fraud-proof process during a challenge period. The family name alone does not reveal the full implementation, including how data is published or how users can recover or exit.

Not every system that processes transactions separately should be treated as a rollup. A sidechain, for example, is a distinct ledger coordinated with another chain. Assets are not physically moved between ledgers; bridge designs coordinate value through mechanisms such as locking and releasing, minting and burning, or swapping. The accounting and redemption path depends on the bridge design. A system that uses its own validator set or a bridge therefore raises questions different from a rollup’s base-chain verification model.

Labels can be inconsistent across the ecosystem. Rather than relying on a project’s category name, inspect its architecture: which chain provides consensus, where transaction data is published, what checks state transitions, and what mechanism connects assets or messages between chains. Those details determine the nature of the dependency.

## The trade-offs to assess

Moving execution away from a base chain can change how much activity that chain must process directly, but the design also creates dependencies. The balance among throughput, data availability, settlement assumptions, and decentralization is system-specific. No conclusion about security follows from the Layer 2 label alone.

For a particular system, investigate at least these questions:

- **Data:** What information is published, where is it available, and can participants obtain what they need to verify or reconstruct state?
- **Verification:** Does the system use a validity proof, a challenge process, or another mechanism? Who can submit a challenge, and what does the base chain actually check?
- **Operations:** Who sequences transactions, administers contracts, or can change system parameters? What upgrade controls exist?
- **Bridges and exits:** How are assets and messages coordinated across ledgers, and what happens if the bridge or a required operator is unavailable?
- **Recovery:** What options exist when a system component fails or a proposed state transition is disputed?

These are investigation prompts, not claims that every design has the same weaknesses or remedies. A framework that classifies rollup maturity in decentralization and trust minimization, for example, is not a complete security score. Likewise, a project’s stated architecture does not prove that its implementation is free of bugs or that its operational assumptions are satisfied.

Performance, fees, and availability also require careful evidence. They can depend on the system, the measurement method, and the conditions being measured. Without current, dated, comparable measurements, it is not sound to infer that a particular Layer 2 is faster, cheaper, or more available than another. The practical takeaway is to treat “Layer 2” as an architectural starting point: trace execution, publication, verification, and recovery, then assess the resulting dependencies on their own terms.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
