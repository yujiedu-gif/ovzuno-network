---
title: "All L1 Blockchains: A Scoped Reference List"
description: "Explore all l1 blockchains through a scoped, criteria-based reference list that distinguishes Layer 1 networks from Layer 2 systems and related components."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["all 1 blockchains"]
author: "editorial_team"
primary_keyword: "all l1 blockchains"
owned_question: "Which networks belong on a clearly scoped reference list of Layer 1 blockchains, and what inclusion criteria distinguish them from Layer 2 networks and other blockchain components?"
risk_level: "medium"
---

A useful reference to “all L1 blockchains” must first say what counts as a network, which operating states are included, and when the list was checked. Here, Layer 1 means a blockchain base network whose own protocol maintains its ledger and establishes its chain history. The evidence available for this article supports that framing and a distinction from Ethereum Layer 2 systems, but it does not provide dated, network-by-network sources for a verified inventory of names. The responsible result is therefore an inclusion method and explicit coverage limit—not a claim to list every current L1.

## What “all L1 blockchains” can reasonably mean

“Layer 1” is commonly used for a blockchain’s base network and protocol. A blockchain can maintain a shared ledger whose published records cannot simply be changed under normal operation. The term does not mean that every network has the same participation rules, consensus process, privacy, finality, or governance. Those properties must be checked separately rather than inferred from the label. [^ledger]

There is also no useful meaning for “all” until the inventory defines its boundaries. A list might mean public mainnets currently operating, or it might include permissioned networks, testnets, inactive projects, and networks in transition. It might include chains created for a particular application, or restrict itself to networks with broader general-purpose roles. Those choices affect which candidates appear and make a list’s headline impossible to assess without its scope.

Architecture adds another complication. A modular architecture model separates execution, settlement, consensus, and data availability into functions that can be assigned to specialized layers. That model is one way to describe system design, not a universal classification rule. An inventory should therefore explain which base-layer responsibilities it expects a candidate to perform and how it treats systems that divide those responsibilities among chains or services. [^functions]

For this article, “L1” is a functional label for an independent blockchain base layer, not a statement about quality or status. The available evidence does not verify whether particular named networks currently operate, qualify under that definition, or belong to a complete set. Accordingly, no dated snapshot of names can be responsibly offered here.

## Criteria for including a network

A reproducible inventory needs evidence for each entry, not simply a familiar name or an ecosystem association. An editor should use documentation that describes the candidate’s own network and protocol, then record the review date and the specific basis for treating it as a base layer. If the evidence does not establish that role, the entry should be marked uncertain or excluded instead of being presented as settled.

The most useful first question is whether the candidate’s own protocol establishes the ledger and chain history, or whether it depends on another blockchain for a core base-layer function. The answer should be based on documented architecture. A label such as “chain,” “network,” or “mainnet” is not, by itself, proof of independent Layer 1 status. Nor does the classification show that the network is secure, active, widely used, or appropriate for any purpose.

Layer 2 systems need to be distinguished from independent base layers. An Ethereum Layer 2 solution derives some of its security from Ethereum’s Layer 1 consensus, although the exact guarantee depends on the system’s proof, data availability, settlement, governance, and exit mechanisms. That dependence is a relevant classification distinction, but it does not mean every system called an L2 has identical architecture or security properties. [^l2]

A useful list should also keep adjacent components out unless its rules explicitly include them. A token is an asset, not a blockchain network. A bridge coordinates activity between otherwise isolated blockchain environments; its existence does not make it an independent L1. Likewise, a system associated with a base chain should not be included merely because it uses blockchain technology. The list must classify the network’s role, not the surrounding product or ecosystem.

Some designs may not fit a simple binary label. A candidate could maintain some functions itself while assigning others elsewhere. In those cases, the entry should state which functions it performs and which it relies on, if the supporting documentation establishes that distinction. The four-function model—execution, settlement, consensus, and data availability—can help organize that description, but it should not be treated as a universal checklist that automatically decides classification. [^functions]

Finally, inclusion criteria should say how they handle networks that are not operating as public mainnets, as well as testnets, inactive projects, and migrations. This article has no evidence establishing current status for named candidates or setting a verified boundary across those categories. A later inventory would need to choose its boundary and check each entry at publication time.

## Examples of Layer 1 blockchain categories

A reference list can group candidates by documented technical characteristics, such as architecture or consensus, provided those groupings are supported by network-specific evidence. Category labels are organizational tools; they do not rank networks or establish comparative performance, security, adoption, or suitability.

Proof of work illustrates why category descriptions should remain narrow. It is a consensus component associated with a computational process, not a complete description of a blockchain’s architecture. Bitcoin provides a concrete, network-specific example: its blocks are linked cryptographically, and its original design uses hash-based proof of work to order history. Bitcoin’s rules should not be generalized to other networks. [^bitcoin]

The supplied evidence supports no comparable, dated classifications for a set of other named networks. Naming familiar projects without sources checked against the inclusion criteria would create the impression of a verified directory when the underlying review had not been established. For the same reason, this article does not assign networks to proof-of-stake, permissioned, modular, or other categories without network-specific evidence.

A future entry format could include the network name, the scope category it belongs to, the evidence supporting its base-layer classification, a concise description of documented architecture, and the date checked. It should flag uncertain or changing classifications instead of concealing them behind a single label. These are fields for a source-checked inventory, not facts about any specific unnamed candidate.

## How to read and verify the list

When using an L1 inventory, begin with its scope. Check whether it includes only public mainnets or also private networks, testnets, inactive projects, application-specific chains, and systems in transition. Then inspect the evidence behind each classification. Documentation should support the claimed role of the network; a list of names without traceable evidence is an examples list, not proof of coverage.

Next, check whether the entry describes dependence on another chain. For Ethereum Layer 2 systems, the amount and form of security derived from Ethereum depends on system-specific mechanisms, so the broad label alone is not enough to establish those details. More generally, the architecture model used by an inventory should be visible to readers, especially where the system distributes execution, settlement, consensus, or data availability across layers. [^l2] [^functions]

Finally, treat the review date as part of the claim. Network status and architecture must be verified for the chosen publication date; this evidence pack does not establish particular upgrades, migrations, shutdowns, or present-day activity for named networks. A list that was once accurate may require rechecking, while a list that does not state when it was reviewed leaves readers unable to judge freshness.

A scoped reference inventory answers a narrower question than a technical comparison or recommendation. It identifies candidates under stated rules and shows what evidence supports their classification. With the evidence available here, the defensible conclusion is limited: distinguish independent base-layer roles from systems that derive some security from another chain, state the inventory’s boundaries and review date, and avoid claiming “all” without dated evidence for every included network and a defined method for assessing coverage.

[^ledger]: The shared-ledger description is a general blockchain claim and does not imply absolute immutability or correctness of off-chain inputs.
[^functions]: The four-function grouping is a modular blockchain model; architectures may combine or assign these functions differently.
[^l2]: This claim concerns Ethereum Layer 2 systems, and its security qualification varies by system.
[^bitcoin]: These are Bitcoin-specific features and should not be applied to other networks without separate evidence.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
