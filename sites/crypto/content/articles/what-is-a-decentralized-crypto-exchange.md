---
title: "What Is a Decentralized Crypto Exchange? How DEX Swaps Work"
description: "Learn how decentralized crypto exchanges use wallets, smart contracts, liquidity pools or orders, slippage controls, and blockchain settlement to execute swaps."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["defi-protocols"]
tags: ["decentralized exchange", "DEX", "how a DEX works", "automated market maker", "DEX settlement"]
author: "editorial_team"
primary_keyword: "decentralized crypto exchange"
owned_question: "How does a decentralized exchange execute swaps without a conventional exchange account?"
risk_level: "high"
---

A decentralized crypto exchange, usually called a DEX, is a protocol that lets users exchange blockchain assets through smart contracts or other onchain programs rather than trading against balances maintained in a conventional exchange account. The user normally signs a transaction from a wallet, and the blockchain records the resulting transfers if execution succeeds.

The word *decentralized* describes part of the system, not an automatic guarantee about every component. A DEX can still depend on a hosted website, a router, administrator keys, governance, token issuers, oracles, validators, bridges, and third-party data. The useful question is which party controls each layer of the trade.

## What makes an exchange decentralized

A centralized exchange usually takes custody of deposited assets, matches trades in an internal system, and records customer balances on its private ledger. Withdrawal is a separate operation that moves assets back to a blockchain.

A DEX generally lets the user retain wallet control until a swap transaction executes. Smart contracts define how assets can be exchanged, and settlement changes token balances on the underlying blockchain. Users do not need the DEX protocol to maintain a conventional account balance for every trade.

That does not mean the interface has no role. BIS research describes DeFi as a stack with settlement, application, and interface layers. The blockchain provides settlement; smart contracts implement exchange logic; a website or wallet makes the protocol accessible. A blocked or misleading interface can affect users even when the contracts remain callable through another route.

## How an AMM-based DEX works

Many DEXs use an automated market maker, or AMM. Instead of waiting for one buyer's order to match one seller's order, a trader swaps against reserves held in a smart-contract liquidity pool. A formula or algorithm relates the pool's reserves to the available exchange rate.

Liquidity providers deposit assets into the pool under its rules. In return, they can receive a share of swap fees. The pool's state changes with each trade: the trader sends one asset, receives another, and pays any protocol-defined fee. The execution price depends on the reserves and the size of the trade relative to available liquidity.

BIS research describes AMMs as multiple smart contracts that hold pool reserves and settle swaps through blockchain transactions. This arrangement removes the need for a centralized exchange operator to custody assets for matching, but it replaces that intermediary with code, token contracts, liquidity providers, and blockchain execution.

AMM formulas differ. Some use two-asset constant-product pools, some concentrate liquidity within price ranges, and others are designed for assets expected to trade near the same value. A quote from one pool should not be generalized to every AMM.

## Order-book and hybrid DEX models

AMMs are not the only form of decentralized exchange. A DEX can use signed limit orders, an onchain order book, a batch auction, a request-for-quote system, or an intent in which solvers compete to produce an acceptable result.

In an offchain-order model, makers sign orders that are distributed through relayers or an indexer. A taker submits a compatible order to a settlement contract. The order can be stored and discovered offchain while final asset transfer occurs onchain. This reduces the cost of writing every open order to the blockchain, but introduces order availability and relay dependencies.

Hybrid systems may route one request across several pools, combine onchain liquidity with professional market makers, or settle transactions on a rollup. The classification should follow custody, execution authority, and settlement rather than the interface's branding.

## The lifecycle of a DEX swap

A typical token swap follows several steps.

1. **The user selects the chain and tokens.** Contract addresses, not symbols or logos, identify the actual assets. Wrapped and bridged versions can be different tokens.
2. **The interface obtains a quote.** A router may examine one or more pools and estimate the expected output, price impact, network fee, and route. The quote is not final because pool state can change.
3. **The user grants transfer authority if needed.** Token standards often require an allowance before a router or settlement contract can move the input asset. The amount and spender address matter.
4. **The user signs a swap transaction.** The transaction identifies the contract call, route, input, minimum acceptable output or other limit, deadline, and recipient.
5. **The network orders and executes the transaction.** The smart contracts check balances, allowances, limits, and current pool state. If a required condition is not met, the transaction can revert.
6. **The blockchain records settlement.** Successful execution transfers the assets and emits records that wallets, indexers, and explorers interpret. Finality follows the underlying chain's rules.

Ethereum's DEX design guidance emphasizes clear display of token identity, allowances, quote details, slippage, price impact, fees, and transaction state. A user should review the wallet's transaction request rather than relying only on a webpage button label.

## Price impact, slippage, and transaction ordering

**Price impact** is the change caused by the proposed trade itself. A large swap relative to pool liquidity moves the pool state farther and produces a less favorable average execution price. **Slippage** is the difference between the quoted result and the result available when the transaction executes. Other trades can change the pool during that interval.

A minimum-output setting or price limit can cause a transaction to revert when execution would be worse than the user's tolerance. A very loose limit makes execution more likely but accepts a wider range of outcomes. This is a transaction-safety control, not a recommendation about market timing.

On public blockchains, a pending swap may be visible before inclusion. BIS analysis explains that transaction ordering and predictable AMM price impact can create opportunities for other actors to place transactions around a swap. This family of ordering behavior is often discussed as MEV. Private order flow, batch auctions, rollups, or protocol-specific protections can change the mechanism but do not remove the need to inspect execution assumptions.

## Liquidity providers and inventory risk

Liquidity providers supply the inventory that AMM traders use. They may receive fees, but they also hold a changing mixture of assets. When relative prices move, arbitrage trades adjust the pool toward external markets. The provider can end with a different asset composition and a lower value than if the original assets had simply remained outside the pool.

This difference is commonly called impermanent loss. The name does not guarantee that it will reverse. Withdrawing the position realizes the current outcome, and fees may or may not compensate for it. Concentrated-liquidity designs add range selection: a position can stop earning swap fees when the market moves outside its active range while remaining exposed to inventory changes.

Providers also face smart-contract, token, oracle, governance, and network risks. A high displayed fee rate is not a return guarantee because volume, competition, asset prices, incentives, and position value all change.

## What decentralization does not remove

A DEX can eliminate the need for one company to hold every trader's account balance while still containing important control points.

- A hosted frontend can filter tokens, alter routing, or become unavailable.
- Router or proxy contracts can be upgradeable or governed by administrator keys.
- Governance token voting can be concentrated.
- Token issuers may pause transfers, block addresses, mint supply, or upgrade contracts.
- Oracle data can be delayed, manipulated, or unavailable.
- A cross-chain trade can depend on bridge validators or custodians.
- The underlying chain can experience congestion, reorganization, censorship, or validator concentration.
- Indexers and RPC providers can present stale or incomplete information.

The label non-custodial is similarly narrow. It can mean the user retains wallet keys until settlement, but a malicious approval or contract call can still transfer assets. Self-custody changes who has signing authority; it does not make every signature safe.

## How to inspect a DEX transaction

Before signing, identify the chain, input and output token contracts, router or settlement contract, recipient, allowance amount, expected output, minimum output, deadline, and network fee. Reject unexplained token approvals or a spender address that does not match trusted protocol documentation.

After execution, use a block explorer to inspect the transaction status, contract calls, token transfers, events, and actual received amount. A successful transaction only proves that the contracts executed under their code. It does not prove that the token is authentic, valuable, redeemable, or legally compliant.

For continued access control, review outstanding token allowances and revoke permissions that are no longer needed. Revocation itself is an onchain transaction and cannot undo an already completed transfer.

A decentralized crypto exchange is therefore an execution and settlement arrangement, not simply a website without registration. Its security and performance depend on wallet authorization, contract design, liquidity, transaction ordering, token behavior, and the underlying blockchain. Evaluating those layers is more useful than assuming that the word decentralized removes intermediaries or risk.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Decentralized exchange (DEX) design best practices](https://ethereum.org/developers/docs/design-and-ux/dex-design-best-practice/) — ethereum.org; retrieved 2026-10-18.
