---
title: "Proof of stake coins list: networks and validator participation"
description: "Review a proof of stake coins list organized by network consensus and validator participation, with notes on scope, verification, and key differences."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["proof stake coins list"]
author: "editorial_team"
primary_keyword: "proof of stake coins list"
owned_question: "Which cryptoassets are associated with networks that use proof-of-stake consensus, and what network-level differences should readers verify before treating them as comparable?"
risk_level: "medium"
---

A proof-of-stake coins list is best read as a list of native assets associated with networks that use proof of stake—not as a claim that those assets share the same validator rules or staking arrangements. The evidence available for this reference supports concise notes on Ethereum and Tezos, but does not support a broader, verified catalog of assets. Treat the entries below as representative, and check current network documentation before relying on them.

## What qualifies for this proof of stake coins list?

The inclusion rule here is narrow: an asset must be identified as native to a network for which the allowed evidence documents proof-of-stake consensus participation. A token used by an application, exchange, or third-party staking product does not qualify on that basis alone. Nor does an asset's name or marketing description establish how its network reaches consensus.

The list is limited by the primary evidence available for this article. It is not a complete census of proof-of-stake assets. The cited evidence describes Ethereum's validator and finality model and Tezos consensus participation rights, but it does not establish a full set of current native-asset associations or the latest operating requirements for every network. That gap matters: where primary documentation does not support an entry, it is better to leave it out than infer inclusion from a familiar ticker or product label.

## Proof-of-stake networks and associated assets

| Network | Associated native asset | Network-level participation note |
|---|---|---|
| Ethereum | ETH | Ethereum's proof-of-stake design combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. Validators perform block-checking and attestation duties, and a validator proposes a block when selected by the protocol. |
| Tezos | tez (XTZ) | Tezos consensus participation rights are selected from delegates according to protocol-defined baking power and pseudorandom selection. The documentation used here does not establish every current participation rule or how each service handles delegation. |

These entries are not interchangeable descriptions of one common mechanism. Ethereum's documented finality model explicitly uses checkpoint votes and a supermajority condition. Tezos documentation describes selection of consensus participation rights using baking power and pseudorandom selection. Those short descriptions identify distinctions to investigate; they do not fully specify either protocol or establish a direct performance, security, or return comparison.

The Tezos evidence is tied to current protocol documentation that cautions that its alpha documentation can change before activation; verify the active protocol version. The Ethereum evidence establishes its consensus design but does not provide a complete current operating checklist. For both entries, confirm the active network specification and asset relationship at the time of use rather than treating this table as a live registry.

## How validator participation differs across networks

A validator is a protocol role, but the details attached to that role are network-specific. On Ethereum, validators check and attest to blocks and propose one when selected. The protocol's incentives include rewards for correct participation, missed rewards or penalties for inactivity, and slashing for specified conflicting proposals or attestations. No current reward rate or universal penalty amount is established here.

Tezos describes consensus rights in terms of delegates selected according to protocol-defined baking power and pseudorandom selection. That statement should not be expanded into an assumption that all Tezos participants operate in the same way, or that a third party's service terms mirror the protocol. The evidence available for this list does not establish every current Tezos delegation rule, validator requirement, or service arrangement.

Keep protocol participation separate from intermediary products. A protocol's consensus rules do not, on their own, establish how an exchange, staking provider, custodian, or liquid-staking arrangement handles keys, withdrawals, fees, rewards, or recovery. Those are separate operational questions and require evidence about the particular service and its current terms. This list therefore does not treat a provider's staking product as proof that its associated token is a network's native asset or that the service reproduces the protocol's direct participation model.

There are also network-specific risks that the table cannot resolve. Ethereum's documented operational risk analysis identifies validator and client concentration, key compromise, inactivity, slashing, censorship, and recovery under extreme conditions as considerations. This is an Ethereum-specific risk set, not a universal ranking of proof-of-stake systems or a conclusion that another network is safer or riskier.

## How to verify an entry before relying on it

Use the same checks for each candidate rather than comparing tickers alone:

1. **Confirm the network's consensus documentation.** Look for current primary protocol documentation that explicitly describes proof of stake and the relevant validator or consensus-participant role. A general product page or a third-party staking offer is not enough to establish network consensus.
2. **Confirm the asset relationship.** Verify from network documentation that the named asset is native to, or directly associated with, that network. Do not infer this from a matching symbol or a wallet listing.
3. **Record what participation means.** Note whether the source documents validator duties, selection, delegation, finality, or penalties. Avoid treating these different dimensions as synonyms. The Ethereum and Tezos notes above illustrate why: one source describes attestations and checkpoint finality; the other describes selection rights by baking power and pseudorandom selection.
4. **Record source scope and date.** Protocol documentation can be version-specific or subject to change. The Tezos source explicitly warns that alpha documentation may change before activation, so check the active protocol version. For any entry, record the source and verification date and flag uncertainty instead of filling it with assumptions.
5. **Separate protocol facts from service terms.** If the question is about a provider, exchange, custodian, or liquid-staking arrangement, verify that specific arrangement independently. Network-level consensus documentation does not establish its fees, availability, custody, or recovery terms.

## What this list does not establish

An entry indicates only that the cited evidence supports a connection between an asset and a network-level proof-of-stake design. It does not establish investment merit, suitability, expected returns, liquidity, or a recommendation to acquire or stake an asset. The available evidence does not support current yields, prices, fees, or service availability, so none are listed.

The entries also do not provide a complete security assessment. Ethereum's documented operational risks are specific to Ethereum, and the limited Tezos evidence here is not enough to make a comparable risk assessment. Nor does inclusion establish that a particular third-party service follows the network's direct participation process.

Legal, regulatory, tax, and compliance treatment is not assessed in this reference. No jurisdiction-specific conclusion follows from a network's consensus mechanism or an asset's appearance in the table. For technical comparison, the useful next step is to verify each network's active protocol documentation, asset relationship, participant duties, and version—not to assume that every item labeled a proof-of-stake coin works alike.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
- [Trillion Dollar Security: Consensus protocol](https://ethereum.org/reports/trillion-dollar-security.pdf) — ethereum.org; retrieved 2026-10-19.
