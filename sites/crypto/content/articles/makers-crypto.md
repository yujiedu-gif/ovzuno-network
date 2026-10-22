---
title: "Makers Crypto: Maker Orders and Exchange Order Books"
description: "Learn what makers crypto refers to in exchange trading, how maker orders interact with order books, and how maker and taker roles differ."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "makers crypto"
owned_question: "What does “maker” mean in crypto exchange trading, and how do maker orders interact with the order book and taker orders?"
risk_level: "medium"
---

In crypto exchange trading, a **maker order** is an order that adds executable liquidity to an order book by resting there for other orders to match against. A **taker order** matches against available orders and removes liquidity. These labels describe an order’s interaction with the book at execution; they do not necessarily describe a trader’s permanent role. The evidence available for this article does not establish specific exchange order-book rules, so venue-specific mechanics must be verified in that venue’s current documentation.

## What “maker” means in crypto exchange trading

An **order book** is a record of buy and sell orders available for possible execution on a trading venue. A **resting order** is one that remains available in the book rather than matching immediately. In the usual maker/taker vocabulary, an order that rests and is later available for others to match is providing liquidity. An order that matches an existing order is taking liquidity.

The distinction is about an order’s behavior, not a permanent label for the person or organization that submitted it. The same participant can place an order that rests in one situation and submit another that matches existing liquidity in a different situation. A participant’s role can therefore vary from one order or execution to another.

“Makers crypto” can also be confused with “crypto market makers.” Here, maker refers narrowly to an order’s interaction with an exchange order book. It does not, by itself, identify a professional business, automated trading system, or provider of market-making services. Those are broader subjects than the order-level distinction addressed here.

## Makers crypto: how an order enters the book

A **limit order** specifies a price condition for buying or selling. For example, a buy limit sets the maximum price the buyer is willing to pay, while a sell limit sets the minimum price the seller is willing to accept. If the order cannot match an available opposing order under the venue’s rules, it may be eligible to rest in the book. If it does match an available opposing order, it can execute immediately instead.

The key qualification is “may.” Sending an order to an exchange does not guarantee that it will rest. Its price in relation to available opposing orders matters, but so can the order type, the instructions governing how long it remains active, other order conditions, and the venue’s handling rules. A submitted order might rest, execute in whole or in part, or be canceled, depending on those conditions and rules.

A **time-in-force instruction** tells the venue how long an order may remain active or what to do if it cannot execute according to its conditions. The available evidence does not describe the specific choices any exchange offers or how each choice is implemented. Those details should be checked in the exchange’s own documentation rather than assumed to work identically across venues.

A **post-only instruction**, where a venue offers one, is another venue-specific feature to check. Its name alone does not establish how the exchange handles an order that would otherwise match immediately. Consult the venue’s explanation of the instruction and its effects before treating a submitted order as one that will necessarily rest.

## How maker and taker roles differ at execution

Consider this hypothetical order book: the best available sell order is priced at $101, and the best available buy order is priced at $99. A new buy limit order at $98 is below the available sell price in this example. If the exchange accepts it and leaves it active, the order can rest as a buy order. If a later sell order matches against it, the resting buy has supplied liquidity and the arriving sell has taken it.

Now consider a buyer submitting an order that can match the available sell order at $101 under the venue’s rules. If it executes immediately against that resting sell order, the buyer’s order takes available liquidity, and the resting sell order supplied it. The example illustrates the relationship between resting and immediately matched orders; it is not a universal matching rule or a promise about execution price, fill size, or classification on every exchange.

The labels apply to the execution interaction, not simply to the order’s original intent. An order submitted with the hope of resting might be eligible to match immediately under the conditions at the time it reaches the venue. Conversely, an order that is not immediately matched may remain in the book if the venue accepts it and its instructions allow that. How the venue classifies an execution—including partial executions—must be verified in its rules.

Maker status does not guarantee that an order will execute. A resting order might remain unmatched or be canceled. Nor does the maker label alone establish that an order will receive a better price, a fee discount, a rebate, or any particular trading outcome. Any fee or rebate is a separate venue-specific term, not something that follows automatically from the basic definition of maker and taker.

## Why the distinction matters to exchange infrastructure

An exchange order book records outstanding buy and sell orders. Its matching process determines which compatible orders execute under the venue’s rules. Maker and taker terminology offers a compact way to describe whether an order adds liquidity by resting or removes available liquidity by matching. When orders execute, the venue’s order and trade records change according to its system design.

This terminology does not specify every part of the infrastructure. It does not tell a reader which order types a venue supports, how it prioritizes compatible orders, whether an instruction prevents an immediate match, or how a partially executed order is treated. Those are implementation and operating details. The venue’s documentation is needed to connect the general terms to its particular matching process.

The distinction is also narrower than the entire exchange environment. Some crypto service providers may combine trading, custody, lending, market-making, and other services, but that does not mean every provider combines them. Maker/taker classification explains an order’s interaction with trading liquidity; it does not establish which other functions a specific operator performs or how those functions are organized.

This article concerns centralized exchange order-book mechanics. It does not explain automated market-maker liquidity pools or decentralized exchange designs. Those systems use concepts and mechanisms that should not be inferred from the order-book meanings of “maker” and “taker.”

## What to verify in a venue’s rules

For a specific exchange, consult current official materials to determine:

- Which order types are supported and how they behave when they could match an existing order immediately.
- How time-in-force instructions affect whether an order can rest, execute, or be canceled.
- Whether a post-only instruction is available and what the venue says happens if an order would otherwise match at once.
- How the venue classifies immediate, resting, and partial executions.
- Which current fees, rebates, or other terms apply, if those details matter to your interpretation.

Treat each item as a venue-specific question. The general maker/taker distinction does not supply the missing operational rules, and documentation may change. Likewise, maker or taker status alone says nothing about security, compliance, account recovery, legal treatment, or regulatory protection. The useful starting point is narrower: determine whether the order rests and adds liquidity or matches available orders and takes liquidity, then confirm how the venue defines and records that behavior.

## Sources and references
