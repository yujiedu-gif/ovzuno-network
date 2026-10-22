---
title: "Delegating crypto: How stake is assigned to validators"
description: "Learn what delegating crypto means, how delegators and validators interact, which network-specific rules shape the process, and what to check before delegating."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["crypto delegation", "staking delegation", "validator delegation"]
author: "editorial_team"
primary_keyword: "delegating crypto"
owned_question: "What does delegating crypto mean in proof-of-stake networks, how does delegation relate to validators, and what should a delegator check before delegating?"
risk_level: "medium"
---

Delegating crypto means assigning stake to a validator under a proof-of-stake network’s rules. It can increase the validator’s consensus weight, but the exact arrangement—including who controls the stake, what duties the validator performs, and how delegation can be changed—depends on the network and the wallet or service used. Before delegating, verify the protocol’s current rules for validator duties, penalties, custody, and exiting.

## What delegating crypto means

A delegator assigns stake to a validator so that the stake can contribute to the validator’s participation in consensus. For example, Solana’s native delegation model lets a delegator assign stake to a validator, increasing that validator’s consensus weight while the delegator retains token control under the stake-account model. That is a network-specific design, not a universal rule for delegation. ([source](<https://solana.com/docs/references/staking>))

The phrase “retains token control” should not be read as meaning that every related action is unrestricted. Delegation, key authority, activation, commission, and slashing behavior must be evaluated under Solana’s rules; other networks can define these features differently. Likewise, a wallet interface or third-party service may add its own permissions or operational steps. A delegation screen alone does not establish what the protocol permits or who holds the relevant keys.

Delegating stake is also different from operating a validator. A validator role may involve protocol duties and operational risks that do not automatically become the delegator’s duties. Delegation does not, however, guarantee that the validator will perform successfully or remove the delegator’s need to understand the terms that apply to their stake.

## How stake moves through the delegation process

There is no single network-neutral transaction sequence. A practical research workflow is to identify the exact network and account type first, then check its official documentation for how stake is assigned and what conditions apply. Confirm that the wallet or service supports that network’s mechanism rather than assuming that similar labels mean the same operation.

Next, establish what the delegation action authorizes. The relevant questions include whether stake is assigned to a named validator, which account retains authority over it, and which protocol rules govern changes or withdrawal. Solana documentation, for example, describes delegation through a stake-account model and specifies that delegation behavior should not be generalized to other networks. ([source](<https://solana.com/docs/references/staking>))

Before acting, look up the network’s documented activation, redelegation, unbonding, and withdrawal procedures, if applicable. The allowed evidence here does not establish universal waiting periods, transaction steps, minimum amounts, or exit rights. Those details should be confirmed for the particular protocol and the specific wallet or service. Do not assume a change is immediate just because an interface allows a request.

## What the validator and delegator each do

A validator performs protocol-defined consensus duties. In Ethereum, validator participation uses ETH deposits as slashable economic collateral. That describes Ethereum’s protocol design; it does not establish the custody terms of every staking product or service offered around it. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

Some networks specify validator selection or duties in other ways. Tezos consensus participation rights, for example, are selected from delegates according to protocol-defined baking power and pseudorandom selection. This is a Tezos-specific description, and the cited documentation is labeled alpha, so the active protocol version should be verified before relying on it. ([source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>))

The delegator’s role is not necessarily passive. A delegator should understand which validator receives the stake, how the network treats that stake, and what actions may be needed if the validator or protocol rules change. Delegation can affect validator consensus weight, but it does not make the delegator the validator operator or establish that the validator will remain available or meet every expectation.

## Risks and terms to verify before delegating

Use a checklist grounded in the current documentation for the exact network and account:

- **Validator selection and duties:** Confirm what the validator is expected to do and how the network selects participants. Do not treat a name, label, or interface description as proof of performance.
- **Commission and reward mechanics:** Check whether a commission applies, how it is calculated, and how rewards are attributed. The evidence available for this article does not establish universal fee rates, reward distribution rules, or minimum stake amounts.
- **Penalties and stake exposure:** Verify whether inactivity, misbehavior, or other events can affect the validator or delegator’s stake. Ethereum’s protocol includes slashing exposure for validator participation, but that statement should not be expanded into a claim about every network or third-party product. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))
- **Custody and permissions:** Determine who controls the keys and what authority the wallet, account, validator, or service has. A protocol’s delegation model does not, by itself, establish the custody or recovery arrangement of an application built on top of it.
- **Exit and changes:** Find the protocol’s rules for changing validators, unbonding, withdrawing, and any required waiting or transaction steps. These are network-specific and are not established here as universal conditions.
- **Operational exposure:** Consider whether validator concentration, client concentration, key compromise, inactivity, slashing, censorship, or recovery in extreme conditions is relevant to the network being assessed. These risks are identified in an Ethereum-specific analysis and should not be treated as a universal ranking of proof-of-stake systems. ([source](<https://ethereum.org/reports/trillion-dollar-security.pdf>))

Rewards, if available, are not guaranteed outcomes. Their terms and any quoted figures require current, network-specific evidence; this article does not estimate returns or recommend a delegation choice.

## How to research a specific network’s delegation rules

Start with the network’s official protocol documentation. Look for separate explanations of delegation mechanics, validator duties, penalties, stake control, and exit rules. Where the documentation distinguishes protocol behavior from wallet or service instructions, keep those layers separate: a protocol defines network rules, while an interface explains how that particular implementation presents or submits an action.

Check version and status as well as the page’s subject. Tezos’s cited baking-rights description is from alpha documentation and explicitly calls for verification against the active protocol version. A statement that may apply to one version should not be treated as a permanent rule. ([source](<https://octez.tezos.com/docs/alpha/proof_of_stake.html>))

Finally, verify the custody and recovery details for the actual account or service you intend to use. Protocol documentation may describe stake behavior without resolving who can authorize transactions, what recovery path exists, or what additional terms a provider applies. The allowed evidence does not establish jurisdiction-specific availability, legal or tax treatment, or compliance duties; those questions require current authoritative sources and qualified professional guidance.

The central decision is therefore not simply which validator to select. First establish how the chosen network assigns stake, what validator participation entails, what can happen to delegated stake, and how the account can change or exit the arrangement. Those answers belong to the exact network, protocol version, wallet, and service involved—not to a universal delegation workflow.

## Sources and references

- [Staking on Solana](https://solana.com/docs/references/staking) — Solana Documentation; retrieved 2026-10-18.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake](https://octez.tezos.com/docs/alpha/proof_of_stake.html) — Octez Documentation; retrieved 2026-10-19.
- [Trillion Dollar Security: Consensus protocol](https://ethereum.org/reports/trillion-dollar-security.pdf) — ethereum.org; retrieved 2026-10-19.
