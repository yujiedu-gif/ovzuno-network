---
title: "Layer 1 crypto list: representative base-layer networks"
description: "Explore a layer 1 crypto list of representative base-layer networks, with inclusion criteria, category boundaries, and notes on how to verify each entry."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 1 crypto list"
owned_question: "Which crypto networks belong on a global Layer 1 crypto list, and what inclusion criteria distinguish them from Layer 2 networks and other blockchain components?"
risk_level: "medium"
---

A useful Layer 1 crypto list identifies base-layer blockchain networks, not tokens or applications, and applies a stated test to each entry. The evidence available for this article does not verify named networks’ current operation, base-layer status, or consensus designs. It therefore cannot support a populated list of network names. The criteria below show how to build and check a representative directory without treating unsupported examples as facts.

## What qualifies for this Layer 1 crypto list?

“Layer 1” is commonly used to mean a blockchain’s base network and protocol. It is a category label, not a guarantee that every project uses the term identically. For a directory, define the term operationally: include a network only when its technical documentation supports its role as a base layer, and when evidence separately confirms that it is operating at the time the entry is checked.

Keep the network distinct from things associated with it. A token is an asset, not the network. A wallet is a tool for interacting with a network; an application is software that uses one; and a bridge coordinates activity between otherwise isolated blockchain environments. None qualifies as a Layer 1 merely because it is used with crypto. Bridge security also depends materially on who or what verifies the source-chain event, so the existence of a bridge should not be mistaken for proof of a separate base-layer network. [source](<https://ethereum.org/developers/docs/bridges>)

For each candidate, require primary technical documentation identifying the network and explaining its architecture or base-layer role. Verify operation independently rather than inferring it from a general project description. If you list a native asset, verify its name and symbol separately and label them as asset information, not network identity. The evidence here does not establish particular asset names or symbols.

Architecture can complicate the label. One modular architecture model separates execution, settlement, consensus, and data availability into functions that may be assigned to specialized layers. A directory should therefore state which functions it treats as evidence of a base layer. It should not assume that every project called a blockchain belongs in the same category. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

## Representative Layer 1 networks by architecture family

No named network can be responsibly entered in this directory from the allowed evidence. It does not establish a named candidate’s current operation, Layer 1 status, or architecture family. Adding familiar names without those checks would undermine the inclusion criteria rather than answer the request with a verifiable list.

When evidence is available, a non-ranked table can make entries auditable. For each network, provide:

- **Network name:** the network’s documented identity, separate from its token.
- **Architecture or consensus family:** include only the description supported by current technical documentation; leave the field open when the source does not substantiate a category.
- **Evidence and check date:** link to documentation establishing the base-layer role and architecture, and record when operation and classification were checked.

Group entries only when documentation supports the grouping. Families need not be exhaustive or mutually exclusive, and a network’s inclusion should not be presented as an endorsement, quality assessment, or investment recommendation. Without verified entries, a list cannot fairly claim to represent global coverage; any eventual directory should describe itself as representative and explain its selection limits.

## How to distinguish a Layer 1 network from a Layer 2 or adjacent system

Read the system’s technical documentation to determine which network performs the relevant functions and where it relies on another chain. For example, an Ethereum Layer 2 solution derives some security from Ethereum’s Layer 1 consensus, but the exact guarantee depends on that system’s proof, data availability, settlement, governance, and exit mechanisms. The classification should follow the documented architecture, not a project’s label alone. [source](<https://ethereum.org/developers/docs/scaling/>)

A system documented as a Layer 2 should not be entered as a separate Layer 1 under the definition used here. Nor should the directory list an individual token, wallet, bridge, or application as a base-layer network. This boundary is about the identity and role of the entry; it is not a full technical comparison of Layer 1 and Layer 2 designs.

Some systems combine or separate functions in ways that make a simple label less useful. Hyperledger Fabric, for example, is documented as a permissioned-network model coordinating organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. That description alone does not establish that it belongs in a public crypto-network list. A directory should say whether permissioned systems are in scope and use its stated base-layer test consistently. [source](<https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html>)

For modular systems, sidechains, and appchains, do not force a classification when the documentation does not settle how the system relates to another layer. Record the relevant relationship and mark the entry as ambiguous, or leave it out. A clear exclusion with a reason is more useful than presenting an uncertain label as settled fact.

## How to verify and keep the list current

Treat the directory as a dated reference, not a permanent inventory. For every proposed entry, preserve the technical source supporting its base-layer role and architecture, plus evidence for its operating status and the date each was checked. Revisit the classification when documentation records a launch, migration, or material architectural change. If the evidence is unclear or out of date, flag the uncertainty or omit the entry.

Data records can help investigate a network, but they do not replace the inclusion test. For example, an Ethereum analytics schema separates blocks, transactions, receipts, logs, decoded events, token transfers, traces, and selected account-state records into queryable tables. Those categories describe available data types; their presence alone does not prove that a project qualifies as a Layer 1 or that it is currently operating. [source](<https://docs.cloud.google.com/blockchain-analytics/docs/schema>)

The evidence available here supports criteria and category cautions, but not a verified set of network entries. A completed directory should show its sources and check dates, identify itself as representative rather than comprehensive unless broader coverage is demonstrated, and keep network names distinct from associated assets. This approach answers the classification question without ranking networks or implying that inclusion is advice to buy, hold, or use an asset.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Blockchain Analytics Dataset Schemas](https://docs.cloud.google.com/blockchain-analytics/docs/schema) — Google Cloud; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
