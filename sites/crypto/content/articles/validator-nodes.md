---
title: "Validator nodes: roles and responsibilities in proof-of-stake networks"
description: "Learn what validator nodes do in proof-of-stake networks, how they participate in consensus, and why duties and requirements vary by protocol."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["staking_validators"]
tags: []
author: "editorial_team"
primary_keyword: "validator nodes"
owned_question: "What are validator nodes in proof-of-stake networks, and what do they do to participate in consensus?"
risk_level: "medium"
---

Validator nodes are network participants assigned protocol-defined duties that help a proof-of-stake blockchain check or confirm its history. Depending on the network, those duties may include proposing blocks, checking proposed blocks, or attesting to them. A validator is therefore a particular consensus role—not a synonym for every blockchain node, every token holder, or every person who delegates stake. The exact role and requirements must be checked in the documentation for the specific protocol.

## What makes a node a validator?

A node is software and infrastructure that participates in a blockchain network. A validator is a participant with an additional role specified by that network’s consensus rules. Those rules determine which participants can act as validators and what actions they are expected to perform; the word “validator” does not describe one universal job across all proof-of-stake protocols.

For example, Ethereum documentation describes validators as checking and attesting to valid blocks, and proposing a block when selected. This is an Ethereum-specific description, not a template that establishes the duties of validators on every network. Other protocols can use different terms, assign distinct responsibilities, or structure participation differently.

It is also useful to separate the validator role from the broader category of nodes. Some nodes participate in consensus; others may have different roles. A network’s documentation is the right place to establish which node types it defines and which duties belong to each.

## How validator nodes participate in consensus

Consensus is the process by which a network’s participants follow rules for accepting new blocks and determining the continuing history. Within that process, a protocol can assign a validator to propose a block, check one, or attest to a block or checkpoint. An attestation is a validator’s protocol-defined statement about the chain or a block; it is not simply a general expression of support.

Ethereum illustrates how these responsibilities can fit together. Its proof-of-stake design combines validator attestations, a fork-choice rule for selecting among competing histories, and checkpoint finality under protocol-defined supermajority conditions. Finality means that the protocol has applied its conditions for treating particular history as finalized; it should not be treated as a universal term with identical rules across networks.

The protocol determines how validators are selected or scheduled, what messages they may submit, and how those messages are evaluated. A validator’s work is only one part of the process: network participants still follow the applicable rules for accepting blocks and determining the chain. Because those rules differ, a description of Ethereum’s attestations and finality cannot establish how another protocol reaches agreement.

## Validator nodes, stake, and other network participants

A validator is a consensus role; holding or delegating tokens is a separate matter. Protocols define how stake relates to participation, and they can provide different ways for token holders to contribute. The details should not be inferred from a generic use of the word “validator.”

Solana provides one example of delegation: a delegator can assign stake to a validator, increasing that validator’s consensus weight while retaining token control under Solana’s stake-account model. That description is specific to Solana; it does not establish that delegation works the same way elsewhere or that a delegator personally performs the validator’s duties.

In another protocol-specific example, Tezos documentation describes consensus participation rights as selected from delegates according to protocol-defined baking power and pseudorandom selection. The terms and rules here are Tezos-specific. Comparing these examples shows why readers should identify the protocol before drawing conclusions about who participates, how influence is assigned, or what a validator must do.

Other network participants may run nodes without holding a validator role. For instance, Ethereum full nodes independently verify blocks and transactions against protocol rules rather than relying entirely on another node. That verification role is distinct from the additional consensus role of an Ethereum validator. The distinction helps avoid the mistaken assumption that every node operator proposes or attests to blocks.

## What operating a validator involves

At a high level, operating a validator means carrying out the duties the chosen protocol assigns. The exact software, participation process, technical requirements, and operational expectations are protocol-specific. The evidence available here does not support a universal hardware specification, uptime threshold, setup procedure, or eligibility rule, so those details should be checked in current primary documentation for the network in question.

Key management is one area that requires particular care. In Ethereum, validator activity is tied to protocol-defined messages and duties, but the precise key arrangements and procedures are not uniform across protocols. An operator evaluating a specific network should consult its current documentation for the relevant validator keys, signing responsibilities, and safeguards rather than applying assumptions from another chain.

Monitoring and correct operation also depend on the network’s rules. For Ethereum, validator incentives include rewards for correct participation, missed rewards or penalties for inactivity, and slashing for specified conflicting messages. These are Ethereum-specific categories, not a statement that every protocol uses the same incentives or consequences. This explainer does not provide a setup guide or an estimate of financial outcomes.

## Protocol rules, risks, and verification

Before treating any statement about validator participation as applicable, verify its scope against the protocol’s current primary documentation. Check what roles the network defines, how validators are selected, what actions they must perform, and which rules govern missed or conflicting actions. A general explanation cannot substitute for that protocol-specific review.

Be equally careful with claims about stake, penalties, and recovery. The allowed evidence supports particular examples for Ethereum, Solana, and Tezos, but not a universal account of validator eligibility, rewards, penalties, or recovery procedures. Nor does it establish a standard security level or a guaranteed outcome for operating infrastructure.

The practical distinction is straightforward: a validator node has consensus duties assigned by a particular protocol; other nodes may perform different functions; and token holders or delegators may participate under separate, protocol-specific rules. Keeping those roles separate makes it easier to read network documentation accurately without treating one chain’s design as a rule for all proof-of-stake systems.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-19.
- [Staking on Solana](https://solana.com/docs/references/staking) — Solana Documentation; retrieved 2026-10-18.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
