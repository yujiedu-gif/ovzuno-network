---
title: "Bitcoin Balance on Exchanges: Meaning, Measurement, and Limits"
description: "Learn what bitcoin balance on exchanges means, how reported figures are estimated, and why attribution limits make them an incomplete measure of exchange-held assets"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "bitcoin balance on exchanges"
owned_question: "What does a reported bitcoin balance on exchanges measure, how is it estimated, and what are its main limitations?"
risk_level: "medium"
---

A reported **bitcoin balance on exchanges** is an estimate of bitcoin attributed to addresses believed to be controlled by exchanges. It measures identified on-chain holdings within a stated dataset—not necessarily every bitcoin an exchange controls, the amount owed to customers, or the exchange’s overall solvency. Interpreting the figure requires checking which exchanges and addresses are included, how attribution was made, and when the data was measured.

## What a bitcoin balance on exchanges represents

The metric usually starts with bitcoin recorded at addresses that an analyst or data provider associates with an exchange. An address is a location in the network’s transaction record; assigning it to an exchange is an attribution, not something the balance itself proves. The reported total therefore depends on both the on-chain data and the address set counted.

A figure may cover only selected platforms or known addresses, rather than every exchange or every address an exchange might use. It may also be published at a particular time, or calculated using a particular definition of which balances count. As a result, two reports can differ without either number being a direct, complete inventory of all exchange-related bitcoin. The useful first question is not simply “What is the total?” but “What entities, addresses, and measurement time does this total cover?”

An attributed on-chain balance should also be separated from customer account balances and liabilities. A centralized exchange commonly transfers customer funds into its custody before trading on an internal order book, where it records customer orders and executed trades in its own account system. Those internal records and the on-chain address balance are different kinds of information. A blockchain address total does not, by itself, show what customers are owed or reconcile an exchange’s assets with its liabilities.

## How analysts estimate exchange-held bitcoin

In broad terms, an estimate is assembled by identifying addresses associated with exchanges and adding the bitcoin balances attributed to those addresses. Public disclosures or other evidence may help connect an address to an entity. But the evidence boundary matters: a label is an analyst’s or provider’s attribution, not a feature of the bitcoin balance that establishes who controls it.

The result depends on the provider’s address labels, the coverage of the address set, the definition of the metric, and the timestamp. Unless a report explains these details, readers cannot assume that its number covers all exchanges, all addresses, or an identical set of holdings to another provider’s figure. No single methodology should be presumed from the headline number alone.

The distinction between attribution and proof is important. A balance is recorded at an address, but that observation alone does not establish who beneficially owns the bitcoin, what contractual claims exist, or whether the assets are available to meet obligations. Likewise, a movement between addresses can change the measured balance of an attributed group without, by itself, explaining the purpose of the transfer or its relationship to customer claims.

## Why exchange balance estimates can be incomplete

Coverage can be incomplete when addresses have not been identified or included in the provider’s dataset. An address set can also be misattributed: an address associated with an exchange may not represent assets controlled by that exchange, or an exchange-associated address may be absent from the estimate. These limitations mean the reported number is best read as a measurement of the provider’s attributed address set, not as a guaranteed ceiling or complete accounting.

Custody arrangements can further complicate interpretation. A centralized exchange typically takes custody of funds before customers trade on its internal system, but custody and legal ownership arrangements vary by platform and jurisdiction. An on-chain balance does not settle those questions. Nor does the number alone reveal the claims of customers or other parties, or establish the completeness of an exchange’s reserves.

The figure also cannot independently explain why balances changed. A change in the addresses counted could reflect transfers or differences in coverage and attribution; the number alone does not establish intent. Market liquidity is a distinct concept: it concerns the time and expense of buying or selling and can include spread, transaction cost, price impact, and immediacy. An exchange-balance statistic is not itself a measure of those dimensions.

## How to read a reported figure responsibly

Before interpreting a reported balance, check the provider and measurement timestamp. Then look for the exchanges and address sets included, the provider’s stated definition, and any explanation of how addresses were attributed. If the report does not disclose these boundaries, treat its coverage as uncertain rather than filling in missing details.

For time-series comparisons, compare like with like: the same provider, definition, exchange coverage, and stated measurement basis. If any of those change, a difference between reported figures may not represent a change in the same underlying set of exchange-attributed holdings. Where methods or coverage are unclear, the data supports a narrower conclusion: the provider reported a change in its estimate, not necessarily a verified change in total exchange-held bitcoin.

Finally, treat the number as an estimate of bitcoin attributed to identified exchange addresses. It is not, by itself, a complete measure of exchange assets, customer liabilities, solvency, or market intent. Keeping those distinctions in view lets readers describe what a reported figure measures without asking it to prove more than its address coverage and attribution support.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
