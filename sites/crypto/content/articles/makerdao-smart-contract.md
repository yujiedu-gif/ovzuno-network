---
title: "MakerDAO smart contract: roles and protocol architecture"
description: "Explore how MakerDAO smart contract components support collateralized positions, Dai issuance, system accounting, and governance, with limits of a high-level map."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["MakerDAO protocol architecture", "Maker Protocol contracts", "Dai stablecoin contracts"]
author: "editorial_team"
primary_keyword: "makerdao smart contract"
owned_question: "What roles do MakerDAO’s core smart contracts perform, and how do they interact within the protocol?"
risk_level: "medium"
---

MakerDAO’s core smart contracts should be understood as a coordinated set of components, not as one all-purpose contract. However, the evidence available for this overview does not verify the Maker Protocol’s specific contract names, collateral-and-debt mechanisms, Dai accounting, or governance flow. A reliable role map therefore requires authoritative, version-specific documentation that is not established here.

## What “MakerDAO smart contract” refers to

The phrase “MakerDAO smart contract” can refer loosely to an individual contract or to the broader set of on-chain components associated with the protocol. Those scopes are not interchangeable: a description of one contract does not, by itself, describe the full architecture. The evidence provided for this article does not establish how the names “MakerDAO” and “Maker Protocol” have been used across periods or implementations, so this article does not treat either phrase as a version-specific technical label.

A contract is generally a program with code and data, but that general definition does not identify the duties of any Maker component. An architecture map would need to connect named contracts to their documented responsibilities and show which relationships apply to the specific implementation under discussion. The allowed evidence does not provide that Maker-specific map.

The scope here is consequently conceptual and limited. It does not attempt to list live contracts, describe a deployment, or give instructions for interacting with the protocol. It also does not infer implementation details from general examples of contract architecture elsewhere.

## Core contract roles in the Maker Protocol

A useful protocol map would distinguish at least three kinds of responsibilities: managing collateralized positions, accounting for debt and Dai-related balances, and carrying out governance or parameter-management functions. But the allowed evidence does not establish which Maker contracts perform those tasks, how responsibilities are divided, or how the relevant contracts communicate. Naming particular components or assigning them those functions would go beyond what is supported.

That distinction matters because a role label can sound more precise than the underlying evidence. Calling a component an “accounting” or “position” contract does not show what state it stores, what operations it permits, which other contracts can invoke it, or which version the label describes. To make those statements accurately, a source would need to identify the applicable code or documentation and substantiate the role and the connection to other components.

General access-control patterns do not fill this gap. Role-based access control, for example, can separate permissions into named roles and use administrator roles to grant or revoke them, creating an authority structure that itself needs protection. That describes an architectural pattern, not evidence that Maker Protocol uses it or assigns particular authorities to any Maker contract. [source](<https://docs.openzeppelin.com/contracts/5.x/access-control>)

For the same reason, a protocol diagram should not be treated as a universal map across all versions. The available evidence does not establish which modules or contract relationships have applied to Maker at any particular time. This overview therefore avoids presenting a fixed list of Maker contract names or responsibilities as though it were verified for every implementation.

## How a collateralized position connects to Dai

At a high level, the question is how the protocol represents a user’s collateral and debt, applies the rules governing a position, and records the related Dai activity. The allowed evidence does not substantiate those Maker-specific mechanisms. It does not verify the contract-level steps by which collateral is recorded, debt is created or updated, or protocol balances are reconciled.

A careful technical explanation would need to follow those relationships in the relevant implementation rather than assume a single, universal path. It would also need to distinguish internal contract accounting from statements about Dai’s market price or value. The evidence here supports neither a claim about a particular price outcome nor a conclusion that any mechanism guarantees one. This explainer makes no such claim.

The distinction between automatic execution and decisions made outside a contract is also important in a complete architecture account. Yet the supplied evidence does not establish which Maker operations execute automatically, which require a governance decision, or how a decision becomes an on-chain action. Without that information, a step-by-step transaction flow would risk implying a mechanism that has not been verified.

As a result, the most accurate account of the position-to-Dai relationship at this evidence boundary is a limitation: the central relationship is part of the intended scope, but the available claims do not establish its implementation. A version-specific explanation should support each step with authoritative protocol material rather than derive Maker behavior from generic smart-contract concepts.

## Governance and supporting modules

Governance and supporting modules can be central to a protocol architecture, but their role must be documented rather than assumed. The allowed evidence does not establish Maker’s governance process, the contracts used to manage parameters, or any supporting modules for risk management, accounting, or liquidation. It also does not show how a governance outcome, if any, relates to contract execution in a particular version.

A general permission model illustrates why these distinctions matter without answering the Maker-specific question. Assigning separate roles and granting or revoking them through administrator roles describes one possible way to structure permissions. It does not establish that Maker governance uses that pattern, who holds relevant permissions, or how a parameter change would proceed. [source](<https://docs.openzeppelin.com/contracts/5.x/access-control>)

A broader system may also rely on decisions or records outside its contracts. For example, one reference architecture coordinates multiple private systems of record using messaging, cryptography, proofs, and a consensus-controlled state machine while keeping business data in those systems. That is an example of a distinct architecture, not evidence about Maker. It cannot be used to infer Maker’s governance, accounting, or supporting modules.

Changes to a protocol’s code or module relationships can make an older diagram incomplete. The evidence provided here does not identify Maker upgrades, migrations, or the effects of any such changes. The practical implication is to treat a role map as tied to a documented implementation, not as timeless merely because it uses familiar contract labels.

## What a contract map can—and cannot—establish

A conceptual map can explain responsibilities when those responsibilities are verified, but it is not a live contract directory. The evidence available here does not establish Maker deployment status, chain-specific addresses, current parameters, upgrades, or migrations. None of those details should be inferred from a general protocol description.

Likewise, a diagram or role summary does not establish security, audit completeness, recovery behavior, fees, yields, availability, jurisdiction-specific access, or regulatory or tax treatment. This article makes no assessment of those matters. It also does not offer investment advice or suggest that Dai or any related asset is safe, suitable, or certain to maintain a particular value.

For a version-specific technical account, the necessary next step is evidentiary, not operational: identify the chain and implementation being discussed, then verify the contract names, source code, documented functions, and inter-contract relationships against authoritative materials for that version. The allowed claims here do not provide those details, so a more specific Maker contract map would require evidence beyond this article’s boundary.

The bounded takeaway is that “MakerDAO smart contract” is not enough to identify one contract or substantiate a full protocol architecture. A trustworthy explanation of core roles and interactions must be anchored to a particular, verified implementation; this overview cannot assign Maker-specific functions without that support.

## Sources and references

- [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control) — OpenZeppelin Documentation; retrieved 2026-10-19.
