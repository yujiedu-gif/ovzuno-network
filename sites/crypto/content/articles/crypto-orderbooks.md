---
title: "Crypto orderbooks: structure, updates, and matching"
description: "Explore crypto orderbooks as exchange infrastructure: how bids and asks represent market state, how updates and matching relate, and what the book omits."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "crypto orderbooks"
owned_question: "What are crypto orderbooks, and how do their data, order-handling, and matching components fit together in exchange market infrastructure?"
risk_level: "medium"
---

Crypto orderbooks are venue-maintained records of buy and sell interest that can inform a matching process. A book’s displayed state is not the matching function itself, a complete picture of market liquidity, or a guarantee that an order will execute at a displayed price. The specific data model, order handling, and matching rules are venue-dependent; the evidence available for this article does not establish universal order fields, priority rules, feed formats, or update semantics.

## What an order book represents

In the usual conceptual model, buy interest is called bids and sell interest is called asks. Orders may be organized by price, and a displayed price level can summarize the quantity associated with that price. The exact fields, quantity units, and inclusion rules depend on the venue’s design. These labels describe the broad idea, not a standardized schema shared by all crypto markets.

A book can be discussed at two levels of detail. An order-level representation distinguishes individual orders. A price-level representation groups orders by price and summarizes their quantity. These are useful ways to describe possible views of market state, but the evidence here does not establish whether a particular venue offers one or both, or how it defines an individual order in its published data. The venue’s documentation is needed to interpret its fields accurately.

The book’s scope is also limited. It represents interest recorded in the relevant venue’s book view; it does not show every possible buyer or seller, including interest that is not represented there or orders that may arrive later. A quantity shown at a price is thus a statement about the data view, not a complete inventory of market participants or a promise about what will be available when a separate action occurs.

This distinction keeps the term “market state” precise. It means the set of order information a venue maintains or displays at a particular point in its system, under its own rules. It does not imply that every interested party is represented, that all recorded state is visible to every observer, or that a displayed view necessarily matches the reader’s timing or perspective.

## How crypto orderbooks change over time

A useful conceptual lifecycle begins when an instruction is submitted to a venue. The venue evaluates it under its own acceptance and handling rules. If the instruction remains available rather than being removed through matching or another venue-defined outcome, it may appear as resting interest in the book. “Resting” here means only that the order remains represented as available interest under that venue’s model; it does not specify a universal duration, order type, or status label.

After an order is represented, its displayed state can change. Orders may be added, amended, canceled, or reduced through execution, depending on the venue’s supported actions and rules. This is why the book is better understood as changing state than as a static catalog. However, those lifecycle labels do not determine what a venue permits, how it records a change, or how the change affects any priority position. Those details require venue-specific documentation.

The distinction between a submitted instruction and a resting order is important. An instruction may be evaluated without becoming persistent displayed interest, and the specific outcomes depend on venue rules. The available evidence does not support a universal list of validation checks, accepted order types, rejection reasons, or state transitions. A general explanation can identify the conceptual stages, but it should not be mistaken for a specification of any particular exchange.

Changes to book state are also distinct from how they are communicated to observers. A system may maintain internal state and publish a representation of it, but this evidence does not establish the precise relationship between those components for any venue. To interpret updates, a reader needs the venue’s definitions of event types, field meanings, and the state to which each update refers.

## From book state to matching

Matching is the function that evaluates eligible incoming orders against interest already available under the venue’s rules. The book represents resting interest; matching logic determines whether eligible orders can be paired and what the venue records as an outcome. The concepts are connected, but the display is not itself evidence that a match has occurred.

Some systems are commonly described using price-and-time priority: price is considered, and time at that price may be used to order interest. That is a conceptual example, not a universal rule for crypto venues. The evidence available here does not substantiate a particular venue’s matching algorithm, tie-breaking method, supported order types, or execution outcomes. Each would require current documentation for the venue being described.

It is equally important not to assume that a displayed price level directly reveals how matching will proceed. A price-level aggregate can summarize interest without identifying every order represented at that level. The matching system may evaluate orders under rules that the aggregate view does not expose. Therefore, the visible organization of data and the internal decision process should be treated as related but distinct components.

Matching outcomes and published market data are also separate concerns. A venue’s matching rules govern its internal evaluation, while its market-data representation communicates some view of the resulting book state. The available evidence does not establish whether a specific publication is immediate, complete, or synchronized with matching. Those properties cannot be inferred from the existence of a displayed book alone.

## Market-data views and their limits

An order-level feed, where offered, can preserve distinctions among individual orders; an aggregated price-level view can combine them into totals by price. These terms describe broad data representations, not a promise that a venue exposes either view or that two venues encode them consistently. Exact feed granularity and field meanings must be verified against the relevant venue’s documentation.

Snapshots and incremental updates are another venue-specific area. A snapshot is a representation of state at a point in time; incremental updates communicate changes relative to some established state. To use such data coherently, a consumer needs the feed’s own rules for sequencing and synchronization. No universal sequence numbering, recovery procedure, or update interpretation is established here, so none should be assumed from the general term “order book.”

A displayed book may be incomplete relative to broader market interest, stale relative to later changes, or specific to one venue. These are limitations on what a reader can infer from a view, not claims that a particular venue’s data is inaccurate. Without documented coverage and update semantics, a reader cannot conclude that a view is complete, current, or synchronized with the matching system. Displayed depth should not be treated as guaranteed executable quantity.

The practical verification task is to identify what the view includes, when its state applies, and how updates relate to that state. For a named venue, documentation should define the relevant fields and data-delivery behavior. In the absence of such evidence, the safe technical conclusion is narrower: a book is a representation of venue-defined order state, and its data may not expose every detail needed to reconstruct internal behavior.

## Where the order book sits in exchange infrastructure

At a conceptual level, order-entry components convey instructions, venue rules determine how those instructions are handled, matching logic evaluates eligible orders, and market-data publication presents a view to downstream consumers. This is a functional map, not a claim about universal architecture. The actual boundaries among components and the relationship between internal state and published data vary by arrangement and must be verified for a specific venue.

The order book is not a liquidity pool. Nor is it, by itself, a complete measure of liquidity or a guarantee of execution. It is a representation of specified buy and sell interest under a venue’s data model. Keeping these concepts separate prevents a common category error: treating a record of resting interest as though it were the entire market, the matching engine, or a commitment that a displayed amount will be available under later conditions.

For builders, operators, institutions, and business decision-makers, the useful mental model has three parts: the venue maintains some defined order state; matching rules evaluate eligible instructions against available interest; and a published view exposes only what that venue’s data model and feed rules provide. Before relying on details about fields, lifecycle, priority, or synchronization, consult the specific venue’s documentation. Without that evidence, the general model explains how the components fit together but cannot establish a particular venue’s operating rules.

## Sources and references

- [Seaport](https://docs.opensea.io/docs/seaport) — OpenSea Developer Documentation; retrieved 2026-10-18.
