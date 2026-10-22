---
title: "Cryptocurrency layers explained: roles, relationships, and trade-offs"
description: "Cryptocurrency layers explained through base-layer and scaling roles, how networks connect, and the trade-offs behind different blockchain designs."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["cryptocurrency layers"]
author: "editorial_team"
primary_keyword: "cryptocurrency layers explained"
owned_question: "What are cryptocurrency layers, how do common layer labels describe where blockchain work occurs, and what trade-offs do these designs introduce?"
risk_level: "medium"
---

Cryptocurrency layers are descriptive groupings of blockchain functions and relationships, not a universal set of numbered components. A base layer commonly supports shared network rules and records, while a scaling layer may execute activity separately and publish data or results in relation to that base. The exact division of work—and the assumptions a system relies on—depends on its design.

## What “layers” means in a cryptocurrency system

A layer is a way to describe where particular network work occurs or how separate systems relate. It is an architectural map, not necessarily a formal protocol category. The labels can help organize questions about transaction processing, shared history, and how components exchange information, but a label alone does not establish a system’s properties.

One useful model separates four functions: execution, settlement, consensus, and data availability. In that model, specialized layers can be assigned different functions. The model is a way to describe an architecture, not a rule that every blockchain must use separate components for all four jobs. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

These terms also should not be confused with cryptocurrency assets, tokens, or token standards. A layer describes a network role or relationship; it is not an asset. To understand a particular system, identify its components and responsibilities rather than inferring them from a layer number or name.

## How a base layer handles shared network work

A base layer, often called Layer 1, is the underlying blockchain in a layered design. It commonly provides protocol rules and a shared history that other components may rely on. The exact work done at this layer differs across networks, so the label is only a starting point for examining the protocol.

Ethereum offers one example of how a blockchain can maintain ordered history: each block references its parent cryptographically, creating a chain of network state. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>) Ethereum full nodes independently verify blocks and transactions against protocol rules rather than relying entirely on another node. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>) These are Ethereum-specific descriptions; they should not be treated as universal requirements for every network or every kind of node.

When assessing a base layer, ask which functions it performs directly and which it delegates or shares with other systems. The four-function map—execution, settlement, consensus, and data availability—helps structure that inquiry. It does not establish that a particular protocol provides every function in the same way, or that a component’s role is identical across networks. Protocol documentation is needed to establish those details.

## Where scaling layers fit

A scaling layer is a system intended to handle activity in relation to a base layer. Rollups provide one example: they separate transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. [source](<https://ethereum.org/developers/docs/scaling/>) This describes a specific architectural pattern, not every system called a scaling layer.

To understand the division of work, ask three questions: where are transactions executed, what information is published to the base layer, and what role does that base layer play in the resulting record? A design may perform execution outside the base layer while relying on the base layer to establish a published record. Other systems may divide these functions differently.

The term “Layer 2” does not, by itself, explain how a system handles proofs, data publication, transaction sequencing, upgrades, or exits. Nor does the label establish a particular speed, fee, or availability outcome. Those are system- and condition-specific questions; do not infer their answers from a layer name or from the fact that execution occurs elsewhere.

## How layers connect—and where assumptions enter

A useful conceptual path begins with a user action in an application. The application may pass that action to a network component for processing; that component may then publish data or results in relation to another layer. The sequence and responsibilities depend on the design. The rollup pattern described above illustrates one arrangement: execution is separated from the base layer, while data is posted to Ethereum. [source](<https://ethereum.org/developers/docs/scaling/>)

Trace each handoff in the system’s documentation. Identify which component receives an action, which processes it, and what another component is expected to verify or record. If a system depends on a base layer, determine exactly which function that layer supplies. “Connected to” or “built on” does not, without further detail, establish the extent of that dependence.

The same care applies to statements about security or recovery. A claim that a system “inherits security” needs to specify which properties are meant and how the relevant mechanism works. The general layer map does not establish a particular system’s data-availability design, verification process, operator responsibilities, upgrade controls, or recovery path. Those details must be checked for the specific protocol; they cannot be supplied by the layer label itself.

## Trade-offs to compare across layer designs

Use the layer map as a checklist, not a scorecard. First, locate execution, settlement, consensus, and data availability in the design. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>) Then examine how those functions are implemented and which components other parts of the system rely on. This makes it easier to distinguish a protocol’s stated architecture from assumptions that arise at connections between components.

Next, compare the documented security assumptions and operational dependencies. Ask what information is available for verification, what role the base layer plays, and what the design documentation says about failure and recovery. The general architecture model does not answer these questions for any particular network. A meaningful comparison therefore requires current, protocol-specific documentation and independent technical analysis rather than a ranking based on layer labels.

Finally, keep performance and other practical claims separate from architectural terminology. Fees, yields, availability, regulation, tax, and compliance are not established by calling a system a base layer or scaling layer. Each requires current, appropriately scoped evidence. The useful result of a layer map is a clearer set of questions: identify where work happens, trace how components depend on one another, and investigate the assumptions the specific design documents.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
