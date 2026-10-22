---
title: "How Automated Market Makers for Decentralized Finance DeFi Work"
description: "Explore automated market makers for decentralized finance defi through their core components, swap flow, pricing logic, and protocol-level risks."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: ["automated market makers decentralized finance defi"]
author: "editorial_team"
primary_keyword: "automated market makers for decentralized finance defi"
owned_question: "What roles do automated market makers play in decentralized finance protocols, and how do their core components connect to support token swaps?"
risk_level: "medium"
---

Automated market makers (AMMs) support token swaps in decentralized finance by connecting pool assets with rules that determine how a trade changes those assets. In a swap, the pool supplies token inventory, the AMM’s specified mechanism governs the calculation, and the contract applies that mechanism when the submitted transaction executes. The exact behavior depends on the particular pool design; one AMM’s mechanics should not be treated as universal.

## Where AMMs fit in a DeFi protocol

A pool-based AMM interaction involves distinct roles. The pool holds the assets made available for swapping. Protocol logic defines how a trade interacts with that pool. A user or application submits a transaction requesting the swap. These roles connect, but they are not interchangeable: an interface can present a request, while the pool’s rules and contract execution determine what happens on-chain.

A liquidity pool is an inventory of assets used to execute swaps. In Uniswap v2, one example of a constant-product AMM, a pool holds reserves of a token pair, and liquidity-provider shares represent contributions to those reserves. This describes that specific pool model, not every AMM. Other AMMs can use different curves, assets, fees, and accounting. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A useful way to understand the protocol boundary is to ask where each decision is made. The pool’s assets establish what inventory is available. The AMM’s rules define how a swap is calculated against that inventory. The transaction caller supplies a request to be processed under those rules. A user-facing application may expose or explain the request, but the application’s presentation is not itself the pool mechanism.

## How liquidity pools and pricing logic connect

Liquidity is the pool inventory that swaps draw on. Pricing logic is the pool’s specified method for determining how a trade interacts with that inventory. These components are linked: the calculation depends on both the chosen mechanism and the pool’s current state. A swap cannot be understood solely as a token pair or a displayed price, because the pool’s available assets and the protocol’s rules also matter.

The Uniswap v2 constant-product pool is a concrete example of this relationship: its token-pair reserves provide the swap inventory, and its design determines how swaps use those reserves. It is an example rather than a general formula for all AMMs. Pool models can differ in curve, assets, fees, and accounting, so documentation for a specific protocol is needed to describe its actual calculation. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

This distinction matters when interpreting a quote. A quote represents an expected result based on the information and conditions used to prepare it; it is not the same thing as a completed swap. The pool’s state and the request’s applicable rules remain part of execution. Without evidence for a specific implementation and transaction, a general explanation cannot establish the exact output or final execution result.

## Automated market makers for decentralized finance defi: a swap, step by step

A pool-based swap can be followed through four connected stages:

1. **The caller prepares a request.** A user or application identifies the intended token exchange and submits a transaction that invokes the relevant pool interaction. The interface may help construct or present the request, but that role is separate from the pool’s pricing mechanism.
2. **The transaction invokes protocol logic.** The AMM’s contract applies the rules associated with the specific pool. In an AMM-based decentralized exchange, smart contracts and liquidity pools implement trading, and transactions settle when included in a blockchain block. This describes the AMM model; other exchange designs can use different execution paths.
3. **The mechanism evaluates the request against pool state.** The calculation uses the pool’s particular design and available reserves. The reserves are the inventory from which swaps execute; they are not a universal promise about the quantity a particular request will return. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)
4. **The exchange takes effect if execution succeeds.** Contract execution applies the specified pool accounting and changes the relevant state as part of the swap. A request or quote alone does not establish that this stage has occurred; the transaction must reach the applicable settlement point for the swap to be settled.

The flow separates the AMM’s calculation from the wider transaction process. A protocol defines the pool behavior, while the caller and application participate in submitting the request. For public-blockchain AMMs, transaction visibility, execution ordering, pool depth, and price impact can affect a swap before block inclusion. These conditions concern execution around the pool mechanism and should not be collapsed into the pool’s quoted calculation.

## What changes when liquidity or pool design changes

Pool composition and reserves shape the inventory available for a swap. A pool with a different state presents a different context for the AMM’s calculation, while a different design may use another curve, asset configuration, fee arrangement, or accounting method. The Uniswap v2 pair-reserve model illustrates one configuration; it cannot establish the behavior of a pool that uses another design. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

Price impact is an execution consideration: the trade interacts with pool inventory, and the resulting effect depends on the pool and request. Public transaction visibility and ordering can also affect a swap before block inclusion. Pool depth and transaction ordering are among the relevant conditions, but the general mechanism does not determine the outcome of any specific transaction. That requires the relevant pool and transaction details.

Liquidity provision is a separate role from swapping. Liquidity providers contribute assets to pools and can receive a share of trading fees, while bearing inventory and adverse-selection risk. This means pool liquidity has both an operational function—providing swap inventory—and exposures for the participants supplying it. Fee participation does not remove those risks.

A provider can also experience inventory-value loss relative to holding assets when pool prices move. Trading fees may or may not offset that loss, and the outcome depends on the pool design, price path, range, fees, timing, and withdrawal state. This is a conditional risk description, not a claim that every provider or pool experiences the same result. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Protocol risks and evidence to check

Understanding a pool’s mechanics is not the same as establishing the safety or outcome of a particular interaction. A technical review should identify the specific pool model and its current state, distinguish the interface from the contract behavior, and determine whether the swap has actually executed. General descriptions cannot establish protocol-specific fee terms, security properties, availability, recovery options, or compliance conditions; those require separate, applicable evidence.

For a swap, keep three questions distinct: what assets the pool holds, what rules the AMM applies, and what happened to the submitted transaction. In public-blockchain AMM execution, visibility and ordering can affect the transaction before inclusion, alongside pool depth and price impact. These conditions help explain why a displayed expectation should not be treated as proof of settlement.

For a liquidity provider, examine the pool’s particular design and account for the possibility that price movements change the value of the pool’s inventory relative to holding the assets. Fees may or may not offset that difference, and outcomes vary with the pool and position conditions. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

The core connection is straightforward: pool assets supply swap inventory, the AMM’s rules calculate how a request interacts with that inventory, and contract execution applies those rules to the transaction. The details vary by design, so protocol-specific behavior should be described from evidence about the relevant pool rather than generalized from one AMM example.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
