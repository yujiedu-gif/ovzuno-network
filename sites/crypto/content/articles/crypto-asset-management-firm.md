---
title: "Crypto Asset Management Firm: Roles, Wallets, and Custody"
description: "Learn what a crypto asset management firm may do, how wallet and custody roles differ, and which operational questions to clarify before evaluating one."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["wallets_custody"]
tags: []
author: "editorial_team"
primary_keyword: "crypto asset management firm"
owned_question: "What does a crypto asset management firm do, and how do wallet and custody arrangements affect its responsibilities?"
risk_level: "medium"
---

A crypto asset management firm may oversee asset-related operations, but its role does not automatically make it the wallet operator or custodian. To understand its responsibilities, establish who manages access credentials, who can authorize movements, and what the firm’s agreement assigns to each party. Those arrangements vary, so verify them in current technical and contractual documentation rather than relying on the firm’s label.

## What a crypto asset management firm does

“Crypto asset management firm” is not enough, by itself, to establish a specific service or legal role. The firm’s scope may be defined by its agreement with a client and by the systems it uses. The available evidence here does not establish a standard set of asset-management services, so do not assume that every firm provides portfolio administration, execution oversight, custody, or any combination of them.

Separate the functions when evaluating an operating model. **Management** concerns the work the firm agrees to perform for the client. **Wallet operation** concerns the system used to manage key-based access. **Custody** concerns who manages access to private keys on a customer’s behalf. These functions may sit with different parties, and the contract and technical design must show how they fit together.

A firm’s involvement in an asset-related decision does not, on its own, establish that it can access or move the client’s assets. Conversely, a party that manages key access may have an operational role even if it is not described as the asset manager. Treat labels as prompts for investigation, not as proof of control or responsibility.

## How wallets and custody fit into the operating model

A wallet generally manages keys or passcodes used to access and authorize crypto assets; it does not generally store the assets themselves. That distinction matters because an interface used by a firm or client may not be the party that holds or controls the credentials behind it. A wallet provider, asset manager, client, and custodian can therefore have different roles.

In a self-custody arrangement, the user controls and is responsible for the private keys and recovery material needed to access the assets. In a third-party custody arrangement, a custodian manages access to private keys on behalf of customers. The precise structure, customer rights, segregation, insurance, regulation, and insolvency treatment vary by provider and jurisdiction; the arrangement should not be inferred from a generic description such as “secure wallet.”

Some operating models may distribute controls among multiple parties. For example, an arrangement might involve one party proposing a movement and another controlling a credential or approval step. The evidence available here does not define a universal shared-control model or establish how any particular firm implements one. Ask for the exact workflow: which party can initiate, approve, sign, broadcast, pause, or recover access, and under what conditions?

## Who controls keys, approvals, and asset movements?

Map the responsibilities by task, not just by organization name. Cryptographic key management includes lifecycle functions such as generation, storage, distribution, use, recovery, revocation, and destruction. That is a useful checklist for asking what a firm, custodian, client, or technology provider actually handles. It does not establish that a particular party performs any of those functions; the firm’s documentation must do that.

For each movement of assets, ask who can request it, who checks it, who supplies the required authorization, and who carries out the operation. Then ask how permissions are enforced and where records of requests, approvals, and outcomes are available. A firm may coordinate instructions without controlling the relevant keys, while a custodian may manage key access without making the client’s management decisions. The specific division depends on the documented arrangement.

Do not treat a description of security controls as a substitute for a responsibility map. Request evidence that is specific to the claimed control, including which party operates it and what happens when a credential is unavailable, an approval is disputed, or an incident is reported. The available evidence does not establish a universal recovery or incident-response procedure; those terms need to be defined in the provider’s documentation and agreement.

Regulatory and compliance language also needs careful boundaries. International standards for virtual asset service providers include preventive measures such as customer due diligence, record keeping, suspicious-transaction reporting, and handling originator and beneficiary information for applicable transfers. Exact legal duties, thresholds, licensing, data handling, and permitted services depend on how each jurisdiction implements those standards. This does not establish that a particular asset management firm is a service provider under a specific rule, or that it is licensed or compliant. Verify such claims with current, jurisdiction-specific authoritative sources.

## Questions to resolve before assessing a firm

Use a written request for information and compare its answers with the contract and the technical operating description. Questions should make responsibility observable rather than accepting broad assurances.

- **Service scope:** Which tasks does the firm perform, and which does it explicitly exclude? Does its agreement authorize it to direct or execute movements, or only to provide administration or oversight?
- **Custody and access:** Who manages access to private keys? Is the client self-custodial, does a third-party custodian manage access, or are controls divided? What document supports that description?
- **Approvals and records:** Who can initiate and approve a movement? How are permissions applied, and what records can the client obtain to review requests and outcomes?
- **Key lifecycle and recovery:** Who is responsible for generation, storage, use, recovery, revocation, and destruction of key material? What documented steps apply if access is lost or an incident occurs?
- **Providers and dependencies:** Which wallet, custodian, or technology providers participate, and which party is accountable for each operational step? Do not assume that the firm itself supplies every component.
- **Current operational terms:** Request current written evidence for supported assets, service availability, fees, and any other operational conditions relevant to the proposed arrangement. The evidence here does not establish any particular firm’s assets, availability, or fee schedule.
- **Jurisdiction-specific claims:** Ask which legal entity provides each service and where it operates, then verify licensing, compliance, and tax questions with appropriate jurisdiction-specific sources and qualified professionals. This article does not determine legal status, tax treatment, or obligations.

The practical outcome is a responsibility map backed by documents: who manages the service, who manages wallet access, who controls or uses keys, and who is accountable for each operational step. If the firm cannot clearly distinguish those roles, its title alone is not enough to resolve the uncertainty.

## Sources and references

- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
- [Virtual Assets](https://www.fatf-gafi.org/en/publications/Virtualassets/Virtual-assets-fatf-standards.html) — Financial Action Task Force; retrieved 2026-10-19.
