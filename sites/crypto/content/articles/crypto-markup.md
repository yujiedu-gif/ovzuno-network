---
title: "Crypto markup: meaning in a transaction quote"
description: "Understand crypto markup in a transaction quote, how it may differ from a reference price or separate fee, and which details to clarify before comparison."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["institutional_crypto_treasury"]
tags: ["crypto trading markup", "cryptocurrency spread", "quoted price"]
author: "editorial_team"
primary_keyword: "crypto markup"
owned_question: "What does crypto markup mean in a quoted transaction, how can it be distinguished from the reference market price and other charges, and what information is needed to assess it?"
risk_level: "medium"
---

A **crypto markup** is a possible amount or price component that makes an execution quote differ from a stated reference price. The label and calculation are not universal: to interpret a quote, identify its benchmark, timing, included charges, and provider-specific terms rather than treating every price difference as a disclosed markup.

## What crypto markup means in a transaction quote

A **transaction quote** states the terms or estimated outcome for a particular purchase or sale. A **reference price** is the benchmark used to compare that quote with a market price or another stated value. If the quoted execution price differs from the reference, a markup may be one explanation—but the difference alone does not establish that a provider has applied or disclosed a markup.

The quote may use a provider-specific label or calculation. Unless the terms explain how the figure is derived, do not assume that “markup” means the same thing across providers or transaction structures. For example, a documented onramp quote API can return estimated conversion outcomes for a combination of source amount, destination cryptocurrency, network, fees, and rate before a purchase flow. That example illustrates why a quote can reflect several inputs; it does not establish a universal markup formula or describe every provider’s quote.

## Reference price, spread, markup, and fee are not interchangeable

A reference price is a comparison point, not necessarily the price at which a transaction will execute. Its source and timestamp matter: a benchmark from a different source or time may not provide a like-for-like comparison with the quote.

A **spread**, where applicable, is a difference between quoted buy and sell prices. A **fee** is a charge that may be shown separately. A markup, by contrast, may be an amount embedded in the quoted execution price—or a provider’s label for a price component. These terms can describe related but distinct parts of a quote, and the wording alone may not explain how they interact.

Do not add an inferred markup to a separately listed fee unless the quote’s terms establish that both are separate charges. If the execution price already incorporates a price component, counting that component again could misstate the total. Ask for the calculation or an itemized explanation rather than assuming that every difference from a reference price is an additional fee.

## Details to check before interpreting a crypto quote

Before comparing or recording a quote, clarify the terms that define what it covers:

- **Asset and direction:** Which crypto asset is being bought or sold, and from whose perspective is the quote stated?
- **Quantity and quote currency:** What amount of the asset is covered, and what currency is used to express the price?
- **Validity period:** When was the quote generated, and how long does it remain valid? Some quote systems provide an estimated outcome that can change before the purchase is completed.
- **Reference benchmark:** What price is used for comparison, from which source, and at what time?
- **Price components:** Does the execution quote include an embedded markup or spread? Are any fees or other adjustments listed separately?
- **Other stated charges:** If relevant to the quote, are network, settlement, or custody charges included in the quoted amount or listed separately?

These are clarification questions, not assumptions that every quote contains each component. A quote may not identify a reference price or separate every charge. If the information is missing, record that limitation rather than inferring a calculation from the final amount alone.

## Why two quotes may not be directly comparable

Two quotes can use different reference sources or timestamps, cover different quantities, remain valid for different periods, or include different charges. Execution conditions may also differ. A displayed price gap therefore does not, by itself, identify the markup or establish the total cost of either transaction.

For a like-for-like comparison, request terms that use a consistent asset, direction, quantity, quote currency, reference source and time, validity period, and description of included charges. If providers use different labels, ask what each label means and which amounts are embedded in the price versus added separately. Without that information, the figures may not describe equivalent transactions.

## What a markup alone does not establish

A markup figure alone does not establish whether a quote is fair, competitive, or appropriate. It also does not explain execution quality, settlement risk, custody arrangements, regulatory status, tax treatment, or asset availability. Those are separate questions requiring evidence about the relevant transaction, provider, product, and circumstances.

For example, if a quote describes a custody arrangement, custody terms are not interchangeable with price terms. A U.S. Securities and Exchange Commission investor bulletin describes third-party custodians as managing access to private keys on customers’ behalf, while noting that custody structure and customer rights vary by provider and jurisdiction. That does not determine the meaning of a quote’s markup; it illustrates why a price label cannot establish custody rights.

The practical conclusion is narrow: treat “crypto markup” as a quote-specific term. Identify the reference price and its timing, distinguish embedded price components from separately listed charges, and ask for the calculation when the quote does not make it clear. A number labeled “markup” is only one part of understanding what the quoted transaction represents.

## Sources and references

- [Crypto Onramp Quotes](https://docs.stripe.com/api/crypto/onramp_quotes) — Stripe Documentation; retrieved 2026-10-19.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
