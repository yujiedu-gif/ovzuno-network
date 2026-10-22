---
title: "Proof of stake blockchain list: networks and consensus checks"
description: "Explore a proof of stake blockchain list with clear inclusion criteria, example networks, and checks for current consensus and validator documentation."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["staking_validators"]
tags: ["proof stake blockchain list"]
author: "editorial_team"
primary_keyword: "proof of stake blockchain list"
owned_question: "Which notable blockchain networks use proof of stake, and how can readers verify each network’s consensus and validator model?"
risk_level: "medium"
---

For readers checking which networks use proof-of-stake consensus, this is a short, evidence-bounded list: Ethereum and Tezos are documented examples, while Decred is a hybrid design that combines proof of work and proof of stake. Confirm each network’s active protocol documentation before treating its consensus or validator model as current; this list is not exhaustive or a ranking.

## How this proof of stake blockchain list is defined

An entry belongs here when the allowed evidence supports describing its network’s consensus design as proof of stake or, in Decred’s case, as a hybrid that includes proof of stake. The available evidence is limited: it does not provide dated, current protocol specifications for every network or establish a research date for a comprehensive survey. The examples below should therefore be read as bounded references, not a complete census of proof-of-stake blockchains.

Consensus participation means a role in the network’s protocol for producing, checking, or approving blocks. It is not the same thing as buying or holding a token, depositing through a service, or receiving a tokenized representation of a stake position. The evidence here does not establish the current availability or mechanics of exchange, pooled, or liquid-staking products for any listed network.

## Example networks using proof-of-stake consensus

- **Ethereum — proof-of-stake consensus.** Ethereum’s protocol combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. A validator checks and attests to blocks and may propose a block when selected. These are protocol roles; they do not, by themselves, describe every way a person might obtain staking exposure through a third party. Verify the active Ethereum documentation for current participation details. (Claims: `claim_eth_finality`.)

- **Tezos — proof-of-stake participation.** Tezos documentation describes consensus participation rights as selected from delegates according to protocol-defined baking power and pseudorandom selection. “Baking” is Tezos-specific terminology in this context; the evidence supports the selection description but does not provide a full account of current eligibility, delegation, or operating requirements. The cited documentation is identified as alpha documentation that may change before activation, so check the active protocol version before relying on it. (Claim: `claim_tezos_baking_rights`.)

- **Decred — hybrid, not a pure proof-of-stake example.** Decred combines proof-of-work block production with proof-of-stake ticket voting. In that design, ticket voting approves blocks and participates in rule-change governance. Include it when the list covers networks that use proof of stake as one part of a hybrid consensus system; do not describe it as an exclusively proof-of-stake network. (Claim: `claim_decred_hybrid_roles`.)

The evidence allowed for this article does not support a wider list of named networks with current primary-source validation. Omitting additional names is more accurate than treating familiar examples as verified without the required evidence.

## Compare validator and staking models carefully

The examples use different role descriptions, so compare the terms the protocol itself defines rather than assuming that “validator,” “delegate,” “baker,” and “ticket voter” are interchangeable. Ethereum’s evidence describes validators attesting to blocks and proposing one when selected. Tezos describes selection of baking rights from delegates using protocol-defined criteria. Decred’s evidence identifies ticket voting alongside proof-of-work block production. Those descriptions establish distinctions in the cited designs, not a universal taxonomy for all PoS networks.

This list does not compare rewards, fees, transaction performance, or staking access. Those claims would require current and comparable evidence for the networks and participation methods being compared. Nor does the list tell a reader how to stake: protocol consensus roles and the terms of a wallet, exchange, pool, or other service are separate questions.

## Verify a network before relying on the list

For each candidate network, use a repeatable source check:

1. **Find the primary protocol documentation.** Confirm that it explicitly identifies the active consensus design and describes the relevant block-production, attestation, voting, or baking role. A general label alone may not clarify what participants actually do.
2. **Check version and upgrade context.** Look for protocol-version information, upgrade notices, or governance decisions. This is especially important where documentation is marked as draft or alpha; the Tezos evidence explicitly warns that its alpha documentation can change before activation.
3. **Separate protocol roles from service products.** Record whether the source describes native consensus participation or a third-party arrangement. Do not infer that a network’s protocol documentation proves a particular product is available or that its mechanics match the native role.
4. **Record the source and date checked.** Keep the document title, version or status when stated, and date of review alongside each entry. If sources conflict or the active design is unclear, mark the entry unresolved rather than presenting a settled classification.

A practical record might include the network, its documented consensus label, the named protocol role, the specification or documentation version, and the date checked. That record makes it easier to revisit an entry when a protocol changes, without implying the list itself guarantees current status.

## What this list does not establish

Inclusion does not establish a network’s safety, decentralization, investment suitability, or expected returns. Ethereum-specific security analysis identifies possible proof-of-stake operational exposures including validator concentration, client concentration, key compromise, inactivity, slashing, censorship, and recovery risks under extreme conditions; this is a risk list, not a comparative security score or a conclusion about another network. (Claim: `claim_pos_operational_risks`.)

The evidence also does not establish current staking access, fees, yields, recovery procedures, or jurisdiction-specific legal, tax, or compliance treatment. Those questions require separate, current sources appropriate to the network, service, and reader’s circumstances. Treat the list as a starting point for verifying consensus terminology and roles, not as a recommendation to use or stake on any network.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Trillion Dollar Security: Consensus protocol](https://ethereum.org/reports/trillion-dollar-security.pdf) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
- [PoS Voting Overview](https://docs.decred.org/proof-of-stake/overview/) — Decred Documentation; retrieved 2026-10-19.
