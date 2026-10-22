---
title: "List of Layer 2 Blockchains: A Criteria-Based Reference"
description: "Explore a list of layer 2 blockchains, grouped by design with concise notes on settlement, data availability, and criteria for classifying each network."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["list layer 2 blockchains"]
author: "editorial_team"
primary_keyword: "list of layer 2 blockchains"
owned_question: "Which blockchain networks can be identified as Layer 2s under explicit classification criteria, and what distinguishing architecture details should readers check?"
risk_level: "medium"
---

A network should appear on a Layer 2 list only when current, network-specific evidence supports a stated architectural relationship with a base layer. The evidence authorized for this article does not identify or verify named networks, so it cannot support a current directory of projects. Instead, this reference sets out a cautious inclusion test, explains what architecture details a future entry should document, and marks where the available evidence stops.

## What qualifies for this list of Layer 2 blockchains?

“Layer 2” is not a single universally settled label in the evidence available here. For this reference, the clearest supported inclusion test is the documented rollup pattern: transaction execution takes place away from a base layer, while data is posted to that layer, where base-layer consensus establishes the published record. This is a practical criterion for identifying rollup-style candidates, not a comprehensive definition of every system described as an L2. [source](<https://ethereum.org/developers/docs/scaling/>)

The criterion requires more than a project’s chosen name or a claim that it scales another network. A candidate’s documentation needs to identify the relevant base layer and explain what it publishes there and what role that layer plays. The word “settlement” can be used differently across technical descriptions; a directory should therefore state the documented mechanism rather than infer a settlement relationship from a label.

A bridge connection, by itself, does not satisfy the test. Bridges coordinate token, message, data, or contract-call activity between otherwise isolated blockchain environments. That describes cross-chain coordination; it does not, on its own, show that a connected network follows the rollup pattern or depends on a base layer in the specified way. [source](<https://ethereum.org/developers/docs/bridges>)

A broader architectural distinction can help frame the investigation. In one described model, a monolithic base layer performs execution, settlement, consensus, and data availability together; a modular stack can assign those functions to specialized layers. Architecture descriptions may group functions differently, and real systems can be partly modular. This distinction is useful for asking which functions a candidate handles, but it does not establish that a particular named network is an L2. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

No named candidate can be confirmed from the authorized evidence. It contains general descriptions of rollups and bridges, but no current documentation for particular networks and no independent, network-specific classification analysis. The absence of entries here is an evidence limitation, not a claim that no Layer 2 networks exist.

## Rollup-based networks

Rollups are the most precise category this evidence can describe. The general pattern separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. That supports a screening rule for a directory: include a named candidate only when its own current technical documentation demonstrates the relevant execution and publication arrangement. [source](<https://ethereum.org/developers/docs/scaling/>)

A consistent entry would name the candidate, identify the base layer its documentation specifies, and describe what it publishes there. It should distinguish statements made directly by the project’s technical documentation from conclusions drawn by an outside analyst. If a source does not clarify whether it publishes transaction data or another form of record, the directory should say that the detail is unverified rather than fill it in from the general rollup model.

The available evidence does not confirm the proof method, data format, or operational configuration of any named network. It therefore cannot responsibly divide real projects into optimistic and zero-knowledge categories, or state that a particular network uses one of those approaches. A general category description is not evidence about an individual implementation.

The same restraint applies to hybrid designs and architecture changes. A directory should not force a network into a simple subtype when its documentation describes more than one arrangement or does not make the details clear. The source pack does not establish which named projects have such designs or changes, so no examples can be given here.

## Other Layer 2 designs and classification edge cases

Some scaling systems may not fit the rollup criterion. The authorized evidence does not describe named networks using state channels, validium-style data availability, or another non-rollup L2 architecture. Those categories therefore cannot be populated or evaluated in this list. Mentioning a design category is not grounds for assigning a network to it without network-specific evidence.

A separate ledger connected by a bridge is an important edge case. A bridge can coordinate activity between ledgers, but that fact alone does not show that one ledger publishes rollup data to another or relies on it in the relevant way. A directory should separate “connected to” from “architecturally dependent on” and document the latter before assigning an L2 classification. [source](<https://ethereum.org/developers/docs/bridges>)

Permissioned-network terminology is another potential source of confusion. Hyperledger Fabric documentation, for example, describes a permissioned network model with organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. Those components describe that particular network model; they do not establish that a Fabric deployment is a rollup or qualifies as an L2 under this article’s test. [source](<https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html>)

When a project’s self-description and an independent classification differ, a useful directory should preserve the disagreement instead of presenting one label as settled. It should identify each source’s basis and show whether the disagreement concerns the base layer, published data, or another architectural feature. No permitted source here supplies a network-specific dispute to assess, so this article cannot resolve such cases.

## How to read and verify each entry

A future directory entry should make its classification auditable. At minimum, it should record the network name, the source and date for its technical description, the stated base layer, the execution arrangement, and what information is published to that base layer. It should describe a data-availability model only where the cited documentation supports it, and label any interpretation as interpretation rather than as a directly documented fact.

For each candidate, readers can ask:

- Does primary technical documentation describe execution away from a base layer?
- Does it identify what data or record is published to that layer?
- Does the documentation explain the base layer’s role in establishing the published record?
- Is a data-availability claim explicit, or is it being inferred from a broader architecture description?
- If sources disagree, what specific design detail explains the disagreement?

These questions keep architecture and node roles distinct. For example, an Ethereum full node independently verifies blocks and transactions against protocol rules rather than relying entirely on another node. That verification role describes what a full node does; it is not, by itself, evidence that a network is an L2. The classification still depends on the documented relationship between the candidate’s execution and its base layer. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

A date-stamped directory also needs date-stamped evidence. Readers should be able to see when a source was checked and whether it describes the relevant architecture. The evidence available here supplies no current network-specific source dates, so it cannot produce a “checked on” inventory or confirm a candidate’s present configuration. A future editor should leave an entry unclassified if its source is missing, unclear, or too old to support the stated claim.

## What this list does not establish

This is a criteria-based reference, not a populated list or a ranking. It does not establish that any named network is secure, decentralized, available, low-cost, or suitable for a particular use. It also cannot support claims about fees, performance, recovery options, yields, or current service availability. Those matters would need current, network-specific evidence and are outside this article’s authorized evidence.

Nor does a classification settle regulatory, tax, or compliance questions. The evidence supplied here does not establish any jurisdiction-specific treatment, so no such conclusions belong in this directory. Inclusion in a future list should not be read as an endorsement, an investment assessment, or proof of universal agreement about the term “Layer 2.”

The defensible conclusion is limited but useful: apply a clear execution-and-publication criterion, check it against current documentation for each named network, and state uncertainty where the evidence does not resolve classification. Under the evidence available for this draft, no named network meets a verifiable inclusion standard. That limitation preserves the distinction between a general architectural pattern and a claim about an individual project. [source](<https://ethereum.org/developers/docs/scaling/>)

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
