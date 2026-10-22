---
title: "AMM Crypto Meaning: A Clear Definition"
description: "Learn the AMM crypto meaning: what the abbreviation stands for, the basic role of an automated market maker, and how the term is used in DeFi."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["defi_protocols"]
tags: ["amm crypto"]
author: "editorial_team"
primary_keyword: "amm crypto meaning"
owned_question: "What does “AMM” mean in crypto, and what is the basic role of an automated market maker in decentralized trading?"
risk_level: "medium"
---

In crypto, **AMM** means **automated market maker**. It describes a trading mechanism that uses programmed rules and available liquidity to facilitate swaps, rather than relying only on matching individual buy and sell orders. AMM is a design term—not the name of a token or one particular service—and it does not mean every system using the label works the same way.

## What does AMM mean in crypto?

An automated market maker is a mechanism for arranging trades through rules that operate on available trading liquidity. In a pool-based design, a **liquidity pool** is a supply of assets held for use in swaps. One example is a pool pairing two tokens, with deposited reserves serving as the inventory from which trades execute. That example helps explain the terminology, but it is not a universal blueprint for every AMM. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The word “automated” points to the use of programmed rules to carry out the trading mechanism. “Market maker” refers here to the mechanism’s role in making trading liquidity available. Together, the words identify a way of organizing swaps; they do not identify a particular asset, company, website, or guaranteed outcome.

The distinction matters because crypto terminology often places several related terms side by side. “AMM” names a mechanism or design approach. “Liquidity pool” names one possible structure used to make assets available for trading. An application may implement a pool-based AMM, but the definition alone does not specify the application, its rules, or who operates its supporting services.

## The basic role of an automated market maker

At a high level, an AMM can facilitate trades using liquidity made available to a protocol. In the Uniswap v2 pool model, for example, deposited reserves of a token pair provide swap inventory, and liquidity-provider shares represent contributions to that pool. Other AMMs can use different curves, assets, fees, and accounting, so details from one pool model should not be generalized to all automated market makers. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

This differs conceptually from a limit order book, which commonly records outstanding buy and sell orders. The distinction is about the mechanism used to organize trading, not a claim that one approach is better. An AMM is associated with liquidity-based trading mechanisms; an order book records orders from buyers and sellers. The term “AMM” does not tell a reader whether a specific exchange also uses another execution model or combines multiple designs. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

The word “liquidity” is useful in this definition, but it should not be read as a promise that a trade will occur at a particular price or under particular conditions. The evidence supports describing pool reserves as trading inventory in the specified pool model; it does not establish that every AMM has the same inventory, pricing rules, or operating characteristics. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How AMM is used in DeFi terminology

AMMs are commonly discussed in connection with decentralized trading and decentralized finance, often shortened to **DeFi**. The distinction is that DeFi is a broader category of applications, while an AMM is a particular kind of trading mechanism. A technology model for DeFi applications separates settlement, application, and interface layers, while noting that systems may distribute or combine them differently. That helps explain why the AMM mechanism, the application a person interacts with, and the underlying settlement environment should not be treated as interchangeable terms.

A liquidity pool is related to an AMM but is not a synonym for it. In the Uniswap v2 example, the pool supplies reserves used for swaps. The AMM describes the trading mechanism that uses liquidity; “pool” describes a way that liquidity can be held and organized. Since other AMMs can use different assets and accounting, a pool-based example provides context rather than a rule for every design. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The label can therefore refer to a broad family of approaches rather than one uniform implementation. A reader encountering “AMM” can infer the general idea—programmed trading rules operating with available liquidity—but should not infer a specific formula, pair of assets, pool structure, or application from the abbreviation alone.

## What the definition does not tell you

The definition does not specify a particular protocol’s trading formula, assets, fees, accounting, governance, or implementation. Even the pool model described above is explicitly one example: other AMMs can vary in curves, assets, fees, and accounting. The term also does not establish the safety, availability, suitability, or financial outcome of any service or activity. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

It also does not explain every feature of a particular trade. Public transaction visibility, execution ordering, pool depth, and price impact can affect an AMM swap before block inclusion in the public-blockchain model analyzed by the BIS. Those are operational details, not part of the short definition of AMM, and their relevance can vary across execution designs. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

Use the term as an entry point: AMM means automated market maker, and its basic role is to facilitate trading through programmed rules and available liquidity. To understand a particular system, its own documentation must provide the implementation details that the abbreviation leaves open. Specific pricing mechanics, protocol comparisons, and liquidity-provider participation are separate questions and are outside this definition.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
