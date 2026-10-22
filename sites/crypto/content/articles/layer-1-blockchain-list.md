---
title: "Layer 1 blockchain list: examples and inclusion criteria"
description: "Explore a layer 1 blockchain list with clear inclusion criteria, representative network examples, and notes distinguishing Layer 1 chains from other blockchain parts"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 1 blockchain list"
owned_question: "Which networks are examples of Layer 1 blockchains, and what inclusion criteria distinguish them from Layer 2 networks and other blockchain components?"
risk_level: "medium"
---

A Layer 1 blockchain is a base network whose protocol maintains its own chain and state, rather than a system that relies on another blockchain for some of its security. Ethereum is one example supported by the available evidence. This is an illustrative, non-ranked list—not an exhaustive directory—because the evidence provided does not verify the Layer 1 status of a broader set of named networks.

## What counts as a Layer 1 blockchain?

“Layer 1” is a category label for a base blockchain network. For this list, the practical inclusion test is whether the network operates as a base chain with its own ordered network state, rather than acting as a system that derives some security from another chain’s consensus. The boundary is useful for organizing examples, but it should not be mistaken for a complete technical definition that applies identically to every architecture.

Ethereum offers a supported illustration of the base-network criterion: its blocks reference parent blocks cryptographically, creating an ordered chain of network state. That property supports identifying Ethereum as an example here; it does not establish facts about other networks or settle every possible classification question. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

A Layer 2 network falls outside this list when it derives some of its security from an L1’s consensus. The specific guarantee depends on the system’s proofs, data availability, settlement, governance, and exit mechanisms. As a result, the label “L2” alone is not a substitute for checking how the particular system is designed. [source](<https://ethereum.org/developers/docs/scaling/>)

The inventory uses category membership only. It does not rank networks by popularity, performance, suitability, or investment value, and it does not assume that all base networks perform the same functions in the same way. The organizing principle is whether a system fits the stated base-network criterion, not whether it is widely discussed or associated with blockchain technology.

## Layer 1 blockchain list: representative networks

The available evidence supports one named entry that can be tied directly to a documented network structure:

- **Ethereum — base-network example.** Ethereum’s blocks reference their parent blocks cryptographically, forming an ordered chain of network state. This is the basis for including it as an L1 example in this limited list. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The entry is illustrative, not exhaustive. The supplied evidence does not establish current Layer 1 classifications for a broader group of named networks, so adding names based on familiarity would not meet the same evidence standard. This limited list should therefore be read as an orientation to the category, not as a complete directory of networks.

The limitation is also important for readers who need a practical inventory. A list can be broad only when each name is supported by evidence that addresses the same question: does the documented system act as a base network under the stated inclusion test? Without that support, a list may mix base chains with scaling systems or infrastructure components and give the impression that the categories are interchangeable.

No ordering is implied by the entry’s placement. Ethereum is not presented as the leading, preferred, fastest, or safest network. The evidence used here supports a description of its block structure, not comparative conclusions about it or any other network.

## How to read the categories and edge cases

Start with the role a system performs. If it operates as the base network under the criteria above, it may qualify for this list. If it relies on another chain’s consensus for some of its security, it is outside the list’s L1 category for this purpose. Because the extent and mechanism of that reliance vary, readers should check a system’s architecture rather than infer its classification from a short label. [source](<https://ethereum.org/developers/docs/scaling/>)

Modular architectures make simple labels less informative. One modular model separates execution, settlement, consensus, and data availability into functions that can be assigned to specialized layers. A component responsible for one of these functions is not automatically a standalone L1 blockchain. Classification depends on how the larger system is organized and whether the candidate itself acts as the base network under the inclusion test. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

Permissioned enterprise networks call for the same care. Hyperledger Fabric is one permissioned-network model involving organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. That architecture identifies a particular network model; it does not justify a blanket rule about whether all enterprise systems belong in a Layer 1 list. The candidate’s documented role and architecture must be considered on their own terms. [source](<https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html>)

These distinctions keep the list focused on networks rather than every technical element connected to them. A base chain, a scaling system, and a specialized component can all belong to a broader blockchain ecosystem while serving different roles. The list includes only examples that the evidence supports as base-network examples; it does not try to classify every related system or component.

## What this list does not tell you

Inclusion does not show that a network is faster, cheaper, more secure, or more decentralized than another. Nor does a base-network label, by itself, establish whether a network is appropriate for a particular application or organization. Those are separate questions requiring evidence about the specific network, its design, and the intended use.

For example, independently operated nodes can reduce the ability of one bad actor to affect consensus, but node count alone does not establish operator independence, geographic diversity, implementation diversity, or block-production power. A simple category list cannot capture those distinctions or serve as a security assessment. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

This inventory is not a technical comparison, deployment assessment, or recommendation. It contains no findings about fees, yields, operating status, availability, recovery procedures, or compliance. Those details should not be inferred from inclusion, and this evidence does not support claims about them.

## Verify network details before relying on them

For a candidate not listed here, consult its official protocol documentation and ask whether the described system maintains its own base chain and state or derives some security from another chain’s consensus. For a layered or modular design, identify the functions assigned to the candidate and the role of the larger system. Keep the classification tied to the documented architecture rather than to a marketing label or an assumed category. [source](<https://ethereum.org/developers/docs/scaling/>) [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

Record what the documentation actually establishes and avoid extending a narrow fact into a broader conclusion. For instance, evidence that a network has an ordered chain of state supports describing that structure; it does not establish that the network is superior to another, or that every associated component is itself an L1. The same evidence discipline applies to any proposed additions to a named list.

The evidence available for this article supports Ethereum as an example and explains distinctions useful for checking other candidates, but it does not verify a larger named inventory. Treat the list accordingly: as a concise, non-ranked starting point for identifying the category, not a comprehensive catalog or a substitute for network-specific research.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
