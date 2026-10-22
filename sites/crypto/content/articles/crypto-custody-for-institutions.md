---
title: "Crypto custody for institutions: assessing control risks"
description: "Assess crypto custody for institutions through governance, key management, transaction controls, recovery planning, and evidence needs for risk review."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "analysis"
topics: ["institutional_crypto_treasury"]
tags: ["crypto custody institutions"]
author: "editorial_team"
primary_keyword: "crypto custody for institutions"
owned_question: "Which governance and operational controls should an institution assess when designing or reviewing crypto custody?"
risk_level: "high"
---

For an institutional custody review, document who governs access, who authorizes transactions, how signing keys are managed, and who directs recovery and incident response. Assess those controls against current, arrangement-specific evidence; do not treat a policy statement or general security assurance as proof that a control works. The available evidence for this article is limited, so it cannot establish legal, tax, or compliance requirements for a particular institution or validate any custody provider’s security or service commitments.

## Define the custody arrangement and its control boundaries

Begin by setting the review’s scope: identify the assets, networks, parties, systems, and operational processes involved. Map who controls access, approves transactions, executes them, maintains records, monitors activity, and handles exceptions. Do not assume that these responsibilities belong to one party or follow a standard custody model; establish the boundaries from the arrangement’s own documentation.

Keep four responsibilities distinct:

- **Access:** Who can use credentials or mechanisms that enable a transaction?
- **Authorization:** Who decides that a transaction is permitted, and how is that decision recorded?
- **Execution:** Which person, system, or service signs and submits the transaction?
- **Oversight:** Who monitors activity, reconciles records, and responds to exceptions?

A valid signature can support the conclusion that a transaction was authorized using the private key corresponding to an Ethereum externally owned account. It does not, by itself, identify the human, organization, device, or service controlling that key. A review should therefore connect technical evidence to documented roles and procedures rather than treating an address or signature as proof of organizational accountability.

List dependencies as well as direct responsibilities. An arrangement can involve internal teams, outside services, network infrastructure, and separate recordkeeping or monitoring tools. For each dependency, note what current documentation supports and what remains unknown. This creates a bounded review rather than a provider comparison or a general claim that custody is safe.

The evidence available here does not establish the assets or networks used by any particular institution, nor does it describe a specific provider’s operating model. Record those details from the arrangement under review. If a party’s role, authority, or dependency cannot be established from current materials, mark it as an open question instead of inferring an answer.

## Crypto custody institutions should review governance and access

Governance defines who may grant, change, approve, and revoke access. Document control owners, decision authority, approval thresholds, and any separation of duties. Then trace the access process: who requests a change, who approves it, who implements it, and where the change is recorded and reviewed.

Ask for evidence covering both routine and exception paths. Determine how the arrangement handles an unavailable approver, a disputed request, suspected credential exposure, or a request that falls outside the normal workflow. These are prompts for assessing whether decision authority and escalation paths are defined; they do not prescribe a single workflow for every institution.

A control inventory makes findings usable. For each control, record its owner, purpose, relevant system or process, evidence reviewed, review date, and unresolved gaps. Distinguish documented design from evidence of operation: a policy may describe an approval workflow without demonstrating that a particular transaction followed it.

Review access changes and removal as well as initial access. Ask how role changes are recorded, how access that is no longer needed is identified, and how exceptions are handled. If the materials do not explain these processes, record an evidence gap. Do not conclude that a control exists merely because it would be a reasonable practice.

## Assess key management and transaction safeguards

Key management is the protection and lifecycle handling of cryptographic key material, including its generation, storage, distribution, use, recovery, revocation, and destruction. For each key or signing mechanism in scope, request current, appropriately scoped documentation showing which party performs each function and what evidence supports the description. A broad statement such as “keys are secure” does not explain these responsibilities or prove how they operate.

Trace transaction authorization from request through completion. Record who initiates a transaction, who reviews its details, who approves it, and what mechanism authorizes it. Where the arrangement uses transaction limits, address restrictions, allowlists, or monitoring, request documentation that explains how each control is configured, changed, and reviewed. These examples are review questions, not a claim that any particular custody arrangement includes such controls.

Separate custody controls from protocol behavior. A blockchain or application can process transactions under technical rules, but that does not establish who inside an institution approved a transaction or whether internal procedures were followed. For example, an AMM-based decentralized exchange can implement trading through smart contracts and liquidity pools, with transactions settling when included in a blockchain block. That describes one trading model; it does not verify an institution’s authorization process or its custody controls. ([source](<https://www.bis.org/publ/work1227.pdf>))

Security evidence needs clear limits. Record the document’s date, scope, system, service, and operating process. Note whether it describes a design, an operating procedure, or evidence of operation. Do not expand a limited statement into a guarantee, or claim independent validation, testing, or certification unless the evidence specifically supports that conclusion. The supplied evidence does not validate the security of a particular provider or institutional arrangement.

## Test recovery, continuity, and incident readiness

Recovery planning should identify who has decision authority, who performs each step, which dependencies must be available, and how affected teams receive information. Review documented procedures for loss of access, suspected key compromise, service disruption, and other interruptions relevant to the arrangement. The available evidence does not establish that a specific institution or provider has a working recovery capability; conclusions must rely on current documentation for that arrangement.

For incident readiness, locate the escalation path, responsible roles, decision points, and communications procedures. Clarify how the institution classifies a suspected incident, who coordinates response, and who has authority to restrict activity if the arrangement allows it. These questions help expose gaps; they do not establish that a particular service offers a pause, recovery, or escalation capability.

A documented procedure is not proof that it has been rehearsed or will succeed. If evidence of a review or exercise exists, record its date, scope, participants, issues identified, and follow-up actions. If no evidence is available, state that limitation plainly. Do not imply an exercise occurred or that recovery is assured.

Include dependencies and handoffs in the record. An institution may rely on different teams or services for access, approval, execution, records, or communications, and a recovery procedure should make those responsibilities legible. If the documentation does not identify who makes a decision when a dependency is unavailable, capture that as an unresolved ownership or continuity question, not as evidence that the process will fail or succeed.

## Validate legal, compliance, and service-specific assumptions

Keep operational control review separate from jurisdiction-specific conclusions. Before stating that a legal, regulatory, tax, or compliance requirement applies, obtain current authoritative materials and qualified review for the relevant jurisdiction and facts. The evidence available here does not support a legal or tax conclusion, a universal compliance checklist, or a claim that a particular control satisfies an obligation.

Verify service-specific claims against current documentation before relying on them. This includes availability, fees, recovery terms, support arrangements, and operational commitments. Record the source and date, and flag items for re-verification when they may change. A general description of a technical model does not establish a provider’s current terms or performance.

Close with a decision-ready record: controls documented, evidence examined, accountable owners, dependencies, unanswered questions, and follow-up assigned to security, operations, legal, tax, or compliance reviewers as appropriate. The result should be a scoped account of what the institution can verify and what remains uncertain—not a blanket judgment that custody is safe. When evidence is missing or too narrow, retain that uncertainty and identify what documentation or qualified review would be needed to address it.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
