---
title: "Proof of Stake Process: How It Works"
description: "Understand Proof of Stake Process, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["proof stake process"]
author: "editorial_team"
primary_keyword: "proof of stake process"
owned_question: "How does the proof-of-stake process work, from validator selection to block finalization?"
risk_level: "medium"
---

# Proof of Stake Process: How It Works

Proof of stake (PoS) is a consensus approach in which protocol rules use validators and stake-related participation to coordinate block production and agreement about blockchain state. The **proof of stake process** is not one universal algorithm: validator duties, selection, block checks, and finality differ among networks. Ethereum and Solana, for example, document distinct staking and consensus behaviors, while Tezos describes its own protocol-defined participation rights. A useful explanation therefore separates the general workflow from network-specific rules.

This explainer follows the path from participation and selection through block validation and finality. It focuses on the accepted documentation for Ethereum, Solana, and Tezos; details attributed to one network should not be assumed to apply to another.

## What Proof of Stake Process means

At a high level, a PoS system coordinates which participants may perform consensus duties and how other participants assess the resulting blocks. Those duties can include proposing a block or checking and attesting to one. The protocol also defines how nodes evaluate proposed blocks and how the network chooses among competing histories or recognizes finalized checkpoints. The specific mechanisms and conditions are implementation-dependent.

The process is best understood as a sequence of protocol-defined decisions, not as a single act of “staking.” A stake arrangement may affect participation or a validator’s consensus weight, but the complete process also depends on client software, network state, messages from other participants, and the chain’s consensus rules. The source documentation supports particular behaviors for named networks; it does not establish a single selection or finalization procedure shared by all PoS chains.

## Core components of Proof of Stake Process

**Validators and consensus duties.** In Ethereum, a validator checks and attests to valid blocks and proposes a block when selected. Other PoS networks assign different duties and schedules, so this description is specific to Ethereum rather than a universal validator job description. [1]

**Stake and participation state.** Stake can be connected to consensus participation in network-specific ways. On Solana, a delegator can assign stake to a validator, increasing that validator’s consensus weight while the delegator retains token control under the stake-account model. That statement describes Solana’s native delegation model only; it does not establish how key authority, activation, commission, or slashing work elsewhere. [2]

**Nodes and block data.** A proposed block is not accepted merely because a participant produced it. In Ethereum’s block-processing overview, a receiving node checks the block and re-executes its transactions to verify the resulting state change before accepting it. The exact validation procedure is defined by current execution and consensus specifications. [3]

**Consensus rules and network state.** Rules govern duties, selection, fork choice, and finality, while the network’s current state informs how those rules apply. Ethereum’s design combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. Other networks can use different finality rules and failure-recovery approaches. [4]

**Protocol version and selection logic.** Selection itself is not necessarily a simple lottery or a fixed schedule. Tezos documentation describes consensus participation rights selected from delegates according to protocol-defined baking power and pseudorandom selection. The cited documentation is labeled alpha and can change before activation, so teams need to verify the active protocol version. [5]

## How Proof of Stake Process works

The following workflow is a conceptual map, not a claim that every network follows the same sequence or terminology.

1. **Participation is established under network rules.** A participant may operate a validator or, on some networks, delegate stake to one. Solana’s documented model illustrates delegation: assigned stake increases a validator’s consensus weight, while the delegator retains token control under the stake-account model. Other networks may define participation and authority differently. [2]

2. **The protocol determines eligible duties or rights.** Selection mechanisms and schedules are defined by the specific protocol. Tezos documents rights selected from delegates using baking power and pseudorandom selection; Ethereum’s documentation describes a validator proposing when selected. These examples should not be combined into a supposed universal selection formula. [1][5]

3. **A selected participant may propose a block.** In Ethereum, proposing a block is one of a validator’s duties when selected. The proposal is an input for the network to process, not proof by itself that the block is valid or final. [1][3]

4. **Receiving nodes check the proposal.** For Ethereum, a node checks the proposed block and re-executes its transactions to verify the resulting state change before accepting it. Exact validation is specified by the current execution and consensus specifications. A team implementing or auditing this step should consult the relevant versions rather than rely on a high-level summary. [3]

5. **Validators attest and consensus rules resolve the chain.** Ethereum validators check and attest to valid blocks. Ethereum’s fork-choice rule and attestations contribute to determining the chain, while checkpoint finality operates under protocol-defined supermajority conditions. These are distinct parts of Ethereum’s design, not synonyms for block production. [1][4]

6. **Finality is assessed under protocol-specific conditions.** In Ethereum, checkpoint finality depends on protocol-defined supermajority conditions. A block being proposed, checked, or included is not automatically the same event as checkpoint finality. The source claim does not specify a universal time-to-finality, nor does it imply that every PoS chain uses Ethereum’s checkpoint mechanism. [4]

This workflow exposes the dependencies: selection rules determine who can act; node software determines how block data is checked; attestations and fork choice affect chain agreement; and protocol-specific finality conditions determine when the system treats checkpoints as finalized. A break or mismatch in any one layer can change observed behavior, so operators should identify which layer a metric or status actually describes.

## Trust and control boundaries

A protocol can define the conditions for participation and acceptance, but a reader should not infer more than the documentation states. For example, Solana’s stake-account model preserves the delegator’s token control in the documented delegation arrangement; this does not establish custody or key-control properties for other staking models, third-party services, or different account configurations. [2]

Likewise, Ethereum’s block checks describe node behavior, while consensus rules describe how attestations, fork choice, and checkpoint finality interact. These mechanisms do not make every operational dependency identical across clients or protocol versions. The accepted claims do not establish a security guarantee, recovery outcome, service-level commitment, or universal threshold beyond the stated Ethereum supermajority conditions. [3][4]

For infrastructure teams, distinguish at least three questions: who controls the relevant keys or stake account; which software performs proposal and validation duties; and which protocol rule determines the status being reported. The answer may differ by network and by the arrangement in use.

## Limitations and failure modes

The most important limitation is portability: a PoS description for one chain is not a specification for another. Ethereum validator duties and checkpoint finality, Solana delegation and stake-account control, and Tezos baking-right selection are separate documented behaviors. Their selection schedules, authority models, finality rules, and recovery procedures must not be inferred from one another. [1][2][4][5]

A second limitation is version sensitivity. Tezos’s cited alpha documentation may change before activation; teams must verify which protocol version is active before relying on its described selection behavior. Ethereum block validation is also bounded by the current execution and consensus specifications, so a summary is not a substitute for the relevant specification version. [3][5]

Finally, process stages should not be collapsed. A proposal is not the same as validation; validation is not the same as attestation; and inclusion or a fork-choice outcome should not be casually described as finality. In Ethereum, checkpoint finality has stated protocol-defined supermajority conditions. The accepted material does not support universal claims about when finality occurs, how every failure is handled, or what penalties or rewards apply in a particular situation. [4]

## What teams should verify

When mapping a proof-of-stake process for a production system, use primary protocol documentation and record the network and active version alongside each answer.

- **Participation model:** Is the participant a validator, a delegator, or another protocol-defined role? What does assigned stake affect on this network? For Solana, confirm the stake-account model and do not generalize its control properties. [2]
- **Selection and duties:** What selects participants, and what actions are assigned? Check the active protocol documentation for schedules, rights, and duty definitions. Tezos’s cited alpha documentation requires an active-version check. [1][5]
- **Block validation:** Which node software checks a proposal, and what does “valid” mean under the current execution and consensus specifications? Ethereum’s overview says receiving nodes check and re-execute transactions to verify the resulting state change. [3]
- **Agreement and finality:** Which attestations, fork-choice rules, and finality conditions apply? For Ethereum, identify the checkpoint-finality rule and its supermajority condition rather than treating block inclusion as finality. [4]
- **Control boundaries:** Who controls the relevant keys, account, or validator configuration in the specific deployment? Do not derive custody or key-authority conclusions from a network’s general consensus description.
- **Evidence and versioning:** Keep links to the applicable protocol documentation, API or specification version, and deployment configuration. Recheck documentation when a protocol version changes, particularly where documentation itself warns that behavior may change before activation. [3][5]

These checks turn “proof of stake” from a broad label into a network-specific process map: identify participation, selection, duties, block verification, consensus, and finality separately, then verify each against the active protocol rules.

## Sources and references

- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Staking on Solana](https://solana.com/docs/references/staking) — Solana Documentation; retrieved 2026-10-18.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
