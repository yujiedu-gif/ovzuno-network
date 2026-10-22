---
title: "Solidity type creationcode: What It Returns and How It Is Used"
description: "Learn what solidity type creationcode returns, how it relates to contract deployment, and how creation bytecode differs from code stored at an address."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity type creationcode"
owned_question: "What does Solidity’s `type(C).creationCode` return, and how is that bytecode used when deploying a contract?"
risk_level: "medium"
---

For a Solidity developer, `type(C).creationCode` refers to the compiler-provided creation bytecode associated with contract type `C`. It is a byte sequence used as part of a contract-creation workflow, not a deployed address or a query of code already stored at an address. On Ethereum, deployment uses a transaction carrying compiled contract bytecode and constructor data; after successful inclusion, that transaction creates a contract at a new address. ([source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>))

## What `type(C).creationCode` means in Solidity

A smart contract, in a general blockchain definition, is code and data deployed through cryptographically signed transactions. ([source](<https://csrc.nist.gov/glossary/term/Smart_contract>)) In the expression `type(C).creationCode`, `C` is a contract type referred to by the source code. The expression provides the creation-code bytes associated with that type so a deployment workflow can use them.

This is a type-level reference, not an onchain lookup. It does not ask a network for the bytecode at an address, identify a particular deployed instance, or reveal whether a deployment has taken place. The term “creation code” describes the bytes’ role in the creation process; it should not be read as meaning the expression creates or deploys a contract on its own.

Keep this byte sequence distinct from an application’s contract interface. The Solidity ABI defines how applications encode function selectors, arguments, return values, errors, and events when communicating with EVM contracts. ([source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)) That interface is relevant to contract interaction, but it is not the same thing as creation bytecode.

## How creation bytecode participates in deployment

Consider a deployment tool preparing a new instance of a contract type. At a high level, the workflow needs compiled contract bytecode and constructor data. On Ethereum, those are carried in a contract-creation transaction, which consumes gas and creates a contract at a new address after successful inclusion. ([source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>)) `type(C).creationCode` is useful in this conceptual workflow because it makes the type’s creation bytes available to code that is preparing deployment.

The expression is not itself a complete factory or deployment procedure. It does not submit a transaction, establish that a transaction was accepted, or supply every value a particular constructor might require. The deployment path must handle the constructor data appropriate to the contract. The precise way arguments are encoded and combined with bytecode belongs to the deployment workflow and its compiler and tooling context; the evidence here does not establish one universal encoding procedure.

For example, source code could refer to the creation code for a contract type when preparing deployment data. That example describes a possible role for the bytes, not a complete implementation or a rule that every deployment workflow must use this particular property.

## What `type(C).creationCode` does not tell you

The property does not return a deployed address or report the code currently held at one. It is associated with a contract type in the build, rather than with a live instance on a particular network. To establish a deployment, a workflow must form and submit the relevant creation transaction; the Ethereum deployment description ties creation of the new address to successful inclusion. ([source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>))

Nor do the bytes alone establish that deployment will succeed. They do not show that constructor data is correct, that a transaction has been submitted, or that the transaction has been included successfully. The property supplies an artifact for a workflow; it is not proof that the workflow has completed.

Treat build and linking details as project-specific verification items. The allowed evidence establishes that Ethereum deployment uses compiled bytecode and constructor data, but it does not specify all compiler-version behavior, library-linking rules, or how every build system prepares the final byte sequence. Check the relevant Solidity compiler and build-tool documentation for the project’s version and output. Avoid inferring that the property alone certifies an artifact as ready to deploy.

## Creation code versus runtime code

Creation code is associated with starting contract creation. Runtime code is the code associated with the deployed contract and its later operation. The deployment process carries compiled bytecode and constructor data and, after successful inclusion, creates a contract at a new address. ([source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>)) These stages are related, but their byte sequences should not be treated as interchangeable.

This distinction helps when reading deployment tooling: creation bytes are used in the creation path, while an address refers to a contract that has been deployed. This is a high-level distinction, not a description of every compiler’s bytecode layout or a claim about every version-specific property. The discussion here does not cover `type(C).runtimeCode` as a separate compiler feature.

## Checks before using creation bytecode

Before relying on `type(C).creationCode` in a deployment workflow, verify the context around the returned bytes:

- **Contract type:** Confirm that `C` names the source-level contract type intended for creation, rather than assuming it selects an existing onchain instance.
- **Compiler and build:** Check the project’s compiler version and build output. The evidence available here does not establish identical behavior across compiler versions.
- **Constructor data:** Confirm how the selected deployment path supplies the data required by the contract’s constructor. Do not assume the property alone provides all initialization inputs.
- **Libraries and linking:** Consult the compiler and build-tool documentation for any library-linking requirements. The available evidence does not define those mechanics, so the property name is not enough to determine whether linking is complete.
- **Transaction step:** Distinguish making bytes available from forming and submitting the creation transaction. On Ethereum, the new address is created after successful inclusion of the deployment transaction. ([source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>))

In short, `type(C).creationCode` refers to creation bytecode associated with a Solidity contract type. It can serve as input to a deployment workflow, while constructor data, build context, and the transaction itself remain separate parts of that workflow.

## Sources and references

- [Deploying Smart Contracts](https://ethereum.org/developers/docs/smart-contracts/deploying/) — ethereum.org; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
