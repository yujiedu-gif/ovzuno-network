---
title: "Blockchain Governance Models: How Networks Make Decisions"
description: "Explore blockchain governance models, including who proposes and approves changes, how decisions are implemented, and where trade-offs can arise."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "comparison"
topics: ["blockchain_payment_foundations"]
tags: ["on-chain governance", "off-chain governance", "blockchain decision-making"]
author: "editorial_team"
primary_keyword: "blockchain governance models"
owned_question: "What are blockchain governance models, and how do they differ in who proposes, approves, and implements changes to a blockchain network?"
risk_level: "medium"
---

Blockchain governance models are the arrangements through which participants propose, evaluate, and carry out changes to network rules or operations. They differ in who can contribute to decisions and how a decision becomes a change in software or network behavior. Governance is distinct from consensus: consensus is part of how a blockchain’s network agrees on state, while governance addresses how participants decide whether the system should change. The process varies by network, so labels such as “on-chain” and “off-chain” do not, by themselves, identify who has final authority. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

## What blockchain governance covers

A blockchain is a database shared across networked computers. Blocks refer to earlier blocks, and participants use consensus to agree on the network’s state. Governance concerns decisions about the network’s rules and operation; routine consensus processes apply those rules to activity and contribute to agreement about the continuing state. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The distinction is practical. A governance proposal can describe a desired change, but the proposal itself is not the same thing as changed network behavior. A technical process may determine how valid activity is handled without deciding who should propose or approve a future rule change. For example, proof of work is one component used for Sybil resistance and block-author selection. It operates alongside validation, networking, incentives, and a fork-choice rule; it is not a complete account of network governance. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

Governance is best examined as a decision path: how an issue becomes a proposal, which participants review or signal on it, and what steps are needed for the change to be implemented and adopted. The process can involve formal procedures as well as coordination beyond the protocol. Specific arrangements may also change over time, so readers should verify the current process for the network they are assessing rather than infer it from a general label.

## Who participates in blockchain decision-making

Different participants can have different roles. Developers may prepare or review software changes; network operators may decide what software to run; users and organizations may contribute feedback or choose whether to rely on a network. These are useful categories for investigation, not a universal roster of formal governance positions. The available evidence does not establish that every network grants these groups the same rights or uses the same approval process.

Separate participation into three questions:

- **Who can propose or review?** This shows who can introduce an idea and who can assess it.
- **Who signals support or approves?** A process may record support, but its significance depends on the network’s own rules and practices.
- **Who implements or adopts?** A decision must be reflected in software or operational behavior, and adoption by relevant participants affects whether it changes how the network runs.

These roles can overlap, but they should not be treated as interchangeable. A person or group that writes code may not be the same as those who decide whether to run it. Likewise, a recorded signal should not automatically be described as binding approval unless the network’s documented process supports that interpretation.

Formal influence and practical influence can also differ. A written procedure can describe who is eligible to participate, but an assessment of actual influence needs evidence about how the process works. Node counts alone, for example, do not establish how independently operators act, how geographically diverse they are, how varied their software implementations are, or how block-production power is distributed. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

## On-chain and off-chain governance

**On-chain governance** uses mechanisms expressed through a blockchain or its protocol. A network may use it to record votes or signals, but that description alone does not show who may participate, how input is counted, or whether an outcome automatically changes protocol behavior. Those details must be verified for the particular network.

**Off-chain governance** involves discussion and coordination outside the protocol. A proposed outcome may then be carried forward through software and participant adoption. This separates the decision process from routine transaction handling, but the label does not identify a single decision-maker or establish that the process is unstructured. Participants may coordinate through multiple steps, and the relevant implementation path still needs to be examined.

A network can combine on-chain and off-chain processes. For example, a recorded signal may inform a decision while software work and adoption take place through other procedures. The useful comparison is therefore not simply where a vote or discussion occurs. Ask what the mechanism records, what authority the result carries, and which actions are required before network behavior changes.

Neither category alone establishes that a process is more transparent, participatory, fast, or accountable than another. The evidence here does not support universal comparisons on those outcomes. A network-specific assessment should distinguish what is documented from what is observed and avoid treating a mechanism’s name as proof of its practical effect.

## From proposal to implementation

A governance process can be traced through several possible stages. Networks may arrange these differently or omit some steps, so this is a guide for investigation rather than a universal procedure:

1. **Proposal:** A participant frames a possible change and describes the issue it addresses.
2. **Review and deliberation:** Relevant participants examine the proposal and discuss it. The network’s own process determines who is involved and how the review proceeds.
3. **Signaling or approval:** Participants may register support or reach a decision through a defined mechanism. A signal is not necessarily binding approval; check the documented rules before treating it as final.
4. **Implementation:** The change is reflected in software or operational practice.
5. **Adoption:** Relevant participants use the changed software or alter their behavior, enabling the decision to affect network operation.

Ethereum’s documented protocol-change process illustrates why these stages should remain distinct: it includes proposal, technical review, implementation, coordination, and adoption across network stakeholders. This is an Ethereum-specific description, not evidence that all blockchain networks follow the same process.

Implementation and adoption matter because a decision recorded or discussed in one place does not automatically establish changed behavior across a network. When reviewing a proposal, identify what software or operational action is needed, who is expected to take it, and what evidence shows that adoption occurred. If those steps are not documented, the extent to which the proposal changed network operation remains unclear.

Disagreement can also affect the path from decision to implementation. A proposal may remain unimplemented if the necessary steps do not occur, while differing approaches can produce competing network paths. The outcome depends on the particular network and its participants; no universal result follows from disagreement alone.

## Trade-offs and questions to assess

A neutral comparison examines how a governance process allocates decision-making rather than declaring one model best. For a specific network, ask:

- **Participation:** Who can propose, review, discuss, signal, or approve? Are these rights limited to distinct participant groups, and where is that documented?
- **Transparency:** Where can readers inspect proposals, deliberation, signals, and decisions? Which steps are recorded on the network, and which are handled elsewhere?
- **Decision authority:** Is a vote binding, advisory, or one input among several? What evidence supports that interpretation?
- **Implementation:** Who prepares the software or operational change, and what actions are needed for it to take effect? How is adoption established?
- **Accountability:** Are responsibilities clear among proposal authors, reviewers, implementers, and operators? What documentation explains how concerns are handled?
- **Influence:** Which participants appear to shape decisions in practice, and what evidence supports that assessment? Do not infer independence or diversity solely from a count of nodes. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)
- **Design objectives:** How does the network approach goals such as speed and throughput alongside decentralization and security? These are objectives for scaling work, not a universal score by which governance models can be ranked. [source](<https://ethereum.org/developers/docs/scaling/>)

The strongest assessment separates written procedure from observed practice. Consult the network’s documentation for stated roles and formal steps, then trace a proposal through review, decision, implementation, and adoption. If the documentation does not establish that a vote is binding, describe it as a signal or input rather than final approval. If no single authority is identified, do not infer one merely because a proposal mechanism exists.

This method keeps the comparison focused on the reader’s central question: who proposes, who approves or signals support, and who implements changes. The answers are network-specific, and the labels attached to a governance model are only a starting point for examining its actual decision path.

## Sources and references

- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
