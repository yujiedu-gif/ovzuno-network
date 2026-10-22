---
title: "Layer 1 2 3 Crypto: Roles in Blockchain Infrastructure"
description: "Understand layer 1 2 3 crypto: how Layer 1, Layer 2, and Layer 3 can divide settlement, scaling, and application-specific functions."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["blockchain layers", "Layer 2 scaling", "Layer 3 blockchain"]
author: "editorial_team"
primary_keyword: "layer 1 2 3 crypto"
owned_question: "What do Layer 1, Layer 2, and Layer 3 mean in crypto infrastructure, and how can their roles differ in a blockchain system?"
risk_level: "medium"
---

Layer 1, Layer 2, and Layer 3 are labels for infrastructure roles, not a universal blueprint. Layer 1 generally refers to a blockchain’s base network; Layer 2 describes systems designed to operate in relation to that base; and Layer 3 is used in some architectures for further specialized or application-focused systems. What each layer actually executes, records, or settles depends on the specific design.

## What the layer labels describe

A **blockchain layer** is a way to describe how infrastructure functions are organized. One useful framework separates execution, settlement, consensus, and data availability. Execution means processing transactions or application logic; settlement concerns the system where relevant outcomes are recorded or resolved; consensus is how network participants agree on the chain’s state; and data availability concerns whether participants can obtain the data needed to verify state changes. These functions can be combined or assigned to different layers. In a monolithic design, a base layer performs multiple functions together; a modular design can assign them to specialized layers. Projects may group or name these functions differently, so the framework is a guide to responsibilities rather than a mandatory blueprint. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

**Layer 1 (L1)** usually means the underlying blockchain network. As one example, Ethereum nodes use a consensus mechanism to agree on new blocks and the continuing chain. Ethereum full nodes independently verify blocks and transactions against protocol rules. This illustrates base-network functions, but it does not define every L1’s architecture. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>) [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

**Layer 2 (L2)** generally refers to a system designed to handle activity in relation to an L1. The label does not specify exactly which functions the L2 performs or which responsibilities remain with the base network. An Ethereum rollup, for example, separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. That is a specific architecture, not a universal definition of every system called L2. [source](<https://ethereum.org/developers/docs/scaling/>)

**Layer 3 (L3)** is used in some architectures for an additional specialized layer, often associated with particular applications or functions. The evidence available for this article does not establish a universal technical definition for L3. Treat the term as a project’s label, then consult its documentation to learn which functions the system actually performs and what other infrastructure it depends on.

The distinction between a role and a label matters. A project can call something a layer without that name proving where its transactions execute, where the corresponding data is recorded, or what system provides consensus. Those details come from the architecture, not the number in the name.

## Layer 1, Layer 2, and Layer 3 roles

A useful first distinction is between a base network and systems that perform activity in relation to it. L1 is the underlying chain in a layered design. An L2 may take on transaction execution or other processing while relying on an L1 for some functions. An L3, where present, may add another specialized environment. These are common ways the terms are used, not guaranteed assignments of responsibility.

The labels alone cannot tell a reader where execution, data availability, or settlement occurs. A design may separate those functions, combine them, or assign them to different components. Even the word “settlement” needs context: documentation should specify which system records the relevant result and what role the base network has in that process.

Consider a conceptual path—not a rule for every architecture—in which an application-specific system handles activity, passes information to an L2, and connects to an L1 for a particular recording or settlement function. Another system might combine roles, omit an additional layer, or use a different path. The diagram below is therefore a question-asking aid, not a claim that every transaction traverses three systems in order:

**Application or specialized activity → possible L3 → possible L2 → possible L1**

At each arrow, ask what is being passed: a transaction, data, a message, or a state update. The architecture may not use every component shown, and a named layer may not correspond to a separate blockchain. Project documentation is needed to establish the actual boundaries.

## How blockchain layers can interact

Layers interact through mechanisms the specific system defines. In the Ethereum rollup example, execution takes place away from the base layer, while data is posted to Ethereum. This distinguishes where execution happens from where data is published. It does not, by itself, establish every security, recovery, or operational detail of a particular rollup. [source](<https://ethereum.org/developers/docs/scaling/>)

An L3 might rely on an L2, an L1, or other infrastructure, depending on its design. To trace those dependencies, identify which components process activity, where relevant data is published or can be obtained, and what mechanism passes messages or state between components. If a bridge or messaging system is involved, examine its specific role and assumptions rather than treating the connection as automatic or risk-free. The layer label alone does not identify the communication mechanism.

Responsibility can also be split among more than blockchain layers. Hyperledger Fabric, as one permissioned-network example, coordinates organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. This illustrates why a system’s functions may be distributed among several technical and organizational components. Fabric is one network model, not a template for every blockchain or a definition of L1, L2, or L3. [source](<https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html>)

When reading an architecture description, separate the protocol’s responsibilities from those of applications and services around it. A protocol may define how a network handles blocks or records, while applications and other components participate in constructing, routing, or displaying activity. A diagram is most useful when it names both the components and the specific tasks assigned to them.

## What layered designs can change—and what they do not guarantee

Separating functions can let a system assign work to specialized layers rather than having one base layer perform every role. That describes an architectural approach, not a guaranteed result. Calling a system “Layer 2” or “Layer 3” does not establish lower fees, faster confirmations, greater security, or uninterrupted availability. Those outcomes would require evidence about the particular system and its operating conditions, which the labels do not provide.

Additional components also create more relationships to understand. If one system relies on another for execution, data, settlement, or communication, a reader needs to identify the dependency and the assumptions behind it. A layer number does not show whether those components have independent operators, how an upgrade is handled, or what happens during a disruption. Such questions require project-specific documentation rather than inference from a category name.

The same caution applies to security descriptions. A project might rely on an underlying network for some functions while using separate mechanisms for others. The general role label does not establish the extent of that reliance or prove that all parts of the system share the same security properties. Assess each documented mechanism on its own terms.

Do not assume every component, asset, or service operates on the same chain. A layered design can include protocol elements and surrounding services with different responsibilities. Understanding the system means distinguishing what the base network does from what the application, provider, wallet, or other infrastructure does. The label alone does not resolve that boundary.

## Questions to ask when evaluating a specific architecture

Use current, project-specific technical documentation to build a responsibility map. Start with the components, then record what each one does and what it depends on. These questions can guide that review without presuming that a particular project uses a standard architecture:

- **Where does execution happen?** Identify the system that processes transactions or application logic. Check whether another layer performs a different part of the work.
- **Where is data published, and who can obtain it?** Do not infer data availability from an L1, L2, or L3 label. Look for the system’s own description of how relevant data is provided.
- **What does the L1 contribute?** Determine whether the documentation assigns it consensus, settlement, data publication, or another role—and what is handled elsewhere.
- **How do components communicate?** Identify any bridge, messaging, or state-transfer mechanism. Note which systems it connects and what assumptions the project documents.
- **What are the upgrade and recovery arrangements?** Look for descriptions of how changes are made and what happens if a component or operation fails. Do not assume the answer from the layer name.
- **Which claims are project-specific?** Verify statements about security, fees, speed, access, or availability in current documentation. General layer terminology does not establish those properties.

Regulatory, tax, access, fee, availability, and compliance questions also depend on the relevant service and circumstances. The layer labels alone do not answer them, and this conceptual comparison does not provide jurisdiction-specific conclusions.

In short, use L1, L2, and L3 to organize questions about infrastructure roles and dependencies. Then verify what each named system executes, records, and relies on. The labels can help describe an architecture, but they are not a universal map, a performance comparison, or a guarantee about how a particular network behaves.

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
