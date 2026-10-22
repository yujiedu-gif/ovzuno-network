---
title: "Tornado Cash smart contract: how deposits and withdrawals work"
description: "Learn how the Tornado Cash smart contract uses commitments and zero-knowledge proofs in its deposit and withdrawal flow, and what that design can verify."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Tornado Cash protocol", "zero-knowledge proof", "Ethereum smart contracts"]
author: "editorial_team"
primary_keyword: "tornado cash smart contract"
owned_question: "How do Tornado Cash smart contracts use commitments and zero-knowledge proofs to enable withdrawals without directly linking them to deposits?"
risk_level: "high"
---

Tornado Cash smart contracts use a commitment-and-proof model: a deposit is associated with a public commitment, and a later withdrawal can be presented with a zero-knowledge proof for on-chain verification. This pattern can let a contract check a defined eligibility claim without directly receiving the private witness used to generate the proof. The evidence available for this article supports that general architecture, but not Tornado Cash’s exact deployed contract mechanics, so specific implementation details should not be assumed.

## What the Tornado Cash smart contract does

A smart contract is an on-chain program whose rules run when it is invoked. In a privacy-oriented design, the contract’s role is to maintain relevant public state and enforce conditions for requested actions. It is distinct from the broader protocol, the application interface, and any off-chain computation used to prepare a transaction.

A useful architectural distinction is between proof generation and proof verification. Private witness data is information used to establish a claim. A zero-knowledge privacy application can generate a proof from private witness data off-chain, then submit a public commitment and proof for an on-chain verifier to check. The verifier checks the submitted proof; it does not need to receive the witness itself as part of that verification pattern. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

This describes a general pattern, not a verified inventory of Tornado Cash contracts. The evidence available here does not identify a particular deployment, contract version, or interface. It therefore cannot establish which exact state variables or transaction fields a specific Tornado Cash contract uses.

## How deposits create commitments

A commitment is a public value used to represent or bind information without publishing the private information itself. In the high-level flow described in the question, a deposit is associated with a commitment that can later be relevant to a proof. The conceptual distinction is between the public commitment that the contract can use and private witness data that can be used during proof generation.

The sequence can be understood without treating the commitment as the secret itself. First, a deposit-related action makes a public commitment available to the contract’s state. Separately, private witness information is retained for a later proof-generation step. At withdrawal, the proof can be checked in relation to the public commitment. This explains how a system can relate a later claim to a prior public record without simply publishing the witness in the verification step.

The available evidence does not establish Tornado Cash’s exact commitment construction, what its contract stores for deposits, or which deposit details are visible in every transaction. It also does not establish denomination rules, event fields, or the precise relationship between any particular deposit record and a later withdrawal. Those details require evidence about the specific implementation; they cannot be supplied by the general commitment-and-proof model alone.

## How zero-knowledge proofs authorize withdrawals

A zero-knowledge proof is a way to let a verifier check a defined claim without requiring disclosure of the private witness used to produce the proof. In a general privacy-application architecture, proof generation can take place off-chain, while a public verifier checks the submitted proof against the relevant public commitment. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

For a withdrawal, the contract-level role is to evaluate the proof through its verification logic and apply whatever additional rules its code specifies. Acceptance means the proof passed that implemented check; it does not, by itself, establish facts beyond the proof statement and public inputs. If the proof fails verification, it does not satisfy that verification condition. What happens next depends on the contract’s actual execution rules, which are not documented in the evidence available here.

This distinction keeps the roles clear. Off-chain proof generation uses private witness data to produce a proof. The transaction presents proof material to the contract. The contract’s verifier checks the proof, and the contract applies its own state-transition rules. The general architecture supports explaining the separation between private witness and public verification, but does not substantiate Tornado Cash-specific withdrawal conditions.

In particular, the allowed evidence does not support claims about Tornado Cash’s exact nullifier format, how a nullifier is stored or marked as spent, or what precise checks are made before a withdrawal. Those details are important to a code-level account and should not be inferred merely because a system uses zero-knowledge proofs.

## What the contract verifies—and what it does not

A proof verifier can establish only the claim encoded by the proof system and the inputs it checks. The general privacy-application model shows how private witness data and public verification can be separated; it does not show that every surrounding transaction or observation is private. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

Consequently, proof acceptance should not be described as a universal anonymity guarantee. A contract’s result is limited to its verification logic and other conditions in its code. The proof check alone does not establish that external observers lack information, or that activity outside the proof is hidden. It also does not verify any fact that is outside the defined proof statement unless that fact is independently included in the checks.

This is a technical boundary, not a judgment about how a person should use a protocol. It means only that a cryptographic proof, its public inputs, the on-chain verifier, and the surrounding transaction are distinct parts of the analysis. The evidence here does not substantiate specific claims about what Tornado Cash transaction metadata reveals or how observers might interpret it, so no deployment-specific privacy conclusion follows.

## Implementation, security, and operational caveats

The description above explains the general commitment-and-proof pattern, not the source code of a specific Tornado Cash deployment. The allowed evidence does not include Tornado Cash primary documentation, deployed contract source, or an audit report. As a result, it cannot confirm the exact deposit and withdrawal steps, proof circuit, contract state updates, nullifier handling, or security findings for a particular implementation.

A concrete code-level explanation would need to tie together the deployed contract and its verifier: what public inputs are checked, what the proof is intended to establish, what state changes follow acceptance, and which deployment those facts describe. General descriptions of zero-knowledge architecture cannot answer those implementation questions by themselves.

Nor should verification be confused with a guarantee that software is correct or secure. The permitted evidence supports a limited account of how a public verifier can check a proof while private witness data remains separate; it does not establish that any particular implementation is free of defects or that broader privacy conditions hold. Availability, fees, recovery, legal status, and compliance are outside this technical explanation. Its narrow conclusion is that commitments and zero-knowledge verification can support a withdrawal design in which on-chain logic checks a defined proof without directly receiving the private witness, while exact Tornado Cash behavior remains unverified by the evidence available here.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
