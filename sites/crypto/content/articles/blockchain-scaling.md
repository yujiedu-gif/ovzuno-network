---
title: "Blockchain Scaling: Approaches to Increasing Network Capacity"
description: "Learn what blockchain scaling means, how on-chain and layered approaches address transaction capacity, and which security and decentralization trade-offs matter."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "blockchain scaling"
owned_question: "What does blockchain scaling mean, which approaches increase transaction capacity, and what trade-offs should readers compare?"
risk_level: "medium"
---

Blockchain scaling means changing a network or its surrounding system so it can process more activity, while balancing verification demands, security assumptions, and decentralization. No single capacity metric captures the whole design: the approach may change the base protocol, move some execution elsewhere, or combine both, with different responsibilities and dependencies in each case.

## What blockchain scaling is meant to solve

A blockchain records transactions in a shared history maintained across network participants. Its replication and validation model helps maintain that shared record, but also means capacity is a system-design question: a network must account for how activity is processed and how participants can verify the resulting history. The details vary among blockchains; replication does not imply that every participant processes data in the same way. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

Several related measures describe different parts of the problem:

- **Throughput** is the rate at which a system processes transactions or other activity. A claim about throughput needs a defined activity type and measurement period.
- **Latency** describes how long an operation takes to reach a stated milestone. A submitted transaction, an included transaction, and a transaction treated as settled are not necessarily the same milestone.
- **Cost** refers to the resources or fees associated with processing activity. A cost comparison needs to say which actions and system components it includes.
- **Capacity** is the system’s ability to accommodate activity under specified conditions. It is not established by one headline number alone.

When demand competes for constrained processing resources, users or applications may face congestion, higher costs, or delays. The scale of those effects depends on the network and the conditions being measured; the available evidence here does not establish current performance for any particular system.

A network can also pursue faster processing or higher throughput without sacrificing decentralization or security. That is a design objective, not proof that a particular implementation achieves all three at once. [source](<https://ethereum.org/developers/docs/scaling/>)

## On-chain changes to transaction capacity

An on-chain approach changes how the base network processes or validates activity. At a broad level, designers might change protocol parameters that govern how much work or data the network handles, or how participants adjust to changing resource conditions. Such changes affect the rules or operation of the base system rather than relocating execution to a separate layer.

For example, proof-of-work difficulty can be adjusted as network mining power changes, altering the expected computational effort needed to publish blocks. The adjustment interval and formula vary by network, so this mechanism should not be read as a universal capacity control. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

Increasing the work or data participants must handle can also affect the practical ability to run and verify network components. The relevant question is not simply whether one parameter permits more activity, but what hardware, bandwidth, storage, and operational demands follow for participants. Those consequences are implementation-specific; the allowed evidence does not establish a universal capacity gain or a fixed relationship between any parameter and decentralization.

Accordingly, a protocol-level capacity claim should identify the design change, the activity being measured, and the verification burden it creates. A larger nominal limit or altered processing rule is not by itself evidence of a better overall network.

## Layered and off-chain scaling approaches

Layered approaches move or coordinate some activity outside the base layer, while retaining a relationship to that layer. “Off-chain” here means that some execution or processing does not occur directly on the base chain; it does not specify how results are checked, published, or settled. Those details depend on the system.

Rollups are one example. They execute transactions outside Layer 1 and post transaction data or commitments to Layer 1, allowing batches to use the base layer for consensus and settlement. Publication format and proof design differ among rollups, and this architecture does not guarantee lower fees or higher throughput for every transaction or operating condition. [source](<https://ethereum.org/developers/docs/scaling/>)

The phrase “layered scaling” covers designs with materially different dependencies. Some systems rely on the base layer for data, settlement, or dispute processes; others may use different arrangements. A system’s label alone does not establish what users can verify, who controls operational components, or how a disputed or failed operation is handled. The allowed evidence supports a particular rollup pattern, not a universal description of every off-chain approach.

For any specific design, readers should identify which work occurs on the base layer and which occurs elsewhere, what information is made available for verification, and what role the base layer plays. User, operator, and application responsibilities also vary; they cannot be inferred from the general term “Layer 2” or “off-chain.”

## Trade-offs to assess across scaling designs

Compare designs by examining what they ask participants to trust, operate, and verify—not by treating throughput as a standalone score.

- **Verification and control:** Who can validate activity, and which system components can influence execution or publication? A distributed network may reduce one actor’s ability to affect consensus as independently operated nodes increase, but node count alone does not establish operator independence, geographic diversity, client diversity, or block-production power. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)
- **Base-layer role:** Determine whether the base chain handles execution, data publication, settlement, or some dispute process. Those roles are separate design questions; a connection to a base layer does not establish that the layer provides every form of protection.
- **Data and failure handling:** Check what data participants need to verify state changes and what happens if data, operators, or dispute processes are unavailable. The evidence here does not establish a universal recovery or withdrawal guarantee, so those claims require documentation for the particular implementation.
- **Performance conditions:** Treat throughput, latency, and cost as network- and condition-specific. A comparison should state which transactions it covers, the measurement period, and whether it includes the components and steps users actually depend on.

No single approach is universally superior on the evidence available here. A design can shift costs or responsibilities rather than remove them, and a capacity improvement on one measure may coincide with new operational or verification assumptions.

## Questions to ask before applying a scaling claim

Before relying on a claim about scaling, make it specific enough to evaluate:

1. **What activity is counted?** Identify the transaction or operation type, and whether the figure describes a base chain, an added layer, or a combined system.
2. **What milestone and period are measured?** Clarify whether the claim concerns submission, processing, inclusion, or another stated outcome, and over what interval it was measured.
3. **Which components are included?** Ask whether the claim covers only execution or also data publication, settlement, verification, and any dispute process.
4. **What assumptions make the result possible?** Check who operates or controls important components and what users can independently verify.
5. **What does the current implementation document?** For a concrete deployment or use case, consult current, system-specific documentation. This conceptual explanation does not provide configuration instructions or jurisdiction-specific legal, tax, regulatory, or compliance advice.

These questions keep “scaling” from collapsing into a single number. They help distinguish changes to the base protocol from systems that relocate or coordinate activity elsewhere, and make the relevant trade-offs visible without implying that capacity alone determines network quality.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [NIST IR 8202: Blockchain Technology Overview](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
