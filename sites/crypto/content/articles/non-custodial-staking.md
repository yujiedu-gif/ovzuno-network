---
title: "Non custodial staking: control, delegation, and protocol risks"
description: "Learn how non custodial staking separates asset control from validator participation, how delegation and rewards work, and which protocol risks to check."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["wallets_custody"]
tags: ["staking delegation", "validator", "staking rewards", "slashing risk"]
author: "editorial_team"
primary_keyword: "non custodial staking"
owned_question: "How does non-custodial staking work, what control does the participant retain, and what responsibilities and protocol risks remain?"
risk_level: "medium"
---

Non-custodial staking generally means a participant retains control of the keys or authorization needed to access and direct assets, while committing or delegating stake under a blockchain’s rules. It does not mean the participant operates the validator, controls consensus, or avoids protocol and operational risks. The exact division of authority depends on the network and staking arrangement.

## What non-custodial staking means

“Custody” concerns who controls access to assets; “staking” concerns committing cryptocurrency to a proof-of-stake system. In a general proof-of-stake model, cryptocurrency is locked or committed as stake, and stake influences consensus weight. The details of how this commitment is made and what authority remains with the participant vary by protocol. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))

The term *non-custodial* is best treated as a description of a control arrangement, not a guarantee about every action or risk. A participant might retain control of assets while another party operates validator infrastructure, or might use a service or contract to participate. The available evidence here does not define the permissions, custody model, fees, safeguards, or recovery procedures of any particular service or contract. Those must be checked in the applicable documentation rather than inferred from a label.

Staking also does not make an asset risk-free or guarantee a reward. For Ethereum specifically, validator participation uses ETH deposited as slashable economic collateral rather than proof-of-work mining. This Ethereum-specific description should not be assumed to define other networks’ staking mechanics. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

## How delegation and validator participation work

A participant may stake directly or delegate under a protocol’s rules. In a delegation arrangement, the participant assigns stake to a validator or other protocol-recognized participant; the protocol determines how that stake affects consensus participation. The person delegating and the validator therefore have distinct roles, even when their activity contributes to the same network process.

Solana provides one specific example: a delegator can assign stake to a validator, increasing that validator’s consensus weight, while the delegator retains token control under the stake-account model. This illustrates that delegation and token control can be separate, but it is not a universal description of delegation on other networks. ([source](<https://solana.com/docs/references/staking>))

Validator duties, selection, voting, rewards, penalties, and withdrawal rules vary by protocol. The general proof-of-stake definition establishes that stake influences consensus weight; it does not establish what a validator must do, how a particular chain calculates rewards, or what happens after a missed or incorrect action. Readers need the rules for the specific network and staking arrangement before drawing conclusions about participant or validator responsibilities.

## Who controls assets, keys, and staking actions

Separate four questions when assessing an arrangement: who controls the assets, who can authorize transactions, who operates the validator, and which protocol rules govern the stake. A participant’s continued control of assets does not by itself show that the participant runs validator infrastructure. Conversely, delegation to a validator does not, by itself, tell you every permission granted to a service or contract involved in the process.

For a concrete model, Solana’s stake-account description says the delegator retains token control while the assigned stake increases validator consensus weight. That evidence supports a distinction between delegation and token control in that model; it does not establish the precise signatures, interfaces, withdrawal steps, or permissions for every Solana application or service. ([source](<https://solana.com/docs/references/staking>))

Before participating, map each action to the party and mechanism that authorizes it. Check the network’s documentation for staking, changing delegation, and withdrawal procedures. If a service or contract is involved, examine its own documentation for what it can authorize or redirect. The evidence available for this article does not specify those service-level permissions, so no general claim about them is warranted.

## Rewards, withdrawals, and protocol risks

Reward accounting and exit mechanics are protocol-specific. The general proof-of-stake definition says stake influences consensus weight, but does not specify a reward rate, payout schedule, fee, unbonding period, or withdrawal path. Nor does it establish that every protocol uses slashing or applies the same penalties. Treat those as questions to verify in current protocol documentation, not as universal features of non-custodial staking.

For Ethereum, the allowed evidence describes validator deposits as slashable economic collateral. That supports identifying a protocol-level loss mechanism for Ethereum validator participation, but it does not establish how any separate staking service handles the risk or whether a participant’s particular delegated arrangement is exposed in the same way. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

Keep protocol risks distinct from custody and service risks. Protocol documentation addresses network-defined behavior; it does not, on its own, establish a service’s key controls, contract permissions, operational safeguards, or recovery process. Conversely, a service’s description of its controls does not define the protocol’s reward, penalty, or exit rules. Review both layers where both are involved, and avoid treating a claim about one layer as evidence about the other.

## What to verify before participating

Use a mechanics-first check rather than relying on the phrase “non-custodial” alone:

- **Control and authorization:** Identify who controls the relevant keys or transaction authorization, and whether any service or contract can take actions affecting the stake. The evidence available here does not establish these details for a particular arrangement.
- **Delegation and validator role:** Read the network’s documentation to determine what delegation changes, what the validator does, and which responsibilities remain with the participant. Do not generalize a network-specific example to another protocol.
- **Rewards and exit:** Verify the current rules for reward accounting, fees, withdrawal, and any waiting or unbonding requirements. The general evidence cited here does not specify those terms.
- **Penalties and dependencies:** Check whether the protocol defines slashing or other penalties, then separately review any service, contract, or validator dependencies. Ethereum’s slashable-collateral description is specific to Ethereum validator participation.
- **Scope of claims:** Distinguish documented protocol behavior from a provider’s statements about its own architecture. This article does not establish jurisdictional availability, legal or tax treatment, or compliance obligations.

Non-custodial staking can separate a participant’s asset control from a validator’s consensus role, as the Solana delegation example shows. But that distinction does not answer every operational question. The participant still needs to verify the protocol’s specific delegation, authorization, reward, withdrawal, and penalty rules, as well as any additional service or contract permissions involved.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Staking on Solana](https://solana.com/docs/references/staking) — Solana Documentation; retrieved 2026-10-18.
