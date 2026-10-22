---
title: "All proof of stake coins: how to identify and verify them"
description: "Learn how to identify all proof of stake coins using network consensus documentation, clear inclusion criteria, and checks that separate native staking from services"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["staking_validators"]
tags: ["all proof stake coins"]
author: "editorial_team"
primary_keyword: "all proof of stake coins"
owned_question: "How can readers identify and verify cryptocurrencies that use proof-of-stake consensus, and what limits apply to any list of them?"
risk_level: "medium"
---

To identify proof-of-stake (PoS) cryptocurrencies, verify the consensus model of each asset’s native network in current protocol documentation, then record the network, native asset, evidence, and date checked. The evidence available for this guide supports a limited reference—not a complete or current inventory of all PoS coins—so treat unverified candidates as unresolved rather than assuming that a token’s staking feature proves its network uses PoS.

## What counts as a proof-of-stake coin?

For this guide, a PoS coin is the native asset of a network whose consensus model uses cryptocurrency committed as stake, with stake influencing consensus participation or weight. The key test concerns the network’s consensus rules, not a feature or label attached to an asset by an exchange, wallet, or application. [source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>)

This is a classification rule, not a claim that every network uses the same validator selection, delegation, custody, reward, penalty, or withdrawal rules. Those are protocol-specific. A candidate should remain outside the confirmed list until documentation establishes that its underlying network uses PoS or a clearly identified PoS variant.

A token can be made available for staking-like activity through a service without being the native asset of a PoS network. Keep those facts separate: identify the network that runs consensus, identify its native asset, and then describe any third-party or application-based participation separately. The evidence available here does not establish a catalog of such services, so this guide does not classify their offerings.

Hybrid designs need a similarly careful description. If a network combines PoS with another consensus component, record the roles supported by its documentation instead of labeling the design as equivalent to a PoS-only system. For example, Ethereum’s PoS model uses ETH deposits as slashable economic collateral for validator participation; that evidence supports the Ethereum entry below, not a general statement about other networks. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

## How to verify a coin’s consensus model

Use a repeatable check for each candidate:

1. **Identify the network, not just the ticker or token name.** Record the network the asset is native to. A similarly named asset on another network is a separate candidate and needs its own evidence.
2. **Find protocol-level evidence.** Look for the network’s current consensus documentation or specification. It must support the specific classification being made; an exchange’s staking page or a wallet’s feature description does not establish the network’s consensus model.
3. **Check what the evidence actually says.** Confirm whether the source describes the network’s active protocol, a former design, a proposed change, or one specific participation method. Do not expand a narrow statement into a broader claim about all network behavior.
4. **Record the verification date and source.** Consensus designs can change. A date makes clear when the documentation was checked; it does not guarantee that the network remains unchanged afterward.
5. **Mark uncertainty explicitly.** If documentation is outdated, ambiguous, or conflicting, leave the entry unconfirmed until the discrepancy is resolved. Do not turn absence of evidence into confirmation.

For a network with documented validator rewards or penalties, those details can help corroborate its participation model, but they are not a substitute for identifying the consensus rules. Ethereum documentation, for example, describes rewards for correct participation, missed rewards or penalties for inactivity, and slashing for specified conflicting messages. These are Ethereum-specific details, not universal PoS rules. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>)

Likewise, a documented finality mechanism can help characterize a network, but it should not be presented as a property shared by every PoS chain. Ethereum’s finality model uses validator votes on checkpoint blocks to distinguish finalized history from blocks that have merely been included. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

## All proof of stake coins: a scoped reference list

The entries below are the PoS classifications supported by the allowed evidence for this guide. They are a limited, evidence-backed snapshot, not an exhaustive list of every cryptocurrency whose network may use PoS. The available evidence does not establish a complete dataset or a single verification date for a broader universe of networks, so no completeness claim is warranted.

| Network | Associated native asset | Evidence supporting classification | Coverage note |
|---|---|---|---|
| Ethereum | ETH | Ethereum proof of stake uses ETH deposits as slashable economic collateral for validator participation. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>) | This supports classifying Ethereum as PoS. The guide does not make claims about provider staking products or present participation terms as universal. |

The table intentionally contains only the network-asset pair supported by the evidence available here. A blank or absent network is not evidence that it does not use PoS; it means this guide cannot confirm it within its evidence limits. To expand the table, apply the verification steps above and add a dated source for each network rather than copying unverified lists.

## Assets and staking claims to keep separate

“Staking” can refer to different activities. Consensus staking means that an asset is committed under a network’s protocol and affects consensus participation or weight. A custodial or application service may also describe an offering as staking, but that label alone does not show that the asset’s underlying network uses PoS. The classification should follow the network documentation, while the service should be evaluated separately under its own terms and evidence.

Delegation does not automatically change which network an asset belongs to. It is a participation arrangement whose permissions, custody, selection, rewards, and withdrawal rules depend on the protocol. Do not infer a network-wide property from a single wallet or provider interface.

For hybrid consensus, name the components and their respective roles only when sources support them. For Ethereum, the evidence here identifies ETH as slashable collateral in PoS validator participation; it does not support a claim that Ethereum currently combines PoS with proof of work. For other candidates, verify the active design rather than relying on an old label or a generic description.

## What a PoS classification does—and does not—tell you

A PoS classification answers a narrow question: whether the network’s consensus model uses stake in consensus participation or weight. It does not establish that the network is safe, decentralized, fast, suitable for a particular user, or likely to operate in a particular way. Those conclusions require separate evidence and criteria.

Nor does the classification establish that a person can participate directly, what a service may offer, what fees apply, or what rewards someone might receive. Participation requirements and operating details must be checked against current network documentation and, where relevant, the specific service. This guide makes no yield comparison or recommendation.

Treat every reference list as time-bounded. Recheck protocol documentation when relying on an entry, record the date, and distinguish confirmed facts from unresolved candidates. Because the evidence here supports only a narrow set of network-specific claims, the practical result is a verification method and one supported example—not a definitive answer to every possible interpretation of “all proof of stake coins.”

## Sources and references

- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
