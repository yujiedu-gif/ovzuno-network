---
title: "Crypto lending: how decentralized protocols manage collateral and borrowing"
description: "Learn how crypto lending protocols handle supplied assets, collateral, borrowing rates, liquidation, and operational risks without treating designs as uniform."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "crypto lending"
owned_question: "How do decentralized crypto lending protocols connect lenders and borrowers, determine collateral requirements, and manage liquidation and other protocol risks?"
risk_level: "high"
---

Decentralized crypto lending protocols connect asset suppliers and borrowers through software rules, often using collateralized positions, price oracles, collateral-ratio requirements, and liquidation processes. Those are common mechanisms, not uniform protocol terms: the contracts, parameters, and operational dependencies must be checked for each implementation. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

## What crypto lending means in decentralized finance

A decentralized lending protocol is an arrangement in which blockchain-based software coordinates lending activity. In a common design, suppliers make assets available under protocol rules, while borrowers obtain assets subject to conditions that may include posting collateral. A smart contract is software deployed on a blockchain; it can apply the rules encoded in its functions, but its presence alone does not tell a reader who can change those rules or what other dependencies exist. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

A widely used conceptual model is an overcollateralized position. “Overcollateralized” means the protocol’s rules require collateral value above the borrowing amount, as measured by the system. The model can use price oracles—services or mechanisms that provide price inputs to contract logic—along with collateral-ratio rules and liquidation processes. The exact calculation, collateral assets, and enforcement details are implementation-specific. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

The term “decentralized” is not a complete description of how a particular system operates. A DeFi application can be examined as having settlement, application, and interface layers, and those layers can have distinct technical dependencies. A system may distribute or combine them differently. The contract’s behavior, the user-facing application, and any supporting services should therefore be distinguished rather than treated as one indivisible mechanism. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

This article follows the general collateralized model. It does not assume that every protocol pools deposits, uses the same borrowing terms, or has the same control structure. It describes mechanisms rather than product choices or expected returns; it also does not determine the legal or tax classification of an arrangement.

## How supplied assets become borrowable liquidity

On the supply side, a user provides an asset according to the protocol’s process. In a pooled design, supplied assets can contribute to liquidity from which borrowers draw, but the general evidence here does not establish a universal pool structure or supplier claim. Nor does it establish that deposited assets are always available for immediate withdrawal. The contract and protocol configuration determine how a particular implementation accounts for supply and applies constraints. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

The useful distinction is between a contribution to a lending mechanism and a promise about access. Whether a supplied asset can be borrowed, withdrawn, or used in another way depends on the specific rules. A general label such as “lending pool” cannot establish which contract receives the asset, how a supplier’s position is recorded, or what withdrawal conditions apply. Those details require the protocol’s own materials.

A practical architecture review follows the asset through the system. Identify the contract or pool involved, the way the protocol records supplier positions, and the conditions attached to borrowing and withdrawal. Then separate the on-chain mechanism from the interface that displays it. The interface may explain a position, but the protocol’s encoded rules determine what the contract can do. Application layers can have dependencies distinct from settlement layers, so a review should map both rather than infer one from the other. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

The term “supplier” also does not settle questions about custody or control. The available evidence supports the general use of collateralized smart-contract positions, not a universal account of who controls keys, administers contracts, or can pause or alter a system. Those are protocol-specific facts to verify rather than assume. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

## Collateral, borrowing capacity, and interest rates

In a collateralized position, the borrower commits assets as support for borrowing. A protocol may rely on an oracle for price inputs, then apply collateral-ratio rules to assess the position. The oracle, assets accepted as collateral, valuation method, and borrowing limit are design-specific. The general model does not establish a standard ratio or a universal calculation. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

Collateral requirements connect asset valuation to borrowing capacity. To interpret a position, a reader needs to know what prices the system uses, how it combines those prices with collateral and debt, and which rule triggers a change in position status. If the documentation does not make those inputs and rules clear, the missing details should not be supplied from assumptions about another protocol. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

Interest-rate behavior needs the same care. The available evidence does not establish a universal rate formula, including whether a given design responds to utilization or uses another mechanism. It supports no specific rate, yield, or return expectation. For a particular protocol, inspect authoritative documentation for how borrowing costs are determined, which events can change them, and which assets and networks the stated rules cover. A quoted or displayed number, if present in a specific application, would not by itself explain the mechanism or its conditions.

Parameters can also change through protocol processes, so an operator or integrator should verify which version and current rules apply. The evidence here does not establish a common method for parameter changes or governance. It does establish that a collateralized design can depend on governance as well as contracts, oracles, liquidity, and collateral prices; each dependency should be evaluated within the specific system rather than generalized. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

## What happens when collateral approaches liquidation

A collateralized protocol may use liquidation when a position no longer satisfies its collateral requirements. In the general model, collateral-ratio rules and liquidation processes are part of the mechanism. But the evidence does not specify a shared threshold, the parties permitted to initiate liquidation, any incentive or penalty, or the amount and sequence of assets involved. These terms must be checked for the particular protocol. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

To understand the path, trace the decision from price input to contract action: identify the oracle, determine how the protocol compares collateral and borrowing, and find the rule that makes a position eligible for liquidation. Then establish which contract action executes the process and how the protocol accounts for the resulting position. The broad mechanism does not document what a specific system does during disrupted pricing, congestion, or limited liquidity; those are risks to investigate, not outcomes that can be presumed. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

Liquidation is not the same as a guarantee that collateral can be sold or that all borrowing will be recovered. The design can face oracle, contract, governance, liquidity, collateral-price, and bad-debt failures. This means a stated collateral requirement is only one part of the operating model: the price inputs and the execution process matter as well. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

For a builder, the task is to distinguish the position state shown by an interface from the actions performed by contracts. For a protocol operator, the task is to document the liquidation assumptions and execution path. For a business decision-maker, the task is to request the specific terms and dependencies rather than relying on a generic description such as “collateralized lending.”

## Protocol risks and evidence to check before relying on a design

A lending design can depend on smart contracts, price oracles, governance, liquidity, collateral prices, and liquidation processes. Failures across these areas can result in bad debt or other losses. Overcollateralization is a mechanism, not proof that liquidation will always work as intended or that supplied assets can always be withdrawn. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

Review the protocol’s documentation to identify the contracts involved and trace supply, borrowing, collateral valuation, rate setting, and liquidation. Review any available audit material for its stated scope and date, and examine upgrade or administrative controls separately. The evidence allowed for this overview does not establish an audit status, control structure, incident history, or security outcome for any specific protocol. An audit or a described control, on its own, would not resolve every dependency in the system.

Next, verify oracle design, supported assets and networks, current parameters, fees, withdrawal conditions, and any stated recovery procedures in current authoritative protocol materials. The evidence here does not establish those details for a named implementation. It also does not establish availability, compliance requirements, or jurisdictional treatment. Those questions require current and applicable evidence; they cannot be answered by extrapolating from the generic mechanism.

The central operating distinction is between the general lending lifecycle and a protocol’s actual implementation. A conceptual model helps organize the review: trace supplied assets into the mechanism, identify the rules for borrowing and collateral, determine how rates are set, and follow the conditions and execution path for liquidation. The protocol’s own materials must supply the specific terms and dependencies. When they do not, preserve that uncertainty rather than treating the design as uniform. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

## Sources and references

- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
