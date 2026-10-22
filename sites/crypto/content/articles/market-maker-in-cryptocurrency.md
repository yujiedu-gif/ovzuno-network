---
title: "Market maker in cryptocurrency: role, mechanics, and risks"
description: "Learn what a market maker in cryptocurrency does, how quotes support exchange liquidity, how the role differs from other mechanisms, and what risks to consider."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto market maker", "market making", "bid-ask spread", "order book liquidity"]
author: "editorial_team"
primary_keyword: "market maker in cryptocurrency"
owned_question: "What does a market maker in cryptocurrency do, how does it provide exchange liquidity, and what risks and limitations shape that role?"
risk_level: "medium"
---

A market maker in cryptocurrency is a participant that supplies buy and sell orders to a trading venue, potentially adding quotes that other participants can trade against. The venue’s matching system and the market maker’s quoting activity are distinct functions. Quotes can change or disappear, so market making does not guarantee execution, continuous liquidity, or a particular trading cost.

## What a market maker does in crypto exchange infrastructure

A **quote** is an offer to buy or sell an asset at a stated price and quantity. A market maker places or maintains such offers on a venue, subject to the venue’s rules and any applicable agreement. Other participants may trade against an available quote, but posting it does not itself complete a trade.

The market maker supplies orders; the exchange’s trading system applies its rules to orders and matches eligible ones. In a centralized exchange model, a venue commonly records outstanding buy and sell orders in an off-chain limit order book. The matching process is therefore a venue function, distinct from the participant’s decision to submit quotes.

A quote is not a promise that another participant will accept it or that it will remain available. The role alone also does not establish that both sides will always be quoted, that an order will execute, or that liquidity will stay at a particular level. Those outcomes depend on the venue, market, current conditions, and terms of any arrangement.

## How quotes affect the order book and bid-ask spread

An **order book** is a venue’s record of outstanding buy and sell orders. A **bid** is a buy price, and an **ask** is a sell price. The **bid-ask spread** is the difference between the best displayed bid and best displayed ask. **Quote size** means the quantity offered at a price. **Displayed depth** refers to the quantities visible at different prices in the book.

For example, if a market maker submits a buy order and a sell order, those orders may appear among the book’s bids and asks. They may add visible quantity at their respective prices and affect the best displayed prices or spread. This is a conceptual illustration, not a universal outcome: a quote does not necessarily narrow the spread, remain in place, or attract a trade.

An order shown in a book is not the same as an executed trade. The displayed order may be matched, changed, or canceled under venue rules. A snapshot of depth describes orders visible at that moment; it does not establish that the same quantity will be available later or that a trade can be completed at the displayed price.

Liquidity also has several dimensions. It can reflect the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. Observed conditions can vary by asset, venue, market conditions, and time. A market-making arrangement alone does not establish the execution cost or depth a participant will encounter.

## Market makers, liquidity providers, and other mechanisms

“Market maker” describes a role or activity: supplying buy and sell orders to a venue. “Liquidity provider” is broader and context-dependent. In an order-book venue, it can describe a participant contributing orders. In decentralized finance, it can refer to someone who contributes assets to a pool used for swaps.

These mechanisms differ. In the Uniswap v2 constant-product example, a pool uses deposited reserves of a token pair as swap inventory, with liquidity-provider shares representing contributions. That is not the same as submitting priced orders to an order book. Other automated market makers can use different curves, assets, fees, and accounting, so the example should not be treated as a universal design.

Liquidity providers in automated market makers contribute assets to pools and can receive a share of trading fees while bearing inventory and adverse-selection risk. They can also experience inventory-value loss relative to holding assets when pool prices move; trading fees may or may not offset it. These pool-specific features help explain why “market maker” and “liquidity provider” are not interchangeable in every context.

The exchange’s matching function is different from both roles: it processes orders under venue rules. Custody and settlement are separate functions too. A participant’s market-making activity, by itself, does not show who holds assets or how settlement is arranged. Those details require evidence about the particular venue and arrangement.

## How market-making arrangements are structured

An arrangement may involve a trading venue and a market-making firm; a customer or issuer may also be involved in some contexts. The parties’ roles and obligations depend on the actual agreement. Relevant terms may address covered markets, quoting expectations, reporting, and operational responsibilities, but those are not established as standard conditions across venues by the general definition of market making.

Commercial terms require the same care. Fees, rebates, incentives, quoting obligations, eligible assets, and service availability are specific to the arrangement. Check current venue documentation and the governing agreement rather than inferring terms from the label “market maker.” No particular payment or incentive should be assumed, and an arrangement does not imply guaranteed income or trading performance.

Separate observable activity from contractual promises. Visible orders can show that quotes were present at a particular time. They do not, on their own, establish future availability, contractual obligations, custody arrangements, or operational controls. Each question requires relevant evidence about the venue and agreement.

## Risks, limitations, and what to verify

Market makers can face inventory exposure when they hold assets after trades, and adverse selection when quotes are traded against before they can respond to changing conditions. Volatility can change asset values and the usefulness of existing quotes. Execution or technology failures, venue outages, and changing market conditions can also affect order availability or behavior. The extent of these risks depends on the participant, venue, assets, and arrangement; the role alone does not establish particular security controls, recovery capabilities, or resilience.

When assessing a description of a market-making service, verify the following against current, primary evidence:

- Which venue, assets, and markets are covered, and what quoting expectations actually apply.
- How the venue handles matching, order changes, cancellations, and trade status.
- Which party is responsible for assets, settlement, and operational response, where relevant.
- Whether stated fees, rebates, incentives, availability, security controls, or recovery capabilities are documented for that specific service.
- What supports any claims about performance or yields, rather than relying on the market-maker label.

Quotes may be unavailable, insufficient, or withdrawn. Market making does not eliminate spreads, price impact, or price risk. Regulatory, tax, and compliance conclusions would require current, authoritative, jurisdiction-specific evidence; the general mechanics described here establish none. The central distinction is functional: a market maker can contribute orders, while the venue matches eligible orders, and neither fact guarantees a particular market outcome.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
