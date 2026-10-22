---
title: "Compound lending crypto: how supply, borrowing, and liquidation work"
description: "Learn how compound lending crypto works, from supplying assets and collateral-based borrowing to interest accrual, liquidation triggers, and key risks."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "compound lending crypto"
owned_question: "How does Compound-style crypto lending work, including supplied assets, borrowing capacity, interest rates, and liquidation?"
risk_level: "medium"
---

Compound-style crypto lending is a pooled lending model: suppliers contribute assets to a protocol market, while borrowers take assets against collateral under rules set by the protocol. Collateral limits borrowing, interest can change with market conditions, and liquidation rules may apply if a position no longer meets required conditions. The specific mechanics and parameters depend on the protocol version, deployment, and market, so this general explanation does not establish current Compound terms.

## What compound lending crypto means

In a pooled lending arrangement, a supplier makes an asset available to a market, and a borrower obtains an asset from that market. The borrower provides collateral to support the debt. Those roles are distinct: supplying an asset is not the same as borrowing, and borrowing creates a position whose collateral must satisfy protocol-defined requirements.

A crypto-collateralized lending model can use overcollateralized smart-contract positions, price oracles, collateral-ratio rules, and liquidation processes. An oracle supplies information from outside the blockchain to a smart contract; in a lending model, price information can be used to evaluate collateral. This describes a general design pattern, not proof that every Compound version, market, or deployment uses the same components or parameters. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

“Compound lending” alone does not identify the rules for a specific position. The version, network deployment, and market matter. Before relying on any operational detail, identify the exact deployment and consult documentation that applies to it. This article explains the broad mechanics without asserting current supported assets, rates, fees, collateral factors, or availability.

## How supplied assets and borrowing capacity fit together

A supplier contributes an asset to a lending market. A borrower takes an asset from the market and provides collateral, creating a position governed by that market’s rules. The amount available to borrow is constrained by the collateral and protocol-defined parameters; it is not simply the same as the collateral’s stated value.

In a collateralized model, collateral-ratio rules help determine how much debt a position can support. The relevant ratio, collateral valuation method, and eligible assets are deployment-specific. Without authoritative details for the chosen version and market, a general explanation cannot establish a borrowing limit or tell a reader how much borrowing a position could sustain.

The position can change after it is opened. Collateral value may move, and debt may grow as interest accrues. Those changes can affect the relationship between collateral and debt, potentially bringing a position closer to the conditions under which the protocol permits liquidation. That is a description of risk mechanics, not a forecast of asset values or a suggested borrowing amount.

For a particular market, verify which assets may serve as collateral, how the protocol obtains price information, how it applies collateral-ratio rules, and whether parameters can change. A rule observed in one market should not be treated as universal across protocol versions or deployments.

## How interest accrues for suppliers and borrowers

Interest is part of the relationship between borrowers and suppliers in a lending market. Borrowers incur interest under the market’s rules; suppliers may receive a return connected to the market’s lending activity. Utilization—the extent to which supplied assets are borrowed—can influence interest rules in pooled lending models. Rates and supplier returns may vary over time and should not be understood as fixed or guaranteed.

The allowed evidence for this article does not specify a Compound deployment’s interest-rate formula, current rates, supplier yields, fees, or accounting method for accrued interest. It therefore supports no numerical rate or return. To understand a specific market, consult its current official documentation and parameters, including how interest responds to market utilization and how accrued amounts are reflected in a position.

A displayed rate or estimate, if provided by a particular deployment, is not evidence that the same rate will continue. A general explanation of utilization does not establish the terms currently offered by any specific market, nor does it establish what a supplier will receive. Those questions require current, market-specific evidence.

It is also useful to keep the two sides of the position separate. A borrower’s interest obligation and a supplier’s return are related through market rules, but this general description does not establish that they are identical amounts or that one particular allocation formula applies. Confirm the formula and any charges in documentation for the exact deployment rather than inferring them from the pooled-lending model.

## What can trigger liquidation

Liquidation is a protocol-defined process that may reduce a borrower’s position when it no longer satisfies required collateral conditions. A decline in collateral value, an increase in debt, or both can weaken the position relative to its requirements. A collateralized model may use price information, collateral-ratio rules, and liquidation processes, but the precise trigger and permitted actions depend on the implementation. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

The liquidation trigger is not a universal threshold. A deployment’s collateral factors, thresholds, eligible collateral, and liquidation procedure must be verified for the exact market and version. Without that information, it is not possible to state a trigger level, how much of a position may be affected, or what costs may apply.

Liquidation puts collateral at risk. The process can reduce the borrower’s position and may result in asset loss or additional costs, but their size and form are deployment-specific and cannot be quantified from the evidence available here. A careful reading of a deployment’s documentation should establish what condition permits liquidation, what actions the protocol allows, and how the remaining position is accounted for.

A position that is initially within its borrowing limit is not thereby guaranteed to remain within required conditions. Collateral values and accrued debt can change, so the relevant operational question is not only the opening limit but also how the market evaluates the position afterward. This explanation does not establish a safe buffer, a liquidation probability, or a method for avoiding liquidation.

## Risks and facts to verify before relying on a deployment

Start by identifying the exact protocol version, network, and market. Then consult the official documentation and current deployment information for supported assets, collateral valuation, borrowing constraints, interest mechanics, liquidation triggers, and parameter-change rules. A general account of pooled lending cannot establish whether a particular market is available or what terms it currently uses.

Treat claims about security, audits, vulnerabilities, past incidents, or recovery as separate claims that require attributable evidence for the relevant version and deployment. The fact that a lending model uses smart contracts and collateral rules does not establish that a specific deployment is free of vulnerabilities, that it has had no incidents, or that funds can be recovered. Do not infer a recovery option from the existence of a protocol or a liquidation process.

Current rates, yields, fees, and market availability also require current, deployment-specific evidence; no figures or availability claims are made here. Likewise, this mechanism explanation does not determine what legal, tax, regulatory, or compliance requirements apply to a reader. Those questions depend on the reader’s circumstances and location and require appropriate authoritative information.

The core sequence is straightforward to describe but deployment-specific in operation: a supplier contributes assets, a borrower takes assets against collateral, market rules govern interest, and protocol-defined conditions may permit liquidation. The precise assets, limits, rates, costs, and triggers cannot be inferred from the label “Compound lending.” Readers should verify those details for the exact deployment rather than treating this general mechanism description as current terms or participation advice.

## Sources and references

- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
