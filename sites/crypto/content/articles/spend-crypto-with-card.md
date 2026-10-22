---
title: "How to spend crypto with card: the payment flow"
description: "Learn how to spend crypto with card, including payment authorization, possible conversion to fiat, settlement timing, and details to verify before a purchase."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_cards_spending"]
tags: []
author: "editorial_team"
primary_keyword: "spend crypto with card"
owned_question: "What happens when someone uses crypto-related funds to pay with a card, from authorization through conversion and settlement?"
risk_level: "medium"
---

Using crypto-related funds to pay by card generally means the purchase is handled through card-payment arrangements, while any conversion from crypto to fiat depends on the specific card program. The card transaction is not automatically an on-chain transfer, and there is no universal conversion point or settlement timeline that applies to every crypto-linked card.

## What it means to spend crypto with card

A crypto-linked card is a card product connected in some way to digital assets and a traditional card-payment network. The label alone does not tell you where the crypto is held, which balance funds a purchase, or when conversion occurs. A program could use a fiat balance, convert supported cryptocurrency to fiat before loading a card, or use another program-defined arrangement.

This distinction matters because a card purchase and a blockchain transfer are different processes. A card transaction follows the payment program’s arrangements. A cryptocurrency transfer, in contrast, uses a digital signature to authorize a transfer between users under the relevant network’s rules. A signature can authorize a transfer, but that does not mean every card purchase is recorded on a blockchain. [source](<https://csrc.nist.gov/glossary/term/Cryptocurrency>)

For some Visa-facilitated programs described by Visa, digital assets may be converted to local fiat at the point of sale, with merchants receiving standard payments through Visa’s existing settlement process. This is one described program model, not a rule for all crypto-linked cards or card networks. Conversion timing and the merchant-side payment path can differ in other products.

So the practical question is not simply whether a card is “crypto.” It is what balance is used, which party or system converts value if conversion is needed, and how the program relates that conversion to the card purchase. The card’s branding does not answer those questions by itself.

## How a card purchase can move from authorization to settlement

A card purchase begins with a merchant submitting a transaction for authorization through its card-payment arrangements. The program applies its approval rules and checks the relevant funding source. The exact authorization checks, account structure, and operational steps vary by program, so a general description cannot establish what happens in every product.

If the funding source involves crypto, conversion may be part of making fiat available for the card payment. In one documented product model, funding can involve topping up with a fiat balance or converting supported cryptocurrency to fiat before loading the card. That example shows why the timing matters: conversion can occur before a purchase in at least one described arrangement. It does not establish that all cards follow this sequence.

Visa describes another model in which digital assets may be converted to local fiat at the point of sale. In that model, the merchant receives a standard payment through Visa’s existing settlement process. The cardholder-facing link to digital assets therefore need not mean that the merchant receives cryptocurrency or that the card network settles a blockchain transfer. Again, this is a described Visa program model, not a universal process.

After authorization, card-network and issuer processes govern the card payment and its settlement. Any crypto conversion is a separate part of the overall arrangement, with timing that depends on the product. A blockchain transfer, if one occurs as part of a funding or conversion process, follows the applicable network rules; it should not be assumed to be the mechanism that authorizes the merchant’s card transaction.

The entities involved also have different roles. The merchant submits the card transaction through its payment arrangements. The card program defines how purchases are approved and funded. A provider or exchange may be involved in handling a balance or conversion, but the available evidence does not establish that every program uses the same type of provider or structure. Some centralized crypto exchange operators may combine trading, lending, token issuance, and custody functions; that fact does not prove any particular exchange is involved in a given card flow. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

This separation helps avoid a common misunderstanding: “authorization,” “conversion,” and “settlement” are not interchangeable terms. Authorization concerns approval of the card purchase. Conversion concerns changing digital-asset value into fiat, if the program does so. Card settlement follows the program and network’s payment process. A blockchain record is relevant only if the arrangement uses a blockchain transaction for a particular step.

## Where conversion, balances, and fees can differ

The balance that appears in an account may not be the balance that directly funds a purchase. A program might draw on fiat that is already available, or it might require crypto to be converted to fiat before the card is loaded. Other arrangements may define funding differently. Confirm the actual funding source in the program’s current terms instead of inferring it from a crypto balance display.

Conversion timing also affects what a reader should verify. If conversion occurs before loading, the conversion and card purchase are distinct events. If a program describes conversion at the point of sale, the program’s terms determine how that step relates to the purchase. The evidence here does not establish a universal rate-setting time, fee schedule, or sequence. Check the specific program’s current documentation for the applicable exchange rate, conversion timing, fees, and limits.

Do not treat an estimate from a different service as the final amount for a card purchase. For example, an onramp quote API can return estimated conversion outcomes based on inputs such as the source amount, destination cryptocurrency and network, fees, and rate. Such a quote is time-sensitive and estimated; it describes an onramp quote, not the conversion method for a card transaction. [source](<https://docs.stripe.com/api/crypto/onramp_quotes>)

Exceptions need separate attention because the card-side result and any conversion-related action may not be identical. Review current terms for how the program handles declined purchases, reversals, refunds, partial authorizations, and transaction amounts that change after authorization. The evidence available here does not establish whether refunds are paid in fiat or crypto, whether conversion fees are returned, or how exchange-rate differences are handled. Those outcomes are program-specific, so they should be verified rather than assumed.

## What to verify before using crypto for a card payment

Use the program’s current official materials to check the details that determine how a purchase works:

- **Availability and eligibility:** Confirm whether the program is available to you, which assets and locations it supports, and what account requirements apply. These details can vary, and the evidence here does not establish current availability or eligibility for a particular product.
- **Funding route:** Identify whether purchases draw on a fiat balance, require converting crypto before loading, or use another defined structure. Do not assume that a card linked to crypto spends directly from a blockchain wallet.
- **Conversion terms:** Check when conversion occurs, how the exchange rate is determined, and which fees and limits apply. Make sure the terms describe the actual card program rather than a separate exchange or onramp service.
- **Settlement and exceptions:** Review how authorization relates to final processing and how declined payments, reversals, refunds, and partial authorizations are treated. Ask whether any conversion action is separate from the card-side outcome.
- **Account access and controls:** Check the product’s current documentation for account-access, recovery, and security details. The fact that a card is connected to crypto does not establish which safeguards or recovery processes the program provides.
- **Restrictions and other obligations:** Review the program’s own spending, merchant, and transaction restrictions. Requirements can depend on the product and a person’s circumstances; this explainer does not determine obligations in a particular location.
- **Tax questions:** Do not assume that card-funded spending has uniform tax treatment. For questions about a specific jurisdiction or situation, consult qualified, jurisdiction-specific sources.

The useful mental model is to keep the parts distinct: a card purchase is authorized and settled through its payment arrangements; the funding source may involve fiat, crypto converted to fiat, or another program-defined setup; and any blockchain transaction is a separate mechanism unless the program’s documentation explains otherwise. Before relying on a crypto-linked card, verify the precise funding and conversion sequence and the terms for fees, limits, settlement, and exceptions.

## Sources and references

- [Cryptocurrency - Glossary](https://csrc.nist.gov/glossary/term/Cryptocurrency) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Crypto Onramp Quotes](https://docs.stripe.com/api/crypto/onramp_quotes) — Stripe Documentation; retrieved 2026-10-19.
