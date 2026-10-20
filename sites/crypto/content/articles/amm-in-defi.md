---
title: "Amm in DEFI: How It Works"
description: "Understand Amm in DEFI, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "amm in defi"
owned_question: "How do automated market makers (AMMs) work in DeFi, and how do they differ from order-book exchanges?"
risk_level: "medium"
---

# Amm in DEFI: How It Works

An automated market maker (AMM) is a way to execute swaps using rules encoded in a protocol rather than matching each trade with a specific counterparty’s resting order. In decentralized finance (DeFi), an AMM-based decentralized exchange can implement trading through smart contracts and liquidity pools; transactions settle when they are included in a blockchain block. This describes one exchange model, not every decentralized exchange: order-book, auction, intent-based, cross-chain, and hybrid designs can follow different execution paths.

The difference from an order-book exchange is therefore about how liquidity is represented and trades are executed. An order book records bids and offers, while an AMM swap interacts with a pool under the pool’s rules. The term “automated” does not mean that execution is free of dependencies, discretionary design choices, or operational risk. Pool mechanics, blockchain settlement, interfaces, and transaction ordering all matter.

## What Amm in DEFI means

An AMM is a mechanism for quoting and executing trades against pooled assets according to a mathematical rule. In one concrete example, a Uniswap v2 pool holds deposited reserves of a token pair as the inventory from which swaps execute. Liquidity-provider shares represent contributions to that pool. This is a specific constant-product AMM example; other AMMs may use different curves, assets, fees, and accounting.

A pool is not the same thing as a conventional broker holding a customer’s order and searching for a matching seller. A swap draws on the pool’s available inventory, and the pool’s design determines how the trade interacts with that inventory. The source material supports this general distinction, but it does not establish a universal formula or fee structure for all AMMs.

It is also useful to distinguish the user-facing exchange from the system that settles a trade. A DeFi application can be analyzed as having settlement, application, and interface layers, each with distinct technical dependencies. A particular system may combine or distribute those layers differently. Thus, a website or wallet interface is not itself the pool or the blockchain settlement mechanism, even when it is the route a user takes to access them.

## Core components of Amm in DEFI

**Liquidity pool and reserves.** In the Uniswap v2 example, deposited reserves of two tokens provide the inventory used for swaps. The pool’s accounting and pricing rule govern how trades interact with those reserves. This example should not be generalized to every AMM without checking its implementation.

**Liquidity providers.** Providers contribute assets to a pool. In Uniswap v2, shares represent those contributions. The value and composition of a provider’s position can change as pool prices move and trades occur; fees may or may not offset the resulting difference in value relative to simply holding the assets.

**Smart contracts and application logic.** In the AMM DEX model described by the BIS, smart contracts and pools implement trading. The precise contract behavior depends on the deployed protocol and version. A protocol’s documentation, contract code, and configuration are therefore relevant evidence; the label “AMM” alone does not specify all execution rules.

**Blockchain settlement.** Under the cited AMM DEX model, a transaction settles when included in a blockchain block. Before inclusion, a submitted transaction is not yet a settled swap. The chain and transaction-submission path are therefore part of the system’s operational dependencies.

**Interface and transaction submission.** A user may interact through an application interface that prepares or submits a transaction. The interface layer can be distinct from the application and settlement layers, though a system may combine or distribute them. Verifying which interface, contract, and chain are involved is part of understanding the actual transaction path.

## How Amm in DEFI works

A typical AMM swap can be understood as a sequence, while recognizing that exact steps and rules vary by protocol:

1. **The user chooses a pool and trade.** The intended swap identifies the relevant assets and pool. In a pool-based design, that pool’s available reserves and rules determine the trade’s interaction with inventory.
2. **The application prepares a transaction.** The interface or other application component presents transaction details and submits or facilitates submission. The interface is not the same as blockchain settlement.
3. **The transaction waits for execution.** On a public blockchain, a submitted transaction may be visible before it is included in a block. Public transaction visibility and execution ordering can affect an AMM swap, alongside pool depth and price impact. These effects are not universal in the same form: private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model.
4. **The protocol executes against pool inventory.** If included and executed under the applicable contract rules, the swap uses the pool’s inventory. In the Uniswap v2 example, the relevant inventory is the deposited reserves of the token pair. Other AMMs may implement different curves, fees, assets, or accounting.
5. **The blockchain records settlement.** In the cited AMM DEX model, settlement occurs when the transaction is included in a blockchain block. Inclusion is a key point for distinguishing a pending submission from a settled transaction.
6. **Pool positions reflect activity.** A completed swap changes the pool’s state according to its implementation. Liquidity providers’ exposure reflects the pool’s assets and design, not simply the number of shares they hold.

This flow contrasts with an order-book model, where bids and offers are represented as orders and execution depends on matching. The distinction is not a claim that every exchange fits one of two pure categories: the accepted source material explicitly allows for order-book, auction, intent-based, cross-chain, and hybrid DEX designs with different paths.

## Trust and control boundaries

AMMs replace some forms of counterparty matching with contract-mediated interaction, but that does not remove trust or control questions. A technical review should separate what the pool contract specifies from what the interface, transaction-submission route, and blockchain do.

The pool’s rules define how trades interact with reserves, but “AMM” does not identify a single curve or accounting model. The interface is a separate layer in the DeFi reference model, and the settlement layer determines when an included transaction is recorded. A system may combine or distribute these layers differently, so teams should map the deployed arrangement rather than assume a standard architecture.

Execution ordering is another boundary. For public-blockchain AMM execution analyzed by the BIS, public transaction visibility and ordering can affect a swap. That claim is scoped: private order flow, batch auctions, encrypted mempools, rollups, and other designs can change the ordering model. It would therefore be inaccurate to treat the public-mempool description as a universal property of every AMM transaction.

Likewise, a pool’s reported mechanics do not by themselves establish the security, availability, or recovery characteristics of the interface or underlying chain. Those properties require system-specific evidence. The available claims do not establish a universal guarantee that a transaction will execute, that a particular interface will remain available, or that an asset can be recovered after an error.

## Limitations and failure modes

**Price impact and pool depth.** Pool depth is one factor affecting public-blockchain AMM execution. A swap’s interaction with available inventory can affect its result, but the accepted claims do not supply a universal threshold or formula. Teams should verify the relevant pool mechanics and transaction parameters for the implementation under review.

**Transaction visibility and ordering.** Public transaction visibility and execution ordering can affect an AMM swap before block inclusion. The scope matters: other transaction-routing and execution designs can alter this model. A review should establish how a given system handles submission and ordering rather than assume all AMMs expose transactions in the same way.

**Liquidity-provider inventory exposure.** When pool prices move, a liquidity provider can experience an inventory-value loss relative to holding the assets. Trading fees may or may not offset that difference. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. This exposure is commonly called impermanent loss, but the name should not be mistaken for a guarantee that the difference will reverse or be offset.

**Implementation variation.** A Uniswap v2 constant-product pool is an example, not a definition for all AMMs. Curves, assets, fees, accounting, and execution paths can differ. A conclusion drawn from one pool’s documentation should not be applied to another without evidence.

**Settlement and layered dependencies.** Because the cited AMM DEX model settles transactions when included in a block, submission and settlement are distinct stages. The interface, application logic, and settlement environment have separate dependencies, though a specific system may combine layers. Reviewing only the visible interface leaves parts of the transaction path unexamined.

## What teams should verify

For a technical assessment, document evidence for each part of the system rather than relying on a product label:

- **Identify the design:** Is the exchange an AMM, order book, auction, intent-based, cross-chain, or hybrid system? What evidence describes its actual execution path?
- **Inspect the pool model:** Which assets and reserves are involved? What curve, fee rules, and accounting apply to the deployed pool? Do not infer these details from another AMM’s documentation.
- **Map participants and state:** Who supplies liquidity, what represents a provider’s contribution, and how does the implementation account for pool assets and shares?
- **Trace a swap:** Which interface prepares the transaction, which application logic is invoked, and which settlement layer records inclusion? Note where the system combines or distributes these layers.
- **Check transaction ordering assumptions:** Is execution on a public blockchain, and what is documented about visibility and ordering? Are private order flow, batch auctions, encrypted mempools, rollups, or another design relevant to the specific system?
- **Separate submission from settlement:** What evidence indicates that a transaction has been included in a block, rather than merely submitted or displayed as pending?
- **Assess provider exposure:** How could pool-price movement affect inventory value relative to holding assets? What pool design, price path, range, fees, timing, and withdrawal state are relevant? Do not assume fees offset the difference.
- **Record scope and version:** Tie conclusions to the documented protocol, pool, and implementation under review. The accepted Uniswap v2 claim is specifically about Uniswap v2 pool mechanics; it is not a universal AMM specification.

These checks help teams understand the mechanics and dependencies of AMM-based trading without treating all decentralized exchanges as identical. The central distinction remains practical: an AMM executes against pool inventory under protocol rules, while an order-book exchange represents bids and offers for matching. In either case, the real system must be evaluated through its documented execution path and settlement dependencies.

### Sources

- Bank for International Settlements, “Trading in the DeFi era: automated market-makers.”
- Bank for International Settlements, “The Anatomy of Decentralised Exchanges,” Working Paper 1227.
- Uniswap Developers, “Pools” (Uniswap v2).
- Bank for International Settlements, “The Technology of Decentralized Finance (DeFi),” Working Paper 1066.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
