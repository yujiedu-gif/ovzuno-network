---
title: "UTXO Blockchain List: Notable Networks and Scope"
description: "Explore a scoped UTXO blockchain list, with notable network examples, inclusion criteria, and distinctions to verify before comparing transaction models."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["utxo blockchains list"]
author: "editorial_team"
primary_keyword: "utxo blockchain list"
owned_question: "Which notable blockchain networks use a UTXO-based transaction model, and what distinctions should readers check before treating them as comparable?"
risk_level: "medium"
---

A reliable UTXO blockchain list should include a network only when primary technical documentation explicitly establishes that its transaction model uses unspent transaction outputs, and should name the layer the documentation covers. The evidence available for this article does not verify a named network as a UTXO example, so the list below provides inclusion and comparison criteria rather than unsupported entries.

## What qualifies a network for this UTXO blockchain list?

UTXO stands for “unspent transaction output.” In this model, a transaction spends one or more specific outputs that have not yet been spent. To qualify for a reference list, a technical source must establish that this model applies to the network or layer being named. A project’s branding, token association, or feature described as “UTXO-like” does not independently prove that the network uses UTXOs.

Scope is important. Documentation about a layer or application does not automatically classify the underlying network. For example, an Ethereum rollup separates transaction execution from the base layer while publishing data to Ethereum; that illustrates why a reader must check which layer a source describes, rather than treating every component as one undifferentiated network. [source](<https://ethereum.org/developers/docs/scaling/>)

Software frameworks require the same care. The Cosmos SDK is a modular framework for building customized application-specific blockchains from reusable and custom modules. That fact alone does not establish the transaction model used by a chain built with the framework. Nor does modular application code prove that execution, consensus, settlement, and data availability operate on separate security layers. [source](<https://docs.cosmos.network/v0.47>) [source](<https://docs.cosmos.network/v0.47>)

This is a scoped, non-exhaustive directory approach, not a ranking. A well-supported entry identifies the network, the specific layer, and the primary technical material that establishes its transaction model. If the source describes only a component or feature, limit the entry to that component or feature.

## Notable UTXO-based blockchain networks

No named network can be listed here as a verified UTXO example: the allowed technical evidence does not establish that model for a specific network. This is a limitation of the evidence for this article, not a claim that no networks use UTXOs.

To create a verified entry, record the network name and layer, then cite protocol specifications or developer documentation that directly describes the transaction model. Preserve the source’s scope: evidence about a particular application, secondary layer, or transaction feature should not be restated as a claim about the entire underlying network.

A candidate list might also record what the source does not establish. A statement confirming a transaction model does not, by itself, show that two networks share the same validation rules, scripting system, asset support, or contract capabilities. Those attributes need separate evidence for each network. Avoid borrowing one network’s documentation to fill a gap in another’s.

The distinction is useful when a network has layers with different roles. A source may describe activity on one layer while another layer handles a different part of the system. For instance, rollup architecture can separate execution from the base layer while publishing data to Ethereum, but that does not make every rollup or base network interchangeable. [source](<https://ethereum.org/developers/docs/scaling/>)

## How UTXO networks can differ

A shared transaction-model label is only one architectural fact. Before treating two verified entries as comparable, check the network-specific documentation for transaction validation, scripting, asset support, and smart-contract capabilities. The available evidence does not establish those details for named UTXO networks, so it cannot support a comparison or ranking on those dimensions.

Keep base-layer design distinct from features provided by secondary layers or applications. A framework can help developers assemble application-specific blockchains without specifying the transaction model of every resulting chain. Likewise, a rollup description must be read at the layer it covers; it should not be stretched into a claim about the full stack. [source](<https://docs.cosmos.network/v0.47>) [source](<https://ethereum.org/developers/docs/scaling/>)

Do not infer performance or operational properties from the UTXO label. A transaction-model classification alone does not establish throughput, privacy, fees, security outcomes, recovery options, or availability. Each question needs evidence for the particular network, feature, and conditions under consideration. The same caution applies to claims about asset support: a network classification is not a catalog of which assets or applications it supports.

## How to verify a network’s transaction model

Start with protocol specifications or developer documentation from the network or the relevant layer. Look for an explicit description of how its transaction system represents and spends outputs. Record the exact scope alongside the proposed list entry: network-wide, layer-specific, or feature-specific.

Next, distinguish protocol behavior from supporting software. Documentation about a framework may explain how a chain is assembled, but that does not necessarily describe the resulting chain’s transaction rules. The Cosmos SDK’s modular framework role is not itself evidence that a particular chain is UTXO-based. [source](<https://docs.cosmos.network/v0.47>)

Check what a source actually documents before relying on a secondary summary. An API schema, explorer, or index can expose information about chain activity, but that is not automatically evidence of the transaction model. For example, an archived Blockscout API V2 schema includes an indexing-status endpoint alongside other resources; this illustrates an API implementation detail, not proof that any network is UTXO-based. [source](<https://raw.githubusercontent.com/blockscout/blockscout-api-v2-swagger/main/swagger.yaml>)

If the technical materials are ambiguous, preserve that uncertainty. Identify the source and layer, state only what the documentation supports, and leave the candidate unverified if no primary material directly establishes the classification. A list built this way may be shorter, but its entries are traceable to evidence rather than inferred from labels.

## What this list does not establish

A UTXO classification does not establish that a network is suitable for a particular use, widely adopted, available under specific conditions, or better-performing than another network. It also does not establish fees, yields, security outcomes, recovery options, or compliance status. These questions need current evidence specific to the network and the circumstances being assessed; they cannot be answered by the transaction-model label alone.

The same limits apply to architecture descriptions. A framework’s modularity does not prove that a particular chain has separate security layers, and a description of one rollup layer does not establish the behavior of every network or application associated with it. [source](<https://docs.cosmos.network/v0.47>) [source](<https://ethereum.org/developers/docs/scaling/>)

For a practical reference list, include only candidates whose technical documentation supports the UTXO classification at the stated scope. Keep the source, layer, and unresolved distinctions visible. Where the evidence supplied here does not verify a named network, omission is more accurate than presenting an unsubstantiated example.

## Sources and references

- [Cosmos SDK Documentation: Explore the SDK](https://docs.cosmos.network/v0.47) — Cosmos SDK Documentation; retrieved 2026-10-19.
- [Cosmos SDK Documentation: Explore the SDK](https://docs.cosmos.network/v0.47) — Cosmos SDK Documentation; retrieved 2026-10-19.
- [Blockscout API V2 OpenAPI Specification](https://raw.githubusercontent.com/blockscout/blockscout-api-v2-swagger/main/swagger.yaml) — Blockscout GitHub Repository; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
