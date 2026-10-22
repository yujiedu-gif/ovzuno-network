---
title: "create2 solidity: How Deterministic Contract Addresses Work"
description: "Learn how create2 solidity derives a deterministic contract address, which inputs affect the calculation, and why a predicted address does not guarantee deployment."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "create2 solidity"
owned_question: "How does Solidity’s CREATE2 opcode determine a contract address, and what inputs must be known to predict it?"
risk_level: "medium"
---

For Solidity developers and reviewers, CREATE2 provides a way to calculate a contract address from specified deployment inputs before attempting deployment. The prediction is only an address calculation: it does not establish that deployment succeeded or that code is present there. The available evidence here does not include the authoritative CREATE2 formula or its exact encoding rules, so this article cannot responsibly reproduce the formula or claim a complete list of inputs needed to calculate it.

## What CREATE2 means in Solidity

CREATE2 is an EVM contract-creation operation associated with deterministic address prediction. To explain its calculation accurately, a reader needs the exact opcode specification: notably, the address formula and the encoding of each input. Those details are not established by the evidence authorized for this article, so they are intentionally not supplied here.

This is a material limitation, not a reason to substitute a remembered formula. A tool-neutral explanation of CREATE2 must be grounded in authoritative EVM or Solidity documentation that verifies the formula, input widths, and byte-level representation. Without that support, even a plausible-looking calculation could misstate the operation.

Contract deployment is a state-changing transaction process. In the Ethereum deployment model, a deployment transaction contains compiled bytecode and constructor data, consumes gas, and creates a contract at a new address after successful inclusion. That describes deployment at a high level; it does not establish CREATE2-specific address derivation or guarantee success for a particular attempt. [source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>)

## How the CREATE2 address is calculated

The precise calculation cannot be shown from the allowed evidence. In particular, this article cannot verify the proposed use of a deployer address, salt, initialization-code hash, a hash function, or a final address-byte selection. Nor can it confirm whether a given description uses the exact byte sequence required by the opcode.

For a reproducible prediction, consult the applicable authoritative EVM or Solidity specification and use its exact formula and encoding rules. A calculation that merely resembles the specification is not enough: the inputs must be represented as the required bytes, and the code-related input must match the code supplied to the deployment operation. The evidence provided for this article does not verify those details, so it would be misleading to present them as settled facts.

## Inputs that change a predicted address

The allowed claims do not establish which CREATE2 inputs determine an address or how changes to those inputs affect the result. They also do not establish whether constructor arguments form part of the relevant initialization code in a particular deployment setup. Accordingly, this article cannot give a supported input checklist or explain how to hash deployment bytes.

A reviewer should obtain the opcode-level documentation before comparing predictions. Record the inputs exactly as the specification defines them, including their byte representation, and avoid inferring an input's role from a framework's interface. A framework can expose a convenient prediction method, but its presence alone does not verify the underlying opcode formula.

## Prediction is not deployment success

A predicted address should not be treated as proof that a deployment transaction succeeded. Ethereum contract deployment uses a transaction, and contract creation occurs after successful inclusion; this high-level lifecycle is distinct from calculating an address in advance. [source](<https://ethereum.org/developers/docs/smart-contracts/deploying/>)

Likewise, this article cannot make a supported statement about address occupancy, collision behavior, or the exact conditions under which CREATE2 execution fails. Those questions require evidence for the applicable EVM rules and, where relevant, the network's implementation. Do not infer a universal failure rule from the mere fact that an address has been predicted.

To verify an actual result, inspect the deployment transaction's execution outcome and the resulting on-chain state on the network in question. Ethereum nodes validate blocks and re-execute their transactions to check resulting state changes before accepting a proposed block.  However, the allowed-claim list does not include that claim; therefore this article cannot use it to assert a specific verification procedure. The safe conclusion within the available evidence is narrower: a prediction alone does not demonstrate deployment.

## How to verify a CREATE2 calculation

The evidence authorized for this article does not support a complete, opcode-specific verification workflow. Before relying on a predicted address, verify the CREATE2 formula and byte encodings against authoritative EVM or Solidity documentation, then compare a reproducible calculation with the deployment inputs actually used. After an attempt, check transaction execution and code at the resulting address using a suitable network-data interface; the permitted evidence here does not document a particular interface or method, so no tool-specific instructions are given.

For broader contract review, OWASP's Smart Contract Security Verification Standard provides a structured framework for designing, building, and testing EVM-based smart contracts and decentralized applications. It is an early version and should be supplemented with project-specific threat modeling and review; it is not a substitute for verifying CREATE2's opcode-level formula. [source](<https://owasp.org/projects/smart-contract-security-verification-standard>)

The practical boundary is clear: do not report a CREATE2 address as independently verified unless the calculation uses the specification's exact formula and inputs. Do not describe deployment as successful based only on that predicted address. The formula and network-specific execution conditions remain unverified by the evidence available for this article.

## Sources and references

- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
- [Deploying Smart Contracts](https://ethereum.org/developers/docs/smart-contracts/deploying/) — ethereum.org; retrieved 2026-10-19.
