---
title: "Cryptocurrency order book: structure, updates, and matching"
description: "Learn what a cryptocurrency order book shows, how bids and asks are organized, how displayed quantities can change, and how the book relates to exchange order-m"
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "cryptocurrency order book"
owned_question: "What information does a cryptocurrency order book contain, and how does it relate to order matching on an exchange?"
risk_level: "medium"
---

A cryptocurrency order book is a venue’s representation of buy and sell orders for a particular market; its matching system is the component that processes incoming orders under venue-defined rules. The two are related, but they are not the same: the book presents order information, while matching determines what happens when orders interact. The evidence available for this article does not document a particular exchange’s order-book schema, update feed, or matching rules, so those implementation details must be checked in that venue’s documentation.

## What a cryptocurrency order book represents

An **order book** is a view of orders available for consideration in a particular market. In ordinary use, it is organized around the prices at which participants are willing to buy or sell. For any specific venue, however, the exact fields, coverage, and display rules depend on the venue and the data source. The evidence available here does not establish a universal order-book format.

The word “available” needs care. A displayed book is a representation of orders reported by its source, not a promise that each displayed order will remain present until someone acts on it. Nor does the display alone prove that it includes every order or every potential buyer and seller. Its scope should be understood through the venue’s own description of the data.

An order book is also distinct from a record of completed trades. A resting order is represented as available for possible interaction; a completed trade records an execution. Those are different kinds of information, even if a venue presents both in the same application. When inspecting a market-data screen, establish which part reports orders and which part reports transactions that have already occurred. Do not infer that an order has executed merely because it appears in the book.

This distinction helps frame the book’s role. It is a representation of order information at the source’s stated level of coverage, not a complete explanation of how the venue operates. The book does not, by itself, describe the venue’s custody arrangements, settlement process, or other services. Those are separate functions, and a book display is not evidence about them.

## Bids, asks, and price levels

A **bid** is a buy-side order, and an **ask** is a sell-side order. An order book commonly presents these sides separately, with orders organized by price. A **price level** is a price at which one or more orders may be represented. The exact display conventions—including which side appears first and how much detail is shown—are properties of the specific venue or interface, rather than universal features established by the evidence available here.

Readers may encounter quantities shown as individual orders or as totals grouped at a price. **Aggregation** means combining records into a summary, such as a combined quantity at a price level. A total at a level is not necessarily one participant’s single order; it may summarize multiple orders. Conversely, a displayed individual order should not be assumed to represent the full quantity available at that price. Whether a feed aggregates orders, and what information it omits when doing so, must be verified in the feed or interface documentation.

The **best bid** is the highest displayed bid in the represented book. The **best ask** is the lowest displayed ask. These labels describe the top displayed prices on their respective sides, not a guarantee that those orders will remain available or that a later order will execute at those prices. They also describe the represented book, not necessarily all venues or all order information beyond its coverage.

That qualification matters when comparing a display with subsequent events. A book is a view of order information, while the matching system processes incoming orders. The displayed price and quantity can therefore be understood only within the source’s documented scope and timing; the display alone does not establish the result of a future interaction.

## How orders enter, change, and leave the book

Orders can be added to a displayed book, changed, canceled, or removed after execution, but the precise lifecycle depends on venue rules. A limit order is an instruction specifying a price condition; whether it rests in the book, how it is represented, and what events cause it to change depend on the venue’s rules. The evidence available here does not establish the treatment of every order type at any particular exchange. Avoid assuming that every submitted order is displayed or that every update appears in the same form.

A data source may provide a **snapshot**, a view intended to represent book state at a point in time, or **incremental updates**, messages that report changes after some starting state. These are useful concepts for describing how a consumer might receive order information, but they do not establish what any specific venue supplies. In particular, the permitted evidence does not confirm a particular snapshot format, message sequence, update frequency, or procedure for reconciling updates. Those are feed-specific details and must not be inferred from the general idea of an order book.

For a reader assessing a screen or dataset, begin by identifying the market and the source. Then determine whether its quantities are displayed order by order or aggregated, what the source says the display includes, and how it describes changes. These checks clarify the meaning of the data being viewed. If the documentation does not specify coverage or update behavior, the display should not be treated as proof of completeness or exact current state.

The same caution applies to missing information. A book that displays only certain order details cannot establish what it does not show. Without source-specific documentation, it is not possible to state whether unshown orders exist, whether quantities are grouped, or how quickly changes are reflected. A careful explanation should distinguish the data that is visible from assumptions about underlying venue state.

## The book and the matching process

An **order-matching system** is the venue component that processes incoming orders according to the venue’s rules. The book and matching system have related roles: the book represents orders available for consideration, while the matching process determines whether incoming orders interact with those orders and what execution follows. The book is not itself the rule set or the process that executes an order.

The boundary is important because a display does not explain all steps between an incoming instruction and a completed trade. The venue’s documented rules determine which orders can interact, how competing orders are handled, and what execution details apply. The allowed evidence for this article does not establish a universal matching algorithm or priority scheme. It therefore cannot support a claim that every venue prioritizes orders in the same way, or that a particular factor—such as price or time—always controls priority.

A venue’s rules should be consulted for its specific behavior. For example, the book’s visible ordering does not by itself prove how the matching system resolves competing orders, and a displayed order does not prove that it will still be present when an incoming order is processed. The general relationship is clear, but implementation details must remain venue-specific.

## What an order book cannot establish on its own

A displayed quantity is not a guarantee that the same quantity will remain available. The evidence available here does not document a particular feed’s latency, completeness, or update schedule, so it would be unjustified to describe any book as universally live, comprehensive, or synchronized with matching. A source’s documentation is needed to support those properties.

A single book view also cannot establish total market liquidity across venues or predict future prices. It represents only the order information its source makes available, within the source’s documented scope. Broader conclusions require evidence beyond that display. This is a limit on what the data can establish, not a recommendation about whether or how to trade.

Finally, order-book visibility does not establish a venue’s security, regulatory status, or execution quality. Those questions concern separate evidence and should not be inferred from the presence of bids, asks, or quantities on a screen.

For builders, operators, and business decision-makers, the practical approach is to treat the book as a structured view of reported orders and to treat matching as a separate, venue-governed process. Confirm how a particular source defines and groups its order data, what its updates represent, and where the venue documents its matching rules. Where those details are not established, preserve the limitation rather than assuming that one exchange’s design is universal.

## Sources and references
