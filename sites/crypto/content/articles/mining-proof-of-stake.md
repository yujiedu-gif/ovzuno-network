---
title: "Mining Proof of Stake: Why the Term Is Used and What Validators Do"
description: "Understand why people say mining proof of stake, how validators participate in consensus, and how the process differs from proof-of-work mining."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["mining proof stake"]
author: "editorial_team"
primary_keyword: "mining proof of stake"
owned_question: "Why is proof of stake sometimes called mining, and how do validators actually help a proof-of-stake network reach consensus?"
risk_level: "medium"
---

People sometimes say “mining proof of stake” as a loose way to describe participating in network consensus, but it is not the same process as proof-of-work mining. In proof of stake, validators take part in consensus through protocol-defined duties, with cryptocurrency committed as stake influencing consensus participation or weight. In proof of work, participants compete through computational work. The precise terms and mechanics depend on the network.

## Why people use the phrase “mining proof of stake”

The informal wording treats “mining” as a broad label for contributing to a blockchain’s operation or consensus. That can make the phrase understandable in casual conversation, but it blurs two different mechanisms. Proof of stake uses cryptocurrency committed as stake, with stake influencing consensus participation or weight; it does not describe the proof-of-work computational process. The selection, delegation, custody, reward, penalty, and withdrawal rules are specific to each protocol. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))

For that reason, “staking” and “validation” are usually more precise terms when discussing proof-of-stake participation. Even those terms should not be assumed to mean exactly the same thing on every network: each protocol defines its own participation model and terminology. A phrase found in a forum or conversation may be an analogy rather than the network’s formal name for a task.

## What a proof-of-stake validator does

A validator is a participant with consensus duties defined by a proof-of-stake protocol. Those duties can include checking blocks, attesting to them, and proposing a block when selected. Ethereum provides one network-specific example: its validators perform block-checking and attestation duties and propose a block when selected by the protocol.

An attestation is a validator’s protocol message about a block or other consensus choice. It is not, by itself, the entire agreement process. The protocol determines which messages count, how they affect the selected history, and what conditions establish finality. Ethereum, for example, combines validator attestations with a fork-choice rule and checkpoint finality under protocol-defined supermajority conditions. These are Ethereum-specific details, not a universal template for every proof-of-stake network. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

Do not treat “validator” as a synonym for “node.” A node is part of a network’s software infrastructure; a validator is a consensus role assigned under protocol rules. Ethereum’s node architecture makes this distinction explicit: a validator client is an additional role, required only when a node proposes and attests to blocks. Other networks may assign roles differently.

## How proof-of-stake consensus proceeds

A simplified sequence helps separate the work done by participants from the rules that govern the network’s decision:

1. **The protocol defines participation.** It specifies how stake relates to consensus weight and sets the requirements for validator activity. The details—including selection and withdrawal rules—are network-specific. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))
2. **Validators carry out assigned duties.** Depending on the protocol and selection, they may check or propose blocks and send attestations. Ethereum’s validator duties are one concrete example, not a rule for every network.
3. **The protocol evaluates the messages.** Its rules determine how valid attestations and other consensus inputs affect the network’s choice of history. In Ethereum, fork choice and attestations work alongside checkpoint-finality conditions. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))
4. **The network applies its finality model.** “Included” and “finalized” need not mean the same thing. Ethereum uses checkpoint finality under protocol-defined supermajority conditions; another protocol may use different rules or terminology. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

This outline is intentionally limited to consensus. It does not explain how to operate a validator, select a service, or evaluate a particular network’s participation conditions.

## Proof-of-stake validation versus proof-of-work mining

Proof of work uses a hard-to-solve, straightforward-to-verify computational problem that consumes time, energy, and computational cycles. Proof-of-work participants use that process in the network’s block-production mechanism. ([source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>))

Proof of stake instead commits cryptocurrency as stake, with stake influencing consensus participation or weight. Validators then perform protocol-assigned duties; they are not defined by competing to solve the proof-of-work problem. The two models therefore differ in how participants take part in consensus—not just in the names given to them. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))

These distinctions do not establish a universal ranking for energy use, security, decentralization, or rewards. The available evidence supports a description of the mechanisms, not a blanket conclusion that one model always has a particular outcome.

## What the word “mining” does—and does not—tell you

When “mining” is applied to proof of stake, read it as informal shorthand unless the network’s own documentation uses it as a defined term. It may signal that someone means participation in consensus, but it does not tell you which validator duties are involved or how the protocol selects participants.

Nor does the word establish that a participant receives a fixed reward or that anyone can validate without conditions. Proof-of-stake rules for selection, delegation, custody, rewards, penalties, and withdrawal vary by protocol. To understand a particular use of the phrase, check that network’s documentation for its official validator terminology, assigned duties, participation requirements, and consensus or finality rules. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))

In short, “mining proof of stake” is often an imprecise analogy. Validators help a proof-of-stake network reach consensus by carrying out the duties its protocol assigns; proof-of-work miners instead use computational work. The network’s own rules determine how those activities contribute to agreement.

## Sources and references

- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
