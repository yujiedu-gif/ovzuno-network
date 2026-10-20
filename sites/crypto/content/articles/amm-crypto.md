---
title: "Amm Crypto: How It Works"
description: "Understand Amm Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["crypto_cards_spending"]
tags: []
author: "editorial_team"
primary_keyword: "amm crypto"
owned_question: "What is an automated market maker (AMM) in crypto, and how does it facilitate decentralized trading?"
risk_level: "medium"
---

# Amm Crypto: How It Works

An automated market maker (AMM) is a way to organize crypto-asset trading through smart contracts and liquidity pools rather than relying on a conventional order book to match each buyer with a seller. In an AMM-based decentralized exchange (DEX), users trade against assets held in a pool, and the contract applies the protocol’s rules to execute a swap. The transaction settles when it is included in a blockchain block. This describes the AMM-based DEX model; order-book, auction, intent-based, cross-chain, and hybrid DEX designs can follow different execution paths. [claim_bis_dex_contract_settlement]

For builders and operators, the key point is that “AMM” names a trading mechanism, not a guarantee about a complete product or service. The pool, contract rules, transaction path, user interface, and any supporting services may differ between implementations. Understanding how those pieces interact helps teams identify what a system does, what it depends on, and what still needs verification.

## What Amm Crypto means

In crypto, an AMM facilitates decentralized trading by using a smart contract to manage a pool of contributed assets and process swaps according to programmed rules. Rather than placing a resting order for a specific price and waiting for another user’s matching order, a trader submits a transaction that asks the contract to exchange assets under the pool’s applicable logic.

The pool is central to the model: it holds the assets against which users trade. Liquidity providers contribute assets to pools and can receive a share of trading fees. They also bear inventory and adverse-selection risk. [claim_bis_amm_liquidity] The exact fee arrangement and economic exposure depend on the protocol and position; pool formulas, fee tiers, price ranges, and loss allocation vary.

An AMM should not be treated as synonymous with every DEX. The AMM model discussed here uses contracts and liquidity pools, with settlement on blockchain block inclusion. Other exchange designs may use order books, auctions, intents, cross-chain mechanisms, or combinations of approaches. [claim_bis_dex_contract_settlement]

Nor does the term by itself establish that a system is permissionless in every respect, has a particular custody model, or offers a specific level of security. Those characteristics depend on implementation and surrounding services. The useful system boundary is therefore the swap path: the trader’s transaction, the relevant contract and pool state, the blockchain’s execution and settlement, and any interface or service that helps construct or submit the transaction.

## Core components of Amm Crypto

**Smart contracts.** Contracts implement the pool’s trading rules and process transactions that interact with it. The specific formula, fee structure, and other parameters are implementation-dependent. A team should inspect the deployed contract and its documented behavior rather than infer details from the AMM label alone.

**Liquidity pools.** A pool holds contributed assets that traders can exchange against. Its available inventory is relevant to execution: pool depth is one factor that can affect price impact before a transaction is included in a block. [claim_bis_amm_ordering] Pool composition and rules are not uniform across protocols.

**Liquidity providers.** Providers supply assets to a pool and can receive a share of trading fees. Their position also exposes them to inventory and adverse-selection risk. [claim_bis_amm_liquidity] For some AMM designs, a provider can experience an inventory-value loss relative to simply holding the assets as pool prices move. Trading fees may or may not offset that loss. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. [claim_bis_lp_loss]

**Traders and transaction interfaces.** A trader initiates a swap, often through a user-facing application or another transaction-construction tool. The interface can help form or submit a transaction, but the AMM’s contract rules and blockchain execution determine the on-chain swap behavior. Teams should distinguish the interface’s role from the contract’s role and verify which component supplies each piece of information or action.

**Blockchain execution and settlement.** A submitted swap is not settled merely because a user has prepared or sent it. In the AMM DEX model described by the BIS research, settlement occurs when the transaction is included in a blockchain block. [claim_bis_dex_contract_settlement] The transaction’s path and timing can matter because public visibility and execution ordering may affect the outcome before block inclusion.

## How Amm Crypto works

A typical AMM swap can be understood as a sequence. The exact interface and contract behavior vary, so this is a model of the principal steps rather than a specification for every protocol.

1. **A pool holds assets.** Liquidity providers contribute assets to a pool under its rules. They can receive a share of trading fees, while accepting inventory and adverse-selection risk. [claim_bis_amm_liquidity]
2. **A trader prepares a swap.** The trader selects the assets and amount to exchange and interacts with an application or transaction tool. The tool constructs a transaction for the relevant contract. The details of transaction construction and any additional checks are implementation-dependent.
3. **The transaction is submitted.** The transaction enters the blockchain’s execution process. In public-blockchain AMM execution analyzed by the BIS, the transaction’s public visibility and its ordering relative to other transactions can matter before block inclusion. [claim_bis_amm_ordering]
4. **The contract applies pool rules.** If the transaction is executed, the contract processes the swap using the pool’s state and programmed logic. Available pool depth and the resulting price impact are among the factors that can affect execution. [claim_bis_amm_ordering]
5. **The transaction is included and settles.** In the AMM-based DEX model, the transaction settles when included in a blockchain block. [claim_bis_dex_contract_settlement] Teams should verify the transaction’s actual status using the relevant chain and protocol evidence, rather than treating submission as proof of settlement.
6. **Pool state and provider exposure change.** A completed trade changes the pool’s holdings. As prices move, liquidity providers can experience inventory-value loss relative to holding the assets; fees may or may not offset it. The outcome depends on design, price path, range, fees, timing, and withdrawal state. [claim_bis_lp_loss]

This sequence shows why an AMM is not just a pricing formula. It connects contract logic and pool state to blockchain ordering and settlement. A user-facing application can simplify interaction, but it does not remove the need to understand those underlying steps.

## Trust and control boundaries

An AMM-based DEX places swap execution in smart contracts and settles transactions through blockchain block inclusion. [claim_bis_dex_contract_settlement] That is a description of the mechanism, not a claim that every surrounding component is decentralized or that any particular implementation is free of operational dependencies.

For technical review, separate at least three questions:

- **What does the contract control?** Identify the deployed contracts and determine which rules, pool state, and transaction actions they govern. Do not assume that different pools or protocols share the same formula, fees, or control structure.
- **What does the interface or service control?** Establish whether a user-facing tool only presents information and constructs transactions, or whether other services participate in routing, submission, or operation. The AMM label alone does not answer this.
- **What does the blockchain determine?** In the model described here, block inclusion is the settlement point. For public-blockchain execution analyzed by the BIS, transaction visibility and ordering can affect an AMM swap before inclusion. [claim_bis_amm_ordering]

This differs from assuming that every crypto exchange has the same organizational structure. BIS notes that a centralized crypto exchange operator may combine third-party trading, proprietary trading, margin lending, token issuance, and custody services. Not every exchange performs every function, and combining roles can create operational dependencies and conflicts. [claim_bis_cex_combined_functions] That observation concerns centralized exchange operators; it should not be generalized to all AMMs or used to infer the structure of a particular DEX.

## Limitations and failure modes

**Execution can be affected before settlement.** Public transaction visibility, execution ordering, pool depth, and price impact can affect a public-blockchain AMM swap before block inclusion. [claim_bis_amm_ordering] This is not a claim that every chain or transaction path behaves identically. Private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model. [claim_bis_amm_ordering]

**Liquidity does not eliminate price impact.** A pool provides assets for trading, but pool depth is relevant to a swap’s price impact. [claim_bis_amm_ordering] The AMM label alone does not tell a team how a particular trade will execute; that requires protocol- and transaction-specific evidence.

**Liquidity provision carries exposure.** Providers can receive a share of trading fees but bear inventory and adverse-selection risk. [claim_bis_amm_liquidity] A provider may incur inventory-value loss relative to holding the assets when pool prices move, and fees may or may not offset it. [claim_bis_lp_loss] The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. It should not be reduced to a universal result.

**The mechanism does not establish product-wide guarantees.** The accepted evidence describes AMM trading, settlement, and liquidity-provider exposure; it does not establish a universal security, recovery, availability, or custody guarantee for every protocol or interface. Those questions require evidence about the specific implementation and services involved.

## What teams should verify

A practical review can follow the transaction path from user action to settled state:

1. **Identify the design.** Confirm that the system actually uses an AMM and liquidity pools for the swap path. Check whether any order-book, auction, intent-based, cross-chain, or hybrid component changes execution. [claim_bis_dex_contract_settlement]
2. **Inspect the relevant contract and pool.** Record which contracts and pool state are involved. Verify the applicable trading rules, fee arrangements, and any position or range mechanics from protocol-specific documentation; do not assume uniform formulas or fee tiers. [claim_bis_amm_liquidity]
3. **Map transaction stages.** Document how a swap is prepared, submitted, executed, and confirmed. Treat block inclusion as the settlement point in the AMM DEX model described here, while checking the actual chain and protocol path. [claim_bis_dex_contract_settlement]
4. **Evaluate ordering assumptions.** Determine whether transaction details are publicly visible before inclusion and what ordering model applies. Account for the possibility that private order flow, batch auctions, encrypted mempools, rollups, or other designs alter the model. [claim_bis_amm_ordering]
5. **Assess pool depth and price impact.** Verify which pool state is relevant to the transaction and how the implementation represents expected execution. The evidence establishes these as factors, not a universal outcome for any particular swap. [claim_bis_amm_ordering]
6. **Separate provider economics from trader execution.** For liquidity-provider positions, review how fees and inventory exposure work under that pool’s design. Include the possibility that inventory-value loss relative to holding may or may not be offset by fees, with outcomes dependent on the price path, range, timing, and withdrawal state. [claim_bis_amm_liquidity] [claim_bis_lp_loss]
7. **Document dependencies and evidence.** List the contracts, interfaces, and external services on the transaction path, then identify what evidence supports each claimed behavior. Keep confirmed implementation details separate from assumptions that require further verification.

An AMM facilitates decentralized trading by using contracts and liquidity pools to execute swaps, with transactions settling on blockchain inclusion in the model covered here. Its real operating characteristics depend on the specific pool, contract, transaction path, and ordering design. A team that verifies each layer can explain both how a swap works and where the AMM model’s documented limits apply.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
