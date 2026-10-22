---
title: "Crypto proof of stake list: networks and verification criteria"
description: "Use this crypto proof of stake list to identify networks using proof-of-stake consensus, understand inclusion criteria, and verify each model."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["staking_validators"]
tags: ["crypto proof stake list"]
author: "editorial_team"
primary_keyword: "crypto proof of stake list"
owned_question: "Which prominent crypto networks use proof-of-stake consensus, and how can readers verify each network’s consensus model and staking role?"
risk_level: "medium"
---

For a scoped crypto proof of stake list, this article identifies the networks supported by the available network-specific evidence: Ethereum and Tezos. Ethereum’s documentation describes proof-of-stake finality, while Tezos documentation describes consensus participation rights assigned to delegates through protocol-defined baking power and pseudorandom selection. This is a limited reference list, not a claim that these are the only networks using proof of stake.

## How this crypto proof of stake list defines inclusion

A network qualifies here only when the allowed evidence supports a proof-of-stake classification or a clearly identified proof-of-stake consensus role for that network. The evidence available for these entries is network-specific: Ethereum’s finality model is described through validator votes on checkpoint blocks, while Tezos materials describe how consensus participation rights are selected from delegates. These are distinct descriptions, not interchangeable accounts of one universal design. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>)

The list concerns a network’s consensus design. It does not treat a third-party staking service, a token marketed as a staking product, or an exchange’s staking offering as proof that the underlying network uses proof of stake. Nor does the classification establish who operates a validator or which custody arrangement a user might encounter; the evidence here does not assess those products or arrangements.

The two entries below are included because their allowed claims identify relevant technical behavior. The evidence packet does not provide primary-source titles, publication dates, or access dates for these claims. For that reason, the list does not label them as verified against a particular current software release. Readers should check the network’s current official documentation before relying on a classification operationally.

## Networks that use proof-of-stake consensus

| Network | Consensus-model note supported by the available evidence | Scope limit |
|---|---|---|
| **Ethereum** | Ethereum proof-of-stake finality uses validator votes on checkpoint blocks to distinguish finalized history from blocks that are merely included. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) | This describes a finality component, not every operational detail of Ethereum consensus or an individual validator’s responsibilities. |
| **Tezos** | Tezos consensus participation rights are selected from delegates according to protocol-defined baking power and pseudorandom selection. [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>) | The cited documentation is described as alpha documentation that can change before activation; verify the active protocol version. |

The entries should not be read as a ranking or endorsement. In particular, a consensus label does not say whether a network, token, validator, or staking arrangement is appropriate for a reader. The evidence here supports only the stated network-level descriptions.

## How to verify a network’s consensus model

Start with the network’s own protocol documentation or consensus specification, rather than a provider’s description of a staking service. Confirm that the source discusses the network’s consensus rules, not simply a product that lets users delegate, pool, or hold an asset. Then check whether the documentation applies to the active protocol version. The Tezos claim illustrates why this matters: its source is explicitly described as alpha documentation that can change before activation. [source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>)

For a technical review, identify what the source actually establishes. Ethereum’s evidence here establishes a role for validator votes in checkpoint finality; it does not, by itself, describe every validator duty. Tezos’s evidence establishes a selection basis for consensus participation rights; it does not provide a complete operating guide. Keep the classification as narrow as the source: a documented mechanism or role should not be expanded into claims about rewards, security, decentralization, or user control.

If official materials appear outdated, conflict, or do not describe consensus clearly, leave the network off a definitive list until the uncertainty is resolved. The allowed evidence for this article does not substantiate additional network entries or provide a source-by-source current-version audit. That is a limitation of this reference, not evidence that other proof-of-stake networks do not exist.

## What the list does not compare

This list does not rank networks, tokens, validators, custodians, or staking providers. It does not compare yields, token prices, fees, or returns, and it gives no validator setup, delegation, custody, or transaction instructions. Inclusion means only that the allowed evidence supports the stated proof-of-stake-related classification.

It also does not equate proof of stake with liquid staking or any other third-party service. A network’s consensus mechanism and a provider’s product are different subjects. Evaluating a service would require evidence about that service’s design and terms, which is outside the scope of the evidence available here.

## Risks and limits when interpreting the list

A proof-of-stake classification alone does not establish that a network is secure or that assets will be recoverable. Ethereum-specific analysis identifies possible operational risks including validator concentration, client concentration, key compromise, inactivity, slashing, censorship, and recovery under extreme conditions. Those are risks identified for Ethereum’s proof-of-stake operation; they should not be generalized into a universal risk ranking of proof-of-stake networks. [source](<https://ethereum.org/reports/trillion-dollar-security.pdf>)

Likewise, the fact that a system is distributed does not by itself show how independent its operators are. A general NIST description says a distributed blockchain network can reduce the ability of one bad actor to affect consensus as independently operated nodes increase, while cautioning that node count alone does not establish operator independence, geographic diversity, implementation diversity, or block-production power. This is general context, not a measurement of either listed network. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

Protocol rules can change, and evidence can be version-specific. Recheck official consensus documentation and relevant upgrade records when using this list, especially where a source is marked as changeable. The available evidence does not support jurisdiction-specific conclusions or claims about fees, yields, availability, tax treatment, compliance, or asset recovery, so none are made here. The practical takeaway is to treat this as a narrow, evidence-limited starting reference and verify each network’s current primary documentation before drawing further conclusions.

## Sources and references

- [Trillion Dollar Security: Consensus protocol](https://ethereum.org/reports/trillion-dollar-security.pdf) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
