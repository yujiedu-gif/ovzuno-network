---
title: "Daml Smart Contract Language: Concepts and Ledger Model"
description: "Learn what the daml smart contract language is, how its contract and choice model represents ledger workflows, and what depends on the platform running it."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Daml programming language", "smart contract programming language", "ledger model"]
author: "editorial_team"
primary_keyword: "daml smart contract language"
owned_question: "What is the Daml smart contract language, and how does its model for defining ledger workflows work?"
risk_level: "medium"
---

The authorized evidence does not establish Daml-specific language semantics, so it cannot support a reliable definition of the Daml smart contract language or an account of how its templates, parties, choices, or ledger workflows work. It does support a narrower distinction: general smart-contract capabilities and access-control patterns do not establish the behavior of a particular language or platform. A Daml-specific explanation requires current Daml documentation for the language version and environment in question.

## What the Daml smart contract language is

The evidence available for this article contains no accepted Daml-specific claim. It therefore does not substantiate what Daml is intended to do, how it defines application logic, or whether it is designed specifically for ledger workflows. Describing Daml in those terms without a primary source would exceed what the evidence supports.

That limitation is not evidence that Daml lacks a feature or purpose. It means that the permitted evidence does not verify the language’s definition. General descriptions of smart contracts cannot fill this gap: a claim about what a deployed contract can do does not establish what a particular programming language means by “contract” or how that language represents an application workflow.

For a grounded definition, the relevant source would be a current Daml language reference or official documentation that identifies the language’s intended use and terminology. The reader should also note the documented version: language semantics and platform behavior should not be treated as interchangeable simply because both are discussed under the same product or technology name.

## How Daml models contracts and workflows

The permitted evidence does not verify Daml’s concepts of templates, contract instances, parties, or choices. It cannot establish that a template defines a contract type, what information a contract stores, or what role a party has in a Daml workflow. Nor does it substantiate how a choice is declared or what conditions govern its exercise.

A general access-control example illustrates why language-specific evidence matters. Role-based access control can separate permissions into named roles, while administrators can grant or revoke those roles; the resulting authority relationships need to be secured. This is a documented access-control model, not a description of Daml. It does not establish whether Daml uses named roles, how Daml identifies participants, or how its ledger enforces authorization. [source](<https://docs.openzeppelin.com/contracts/5.x/access-control>)

A reader investigating Daml should look for explicit definitions in the language reference for the version under consideration. In particular, the documentation would need to explain the relationship among workflow participants, contract data, permitted actions, and any authorization rules. Without that source, it would be misleading to supply a Daml example or present familiar terminology from another system as if it applied to Daml.

## What happens when a choice is exercised

The evidence does not establish what a Daml choice is or what its exercise does. It cannot support a claim that a choice creates or archives contracts, changes ledger state in a particular way, or follows the same transaction behavior across Daml-compatible platforms. Those are specific semantic and implementation questions, and they need Daml-specific documentation.

A broader statement about smart contracts is available: a deployed contract can hold and manage onchain assets and apply programmed actions when receiving or transferring them. The evidence conditions this behavior on a transaction or another supported trigger and enough gas, and notes that behavior depends on the program’s correctness and inputs. This is a general smart-contract capability, not an account of Daml choices or their ledger effects. [source](<https://docs.chain.link/getting-started/conceptual-overview>)

The distinction is important when interpreting technical explanations. A general description of program execution cannot tell a reader which state transitions a particular language permits, what authorization conditions it specifies, or how a selected platform processes an action. To answer those questions, documentation must address the language semantics and the relevant runtime or ledger rather than relying on analogy.

## Language semantics versus platform behavior

A language reference describes what the language defines; a platform’s documentation is needed to establish what a particular runtime or ledger implements and operates. The authorized evidence does not identify a Daml runtime or ledger, or describe Daml deployment, transaction processing, interoperability, or operational controls. It therefore cannot establish how those capabilities work or whether they are identical across environments.

The same evidence limit applies to availability, fees, performance, recovery, security properties, regulatory status, tax treatment, and jurisdictional access. No conclusion about those topics follows from a programming-language name or from general smart-contract behavior. They would require current, authoritative evidence specific to the relevant platform, service, or context.

This boundary prevents three different questions from being conflated: what a language’s semantics specify; what a ledger or runtime implements; and what an application or its operators provide. General access-control patterns and contract capabilities can help frame questions, but they do not establish Daml’s answers. In particular, the role-based permissions example above cannot be expanded into a claim about Daml authorization, and the general contract-action description cannot be expanded into a claim about Daml transaction processing.

## When to investigate Daml further

For a version-specific technical assessment, consult current primary Daml documentation and verify its definitions of contracts, participants, choices, authorization, and state changes. Then examine documentation for the specific runtime or ledger to establish what happens during transaction processing and which deployment or operational properties belong to that environment. The available evidence does not supply those Daml-specific details, so this article does not infer them.

The supported conclusion is deliberately bounded: general smart-contract and access-control claims provide context, but they do not define the Daml smart contract language or establish how its workflow model works. A complete explanation of Daml’s templates, parties, choices, and ledger effects requires Daml-specific sources for the relevant language version and platform.

## Sources and references

- [Smart Contract Overview](https://docs.chain.link/getting-started/conceptual-overview) — Chainlink Documentation; retrieved 2026-10-19.
- [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control) — OpenZeppelin Documentation; retrieved 2026-10-19.
