---
title: "Amm in Crypto: How It Works"
description: "Understand Amm in Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "amm in crypto"
owned_question: "What is an automated market maker (AMM) in crypto, and how does it enable decentralized trading?"
risk_level: "medium"
---

# Amm in Crypto: How It Works

An automated market maker (AMM) is a way to organize trading through a set of rules implemented by software, rather than matching each buyer with a specific seller through a conventional order book. In an AMM-based decentralized exchange, smart contracts and liquidity pools provide the trading mechanism, and a transaction is settled when it is included in a blockchain block. The exact execution path depends on the exchange design: an AMM is one model, not a description of every decentralized exchange.

Understanding an AMM therefore means looking beyond its pricing rule. A team evaluating one should identify the pool’s assets and accounting, the contract and blockchain that process swaps, the interfaces and other services involved, and the conditions that can affect execution. The description below distinguishes a documented AMM pattern from features that vary by implementation.

## What Amm in Crypto means

An AMM uses a pool of assets and a programmed mechanism to execute swaps. In the Uniswap v2 constant-product example, a pool holds deposited reserves of a token pair. Those reserves are inventory from which swaps execute, while liquidity-provider shares represent contributions to the pool. This is a specific implementation example, not a universal definition of AMM accounting: other designs can use different curves, assets, fees, and accounting methods.

The broader AMM-based decentralized-exchange model connects that pool to smart contracts. A trader submits a transaction that requests a swap under the protocol’s rules. If the transaction is included in a blockchain block, the exchange’s contract logic applies and the transaction settles on-chain. The pool’s state and the contract rules—not a guaranteed match with a particular counterparty—form the mechanism for completing the trade.

This distinction also sets a boundary around the term “decentralized exchange.” Decentralized exchange designs include more than AMMs: order-book, auction, intent-based, cross-chain, and hybrid systems can use different execution paths. Even within the AMM category, reliance on an interface, relayer, administrator, or off-chain component can vary. The label alone does not establish how every part of a particular system works.

## Core components of Amm in Crypto

A useful architecture map separates the following components and responsibilities:

- **Liquidity pool and state:** The pool holds assets used for swaps and maintains state relevant to its design. In the Uniswap v2 example, that state includes the deposited reserves of a token pair. Other AMMs may represent assets or calculate exchange outcomes differently.
- **Smart contracts:** Contract logic applies the exchange’s rules and processes transactions. In the AMM-based DEX model discussed by the BIS, trades are implemented through smart contracts and pools, with transactions settled when included in a blockchain block.
- **Liquidity providers:** Providers contribute assets to a pool. In the Uniswap v2 example, shares represent those contributions. Their exposure is not simply equivalent to holding the deposited assets outside the pool: price movements can produce an inventory-value loss relative to holding, and fees may or may not offset it.
- **Traders and transaction submitters:** A user or a connected service constructs and submits a transaction to request a swap. The path from user action to blockchain submission can involve an interface or other components, depending on the design.
- **Blockchain and block production:** The blockchain supplies the environment in which the relevant contracts run and transactions settle. Inclusion in a block is part of the settlement path; it does not mean every submitted transaction will be included or that execution conditions are identical across designs.
- **Interfaces and supporting services:** A front end can help users inspect a pool and prepare a transaction. Interfaces, relayers, administrators, and off-chain order components may also be dependencies. Their presence and authority are implementation-specific, so teams should not infer a trust model from the AMM label alone.

This component view helps distinguish protocol logic from the surrounding operational stack. A pool contract may govern swap execution, while a separate interface helps a user formulate a request. The contract’s behavior, the user’s route to that contract, and the blockchain’s transaction process are related but not interchangeable questions.

## How Amm in Crypto works

A typical AMM swap can be understood as a sequence. The details below describe the general contract-and-pool model; exact transaction fields, pricing rules, and service dependencies vary by implementation.

1. **A pool has assets available for trading.** Liquidity providers deposit assets into a pool. For the Uniswap v2 example, the pool’s token-pair reserves provide swap inventory, and provider shares represent contributions.
2. **A trader selects a swap and prepares a transaction.** The user specifies the requested trade through a wallet or an interface that prepares a transaction. The particular interface, routing mechanism, and transaction controls are not established by the general AMM model and should be checked for the system in question.
3. **The transaction is submitted to the blockchain.** A submitted transaction may become publicly visible before block inclusion in public-blockchain execution models. Its path may also involve services or designs that change how it is submitted or observed.
4. **The transaction is ordered and included.** Public transaction visibility, execution ordering, pool depth, and price impact can affect an AMM swap before block inclusion. The resulting execution is not determined by the pool formula alone. Private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model, so the public-blockchain account should not be assumed to describe every system.
5. **The contract processes the swap against pool state.** If included, the transaction is handled under the relevant contract rules and pool state. A pool’s depth and the requested trade’s size matter to the execution context; the exact pricing curve and fee mechanics depend on the implementation.
6. **Settlement occurs on-chain.** In the AMM-based DEX model discussed by the BIS, the transaction settles when included in a blockchain block. A team should verify the actual settlement conditions and transaction status for the particular chain and protocol rather than treating submission as settlement.

The sequence explains why an AMM is not simply a formula. The pool’s inventory and contract logic are central, but the user’s transaction also passes through a submission and inclusion process. A system’s ordering model and surrounding services can affect what happens before settlement.

## Trust and control boundaries

A public permissionless decentralized-exchange model can allow a user to retain control of assets while trades execute or settle through smart contracts on a blockchain. That is a meaningful distinction from a system in which a user must transfer assets to a counterparty for custody. It is not, however, a blanket assurance that every interface or supporting service is non-custodial, or that every DEX has the same control model.

Teams should separate at least three questions:

- **Who controls the assets before a swap?** The DEX model can let users retain control while trades execute or settle through contracts. Check whether the actual product introduces custody or another asset-control step.
- **What controls the execution rules?** Inspect the contracts and pool mechanics that apply to a swap. Do not assume that one AMM’s curve, fees, or accounting describe another.
- **Which supporting components can affect access or execution?** Interfaces, relayers, administrators, and off-chain order components may be dependencies. Their role and authority can differ, and the DEX label does not answer those questions.

These boundaries keep the analysis precise: documented behavior of a pool or contract does not, by itself, document the behavior of every service through which users reach it.

## Limitations and failure modes

AMM execution does not guarantee a particular result merely because a swap was submitted. In public-blockchain AMM execution analyzed by the BIS, public transaction visibility, execution ordering, pool depth, and price impact can affect a trade before block inclusion. The ordering model can differ in systems that use private order flow, batch auctions, encrypted mempools, rollups, or other designs. Evaluation therefore needs to account for the actual execution environment, not just the pool’s stated mechanism.

Liquidity provision has a separate exposure. When pool prices move, a liquidity provider can experience an inventory-value loss relative to holding the assets outside the pool. Trading fees may or may not offset that loss. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. This commonly discussed exposure, often called impermanent loss, is not a claim that every provider will incur the same result or that fees will reliably compensate for it.

Finally, AMMs are not the only way to build a decentralized exchange. Order-book, auction, intent-based, cross-chain, and hybrid designs can use different execution paths. A technical review that treats all DEXs as AMMs—or assumes all AMMs share one pool formula—can miss material differences in state, transaction flow, and dependencies.

## What teams should verify

For a protocol, integration, or operational review, use evidence tied to the exact system and version under consideration. A practical checklist is:

1. **Identify the mechanism.** Confirm that the system actually uses an AMM, and record whether its execution path also includes order-book, auction, intent-based, cross-chain, or hybrid elements.
2. **Map pool state and accounting.** Determine which assets a pool holds, how its state is represented, what a provider share means, and which pricing curve and fee rules apply. Treat Uniswap v2’s token-pair reserves and contribution shares as one example, not a default for every AMM.
3. **Trace a transaction end to end.** Document how a user action becomes a submitted transaction, which contracts process it, how it reaches the blockchain, and what event or condition constitutes settlement. Distinguish submission from block inclusion and settlement.
4. **Examine execution ordering.** Establish whether the relevant path exposes transactions publicly before inclusion and whether private order flow, batch auctions, encrypted mempools, rollups, or other designs change the ordering model. Assess pool depth and price impact as part of the execution context.
5. **Locate control and service boundaries.** Identify who controls assets at each step and which interfaces, relayers, administrators, or off-chain order components are involved. Verify their responsibilities rather than inferring them from the term “decentralized.”
6. **Assess liquidity-provider accounting.** Review how provider exposure is measured, including the comparison with holding assets, and how pool design, price path, range, fees, timing, and withdrawal state enter the analysis. Do not assume fees offset inventory-value loss.
7. **Check the evidence’s scope.** Confirm that documentation covers the specific contracts, pool design, chain, and operating path being evaluated. A claim about one constant-product pool or public-blockchain execution model does not automatically extend to other implementations.

An AMM enables a form of decentralized trading by using pool inventory and smart-contract rules to process swaps, with blockchain inclusion and settlement in the AMM-based DEX model described here. Its practical behavior still depends on the pool design, transaction-ordering environment, and surrounding services. Keeping those layers distinct gives builders and operators a clearer basis for technical review without treating a general model as a guarantee about a particular deployment.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
