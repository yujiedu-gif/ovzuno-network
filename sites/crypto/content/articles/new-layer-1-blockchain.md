---
title: "New Layer 1 Blockchain: Meaning, Design, and Scaling"
description: "Learn what defines a new layer 1 blockchain, how it differs from a Layer 2, and which protocol design choices shape its scaling approach and trade-offs."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "new layer 1 blockchain"
owned_question: "What distinguishes a newly developed Layer 1 blockchain from an existing Layer 1 network or a Layer 2 system, and what design choices affect its scaling approach?"
risk_level: "medium"
---

A new Layer 1 blockchain is a newly developed base network whose protocol governs how the network validates and records its shared state. It may introduce a distinct protocol or create a new network instance using an existing protocol. To classify it, inspect the system’s actual architecture and dependencies: the label “Layer 1” and the fact that a network is new do not establish its capacity, security, or reliability.

## What makes a blockchain a new Layer 1?

A blockchain is a digital ledger implemented in a distributed fashion. It is designed to be tamper-evident and tamper-resistant, and commonly operates without a central repository and often without a central authority. These are broad characteristics, not guarantees that all blockchains use the same participation, consensus, privacy, finality, or governance rules. A blockchain can also be described as a database shared and updated across networked computers, with cryptographic references between blocks and a consensus mechanism for agreeing on state. ([source](<https://csrc.nist.gov/pubs/ir/8202/final>); [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

In common crypto usage, “Layer 1” refers to the base blockchain network and its protocol. The term is common usage rather than a separately standardized technical category. For the reader assessing a proposed network, the useful question is what its base protocol itself does: which rules it defines for validating and recording state, and how it fits into the network’s operation.

“New” can mean different things. A project may introduce a distinct protocol, or it may launch a new network instance using protocol rules that already exist. Those possibilities should not be conflated. To distinguish them, review the network’s technical documentation for the rules and components it identifies as part of its own design. The evidence available here does not establish the architecture of any particular new network.

A project’s label is not enough. Seek documentation that explains how participants agree on the ledger state and how the network handles conflicting histories. Also establish who can participate and what functions the network operates itself. General blockchain characteristics cannot prove that a specific system uses a particular consensus mechanism, has particular validator requirements, or achieves a stated performance level.

## How it differs from a Layer 2 system

A Layer 1 is the base network in this common usage. A Layer 2 is designed around an underlying network. For example, some Ethereum Layer 2 systems derive some of their security from Ethereum’s Layer 1 consensus. The extent of that relationship depends on system-specific proof, data-availability, settlement, governance, and exit mechanisms. ([source](<https://ethereum.org/developers/docs/scaling/>))

When classifying a proposed network, ask which protocol is responsible for its core validation and what relationship it has to any other network. Then check where validation, settlement, and data availability occur, if the documentation describes those functions. A label or marketing description cannot establish those details. Nor does evidence of one connection establish every security property of a system.

This is a classification test, not a catalog of Layer 2 designs. If the project documentation leaves its dependencies unclear, the available evidence may not support a confident classification. State that uncertainty instead of inferring architecture from terminology alone.

## Which protocol choices shape Layer 1 scaling?

A Layer 1’s scaling approach depends on the rules and limits in its own protocol. Areas to examine include how the network reaches agreement, what participation its rules require, how much transaction processing the protocol permits, and how it manages the state accumulated over time. The allowed evidence here does not establish specific validator requirements, execution limits, state-growth rates, or throughput figures for any new network. Such claims need network-specific documentation and evidence.

Scaling work is often framed as seeking higher transaction speed and throughput without sacrificing decentralization or security. This describes a design objective, not a guaranteed outcome, universal theorem, or single score. A network’s performance figures should therefore be interpreted in context: do they describe a theoretical limit, a benchmark, or observed activity, and under what conditions? A throughput number alone does not establish a network’s security assumptions or how distributed its control is. ([source](<https://ethereum.org/developers/docs/scaling/>))

Participation and control also require more than a headline count. A distributed blockchain can reduce the ability of one bad actor to affect consensus as independently operated nodes increase. But node count by itself does not reveal whether operators are independent, geographically diverse, or using different implementations, or how block-production power is distributed. Conclusions about decentralization need evidence on those dimensions, not just a total number of nodes. ([source](<https://csrc.nist.gov/pubs/ir/8202/final>))

These questions connect capacity to design without presuming a universal trade-off or a particular result. The evidence does not support a numerical comparison or conclusion about any newly developed network. For a specific claim, the relevant assessment must use that network’s documentation and operating evidence, with the conditions of measurement stated.

## What evidence is needed to assess a new network?

Start with protocol documentation. Check whether it explains the rules for validating and recording state, who can participate in the relevant roles, and whether the network relies on another system for any part of its operation. Technical documentation supports claims about intended architecture; it does not, by itself, demonstrate observed throughput, availability, or reliability.

For operating claims, look for independently verifiable network data and preserve the conditions behind any figures. Keep theoretical limits, benchmark results, and observed activity separate. If the source does not state how a number was obtained or what conditions it reflects, avoid presenting it as a general capacity figure. The evidence allowed for this explainer does not provide reproducible performance data for a specific new network.

Treat security and recovery claims the same way: identify the documented assumptions and procedures that apply to the particular network. A general description of blockchain technology cannot establish that a given implementation is secure or that it has a particular recovery process. If the relevant evidence is unavailable, the claim remains unverified rather than becoming true by analogy.

Novelty alone does not establish reliability, adoption, or suitability. Keep project descriptions separate from independently supported conclusions, and do not infer a system’s technical properties from promotional claims. A careful assessment can identify what the documentation establishes and what remains unknown without making a ranking or recommendation.

## What questions to ask before drawing conclusions

Use the following questions to organize an initial review:

- Which protocol rules does the network operate itself, and which parts depend on another system?
- Does the documentation show whether this is a distinct protocol or a new network instance using existing rules?
- What does the protocol specify about participation, validation, and recording shared state?
- Are capacity figures theoretical, benchmarked, or observed, and are their measurement conditions disclosed?
- What network-specific evidence supports claims about security, recovery, or availability?
- If claims involve fees, yields, regulation, tax, or compliance, are they supported for the relevant network and jurisdiction?

The last question is a prompt to verify evidence, not a conclusion about fees or legal or tax treatment. This explainer does not establish any such facts. Keep technical classification separate from decisions about deployment, participation, or financial exposure. A network may fit the common usage of Layer 1 without its novelty proving anything about performance or suitability; where evidence is limited, the conclusion should remain limited too.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
