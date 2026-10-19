---
title: "What Are Tokenized Assets? Tokens, Records, and Legal Rights"
description: "Understand how tokenized assets represent financial or real-world rights, how native, custodial, and synthetic models differ, and what holders must verify."
date: "2026-10-18"
draft: false
content_type: "definition"
topics: ["tokenization-rwa"]
tags: ["what are tokenized assets", "asset tokenization", "tokenized real world assets", "tokenized securities", "digital representation of assets"]
author: "editorial_team"
primary_keyword: "tokenized assets"
owned_question: "What are tokenized assets, and what relationship exists between the token and the underlying rights?"
risk_level: "high"
---

Tokenized assets are digital tokens that record or represent rights connected to a financial, physical, or intangible asset on a programmable ledger. The represented item might be a bond, fund interest, bank deposit, commodity, invoice, property interest, intellectual-property licence, or another claim.

The critical word is *represent*. Possessing a token does not automatically prove legal ownership of the referenced asset. The token's meaning comes from its issuance structure, governing documents, authoritative ownership records, custody arrangements, redemption terms, and applicable law. Two tokens referring to the same asset can give holders materially different rights.

## A token is a record, not automatic ownership

The CPMI describes digital tokens as ledger entries that can contain information about an asset and its owners and can also contain programmable rules governing use. This combines record-keeping with executable logic, but technology cannot create a missing legal relationship.

A useful tokenized-asset definition has three parts:

1. **The token:** the blockchain or DLT record controlled through keys and protocol rules.
2. **The represented interest:** ownership, a security entitlement, a contractual payment claim, redemption right, licence, receipt, or synthetic exposure.
3. **The legal and operational bridge:** the issuer, custodian, registry, contract, oracle, and procedures that make changes to the token correspond to changes in the represented interest.

If the bridge is incomplete, transferring the token may move only a digital record. It may not transfer title to property, voting rights, income, possession, or an enforceable claim.

## The main tokenization models

In a **native or issuer-sponsored model**, the issuer creates the asset in token form. The ledger may be part of the authoritative holder register, so a valid token transfer updates ownership under the governing arrangement. A tokenized bond issued directly by its obligor can use this structure.

An issuer can also keep the legally authoritative register offchain. The token transfer then acts as an instruction or notice, and the issuer or transfer agent updates the master record. The SEC staff's 2026 tokenized-securities statement distinguishes these models and emphasizes that transfer mechanics and holder rights depend on the structure.

In a **custodial or wrapped model**, a third party holds an underlying asset and issues tokens representing a direct or indirect entitlement to it. The holder depends on the custodian, segregation of assets, reconciliation, and redemption process. A one-to-one marketing claim does not explain whether the holder owns the asset, owns a security entitlement, or is merely an unsecured creditor.

In a **synthetic model**, the token promises payments linked to the price or performance of a reference asset without giving the holder ownership of that asset. The issuer's credit, collateral, calculation method, and contractual terms become central. The SEC staff notes that third-party tokenized securities can confer rights materially different from direct ownership and can add counterparty or bankruptcy exposure.

## How a tokenized asset is created and maintained

A credible arrangement begins by identifying and verifying the asset or obligation. The issuer then defines the holder's rights, selects the authoritative record, appoints any custodian or administrator, and establishes eligibility and transfer rules. Tokens are minted only after the required asset, claim, or liability exists under that framework.

Ongoing operation can require:

- reconciliation between token supply and custody or registry records;
- processing income, interest, voting, splits, maturities, or other asset events;
- enforcing identity, jurisdiction, transfer, or holding restrictions;
- updating valuations or offchain facts through approved data sources;
- redeeming tokens for cash, the underlying asset, or another entitlement; and
- burning or locking tokens when the represented claim ends.

A smart contract can automate instructions, but it cannot independently verify that a building exists, a custodian still holds a bond, or an issuer can meet its obligations. Those facts require legal accountability and reliable offchain evidence.

## What an onchain transfer changes

An onchain transaction proves that the ledger changed under its technical rules. What that change means legally depends on which record the governing framework recognizes.

When the ledger is the master ownership record and legal requirements are satisfied, token transfer can transfer the relevant security or entitlement. When an offchain register remains authoritative, the token transaction may only instruct an issuer or agent to update that register. A failed reconciliation can leave the onchain and legal records inconsistent.

For physical assets, a token transfer may represent a contractual claim to delivery rather than transfer possession or registered title. Property, commodities, invoices, and licences follow different laws and registries. The applicable jurisdiction, conflict-of-law rules, and insolvency treatment must be identified.

Blockchain finality is also not identical to legal settlement finality. A technically final transaction can still face fraud claims, court orders, invalid issuance, registry conflicts, or contractual disputes. Conversely, a legally effective transfer may depend on an offchain step completed after the token moves.

## Programmability and settlement

Tokenization can place asset records and transfer logic on a programmable platform. A contract can condition delivery on payment, restrict transfers to eligible addresses, distribute cash flows, or combine several actions. The IMF describes financial tokenization as representing assets and liabilities on programmable digital ledgers.

Delivery-versus-payment can reduce principal risk when the asset and payment legs complete together. Achieving that outcome still requires a reliable settlement asset, compatible ledgers, valid legal transfer, sufficient liquidity, and code that handles failure correctly. A transaction that is atomic in software may depend on a custodian, bank, oracle, bridge, or registry outside the atomic boundary.

Programmability can also increase operational complexity. Upgrade keys, administrator roles, identity lists, oracle controls, cybersecurity, privacy, and interoperability become part of the asset's risk model.

## Rights and risks to verify

Before treating a token as an asset or an ownership record, verify:

- **Issuer:** Who created the token, and who owes each obligation?
- **Right:** Does the holder receive title, an entitlement, redemption, income, voting, delivery, or only price exposure?
- **Authoritative record:** Is ownership determined onchain, offchain, or by reconciling both?
- **Underlying asset:** Does it exist, who verifies it, and can it be pledged, sold, or tokenized elsewhere?
- **Custody:** Who holds the asset, how is it segregated, and what happens in insolvency?
- **Supply:** What permits minting and burning, and who controls those functions?
- **Transfer:** Which addresses are eligible, and can transfers be paused, frozen, reversed, or rejected?
- **Redemption:** What can the holder receive, on what timetable, at what cost, and under which restrictions?
- **Asset events:** How are income, voting, maturities, defaults, and corporate actions passed through?
- **Technology:** Which ledger, contracts, administrators, oracles, bridges, and upgrade mechanisms are required?
- **Law:** Which jurisdiction and documents establish enforceability, title, settlement finality, and remedies?

The CPMI has emphasized that an asset-backed token needs clear answers about what or whom the holder has a claim against and how the backing relates to that right. That question is more important than whether a dashboard displays a token balance.

Tokenized assets can make records and transfer rules programmable, but the token is only one layer. The full asset consists of the ledger entry plus the enforceable rights, authoritative records, custody, governance, redemption process, and legal framework that give the entry meaning.

## Sources and references

- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-18.
- [Statement on Tokenized Securities](https://www.sec.gov/newsroom/speeches-statements/corp-fin-statement-tokenized-securities-012826-statement-tokenized-securities) — U.S. Securities and Exchange Commission staff divisions; retrieved 2026-10-18.
- [Wholesale Digital Tokens](https://www.bis.org/publications/wholesale-digital-tokens) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-18.
- [Tokenized Finance](https://www.imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921) — International Monetary Fund; retrieved 2026-10-18.
