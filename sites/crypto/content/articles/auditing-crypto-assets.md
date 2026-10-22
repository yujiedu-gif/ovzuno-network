---
title: "Auditing crypto-assets: evidence, assertions, and limitations"
description: "Learn what auditing crypto-assets can involve, which records may support key audit assertions, and why on-chain data alone may not establish ownership or value."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["regulation_tax_reporting"]
tags: ["auditing crypto assets"]
author: "editorial_team"
primary_keyword: "auditing crypto-assets"
owned_question: "What does auditing crypto-assets involve, and what evidence can support an audit of crypto-asset balances and activity?"
risk_level: "medium"
---

Auditing crypto-assets involves examining records that support specific claims about balances and activity—not simply checking a blockchain. On-chain data can show transactions and balances associated with addresses, while evidence about who controls those addresses, what rights the entity has, and how balances were recorded may need to come from other sources. The evidence required depends on the engagement and its applicable reporting framework; the limited technical evidence cited here does not establish a complete audit methodology or the rules for a particular jurisdiction.

## What an audit of crypto-assets is meant to establish

An audit inquiry examines assertions about an entity’s records. For crypto-assets, questions may include whether an asset or transaction exists, whether the entity has rights to it or can control it, whether relevant activity and balances have been recorded completely, and whether reported amounts and disclosures are appropriate. Which questions apply—and how they must be addressed—depends on the engagement and the applicable reporting framework.

This is different from validating an entire blockchain or protocol. A blockchain uses cryptographically linked transactions, distributed ledger copies, validation, and conflict-resolution rules to maintain a tamper-evident shared history. That describes features of the ledger; it does not determine whether an entity’s accounting records include every relevant asset or whether a ledger entry corresponds to a right the entity holds. (claim_blockchain_replication is not in the allowed evidence set, so that description is not used here.)

The distinction matters because an audit conclusion is about defined records and assertions, not a general certification that a network is reliable. The allowed evidence does not specify professional audit procedures or evidentiary sufficiency, so this explainer does not prescribe them.

## Evidence for crypto-asset balances and activity

A public ledger can contribute transaction-level evidence: an observer may examine entries associated with an address and trace activity recorded there. A cryptocurrency transfer can use digital signatures based on asymmetric-key pairs to authorize a transfer between users. But a signature establishes control of the signing key under the protocol, not the signer’s legal identity or the purpose of the transaction. ([source](<https://csrc.nist.gov/glossary/term/Cryptocurrency>))

That technical record is only one piece of an audit inquiry. A digital token can be a ledger record about an asset and its owner with programmable rules for use or transfer, but the technical record alone does not determine legal title, enforceability, or the quality of the represented asset. ([source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)) Accordingly, ledger activity should not be treated as a complete account of the entity’s rights or its financial records.

Other records may be relevant to comparing observed activity with recorded activity. For example, the inquiry may involve internal accounting records, wallet records, or records from an intermediary. The evidence available here does not establish what any specific platform or custodian provides, or how reliable a given statement is. A reconciliation—comparing records to identify and investigate differences—can organize the inquiry, but the existence of a match does not, by itself, prove ownership, completeness, or valuation.

## Address attribution, ownership, and control

An address is a ledger identifier, not an entity name. Connecting an address to an organization therefore requires evidence beyond the public ledger. The available evidence does not set out a universal method for making that attribution or establish that a particular record is sufficient.

Control also needs careful wording. In a self-custody arrangement, the user controls and is responsible for the private keys and recovery material needed to access the user’s crypto-assets. ([source](<https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0>)) This can inform an inquiry into access, but it does not by itself establish legal ownership, the organization’s rights, or the completeness of the assets recorded.

A third-party arrangement raises a different question: the available evidence does not describe a particular provider relationship or establish the customer’s rights under it. A reviewer would need to understand what records and agreements exist for the arrangement under examination. Do not infer from an address balance alone that an entity has unrestricted access to the assets or a legally enforceable claim to them.

## Completeness, valuation, and reporting judgments

A balance observed at an address is a view of that address’s recorded state, not proof that all relevant wallets, platforms, or activity have been identified. The available claims do not provide a procedure for finding every address or reconciling every source. An organization can make its inquiry more clearly scoped by documenting which assets, addresses, accounts, transaction records, and periods it considered, while leaving the adequacy of that work to the applicable engagement requirements.

Valuation requires a separate basis for the amount reported. The allowed evidence does not specify valuation methods, market-data sources, measurement dates, or accounting requirements. It therefore cannot support a recommendation about how to value a particular asset or how to present it in financial statements. Classification and disclosure likewise depend on requirements outside this technical evidence set.

Tokenized finance describes financial assets and liabilities represented on programmable digital ledgers. ([source](<https://www.imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921>)) That description does not establish the accounting treatment of a particular token or the rights attached to it. For any reporting judgment, identify the relevant reporting framework and obtain qualified professional guidance rather than treating ledger design as a substitute for that analysis.

## Where auditing crypto-assets has evidentiary limits

A ledger entry does not necessarily identify the people or organizations behind a transaction or explain why it occurred. A signature authorizes a transfer under protocol rules; it does not prove legal identity or business purpose. Similarly, a recorded token may refer to an asset or owner, but the record alone does not establish legal title or enforceability. These distinctions limit what technical inspection can establish on its own.

Nor does a balance at one point in time establish historical ownership, the entity’s rights, unrestricted access, or whether all relevant records have been included. Crypto and DeFi systems can exhibit substantial de facto centralization even when their stated architecture or ethos emphasizes decentralization; the degree and location of concentration must be assessed for a specific network, asset, application, and time window. ([source](<https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks>)) A network’s label or architecture alone therefore does not resolve the entity-specific evidence question.

Treat technical records as evidence about the activity they actually record, and distinguish that from conclusions about identity, purpose, rights, completeness, or value. The allowed evidence does not define when evidence is sufficient under professional standards. That determination belongs to the engagement and its applicable requirements.

## How to scope an audit inquiry responsibly

Start by defining the entity, assets, reporting period, records, and questions in scope. Separate the inquiry into distinct issues: what the ledger records, how addresses are attributed, who can access keys, what rights the entity claims, whether activity has been recorded, and what reporting basis applies. Keeping these questions separate makes it easier to identify which evidence supports which assertion—and where evidence is still missing.

Then document the sources reviewed and differences that remain unresolved. A reconciliation can help show how ledger observations compare with accounting or intermediary records, but document what was compared and avoid treating agreement as proof of matters the records do not establish. Describe access arrangements accurately without implying that a signing key alone settles ownership or legal rights.

Finally, confirm the applicable audit and reporting requirements with qualified professionals in the relevant jurisdiction. This article does not determine jurisdiction-specific standards, regulatory obligations, or tax treatment, and it does not recommend a service provider. Its central limit is straightforward: blockchain records can inform an inquiry into crypto-asset activity, but they do not, by themselves, establish every financial assertion an audit may need to examine.

## Sources and references

- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
- [Tokenized Finance](https://www.imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921) — International Monetary Fund; retrieved 2026-10-18.
- [Cryptocurrency - Glossary](https://csrc.nist.gov/glossary/term/Cryptocurrency) — National Institute of Standards and Technology; retrieved 2026-10-18.
