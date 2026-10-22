---
title: "Digital asset treasury mNAV: meaning, calculation, and limits"
description: "Understand digital asset treasury mNAV, the inputs used to calculate it, how to interpret the ratio, and why it is not a standalone measure of treasury value."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["dao_governance"]
tags: []
author: "editorial_team"
primary_keyword: "digital asset treasury mnav"
owned_question: "What does mNAV mean when evaluating a digital asset treasury, how is it calculated, and what can—and cannot—it tell DAO governance participants?"
risk_level: "medium"
---

For DAO governance participants, **mNAV** is a ratio that compares a chosen market value with a chosen net asset value (NAV). It can summarize how those two reported figures relate, but it is not a standalone measure of treasury value, asset quality, liquidity, or governance effectiveness. Before interpreting a result, identify what the numerator and denominator represent and how each was measured.

## What mNAV means for a digital asset treasury

In this context, *market value* is the market-based value selected for the numerator. *Net asset value* is the value assigned to included assets minus included liabilities. The general idea behind mNAV is to compare the two. The label does not, by itself, specify a universal set of accounting rules or settle which entity or instrument should be measured.

The numerator might refer to a particular token, a share-like instrument, or an organization’s market value. These are distinct possibilities, not interchangeable labels. The denominator might cover a DAO treasury, a broader organization, or another defined pool of assets and liabilities. A reader needs to know the boundary on each side to determine whether the comparison is coherent.

It also helps to distinguish a token record from the asset or rights it may represent. A digital token can be a digital ledger record about an asset and its owner, with programmable rules governing use or transfer. The technical record alone does not determine legal title, enforceability, or the quality of the represented asset. So a treasury’s asset list and the rights associated with those assets are relevant context, but they are not supplied by the mNAV ratio itself. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

## How digital asset treasury mNAV is calculated

A useful general form is:

> **mNAV = selected market value ÷ selected net asset value**
>
> **Selected net asset value = included asset values − included liabilities**

These formulas express the arithmetic, not a universally prescribed accounting policy. The word “selected” matters: the calculation depends on what is included and how the inputs are valued. A report should state what the numerator measures and describe the assets, liabilities, and methods used to arrive at NAV. Without those details, the ratio’s name is not enough to reproduce or compare it.

**Hypothetical example—not a real organization or market figure:** Suppose a DAO report assigns its included treasury assets a value of $12 million and includes $2 million of liabilities. Under those assumptions, its stated NAV is $10 million. If the chosen market value for the entity or instrument is $15 million, then:

> **$15 million ÷ $10 million = 1.5**

The result means the selected numerator is one and a half times the selected denominator. The example demonstrates division only. It is not a typical result, market benchmark, recommended valuation approach, or statement about any real DAO.

Several methodological choices can change the result. A report may use different valuation timestamps or pricing inputs for assets; it may define the treasury boundary differently or treat liabilities differently. If the numerator concerns an instrument with a share count, the calculation may also depend on whether the count is circulating or diluted. These choices should be disclosed as part of the method, not guessed from the reported ratio.

For a clear calculation, the reader should be able to follow a chain of inputs: identify the entity or instrument, identify the valuation date, see how included asset values and liabilities were assembled, and confirm the units used in the division. If a report supplies only the final number, readers may be able to understand the stated ratio but not verify the assumptions that produced it.

## How to interpret an mNAV result

When the numerator and denominator use compatible units and refer to clearly defined subjects, a result above 1 means the selected market value is greater than the selected NAV. A result below 1 means it is smaller. A result equal to 1 means the two selected figures are equal. Those statements describe the arithmetic; they do not explain the difference or judge whether it is desirable.

Comparisons require consistent definitions, dates, and units. For example, a market value for one instrument should not be treated as directly comparable to NAV for a different entity or period without explaining the relationship. Even two figures using the same label may rest on different boundaries or valuation choices. A ratio can be calculated precisely while its inputs remain method-dependent.

In a governance discussion, mNAV can be a starting point for asking about context such as liabilities, asset concentration, liquidity, or treasury policy. The ratio alone does not establish that any of those factors caused a gap between the selected figures. Nor does it measure the quality of governance decisions. Keep the calculation separate from explanations or judgments that require other evidence.

A useful interpretation therefore has two parts: first, state what the reported number says under its specified formula; second, identify what it does not establish. For instance, the hypothetical result of 1.5 says that the chosen numerator is 1.5 times the chosen NAV. By itself, it does not identify why the figures differ, whether the inputs are complete, or whether the underlying assets and liabilities were measured in a way suitable for another comparison.

## What mNAV leaves out

An mNAV ratio does not by itself establish whether reported assets can be recovered, how readily they can be converted or used, who controls them, or whether governance decisions are sound. Those questions concern rights, operations, and decision-making beyond the ratio’s arithmetic. A token record about an asset likewise does not, on its own, settle what claim a holder has or how backing assets relate to that claim. [source](<https://www.bis.org/publications/wholesale-digital-tokens>)

The result also leaves open how measurement uncertainty and commitments are handled. Asset valuation choices, included liabilities, off-balance-sheet commitments, and changes in token or share supply can affect interpretation. If those items are not described, a reader may not be able to distinguish differences in the underlying situation from differences in measurement choices. The ratio cannot compensate for missing disclosure about its inputs.

Nor does mNAV establish that all parts of an organization are captured by the denominator. A reader should check whether the calculation is limited to treasury holdings or includes a broader set of assets and liabilities. The same question applies to the numerator: does it measure an entity, an instrument, or something else? A mismatch can limit the meaning of the comparison even when the division itself is correct.

Finally, mNAV is a descriptive valuation comparison, not a legal, tax, regulatory, or investment conclusion. It does not establish an asset’s legal status, the enforceability of a holder’s rights, or whether a particular course of action is suitable. Those matters are outside what the ratio calculates.

## Questions governance participants can ask about mNAV

When a reported figure comes up in a DAO governance discussion, ask for the method and its boundaries before debating what the result means:

- What exactly is the market-value numerator: the organization, a token, or another instrument?
- Which assets and liabilities are included in NAV, and how are they valued?
- What are the data sources, valuation date, and units?
- If the numerator depends on a share or token count, what count is used and how is it defined?
- Do the numerator and denominator refer to the same entity, scope, and period?
- What assumptions or changes could materially alter the result, and what limitations are disclosed?

These questions are not a substitute for a calculation methodology. They help governance participants test whether the number can be understood on its stated terms. If a report does not identify its inputs or the two sides refer to different scopes, the appropriate conclusion is limited: the arithmetic may be visible, while the comparison’s meaning remains uncertain.

A careful governance discussion can therefore treat mNAV as one defined ratio rather than a complete treasury assessment. State the formula, preserve the assumptions, and describe the result narrowly. That approach helps prevent a single number from being mistaken for a conclusion about recoverability, liquidity, rights, or governance performance.

## Sources and references

- [Wholesale Digital Tokens](https://www.bis.org/publications/wholesale-digital-tokens) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
