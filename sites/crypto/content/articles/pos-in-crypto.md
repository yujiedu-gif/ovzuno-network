---
title: "Pos in crypto: How validators coordinate consensus"
description: "Follow pos in crypto from validator selection through block proposals and attestations, with a clear distinction between protocol operation and user staking."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["staking_validators"]
tags: []
author: "editorial_team"
primary_keyword: "pos in crypto"
owned_question: "How does proof of stake operate in crypto networks, and how do validator selection, block proposals, and attestations fit together?"
risk_level: "medium"
---

Proof of stake in crypto is an operational process: protocol rules determine which validators have duties, a selected proposer may offer a block, and other validators check and report on it. Those messages feed the network’s rules for accepting a shared history. The exact selection, voting, and finality mechanics differ by network, so this sequence is a framework—not a universal protocol specification.

## What the protocol coordinates during consensus

A blockchain needs participants to follow rules for evaluating proposed updates and maintaining an agreed history. In proof-of-stake systems, validators perform protocol-defined duties that contribute to this coordination. On Ethereum, for example, validators check and attest to valid blocks and may propose a block when selected by the protocol. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

Consensus duties are not the same thing as every activity performed by a network node. A node can help process or relay network data, while a validator role adds specific responsibilities for proposing or attesting under the protocol. Ethereum’s documentation describes the validator as performing duties within its proof-of-stake system; it does not make every node a validator. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

The terms also need to be read in context. “Attestation” describes a validator message in Ethereum’s process; other protocols may use different messages, roles, and names. Even where two systems both use proof of stake, their schedules, selection rules, and voting procedures should not be assumed to match.

## How pos in crypto selects validators for a round

Selection begins with the protocol’s eligibility rules. In a general sense, stake can influence consensus participation or weight, but that does not tell you exactly who will act next or how a particular network chooses them. The mechanism, timing, and eligibility conditions have to be established from that network’s own rules; the evidence available here does not support a universal selection formula.

It is useful to separate two ideas: being eligible to participate and receiving a particular duty. A validator could be eligible under a network’s rules without being assigned to propose a block at a given moment. On Ethereum, the supported description is narrower: a validator checks and attests to valid blocks and proposes a block when selected. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

For builders and operators, the practical verification question is therefore not simply “who has stake?” It is: which protocol version defines eligibility, how does that version assign duties, and what message is expected from a validator at each step? Without those details, an explanation of selection should remain at the level of the process rather than inventing a schedule or weighting rule.

## From block proposal to attestations

When a validator is selected to propose, it can produce a candidate block under the network’s rules. In Ethereum’s documented duties, a validator proposes a block when selected, while other validator duties include checking and attesting to valid blocks. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

An attestation is not just a signal of approval. It is part of a protocol-defined validation and voting process: validators assess whether a block is valid and communicate their view through the required message. Ethereum’s description expressly includes checking and attesting to valid blocks, so the attestation stage belongs after validation rather than replacing it. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

The sequence can be summarized as follows:

1. The protocol establishes which validators are eligible and assigns duties according to its rules.
2. A selected proposer offers a candidate block.
3. Validators with checking and voting duties assess the block under the protocol and send the required messages.
4. The network applies its consensus rules to those messages and the candidate history.

This outline does not specify committee sizes, message formats, timing, or exact validation checks. Those are implementation-specific details, and the Ethereum example should not be treated as proof that every proof-of-stake network uses attestations or the same role division.

## How agreement, finality, and missed duties fit together

Validator messages contribute to agreement only through the network’s defined rules. Ethereum’s proof-of-stake design combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) A fork-choice rule helps determine which history is treated as the current chain when competing histories are considered; checkpoint finality addresses when the protocol treats history as finalized. These are related but distinct parts of consensus.

This distinction matters because a block’s presence in a chain and its finality are not necessarily the same event. Ethereum’s finality model uses votes on checkpoint blocks to distinguish finalized history from blocks that are merely included. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) Other networks may use different terminology and finality conditions, so the Ethereum distinction should not be generalized as a universal rule.

The available evidence does not establish a general account of missed duties, conflicting messages, recovery, or penalties across proof-of-stake networks. For any specific system, consult its protocol documentation to determine what happens when a validator fails to act or sends a message that conflicts with protocol rules. Do not infer universal slashing or recovery behavior from the word “validator.”

## What this lifecycle does—and does not—explain

The operational sequence is eligibility and assignment, a possible block proposal, independent checking, validator messages, and protocol resolution. In Ethereum, the documented duties include checking and attesting to valid blocks and proposing when selected; its consensus design combines attestations with fork choice and checkpoint finality. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>) [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

That sequence explains protocol coordination, not how a user delegates tokens, chooses a staking service, or evaluates staking returns. Those are separate questions involving user and service arrangements beyond the validator’s consensus duties. For technical due diligence, identify the network and active protocol version, then verify its selection rules, proposer duties, validation process, voting messages, and definition of finality in the network’s documentation. Details from one network should not be silently transferred to another.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-19.
