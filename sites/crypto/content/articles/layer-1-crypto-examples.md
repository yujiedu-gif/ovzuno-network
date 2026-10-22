---
title: "layer 1 crypto examples: representative networks and how to identify them"
description: "Explore layer 1 crypto examples by network role and protocol design, and learn how to distinguish a Layer 1 network from a token or Layer 2 system."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 1 crypto examples"
owned_question: "Which blockchain networks are representative layer 1 crypto examples, and what distinguishes a Layer 1 network from a token or a Layer 2?"
risk_level: "medium"
---

Layer 1 crypto examples are base blockchain networks whose own protocol maintains network state and performs core functions such as consensus or transaction execution. The evidence available for this article supports Ethereum as a specific example; it does not verify the protocol architectures of Bitcoin, Solana, or Cardano, so they should not be presented here as confirmed examples. A network is distinct from its native asset, and a Layer 2 operates in relation to an underlying Layer 1.

## What qualifies as a Layer 1 network?

“Layer 1” is commonly used to refer to a blockchain’s base network and its protocol. It is a practical architectural label, not a separately standardized technical category. A useful classification question is whether the network’s own protocol supplies the base environment for validating activity and maintaining state, or whether the system being examined depends on another network for some of those functions.

Blockchains do not all assign functions in the same way. A blockchain can use cryptographically linked transactions, distributed ledger copies, validation, and conflict-resolution rules to maintain a shared history, but participation, consensus, privacy, finality, and governance vary. For that reason, the label should be supported by architecture evidence rather than assumed from a project name or token ticker.

Ethereum offers a concrete example of what protocol-level evidence can look like. An Ethereum full node independently verifies blocks and transactions against protocol rules, rather than relying entirely on another node. Ethereum nodes combine an execution client and a consensus client; a validator client is an additional role required only when a node proposes and attests to blocks. These are Ethereum-specific details, not a universal checklist requiring every Layer 1 to use the same client structure.

The network and its native asset are also different things. Ether is Ethereum’s native cryptocurrency and part of the protocol’s market for computation; Ethereum is the network and protocol environment. Knowing the asset’s name does not, by itself, establish how the associated network is built. To classify a candidate, inspect documentation that explains the network’s protocol and the roles responsible for its operation.

## layer 1 crypto examples: representative networks

A reference list should distinguish verified examples from familiar names that lack support in the evidence at hand. The entries below are illustrative, not exhaustive or ranked. The available claims authorize one confirmed network example; they do not establish a broader list of current network architectures.

- **Ethereum:** Ethereum is a Layer 1 example in this article’s practical sense because it has its own protocol-defined execution and consensus roles, and a full node verifies blocks and transactions against protocol rules. Its node architecture provides specific evidence of base-network functions. This description does not imply that every Ethereum participant runs a validator client: that client is required only for nodes proposing and attesting to blocks.
- **Bitcoin, Solana, and Cardano:** These names are not confirmed examples in this reference list. The evidence supplied here does not verify their current protocol architectures or establish their classification. Their inclusion based only on common usage would go beyond the available support. Check current protocol documentation for each network before treating it as a verified example.

This narrow list reflects an evidence boundary, not a judgment about the networks omitted. A responsible catalog needs evidence about each candidate’s protocol-level functions. A familiar crypto name, asset symbol, or general reputation cannot substitute for that check.

The distinction matters because “network” and “asset” answer different questions. Network documentation describes protocol rules and system roles; an asset description identifies a cryptocurrency. Even where an asset is native to a network, it remains a different category from the network itself. Ethereum and ether illustrate the difference, but this example should not be generalized to claim that every crypto asset is a native asset or that every network has the same asset model.

## Networks, native assets, and Layer 2s are different things

A **network** is the protocol environment whose participating software follows rules for maintaining and validating shared state. A **native asset** is a cryptocurrency associated with a network and used according to that network’s design. A network’s asset may be important to protocol operation, but the asset is not the network, its nodes, or its protocol rules. Check the documentation for the network and the asset separately when a distinction matters.

A **Layer 2** is a separate system that handles some activity in relation to an underlying Layer 1. Ethereum rollups illustrate one architecture: they separate transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. This is a relationship between systems, not a reason to call the rollup itself the underlying Layer 1. Rollups differ in proof systems, data formats, sequencing, upgrade arrangements, and bridge design, so the label alone does not establish all details.

This brief distinction is intended to prevent category errors, not to explain scaling architecture in full. Readers who need a detailed account of how Layer 1 and Layer 2 systems differ and work together should consult the dedicated Layer 1 and Layer 2 explainer.

## How to verify a Layer 1 example

Use a consistent verification process, and keep network-level claims separate from claims about a wallet, application, service, or asset.

1. **Locate current protocol documentation.** Look for material explaining the network’s architecture and rules, not only a project overview or a page naming its cryptocurrency.
2. **Identify the roles the protocol defines.** Check what the network’s own software does to validate activity, maintain state, and reach agreement on updates. The exact roles may differ by network, so do not require Ethereum’s client structure as a template.
3. **Ask what depends on another network.** If the candidate is a separate system that executes activity outside a base network and relies on that network for published data or consensus, examine whether it is being described as a Layer 2 rather than the base network itself. Architecture matters more than the label a project uses.
4. **Separate primary descriptions from analysis.** Official protocol documentation can establish how a project describes its design; independent technical analysis can help assess the meaning or limits of that description. Do not treat a project’s terminology as independent confirmation.
5. **Check dates and scope.** Protocols and supported features can change. Verify that the material is current, and keep claims limited to the network, version, role, or condition actually described.

Classification is only one part of understanding a blockchain. Ethereum’s full-node verification claim, for example, says what that node role checks against protocol rules; it does not establish that every application built on Ethereum behaves correctly. Likewise, knowing that a system is a base network does not, by itself, answer questions about a wallet, exchange, bridge, or other provider. Those involve separate systems and responsibilities.

## What this list does not establish

Inclusion is not a ranking, endorsement, investment recommendation, or guarantee of technical performance. The list identifies a network category, not a conclusion about which network is preferable for a particular person or use. It also does not establish security, transaction fees, yields, recovery options, or compliance status. Those questions require evidence specific to the relevant protocol, application, provider, user circumstances, and—where applicable—jurisdiction.

The evidence boundary is especially important when extending the list. This article does not claim that omitted networks fail to qualify; it states that their classifications are not verified by the supplied evidence. Nor does a Layer 1 label prove that a network has a particular feature or that a service supports it. Readers should verify each separate claim against current, relevant documentation rather than infer it from the category name.

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Node architecture](https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
