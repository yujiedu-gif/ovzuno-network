---
title: "How a proof of stake network coordinates validators"
description: "Learn how a proof of stake network coordinates validators, stake, block proposals, consensus, and finality, and why rules differ by protocol."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["proof stake network"]
author: "editorial_team"
primary_keyword: "proof of stake network"
owned_question: "How does a proof of stake network use validators and stake to propose and confirm blocks, and what network-specific rules shape that process?"
risk_level: "medium"
---

A proof-of-stake network uses protocol rules to assign validators tasks such as proposing blocks and checking or voting on them; those rules determine how the network accepts a shared history and, in some designs, when a block becomes final. The details—including who is eligible, how work is assigned, and what counts as final—are specific to each protocol. For a concrete example, Ethereum combines validator attestations, fork choice, and checkpoint finality under protocol-defined supermajority conditions. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

## What defines a proof of stake network

A proof-of-stake network is not a single, universal validator procedure. The useful way to understand one is as a set of protocol rules that coordinate validators around proposed blocks and a continuing chain. The rules establish which participants may perform consensus duties and how their actions affect the network’s view of valid history.

This article focuses on that network-level coordination. It does not describe staking interfaces, pooled services, or how to operate a validator for a particular chain. Those are separate layers: a user-facing service can provide access to staking, but its own procedures should not be mistaken for the network’s consensus rules.

The word “stake” also does not specify one selection algorithm. In Ethereum, validator participation involves ETH deposited as slashable economic collateral. That describes Ethereum’s design, not a universal rule for every proof-of-stake network. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

## How validators are selected and assigned work

A protocol defines the conditions under which a participant can serve as a validator and how consensus duties are assigned. Those conditions may determine who can propose a block, who checks or votes on a proposal, or how the roles work together. There is no basis in the evidence here for treating a particular selection method, stake weight, committee structure, or participation threshold as universal.

Tezos illustrates why network-specific documentation matters. Its current protocol documentation describes consensus participation rights as selected from delegates according to protocol-defined baking power and pseudorandom selection. That is a Tezos-specific example, not a template that can be applied to other networks. [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>)

For any network, distinguish eligibility from assignment. A rule that defines who may participate does not, by itself, tell you which participant proposes the next block or which participants vote on it. Look for separate descriptions of validator admission, proposer selection, and attestation or voting duties in that protocol’s documentation.

## From block proposal to confirmation

A conceptual lifecycle begins when a selected validator proposes a candidate block. Other validators can then check the candidate and submit attestations or votes according to their network’s rules. The protocol uses these actions to decide which blocks and history to recognize.

Ethereum’s block-processing description gives a concrete verification step: a node receiving a proposed block checks it and re-executes its transactions to verify the resulting state change before accepting it. This is an Ethereum-specific description; other networks may define different validation steps. [source](<https://ethereum.org/developers/docs/blocks/>)

Proposal and confirmation are not synonyms. A proposal is a candidate submitted by a participant; acceptance depends on the network’s validation and consensus rules. Nor does the word “confirmation” necessarily mean finality. In Ethereum, proof of stake combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

That example shows why it helps to read about three steps separately: checking a candidate block, choosing among competing histories when the protocol provides for that, and establishing finality. Protocol documentation should define how these steps fit together; the terms and conditions should not be assumed to mean the same thing across networks.

## What stake changes—and what it does not

Stake can be part of a protocol’s validator design, but the exact role is network-specific. Ethereum uses ETH deposits as slashable economic collateral for validator participation. The claim is limited to that network and does not establish how another protocol uses stake or what economic outcome a participant will receive. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

Stake alone does not tell a reader whether a block will be proposed, how a vote is counted, or when a block is final. Those are determined by the protocol’s assignment, validation, and consensus rules. Likewise, a description of stake as collateral should not be expanded into a claim that a network is secure or that a participant is guaranteed a particular result.

Keep protocol behavior distinct from service terms. A staking product may present participation through its own interface, but its availability, fees, rewards, custody arrangements, and withdrawal terms are not established by the protocol facts described here. Assess those separately rather than reading them into validator selection or consensus.

## Failures, penalties, and network-specific rules

Protocol rules can attach consequences to validator behavior, but the available evidence for this explainer does not establish a general penalty schedule or universal treatment of downtime, conflicting votes, or coordination failures. Do not infer such rules from the word “stake” or from one network’s design.

For Ethereum, the evidence supports only the bounded point that ETH deposits used for validator participation are slashable economic collateral. It does not specify here the full set of triggering conduct, thresholds, recovery procedures, or current operating requirements. For Tezos, the cited selection description establishes how baking participation rights are selected, not the consequences of validator failure. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>)

This distinction matters when making security or recovery assessments. A high-level consensus description does not demonstrate that every implementation is free of faults, nor does it establish the procedures a participant must follow after an incident. Consult the relevant protocol documentation for those details; do not treat an illustrative network example as a universal guarantee.

## How to evaluate a specific network's design

Start with the protocol’s own documentation and trace the lifecycle rather than relying on a generic summary. Identify the eligibility rules, how block proposers are chosen, what other validators check or vote on, and the rule that selects accepted history or establishes finality. Where documentation uses terms such as “confirmation” and “finality,” check how it defines each term.

Then verify that each statement applies to the network and protocol version under review. For example, Tezos documents selection from delegates using baking power and pseudorandom selection, while Ethereum documents block re-execution by receiving nodes and checkpoint finality under protocol-defined conditions. These examples illustrate different protocol-specific facts; they do not form a combined rule for proof-of-stake networks generally. [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>) [source](<https://ethereum.org/developers/docs/blocks/>) [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

Finally, keep questions outside consensus in their own evidence review. Participation requirements, key management, exits, service terms, fees, yields, taxes, and legal or regulatory treatment are not answered by the validator lifecycle alone. For network-level mechanics, the practical test is straightforward: locate the current protocol documentation for selection, proposal, validation, voting, and finality, and keep each conclusion within the scope of what that documentation actually says.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
