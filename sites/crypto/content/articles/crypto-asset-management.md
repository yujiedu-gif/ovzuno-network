---
title: "Crypto Asset Management: Roles, Controls, and Custody"
description: "Learn what crypto asset management covers in wallets and custody, how responsibilities differ, and which controls organizations should assess before defining a model"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["wallets_custody"]
tags: ["digital asset custody", "crypto portfolio administration", "custodial and non-custodial management"]
author: "editorial_team"
primary_keyword: "crypto asset management"
owned_question: "What does crypto asset management mean in a wallets-and-custody context, and which operational responsibilities does it cover?"
risk_level: "high"
---

Crypto asset management, in a wallets-and-custody context, means organizing how digital assets are accessed, controlled, approved, and administered. The term does not have one universal operational definition in the evidence available here. It is useful to separate management of access and transactions from investment decisions: this explainer covers operational responsibilities, not what assets to buy or how to allocate them.

## What crypto asset management means in a custody context

An organization’s management model describes who can access assets, who may authorize actions, and how those actions are administered. Custody is one part of that model: it concerns the arrangement for controlling access to assets, often through control of private keys. Administration may also involve assigning permissions and setting approval processes. These functions should be defined separately rather than treated as one job.

The phrase “crypto asset management” can mean different things in different organizations or service arrangements. It should not be assumed to mean portfolio management or investment advice. For example, a service that administers access or transactions is performing an operational function; that fact alone does not establish that it makes investment decisions.

## Who controls assets, keys, and approvals

A private key is cryptographic material used to authorize activity associated with an address. In Ethereum, an externally owned account is controlled by the private key corresponding to its cryptographic address. A valid signature can support attribution of key control for a transaction, but it does not identify the person, organization, device, or service that controls the key.

That distinction matters when assigning roles. An organization might identify an asset owner, a custodian or key controller, an operator who prepares an action, and an approver who authorizes it. These are useful governance labels, not a universal standard structure. One party may perform several roles, or responsibilities may be divided among parties.

To understand actual control, examine the documented arrangement and technical permissions. Ask who can produce a valid authorization, who can initiate or approve a transaction, and what conditions govern each action. A contractual label by itself does not establish who technically controls a key or can act on an account.

## Core operating responsibilities beyond custody

Custody answers only part of the operational question. A complete internal model should assign responsibility for maintaining records of assets and movements, reviewing access, authorizing transactions, monitoring activity, and escalating suspected incidents. These are responsibilities to define; the available evidence does not establish that every organization performs them in the same way or under the same requirements.

Recordkeeping and reconciliation require the organization to decide which records it treats as authoritative and how it compares them. Access governance should identify who has permissions and who reviews changes to those permissions. Transaction governance should document who prepares, checks, and approves actions. Monitoring and escalation procedures should state who receives an alert and who is responsible for responding.

Service providers may also have duties under applicable rules. As one example of a bounded international standard, FATF standards expect virtual asset service providers to implement preventive measures that include customer due diligence, record keeping, suspicious-transaction reporting, and originator and beneficiary information handling for applicable transfers. Exact legal duties, thresholds, licensing, data handling, and permitted services depend on how those standards are implemented in a jurisdiction. This example does not establish the obligations of every organization that holds or administers crypto assets.

## Custodial and non-custodial management models

In a custodial arrangement, another party manages access to private keys on behalf of customers. The exact custody structure, customer rights, segregation, insurance, regulation, and insolvency treatment vary by provider and jurisdiction. Organizations should therefore examine the actual agreement and implementation rather than infer protections from the word “custody.”

In a self-custody arrangement, the user controls and is responsible for the private keys and recovery material needed to access the assets. For an organization, that means assigning responsibility for key access and recovery as well as defining who may authorize transactions. Retaining key control does not automatically resolve how approvals, operational access, or continuity should work.

Some arrangements divide control. For instance, one documented wallet model distinguishes end-user-owned wallets from API-key wallets owned and controlled by a developer’s server. This is a provider-specific distinction, not a universal definition of custody. In any shared or delegated arrangement, determine which party can act, what permissions it has, and what approval or recovery conditions apply.

## Controls and risks to assess before defining a model

Before choosing an operating model, map the roles and permissions against the actions the organization expects to perform. The review should cover separation of duties, approval thresholds, access reviews, recordkeeping, and change controls. It should also specify how transaction monitoring and incident escalation fit into the same chain of responsibility.

Examine the security architecture, recovery procedures, incident response process, and dependencies on other parties. A design description is not proof that a control is effective, and no particular architecture should be treated as risk-free on the evidence presented here. Ask what the documentation actually establishes, what it leaves unspecified, and whether claimed outcomes have been independently verified.

The same evidence discipline applies to claims about fees, yields, availability, security, recovery, or compliance. Require current, appropriately scoped documentation before relying on them; do not infer a universal service feature or guaranteed result from a general description. Keep operational requirements distinct from investment decisions, which are outside this explainer’s scope.

## What must be verified for a specific jurisdiction

Licensing, custody classifications, reporting duties, tax treatment, and compliance obligations can depend on jurisdiction and activity. This explainer does not establish the rules for any particular location. Before making a jurisdiction-specific claim or setting policy, obtain current authoritative evidence for the relevant jurisdiction and arrangement, and consult qualified legal, tax, and compliance advisers about the organization’s circumstances.

The practical starting point is a responsibility map: identify who controls keys, who may initiate and approve actions, who maintains records, and who handles monitoring, recovery, and escalation. Then verify the governing agreements, technical permissions, and applicable local requirements. That process defines the organization’s operating model without confusing custody with every other form of crypto asset management.

## Sources and references

- [Virtual Assets](https://www.fatf-gafi.org/en/publications/Virtualassets/Virtual-assets-fatf-standards.html) — Financial Action Task Force; retrieved 2026-10-19.
- [Create and Manage Wallets](https://docs.cdp.coinbase.com/server-wallets/v2/using-the-wallet-api/managing-accounts) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Ethereum accounts](https://ethereum.org/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-19.
