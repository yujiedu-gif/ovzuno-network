---
title: "New Layer 1 Crypto: Meaning, Architecture, and Scaling"
description: "Learn what new layer 1 crypto means, how a Layer 1 handles core blockchain functions, and what to check when evaluating its scaling design."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "new layer 1 crypto"
owned_question: "What does “new Layer 1 crypto” mean, and how can readers assess the blockchain’s architecture and scaling approach without confusing it with Layer 2 networks?"
risk_level: "medium"
---

“New Layer 1 crypto” usually means a recently launched or developing crypto network that serves as its own base blockchain, rather than a token or application built on another network. To assess the label, map which functions the network performs itself, what it delegates, and whether scaling claims describe live operation or a planned design. The term alone does not establish performance or security.

## What “new Layer 1 crypto” refers to

“Layer 1” is common terminology for a blockchain’s base network and its protocol. The word “new” refers to the network’s launch or development status; it is not a separate technical category. A new token on an existing blockchain is not, by that fact alone, a new Layer 1: the token may use the existing network’s infrastructure without introducing a separate base network.

A network’s own documentation is needed to determine how it is organized. A name, token description, or marketing label does not demonstrate which functions the system operates or which other systems it depends on. Treat a Layer 1 designation as a classification to verify, not as evidence that a network is independent, fully operational, or capable of a particular performance level.

It is also useful to distinguish a base network from a system that uses one. As an example, an Ethereum rollup separates transaction execution from the base layer while publishing data to Ethereum, where base-layer consensus establishes the published record. That illustrates a different role from operating the base network itself. It is an architectural example, not a description of every system called a rollup or every newly launched chain.

## How a Layer 1 handles blockchain functions

A blockchain’s functions can be mapped before evaluating claims about speed or capacity. **Consensus** is the process through which a network agrees on blocks and its continuing chain. **Execution** processes transactions according to network rules. **State** is the resulting information about the network after transactions are applied. **Data availability** concerns whether relevant data is accessible for checking the recorded activity. **Settlement** identifies where a transaction or state result is established in the ledger.

These functions are related, but a network may assign them to different components. For a particular system, ask which functions are performed by the base protocol, which are handled by additional components, and which depend on outside systems. A layered diagram or protocol description is more informative than a broad label if it identifies those responsibilities.

Then follow the transaction path: who proposes or orders blocks, what software checks them, and how accepted transactions change state. In Bitcoin, full nodes use a peer-to-peer protocol to exchange transactions and blocks and synchronize validated chain data. This is a specific example of network operation, not a universal account of how every Layer 1 communicates or validates activity.

For another concrete example of why responsibilities matter, Ethereum’s documentation describes full nodes as independently verifying blocks and transactions against protocol rules rather than relying entirely on another node. That example does not show that a different network has the same node roles or verification process. Look for the target network’s own documentation about which participants perform checks and what those checks cover.

## Where scaling design choices appear

A scaling claim should be tied to a specific function and component. A throughput figure may concern transaction execution, while a broader capacity claim might rely on how execution, data handling, and settlement work together. Before interpreting a number, establish what is counted and whether the measurement concerns the base network alone or a wider system that includes external components.

Delegating a function changes the architecture readers need to examine. If another chain, service, or protocol handles part of the work, identify that dependency and what role it plays. Do not treat a design as self-contained simply because it is described as a Layer 1. Conversely, a function handled by an additional component does not, without more evidence, establish that the base network is or is not a Layer 1.

Separate design targets from measured results. A planned capacity, roadmap objective, or stated target is not the same evidence as an observed result. For a reported performance comparison, look for a dated, reproducible methodology, the test conditions, what was measured, and which components were included. The available evidence here does not provide benchmark results, fee data, or measurements for a particular new network, so no performance figure or comparison can be inferred.

If documentation omits the method or conditions behind a number, preserve that uncertainty. A result without a clear scope cannot establish a general property of the network. Similarly, architecture descriptions alone do not show what performance users experience under different operating conditions.

## A checklist for assessing a newly launched network

Use this sequence to classify the network and inspect its scaling statements:

1. **Locate primary technical documentation.** Look for a protocol specification or architecture description that explains the network’s rules. Confirm that it identifies consensus, execution, state updates, and data handling. If a role is not explained, record the gap rather than assuming how it works.

2. **Map each function to its component.** Note whether the base network performs each function or whether another chain, service, or protocol is involved. This makes dependencies visible and helps distinguish a base network from systems that use one.

3. **Trace validation and state changes.** Find out which participants and software check blocks and transactions, and how accepted activity changes the ledger state. Do not assume that node roles or verification requirements from another network apply.

4. **Separate live components from plans.** Check what documentation says is operational and what remains proposed, under development, or described as a future target. A launch description does not by itself establish that every component in an architecture diagram is running.

5. **Identify external dependencies and controls.** Look for named outside systems and documented governance or upgrade controls that affect the architecture. If these are not described, treat them as unanswered questions; absence of detail is not proof that there are no dependencies or controls.

6. **Audit every scaling number.** Ask what is measured, whether the figure is a target or a measured result, and whether the date, method, conditions, and included components are disclosed. Avoid extending a narrow result into a claim about the whole network.

7. **Keep the conclusion bounded.** State what the documentation supports and what remains unknown. Require current, attributable evidence before making claims about security, recovery, availability, fees, or compliance; an architecture label does not establish those properties.

## What this explanation does not establish

Being described as a Layer 1 does not, on its own, prove scalability, security, decentralization, or adoption. The architecture examples above illustrate ways to examine responsibilities; they do not establish the design, operational status, benchmark results, or security assumptions of any particular newly launched network.

This is a framework for reading technical claims, not a ranking or recommendation. It can help readers identify whether a network operates as a base layer and what questions to ask about its scaling design. Any conclusion about a specific system requires attributable documentation for that system and must stay within what that evidence shows. No investment, price, legal, tax, or compliance conclusion follows from the phrase “new Layer 1 crypto.”

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin Developer Documentation; retrieved 2026-10-18.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
