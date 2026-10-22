---
title: "List of l2 blockchains: examples and how they differ"
description: "Explore a non-exhaustive list of l2 blockchains, with clear criteria for identifying Layer 2 networks and distinguishing their scaling approaches."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["list 2 blockchains"]
author: "editorial_team"
primary_keyword: "list of l2 blockchains"
owned_question: "What are examples of Layer 2 blockchains, and how can readers distinguish them by their relationship to a base layer and their scaling approach?"
risk_level: "medium"
---

Layer 2 (L2) blockchains are systems that move some transaction execution away from a base blockchain while relying on that base layer for specified functions. To identify examples accurately, check each network’s technical documentation for its scaling design and its actual base-layer relationship; a project label alone is not enough. The evidence available for this article supports the classification framework, but not a verified roster of named networks, so this reference explains how to assess and distinguish examples without supplying unsubstantiated names.

## What qualifies as a Layer 2 blockchain?

A **base layer** is the blockchain that provides an underlying set of network functions. In a modular architecture, execution, settlement, consensus, and data availability can be treated as separate functions and assigned to specialized layers. This vocabulary helps explain where a system performs work, but it does not, by itself, establish that the system is an L2. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A useful L2 classification asks whether a system moves execution away from the base layer and uses that layer for a documented role. The relationship can include deriving some security from the base layer rather than operating only under a separate validator set. That reliance is conditional: the system’s proof, data-availability, settlement, governance, and exit mechanisms all affect the exact guarantee. [source](<https://ethereum.org/developers/docs/scaling/>)

Therefore, a connection to a base chain is not enough. A project entry should explain which activity happens away from the base layer and what the base layer does with the resulting records, proofs, or other information. It should also make clear which functions remain outside the base layer. Avoid broad wording such as “inherits all security” unless project-specific evidence supports that precise claim.

For this reference, the inclusion test is deliberately narrow: a named example would need current primary technical documentation describing both its scaling approach and its relationship to a named base layer. The allowed evidence does not document individual L2 networks or their current deployment status. It would be inaccurate to populate a named list using general familiarity or marketing descriptions, so no named projects are treated here as verified examples.

## List of l2 blockchains: examples by design

A source-backed list should organize networks by documented design rather than popularity, perceived quality, or assumed performance. The following categories are useful fields for such a list. They describe what to look for in project documentation; they are not claims that a particular unnamed network belongs in a category.

**Execution away from the base layer.** Start by identifying which transactions or state changes are executed outside the base layer. Then record the role the base layer has in relation to those results. Ethereum’s scaling overview describes rollups as executing transactions outside Layer 1 and posting transaction data or commitments to Layer 1 so the base layer can provide consensus and settlement. This is a documented architectural pattern, not a verified roster of projects or a claim that every system described as an L2 follows it in the same way.

**Validity-proof approach.** A listing may identify a design by the mechanism it documents for accepting proposed state changes. In the cited Ethereum model, a validity rollup’s canonical state is updated after a base-layer verifier contract accepts a cryptographic validity proof for the proposed offchain transition. This describes that model; it does not establish that any particular network uses it, that its verifier is correct, or that its implementation is free of other dependencies.

**Challenge-based approach.** Another documented model uses an optimistic acceptance process with a challenge period and a fraud-proof process for disputing incorrect execution. The specific system’s proof implementation, challengers, upgrade controls, and withdrawal design require separate examination. This category is not a conclusion about a named network’s present configuration or security.

**Data handling and base-layer role.** For each entry, state where transaction data is published or made available, and distinguish that from where execution takes place. Data availability is a separate architectural function; a label like “rollup” does not replace checking the project’s technical description of its data and settlement arrangements. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A directory can use these fields to describe a verified example consistently: network name, base layer, execution location, proof or dispute approach, data arrangement, and source documentation date. That format makes clear what is known and what still needs verification. The categories are not mutually exclusive rankings, and an entry’s inclusion would not establish equivalence, safety, suitability, or measured performance.

## How Layer 2 designs differ

The main architectural differences concern where execution occurs, how proposed state changes are checked or challenged, and how the system handles the data needed to establish those changes. These choices describe how a system relates to its base layer. They should not be converted into conclusions about fees, throughput, or safety without separate, appropriately scoped evidence.

The base-layer dependency deserves particular attention. An L2 may derive some security from its base layer, but the extent of that relationship depends on its proof, data-availability, settlement, governance, and exit mechanisms. A high-level description of an approach cannot establish the strength of any one project’s implementation or cover conditions its documentation does not address. [source](<https://ethereum.org/developers/docs/scaling/>)

It is also useful to separate architectural goals from measured results. Scaling work may seek to increase transaction speed and throughput without sacrificing decentralization or security. That is a design objective, not a universal performance result, a score, or evidence that a particular network achieves all three goals under particular conditions. [source](<https://ethereum.org/developers/docs/scaling/>)

Documentation and implementations can change. A comparison should therefore state what the cited technical documentation actually describes, and avoid treating a historical description as proof of present network status or availability. Where information about a live deployment is needed, verify it through current, authoritative, dated evidence rather than inferring it from an architectural category.

## Layer 2 versus sidechains and other scaling networks

A separate blockchain is not automatically an L2. The relevant distinction is the documented relationship to the base layer: an L2 may derive some security from that layer, while a system that relies only on a separate validator set has a different relationship. This architectural distinction does not, by itself, determine whether either design is safe or suitable. [source](<https://ethereum.org/developers/docs/scaling/>)

The word **scaling** is broader than **Layer 2**. A network may aim to improve throughput or transaction speed, but that objective alone does not establish that it relies on another chain for settlement or security. Similarly, a project’s use of “L2,” “sidechain,” or another label is not a substitute for examining its documented dependencies.

If terminology is ambiguous, describe the facts the project documents: where execution takes place, what the base layer records or verifies, what proof or dispute process applies, and how data is handled. If those details do not establish the required relationship, leave the classification open rather than silently assigning the project to an L2 category. Architectural boundaries can vary across projects, so precise descriptions are more useful than a label without explanation.

## What to verify before relying on a network listing

For each proposed entry, use current technical documentation to answer these questions:

- **Execution:** Which transactions or state changes are handled away from the base layer?
- **Base-layer role:** What does the base layer do with the system’s data, proofs, or settlement?
- **Proof or dispute method:** How are proposed state changes checked or challenged, according to the project’s documentation?
- **Data arrangement:** Where is the information needed to understand or verify those changes made available?
- **Evidence date and status:** Is the source current and authoritative for the specific claim being made?

Keep each claim within what its source establishes. A category label does not support claims about fees, yields, performance, security, recovery options, or current availability. Those attributes require separate, current evidence and are not established by the design descriptions here. Legal, tax, and compliance conclusions are also outside this architectural reference and would require jurisdiction-specific support.

A useful list of L2 blockchains is therefore a maintained, source-backed classification rather than an assumed fixed roster. State the inclusion test, identify the base-layer relationship for each named entry, and distinguish documented architecture from operational outcomes. Because the available evidence for this article does not substantiate named networks, this article supplies the classification method rather than an invented list. That limitation preserves the central distinction: an architectural category is a way to describe a design, not a ranking, endorsement, or guarantee.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
