---
title: "Crypto custody: institutional controls for treasury risk assessment"
description: "Assess crypto custody controls for institutional treasury operations, including key governance, transaction authorization, continuity planning, and oversight."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "analysis"
topics: ["institutional_crypto_treasury"]
tags: []
author: "editorial_team"
primary_keyword: "crypto custody"
owned_question: "What controls should an institutional treasury assess when designing and overseeing crypto custody?"
risk_level: "high"
---

Institutional treasury teams assessing crypto custody should identify who controls signing credentials, who can authorize transactions, how key material is managed, and which activities depend on external parties. These are separate control questions: a custody arrangement alone does not establish who may initiate or approve activity, what recovery is possible, or how responsibilities are divided.

## Crypto custody in an institutional treasury context

For this operational assessment, custody refers to the arrangements through which an organization controls access to the keys used to authorize crypto-asset activity, alongside the governance and service relationships around that control. This is not a universal legal definition. The assessment should identify the actual arrangements without deciding their legal status.

Start by defining what is in scope: assets, networks, organizational entities, accounts or addresses, systems, and transaction flows. Record which credentials can authorize activity and which people, systems, or external parties can access them. This inventory is a map for the control review, not proof that the institution has established legal ownership or complete control over every asset.

Distinguish key control from account use. In a centralized exchange model, customers typically transfer assets into the exchange’s custody before trading through its internal system, although some venues and products use different custody, brokerage, or settlement arrangements. An exchange account relationship should therefore be documented separately from any assumption about direct control of signing keys. The description is a general operating model, not a rule for every venue. [source](<https://www.bis.org/publ/work1227.pdf>)

The review should also distinguish institutional activities from service-provider functions. A centralized exchange operator may combine trading, proprietary activity, lending, token issuance, and custody, but not every operator performs all those functions. Map which functions are relevant to the institution’s arrangement instead of inferring them from a product label. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

## Map key control and transaction authority

Use the key-management lifecycle to organize questions about credentials. Key management covers protection and lifecycle functions including generation, storage, distribution, use, recovery, revocation, and destruction. For each function, identify the responsible organizational role or service, the permitted actions, and the evidence available to show how those actions are governed. The lifecycle is a framework for assessment, not evidence that any particular control is effective. [source](<https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines>)

For each lifecycle stage, ask:

- **Generation:** Who or what generates signing keys, and which documented procedure governs the activity?
- **Storage and access:** Where is keying material protected, who can access or use it, and how are permissions reviewed and changed?
- **Distribution and use:** Which people or systems can request or perform signing, and what records connect those actions to authorized instructions?
- **Recovery and revocation:** What assumptions apply if access is lost, compromised, or no longer authorized? Who can request or approve a change, and how is it recorded?
- **Destruction:** How is obsolete or revoked keying material handled, and what evidence records the change?

Map transaction authority separately from key administration. Identify who initiates instructions, who approves them, who performs signing, and who reviews the resulting activity. Where the operating model permits, assess whether these roles are separated. If duties are combined, document the reason, any additional review, and the accountable owner. This is a control-design assessment, not a claim that a particular role structure is universally required.

Record transaction limits, approval thresholds, and exception paths in the institution’s control materials. Then compare the documented design with available evidence, such as access records, approval records, and change logs. A policy describes intended controls; it does not by itself demonstrate that a control operated as intended. Record that distinction when identifying gaps.

## Test operational resilience and incident readiness

Review how the institution would make decisions if authorized personnel, systems, or an external service became unavailable. Identify escalation responsibility, decision authority for urgent actions, communication roles, and the records expected after an incident. These questions help expose dependencies without assuming that a contingency plan will succeed.

Make continuity assumptions explicit. List the people, systems, credentials, and external parties on which each process depends. For every stated fallback or recovery path, record what evidence supports the assumption and what conditions would need to be met. If a process depends on a provider or designated personnel, identify that dependency rather than describing recovery as automatic.

Recovery is a lifecycle function to assess, not a guaranteed outcome. The key-management framework includes recovery, but it does not establish that a specific institution can recover particular credentials or assets. Do not treat a written plan, a service description, or the presence of backup material as proof of recoverability. [source](<https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines>)

Track incidents, control exceptions, and remediation with accountable owners. If evidence of an exercise or other validation is unavailable, record the limitation rather than implying that a test occurred or that continuity has been demonstrated. This review should describe evidence actually available to the institution, not invent outcomes.

## Oversee external custody dependencies

Map which custody-related activities are handled internally and which rely on external parties. For each dependency, identify the service involved, the institution’s relevant responsibility, and the evidence needed for oversight. Where an exchange combines custody with other functions, consider those functions in the dependency map; their combination can create operational dependencies or conflicts, but the exact implications require review of the arrangement. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Review current contracts and service documentation for how responsibilities are described and what records or control evidence are available. Note the scope and date of materials reviewed. Distinguish a provider’s assertion from evidence the institution has independently examined; neither a product description nor a general industry model establishes the terms of a particular arrangement.

Set an oversight process for reassessing external dependencies when contracts, services, control materials, or institutional use change. Assign an owner for monitoring and escalation. Before relying on statements about availability, security measures, fees, or exit arrangements, verify them against current authoritative documentation specific to the service. The evidence in this article does not establish those details for any provider.

Treat exit planning as a dependency review, not proof that assets, credentials, or operations can be transferred on a particular schedule. Record assumptions, required decisions, and unresolved questions so they can be reviewed with the relevant parties. Do not turn an unverified continuity assumption into a promise of access or recovery.

## Build a reviewable custody control record

Maintain a record linking each in-scope asset and workflow to key-management responsibilities, transaction-authority roles, continuity dependencies, external services, evidence reviewed, identified gaps, and accountable owners. Record decisions and reassessment dates so future reviewers can understand what was considered and what remains uncertain. Such a record supports review; it is not a certification or guarantee.

A practical review sequence is:

1. Define the assets, entities, accounts, systems, and transaction flows in scope.
2. Map key lifecycle responsibilities separately from transaction initiation, approval, and execution.
3. Identify continuity dependencies and the evidence supporting each recovery assumption.
4. Compare external-party responsibilities with current contracts and service documentation.
5. Record gaps, decisions, owners, and reassessment dates; escalate jurisdiction-specific legal, regulatory, tax, or compliance questions to qualified advisers and authoritative sources.

The resulting assessment should make control ownership and uncertainty visible. It should not imply that custody risk has been eliminated, that any provider is suitable, or that legal, tax, or regulatory treatment has been determined.

## Sources and references

- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
