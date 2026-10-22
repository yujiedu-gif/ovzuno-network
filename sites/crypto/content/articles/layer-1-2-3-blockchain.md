---
title: "Layer 1 2 3 blockchain: How the architecture labels relate"
description: "Understand what layer 1 2 3 blockchain labels commonly describe, how their roles can differ, and why definitions vary across blockchain systems."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 1 2 3 blockchain"
owned_question: "What do Layer 1, Layer 2, and Layer 3 mean in blockchain architecture, and how can their roles differ across systems?"
risk_level: "medium"
---

Layer 1 usually means a blockchain’s base network, Layer 2 usually describes a system that relies on a base chain for some functions, and Layer 3 is a label whose meaning varies by project. To understand a particular design, trace where it performs execution, settles results, reaches consensus, and makes data available; the layer number alone does not settle those questions.

## What the layer numbers describe

Layer labels are architectural shorthand. They can suggest how one system relates to another, but they do not form a universal taxonomy with identical definitions across every blockchain. A useful interpretation starts with the system’s documented functions and dependencies, rather than assuming that a familiar label carries the same technical meaning everywhere.

One way to organize those functions is to distinguish **execution**, **settlement**, **consensus**, and **data availability**. Execution means processing operations and producing state changes; settlement concerns recording or resolving those results; consensus is the process by which network participants agree on blocks or state; and data availability concerns whether relevant data is accessible for checking the published result. A modular architecture model separates these functions so that specialized layers can perform them. It is an analytical model, not a rule that every blockchain must use the same arrangement. [^1]

That distinction matters because a diagram’s numbered boxes are names assigned within a particular design. To interpret them, ask what each component does and which other component it depends on. A project may use “Layer 2” or “Layer 3” as shorthand for a relationship, but the term does not replace a description of the actual architecture.

## Layer 1: the base network

Layer 1 commonly refers to a base blockchain: the underlying network and protocol. A blockchain can be described as a database shared across networked computers, where blocks cryptographically reference earlier blocks and nodes use consensus to agree on state. [^2] The label “Layer 1” points to this underlying network, but does not by itself specify every mechanism or function it provides.

A transaction’s path into a shared ledger helps explain the base-network role. At a high level, a transaction must be cryptographically authorized, checked against network rules, grouped into a block, and included through a consensus decision. These steps are part of the process by which a transaction becomes part of the shared ledger. [^3]

The term “Layer 1” does not require every design to handle all functions in the same way. Some architectures combine execution, settlement, consensus, and data availability at a base layer; other architectures may assign functions to specialized components. The four-function model is one way of examining those choices, not a claim that every base network has identical responsibilities. [^1]

For a reader encountering the label, the practical question is therefore not just “Which chain is Layer 1?” It is also “Which rules does this base network enforce, and what roles does the project assign to it?” The answers depend on the network’s own design. The label offers an initial reference point, while the documentation explains what the network actually does.

## Layer 2: systems built around a base chain

Layer 2 is commonly used for systems built on or connected to a base chain. In the Ethereum context, an Ethereum Layer 2 solution derives some of its security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. The exact guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. [^4]

This is a relationship, not a complete description of a particular mechanism. The label alone does not tell a reader where execution occurs, how a result is settled, or which network provides the data needed to check that result. It also does not mean that every system called Layer 2 has the same dependencies or receives the same guarantees. The architecture and its stated conditions must be examined separately.

A useful distinction is between the broad label and the evidence for a specific dependency. If documentation says that a system relies on a base chain for a function, identify that function and the conditions attached to it. Do not infer that it relies on the base chain for every function, or that its whole security model is inherited automatically. The Ethereum-specific description above is an example of how the term can be used; it should not be treated as a universal definition for all networks.

## Layer 3: a label with multiple uses

Layer 3 has no single universally applied definition in the evidence used here. A project may use the term for an additional execution layer or an application-focused component, but those descriptions cannot be treated as a standard definition for every system. The name alone does not establish what the component executes, where its results are settled, or which network supplies consensus or data availability.

When a project calls a component Layer 3, use that as a prompt to inspect its architecture documentation. Look for the functions the project assigns to the component and the relationships it describes with other layers. Does the component execute operations? Where are the resulting changes settled? Which network, if any, provides consensus or data availability? If those details are not made clear, the number in the label cannot fill in the missing information.

It is also important to separate a project’s naming convention from technical roles that can be independently described. The four-function model—execution, settlement, consensus, and data availability—can help organize questions about a Layer 3 component, but it does not prescribe what “Layer 3” must mean. [^1] The same label may therefore refer to different arrangements in different project materials.

## How to read a three-layer diagram

Treat a three-layer diagram as a map of one documented design, not as proof of a universal blockchain stack. Follow the connections and record which component is responsible for each function. This keeps architectural claims attached to the system that makes them instead of importing assumptions from another project’s terminology.

A practical reading sequence is:

1. **Locate execution.** Identify where the design processes operations and produces state changes. If the diagram does not say, consult the accompanying architecture description rather than guessing from the layer number.
2. **Trace settlement.** Find where the design records or resolves those results. The component doing execution need not be assumed to be the component assigned settlement responsibilities; the design must specify the relationship.
3. **Check consensus.** Identify which network’s rules are used to agree on blocks or state. A diagram that shows a connection to a base network does not, by itself, establish the extent of that dependency.
4. **Look for data availability.** Determine which component is responsible for making the relevant data available, if the documentation specifies this. Data availability is a distinct function in the modular model, so it should not be inferred solely from an execution or settlement label. [^1]
5. **Read dependency statements carefully.** If the project says it relies on another network, note which function it relies on that network for and any stated conditions. For Ethereum Layer 2 systems, for example, the precise security relationship depends on the system’s proof, data availability, settlement, governance, and exit mechanisms. [^4]

This sequence helps distinguish what a diagram names from what its components do. A simple stack drawing may place boxes in an order, but the drawing’s labels should be checked against explanatory documentation. If roles are combined, distributed, or left unspecified, record that rather than assuming a standard arrangement.

## What the layer labels do not establish

A Layer 1, Layer 2, or Layer 3 label alone does not establish a system’s speed, cost, security, decentralization, interoperability, recovery options, or operational availability. Those are separate properties that require evidence about the specific network and design. The supplied architecture definitions support using the labels as signposts, not as a scorecard or a guarantee.

Nor does a number automatically show that one component inherits every property of another. A documented dependency may concern only a particular function, and the conditions can matter. For example, the Ethereum Layer 2 description ties the exact security guarantee to proof, data availability, settlement, governance, and exit mechanisms—not simply to the presence of a Layer 2 label. [^4]

The safest reading is to use layer terminology to orient yourself, then verify the functions and dependencies in the project’s own documentation. If a project’s definition of Layer 3 is not explicit, treat that meaning as unresolved rather than supplying a universal definition. The same rule applies to any diagram: rely on described technical roles, not on the number alone.

[^1]: [Celestia Documentation, “Celestia’s Data Availability Layer”](https://docs.celestia.org/learn/celestia-101/data-availability/).
[^2]: [ethereum.org, “Technical Intro to Ethereum”](https://ethereum.org/developers/docs/intro-to-ethereum/).
[^3]: [NIST, “Blockchain Technology Overview”](https://csrc.nist.gov/pubs/ir/8202/final).
[^4]: [ethereum.org, “Scaling”](https://ethereum.org/developers/docs/scaling/).

## Sources and references

- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
