---
title: "L1 crypto projects: what the term means and how to identify them"
description: "Learn what l1 crypto projects are, which blockchain functions define a Layer 1, and how to distinguish a base network from a Layer 2."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["1 crypto projects"]
author: "editorial_team"
primary_keyword: "l1 crypto projects"
owned_question: "What does L1 crypto project mean, and how can readers identify a project whose blockchain operates as a Layer 1?"
risk_level: "medium"
---

An “L1 crypto project” is a project that operates or builds a blockchain serving as a base network. To identify one, check the architecture: which network validates or orders transactions, maintains a ledger, and handles functions such as execution or settlement—and whether it relies on another chain for those functions. The label alone is not enough; classify the documented design, not the marketing description.

## What does “L1 crypto project” mean?

“Layer 1” is common terminology for a blockchain’s base network and its protocol, rather than a separately standardized technical category. In this article, an L1 crypto project means a project that operates or builds that foundational network. The phrase identifies an architectural role; it is not a category of token by itself.

Keep the network distinct from the things built around it. A blockchain network has its own architecture and responsibilities. An application can use network capabilities, while an asset can be associated with a network without being the network. A project may also involve multiple organizations, software components, and services, so its public-facing name alone does not tell you which component performs each network function.

A permissioned-network example illustrates why “project” can cover several parts: a Hyperledger Fabric network coordinates organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. Those components describe one permissioned-network model, not a universal definition of every L1 project.

Because “Layer 1” is common usage rather than a single standardized category, classification should follow documented responsibilities. Ask what the network itself does and what it depends on other systems to do. If the documentation does not make a role clear, record the uncertainty rather than assigning a label based on a token name or broad project description.

## Which functions identify a Layer 1 blockchain?

Start with the ledger and validation role: which network maintains the transaction record, and what rules does it use to validate activity? A blockchain can be understood as a distributed ledger whose records are linked and maintained according to network rules, but participation, consensus, privacy, finality, and governance vary among systems. Therefore, “it has a ledger” is not enough to establish exactly how a particular network works.

Next, identify how the system reaches agreement about its records. Documentation should describe the consensus process and who can participate in relevant roles. Network participation can be permissionless, with participation open to participants, or permissioned, with access controlled by identified operators; real systems may combine open transaction submission with restricted validation or other controls. Do not assume that one participation model defines all Layer 1 networks.

Then locate execution and settlement. Execution means processing transactions or application instructions; settlement refers here to recording or confirming resulting state under network rules. These functions are not arranged identically in every architecture. Some designs assign execution, settlement, consensus, and data availability to one base layer; modular designs can assign those functions to specialized layers. These are architectural patterns, not a rule that every network must fit one pattern exactly.

For a concrete example of how to inspect roles, an Ethereum full node independently verifies blocks and transactions against protocol rules rather than relying entirely on another node. That statement concerns Ethereum’s full-node role; node roles and verification requirements differ across networks. For another permissioned-network example, Fabric’s documented components show why a classification should consider the whole system, not just its ledger or smart-contract component.

A project may provide some functions while depending on other systems for others. The useful conclusion is therefore specific: name the functions the project’s network handles, identify dependencies that documentation supports, and avoid assuming that every blockchain supplies every service itself.

## How to distinguish an L1 project from a Layer 2

Ask whether the system relies on another blockchain for a core function, rather than deciding by its name. In L2BEAT’s terminology, a rollup uses a Layer 1 for consensus and data availability; systems that publish data elsewhere add external data-availability assumptions and are classified differently in that terminology. Industry use of “L2” is not fully uniform, so state the terminology being applied and trace the architecture instead of treating a label as conclusive.

The distinction is about the relationship between systems and the functions they perform. A project might describe itself as a base network, but the label alone does not show where consensus, data availability, execution, or settlement occurs. Look for technical documentation that identifies those responsibilities and any reliance on a separate network. If the roles are shared or the documentation is incomplete, describe the uncertainty rather than forcing a simple classification.

Do not confuse a bridge with the base network itself. Bridges coordinate token, message, data, or contract-call activity between otherwise isolated blockchain environments. That cross-chain role does not, on its own, establish which network is the base layer for a particular system. Keep bridge design separate from the question of which network performs the underlying layer functions.

This is a classification prompt, not a full Layer 1-versus-Layer 2 comparison. For the detailed comparison of how the layers differ or work together, consult a dedicated explainer.

## A practical checklist for assessing project claims

Use a consistent review process to make the classification traceable:

1. **Find the technical architecture documentation.** Look for descriptions of the network, ledger, node roles, and dependencies. If documentation does not explain a function, mark it as unclear rather than inferring an answer from a label.
2. **Trace transaction handling.** Record which network validates or orders activity and maintains the relevant ledger. If more than one system participates, note the role assigned to each in the documentation.
3. **Locate execution and settlement.** Check where application instructions are processed and where resulting state is recorded or confirmed. Do not assume these responsibilities always sit together.
4. **Check consensus and participation.** Identify which network coordinates agreement over its ledger and who is permitted to take part in relevant roles. Note any restrictions or shared responsibilities the design documents.
5. **Map dependencies.** Check whether another chain supplies consensus, data availability, settlement, or another core function. Distinguish the project’s own responsibilities from functions it obtains elsewhere.
6. **State the conclusion with limits.** Explain what the documentation supports, which terminology you used, and what remains uncertain. If the architecture is shared, modular, or evolving, describe that instead of forcing a simple label.

This checklist is an evidence-gathering method, not a formal certification. Its purpose is to make the reasoning transparent and repeatable. It does not imply that every architecture fits a single neat category, or that a project’s own terminology has been independently established by the checklist.

## What this classification does not establish

Calling a project an L1 identifies an architectural role. It does not by itself establish scalability, decentralization, security, adoption, or network performance. Those questions require separate evidence about the specific design and operating conditions. A description of functions is not proof that a system achieves every goal associated with its design.

Nor is L1 status a recommendation or a complete risk assessment. It says nothing on its own about whether a project suits a particular user or business need. Availability, fees, legal or tax treatment, and compliance obligations are separate questions that require current, relevant evidence; they are not answered by layer classification. Keep those questions outside this classification unless they are independently documented and assessed.

The practical takeaway is simple: use “L1” to describe a project’s relationship to a base blockchain only after tracing documented network responsibilities and dependencies. Where the evidence does not resolve a role, say so. That approach preserves the term’s usefulness without treating a label as a technical guarantee.

## Sources and references

- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
