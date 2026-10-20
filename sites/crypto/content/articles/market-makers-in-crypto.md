---
title: "Market Makers in Crypto: How It Works"
description: "Understand Market Makers in Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto market makers"]
author: "editorial_team"
primary_keyword: "market makers in crypto"
owned_question: "What do crypto market makers do, and how do they support liquidity on exchanges?"
risk_level: "medium"
---

# Market Makers in Crypto: How It Works

Market makers in crypto help connect buyers and sellers by making trading interest available on an exchange. The term describes a market function, not one universal business model or a guarantee that a trade will be available at a particular price or size. To understand what market makers do, it helps to distinguish the liquidity they may provide from the exchange infrastructure, custody arrangements, and risks surrounding a trade.

## What Market Makers in Crypto means

A market maker is a participant that supplies trading interest to a market. On an order-book venue, that interest can appear as orders to buy or sell. When traders can transact against available orders, they may find it easier to trade than if they had to wait for a specific counterparty to arrive. The presence of orders does not, by itself, establish that the market is liquid in every practical sense.

Market liquidity has several dimensions: the time and expense involved in buying or selling, including the spread between available buying and selling prices, transaction costs, price impact, and immediacy. It changes with transaction size and market conditions. A venue can show orders yet still impose substantial costs or delays for a particular trade, especially if the available interest is insufficient for its size. These dimensions are a useful way to evaluate the function market makers may serve; they do not guarantee any particular outcome. [claim_market_liquidity_dimensions]

The system boundary matters. A centralized exchange may combine third-party trading, proprietary trading, margin lending, token issuance, and custody. Not every exchange performs every function, and combining roles can create operational dependencies and conflicts. A market maker may be independent of an exchange or operate within a broader organization that performs other functions; the accepted evidence does not establish one standard arrangement for all venues. [claim_bis_cex_combined_functions]

Market making should also be distinguished from decentralized-exchange liquidity provision. In an automated market maker (AMM) model, a liquidity provider contributes assets to a pool and can receive a share of trading fees while bearing inventory and adverse-selection risk. Pool formulas, fee tiers, price ranges, and loss allocation vary by protocol and position. That pool-based mechanism is not the same thing as placing orders on an internal order book. [claim_bis_amm_liquidity]

## Core components of Market Makers in Crypto

An order-book market-making arrangement involves several connected elements, though their implementation varies by venue:

- **The exchange and its market:** The venue defines how trading interest is represented and how orders and trades are handled. A market maker’s activity is meaningful only in relation to the venue’s instruments, rules, and available counterparties.
- **Orders and available liquidity:** Buy and sell interest can contribute to the opportunities other participants see. The amount available, its price, and how quickly it changes affect whether a trader can transact and what costs or price impact may result. Liquidity is not a single number that captures every transaction size or market condition. [claim_market_liquidity_dimensions]
- **The market-making participant:** This is the party supplying trading interest. Its role does not alone reveal whether it is acting for clients, trading for its own account, or operating in an organization that performs other exchange-related functions. Those relationships require separate evidence. [claim_bis_cex_combined_functions]
- **Assets and funding:** Trading requires access to the relevant assets or other venue-supported balances. How those assets are held, controlled, and made available depends on the platform and its arrangements; the general label “market maker” does not settle custody or ownership questions.
- **Operational systems:** A participant needs a way to interact with the venue and monitor its activity. Exact software, interfaces, automation, risk controls, and operating procedures are implementation-dependent; the accepted evidence does not support treating one technical architecture as universal.

For a centralized exchange, there is an additional custody boundary. Users typically transfer funds and their custody to the exchange before trading on its internal order book. However, custody and legal ownership arrangements vary by platform and jurisdiction. The order-book function therefore should not be confused with a complete description of who controls assets or what legal arrangement applies. [claim_bis_cex_custody]

## How Market Makers in Crypto works

A simplified order-book workflow can be understood as a sequence of questions rather than a claim that every venue follows an identical process:

1. **A venue makes a market available.** The exchange provides the trading environment and an internal order book. In the centralized model described by the BIS, users typically transfer funds and custody to the exchange before they trade there; the details of custody and ownership vary. [claim_bis_cex_custody]
2. **A participant supplies trading interest.** A market maker makes buy or sell interest available on the venue. The accepted sources support the general role of liquidity provision but do not specify a universal quoting algorithm, order size, update frequency, or obligation to remain present.
3. **Other traders assess the available market.** A trader’s practical ability to buy or sell depends on more than whether an order exists. Spread, transaction cost, price impact, and immediacy all matter, and their effects depend on trade size and market conditions. [claim_market_liquidity_dimensions]
4. **Trading interest may be matched.** If a trader’s order can interact with available interest under the venue’s rules, a trade may occur. The available evidence does not establish the matching rules or execution guarantees of any specific exchange, so those must be checked in that venue’s documentation.
5. **Exposure and inventory remain relevant.** Supplying liquidity means taking or managing exposure to assets and market movements. In the distinct AMM-pool model, liquidity providers bear inventory and adverse-selection risk; the specific consequences depend on the protocol and position. That evidence should not be generalized into a claim about identical risk mechanics for every order-book market maker. [claim_bis_amm_liquidity]

The practical contribution is thus conditional: market-making activity can add trading interest that other participants may trade against, but the resulting experience depends on the amount and price of interest available, transaction costs, market conditions, and venue operation. It does not establish that every order can be filled promptly, at a preferred price, or without price impact. [claim_market_liquidity_dimensions]

## Trust and control boundaries

Market-making activity does not eliminate the need to assess the venue and its operating structure. A centralized exchange may combine trading for users, proprietary activity, lending, token issuance, and custody, but not every exchange performs all of these functions. Combining roles can create operational dependencies and conflicts. The existence of a market maker or visible trading interest does not show how those roles are separated or controlled. [claim_bis_cex_combined_functions]

Custody is a separate question from liquidity. Users typically transfer funds and their custody to a centralized exchange before trading on its internal order book, while custody and legal ownership arrangements vary by platform and jurisdiction. A reader should not infer asset control, segregation, or legal rights from the mere fact that an exchange supports order-book trading. [claim_bis_cex_custody]

For decentralized exchange pools, the relevant boundary differs: the cited research describes liquidity providers contributing assets to pools and potentially receiving trading-fee shares while bearing inventory and adverse-selection risk. Pool design and loss allocation vary. These facts describe the AMM model covered by the source, not a blanket guarantee about custody, execution, or risk across all decentralized protocols. [claim_bis_amm_liquidity]

## Limitations and failure modes

Market-making activity cannot guarantee continuous liquidity. Available liquidity changes with transaction size and market conditions, and liquidity itself includes spread, transaction cost, price impact, and immediacy. A market that appears usable for a small order may impose different costs or delays for a larger one. [claim_market_liquidity_dimensions]

Nor does the label establish an operator’s independence, incentives, or relationship with an exchange. Because centralized exchanges may combine functions, organizational dependencies and conflicts are possible; the evidence does not establish whether a particular venue has them or how it addresses them. [claim_bis_cex_combined_functions]

In an AMM pool, contributing assets can expose a provider to inventory and adverse-selection risk, and fee sharing does not remove those risks. The outcome depends on protocol-specific formulas, fee tiers, price ranges, and loss allocation. Those variables make it unsafe to assume that pool liquidity behaves like order-book quotes or carries the same risk profile. [claim_bis_amm_liquidity]

Finally, broad descriptions cannot substitute for platform-specific evidence. The accepted sources do not establish particular exchange interfaces, fees, order-handling guarantees, security outcomes, recovery processes, or legal arrangements. Those details should be verified directly rather than inferred from general descriptions of market making.

## What teams should verify

Builders, operators, and institutions evaluating a market-making arrangement can use the following evidence-led checks:

1. **Identify the market model.** Confirm whether the venue uses an internal order book, an AMM pool, or another documented mechanism. Do not treat order-book market making and pool liquidity provision as interchangeable.
2. **Examine liquidity across relevant trade sizes.** Assess spread, transaction cost, price impact, and immediacy for the sizes and conditions that matter to the use case. A single liquidity observation cannot establish performance across changing conditions. [claim_market_liquidity_dimensions]
3. **Establish who performs each function.** Determine whether exchange activity includes third-party trading, proprietary trading, lending, token issuance, or custody, and whether the relevant functions are performed by the same operator. The fact that a centralized exchange may combine these functions does not mean every exchange does so. [claim_bis_cex_combined_functions]
4. **Verify custody and ownership arrangements.** For a centralized venue, review its current documentation to understand when funds and custody are transferred and what the platform says about ownership. These arrangements vary by platform and jurisdiction, so general exchange descriptions are not sufficient. [claim_bis_cex_custody]
5. **Check venue-specific execution and operating documentation.** Confirm the applicable order, matching, interface, and operational terms from the venue itself. The general evidence here does not establish those implementation details or guarantee executions.
6. **For AMM pools, review protocol-specific risk parameters.** Verify the pool formula, fee tier, price-range rules, and loss allocation for the position under consideration. Liquidity providers may receive trading fees while bearing inventory and adverse-selection risk; fee sharing is not a guarantee against loss. [claim_bis_amm_liquidity]
7. **Keep claims within the evidence.** Treat statements about persistent liquidity, role separation, custody, or execution outcomes as questions for verification unless supported by current, specific documentation. A market maker can contribute to liquidity, but the market’s actual accessibility and cost remain conditional on venue, size, and conditions.

The central distinction is that a market maker supplies trading interest, while liquidity describes the broader cost and ease of executing a trade. Evaluating the two together requires examining the market model, trade size, venue roles, and custody arrangements rather than relying on the label alone.

## Sources and references

- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
