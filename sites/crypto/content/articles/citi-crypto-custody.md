---
title: "Citi Crypto Custody: Security Controls Institutions Should Assess"
description: "Assess citi crypto custody through institutional control questions on key management, approvals, operational resilience, oversight, and evidence to verify."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "analysis"
topics: ["institutional_crypto_treasury"]
tags: []
author: "editorial_team"
primary_keyword: "citi crypto custody"
owned_question: "What controls should an institution evaluate when assessing the security risks of crypto custody associated with Citi?"
risk_level: "medium"
---

When assessing crypto custody associated with Citi, an institution should first verify the specific service and its scope from current primary documentation, then map who controls keys, authorizes transactions, handles disruptions, and provides evidence for each control. The phrase “Citi crypto custody” alone does not establish that a service exists, who may use it, which assets it supports, or how it operates. This review therefore offers a due-diligence framework, not a claim about a particular Citi offering.

## What the phrase “Citi crypto custody” does—and does not—establish

A search term, discussion, or reference to a financial institution is not proof of a current custody service. Before evaluating security, request primary documentation that identifies the service, its operating model, supported assets and networks, customer eligibility, and relevant service providers. These details are deliberately not assumed here. If current documentation does not establish them, record them as unresolved rather than inferring availability or scope.

The word “custody” also does not specify one uniform allocation of responsibility. In a third-party custody model, a provider manages access to private keys on behalf of customers. Custody structure, customer rights, segregation, insurance, regulation, and insolvency treatment can vary by provider and jurisdiction. The label itself does not resolve those matters. For the arrangement under review, ask what the customer’s rights are, which party performs each function, and what documents define those relationships. [source](<https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0>)

Keep the service question separate from the control question. Even when an institution’s role is documented, that does not by itself explain how transaction authority is divided or what happens during an incident. Conversely, a description of a technology or control does not establish that a named institution offers it. Review the current service materials first; then assess the operating and control details within the scope they actually describe.

## Citi crypto custody due diligence: map the custody and control model

Begin with a role map naming the institution, any custodian, technology providers, and other parties involved in custody operations. For every function, record who performs it, who oversees it, and who can grant, change, or revoke access. Distinguish operational execution from institutional oversight, and do not assume that the same party controls the keys, authorizes a transfer, and handles communications.

A third-party arrangement may involve several organizations. Ask which entity holds or manages access to private keys, which entity provides the customer-facing account or interface, and whether another service provider supports signing, monitoring, or recovery. Identify how each role is defined in current service documentation and contracts. If the documents use broad labels without identifying authority or responsibility, mark the point for clarification.

The distinction matters because a provider’s technical ability to perform a task is not necessarily the same as the institution’s approval of that task. Map separately who can initiate a transaction, who can approve it, who can execute it, and who can stop or escalate it. Document how account permissions and administrative privileges are changed, and who reviews those changes. If a control depends on an outside provider, include that dependency in the review rather than treating the institution’s own procedures as the entire operating model.

For each role, ask:

- Who manages the private keys, and who can access systems or credentials that could initiate signing?
- Who can approve, reject, or release transactions, and how are approval authority and administrative access separated?
- Who can change account permissions, recovery settings, or transaction policies?
- Which party monitors activity and is responsible for escalation and communications?
- What assets, networks, and transaction types are explicitly within the documented scope?

A centralized crypto exchange may combine custody with trading, lending, proprietary activity, or token issuance, but not every operator performs every function. This is a reason to verify roles in the actual arrangement, not to assume that a custody provider performs any of them. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

## Assess key management, approvals, and transaction safeguards

Key management means the protection and lifecycle of cryptographic keying material. The lifecycle includes generation, storage, distribution, use, recovery, revocation, and destruction. Ask which party is responsible at each stage, what policy governs it, and what evidence supports the stated practice. [source](<https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines>)

For key generation and storage, seek documentation that identifies the responsible function and the access rules. For key use, determine how an authorized transaction reaches signing and which roles may request or authorize that action. For recovery, revocation, and destruction, ask what procedures apply and which party is accountable. The purpose is not to infer a particular technical setup; it is to establish whether the institution can explain each stage and its control owner.

Then examine transaction safeguards. Ask how signing authority is granted and reviewed, how privileged access is limited, and what checks apply before a transfer is authorized. Request the approval model, including any separation between transaction request, approval, and execution. Clarify how exceptions are escalated and how suspected unauthorized or erroneous transfers are handled. If documentation does not identify who can approve or initiate a transaction, record that as a control gap rather than presuming a particular safeguard exists.

Evidence should be matched to the claim. A policy or public description can show what a provider says its controls are designed to do; it does not alone establish that the controls operated as described. Separate such materials from contractual commitments, operational attestations, and independent assurance. For each item, record its issuer, date, covered services and systems, exclusions, and whether it describes design or operation. Do not call a control independently verified unless the evidence supports that characterization and covers the relevant service and period.

Finally, identify where the evidence stops. A document may describe one provider, system, or process without covering other parties in the arrangement. A control statement may also leave unanswered who has authority to change the control or respond when it fails. Keep those limits visible in the review record; do not extend a narrowly scoped document into a broader assurance conclusion.

## Evaluate operational resilience and incident response

Ask what happens when ordinary custody operations are disrupted. Request current, scoped documentation about business continuity, disaster recovery, service dependencies, incident escalation, and communications. Identify who owns each action and how the institution is expected to learn that a service, system, or control is unavailable. If several providers are involved, determine how their respective response roles connect.

For suspected key compromise or unauthorized activity, seek the documented escalation sequence, decision authority, and communication responsibilities. Ask which party can suspend or otherwise restrict affected activity, if such a process is described, and how the institution is informed. For incidents involving a network or external service, clarify which party assesses the event and what information is passed to the institution. These are diligence questions, not assertions that any specific control or response capability exists.

Recovery claims need particularly careful wording. Ask what scenarios a recovery procedure covers, which systems and assets it includes, who must participate, and what conditions or dependencies apply. Determine whether the evidence describes a plan, an operational attestation, or an independently assessed capability. A recovery plan does not by itself establish that access will be restored in every scenario, that assets can always be recovered, or that a specific timeline will be met. Preserve those limits rather than turning a process description into a guarantee.

The same distinction applies to continuity documentation. A document can set out intended actions while leaving questions about actual execution, coordination across providers, or the scope of testing unanswered. Record the evidence category and its limitations, and seek clarification where a decision depends on an unverified assumption. Avoid treating a general statement about resilience as proof that every relevant disruption has been addressed.

## Build an evidence-based review and decision record

Use a control register to make the review repeatable and to separate confirmed information from unanswered questions. For each item, record the control question, the requested evidence, its source and date, the service and systems it covers, limitations, and unresolved risk. Keep public disclosures, contractual commitments, audit or assurance materials, and operational attestations distinct; they answer different questions and should not be treated as interchangeable.

A practical register can include these fields:

1. **Service identity and scope:** What current primary documentation identifies the service, its provider roles, and its stated asset, network, and customer scope?
2. **Control ownership:** Who manages key access, permissions, signing authority, transaction approvals, and escalation?
3. **Key lifecycle:** What evidence addresses generation, storage, distribution, use, recovery, revocation, and destruction, and which party owns each stage?
4. **Transaction safeguards:** Who can request, approve, execute, or interrupt activity, and what evidence describes the relevant controls?
5. **Operational response:** What materials cover continuity, dependencies, incidents, and recovery, and what do they not establish?
6. **Evidence limits:** Is each item a disclosure, contractual commitment, operational attestation, or assurance material, and what entities or systems are outside its scope?
7. **Open issues:** Which answers are missing, outdated, ambiguous, or dependent on a party not yet assessed?

A useful decision record does not need to turn every question into a binary pass or fail. It should show what the available evidence supports, what remains uncertain, and what additional documentation or clarification is needed before the institution relies on a control claim. Where a source is incomplete, keep the conclusion narrow and preserve the gap for the appropriate reviewer.

Escalate legal, regulatory, tax, and compliance questions to qualified advisers for the relevant jurisdictions; this technical control review does not resolve them. Revisit the record when the documented service scope, counterparties, technology, or institutional requirements change. The outcome should be a traceable assessment of responsibilities and evidence—not an assumption that a named institution provides a particular service or that any custody arrangement eliminates risk.

## Sources and references

- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
