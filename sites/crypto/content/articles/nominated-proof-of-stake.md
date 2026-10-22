---
title: "Nominated proof of stake: roles and consensus mechanics"
description: "Learn how nominated proof of stake connects nominators and validators in consensus, which responsibilities each role may have, and why rules vary by network."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["nominated proof stake"]
author: "editorial_team"
primary_keyword: "nominated proof of stake"
owned_question: "How does nominated proof of stake assign staking support to validators, and what roles do nominators and validators have in consensus?"
risk_level: "medium"
---

Nominated proof of stake is a network-specific arrangement in which participants nominate or support validators that take part in consensus. Nominators express that support; validators perform the duties defined by their protocol. The precise selection process, eligibility rules, and consequences depend on the individual network, so the term is not a universal specification.

## What nominated proof of stake means

The word *stake* refers to cryptocurrency committed to a consensus process, with stake influencing consensus participation or weight. That is a general proof-of-stake description, not a complete account of how any one network handles nominations, validator selection, or operations.

In a nominated design, the key relationship is between a nominator’s support and a validator’s participation. A nominator indicates which validator or validators to support under that network’s rules. The protocol then applies its own selection and participation process. The exact effect of a nomination cannot be inferred from the name alone: networks may define nomination, selection, and validator duties differently.

This distinction matters because “nominating” does not, by itself, say that a participant runs validator software or directly produces blocks. It describes a role in allocating or expressing support within a particular design. To understand what that role actually does, consult the network’s current protocol documentation rather than treating the label as a standard with fixed mechanics.

## How nomination and validation fit together

A useful high-level sequence is:

1. **A participant nominates or backs a validator.** The participant expresses support according to the network’s nomination rules.
2. **The protocol determines validator participation.** How support affects selection or consensus weight is network-specific; the word “nomination” does not establish a universal formula.
3. **Validators carry out consensus duties.** Those duties are set by the protocol and can include checking or attesting to blocks. As one network-specific example, Ethereum validators check and attest to valid blocks and may propose a block when selected. That example describes Ethereum’s proof-of-stake design, not nominated proof of stake generally.
4. **The network applies its own consensus and finality rules.** Ethereum, for instance, combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. This is not evidence that another network uses the same process.

The sequence separates support from consensus operation. A nominator’s action is not interchangeable with a validator’s protocol duties. Nor does the high-level relationship tell a reader whether nominations are direct, delegated through an interface, capped, changeable, or subject to a waiting period; those details require network-specific documentation.

## Nominator and validator responsibilities

A **nominator** is a participant who expresses support for validators under a particular protocol. The relevant questions are practical and specific: what action counts as a nomination, how the protocol uses that support, and what conditions apply to the nominator. The allowed evidence does not establish one set of nomination limits, eligibility criteria, or operational responsibilities for all networks.

A **validator** is a participant assigned consensus duties by the network. Depending on the protocol, those duties may involve checking or attesting to blocks and proposing a block when selected. Ethereum is one example of such duties, but it should not be generalized to every proof-of-stake system. The validator’s work is governed by the protocol, not by the nominator’s independent choice about how to validate a block.

The roles can therefore differ in what a participant must do. Nominating support does not necessarily mean operating a validator node. Conversely, describing someone as a validator does not tell the reader how that network chooses validators or what infrastructure and availability it requires. Those operational details must be verified for the relevant protocol and current software or documentation.

## Network rules that change the details

Do not assume that familiar terms imply identical mechanics. Check the network’s own documentation for:

- **Nomination and selection:** How support is recorded and how the protocol uses it to select or authorize validators.
- **Eligibility and limits:** Who may nominate or validate, and whether the protocol sets conditions or limits.
- **Consensus duties:** What validators must do, and how the network defines valid participation.
- **Rewards and consequences:** What the protocol provides for correct participation and what it specifies for inactivity or conflicting behavior. Ethereum’s rules include rewards for correct participation, missed rewards or penalties for inactivity, and slashing for specified conflicting proposals or attestations. These are Ethereum-specific examples, not universal terms for every nominated design.
- **Withdrawal and recovery:** How the network handles changes to participation, withdrawals, or recovery. The allowed evidence does not establish general withdrawal or recovery procedures, so those must be checked in current network documentation.

These checks also prevent an explanation of a consensus mechanism from being mistaken for a claim about return, security, or availability. None follows automatically from the label “nominated proof of stake.” No general reward rate, guaranteed outcome, or universal penalty rule can be derived from the role names alone.

## How to assess a nominated proof-of-stake design

When evaluating a specific implementation, start with its authoritative, current protocol documentation. Find the definitions of *nomination* and *validator*, then trace how the protocol moves from support to validator participation. Confirm the validator duties and the rules for selection, participation, rewards, penalties, and withdrawal; do not fill gaps with assumptions borrowed from another network.

Keep the questions distinct. The protocol documentation can explain the consensus mechanism and participant roles, but it does not by itself settle every operational or jurisdiction-specific issue. Verify security assumptions and recovery procedures from relevant authoritative sources for that implementation. Any compliance obligation requires relevant jurisdiction-specific authority; the technical description alone does not establish one.

The safest general conclusion is narrow: nominators express support for validators under network-defined rules, and validators carry out that network’s consensus duties. How support affects selection, what each role must do, and what happens when participation changes are implementation-specific questions—not universal properties of nominated proof of stake.

## Sources and references

- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-18.
