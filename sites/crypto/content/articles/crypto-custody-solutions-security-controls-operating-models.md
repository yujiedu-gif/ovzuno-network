---
title: "Crypto Custody Solutions: Security Controls and Operating Models to Evaluate"
description: "A neutral guide to comparing crypto custody operating models and assessing key management, transaction controls, resilience, and evidence before making an informed,1"
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["wallets_custody"]
tags: ["institutional crypto custody", "digital asset custody models", "crypto custody security controls", "self-custody and third-party custody"]
author: "editorial_team"
primary_keyword: "crypto custody solutions"
owned_question: "What security controls and operating models should institutions evaluate when choosing crypto custody solutions?"
risk_level: "high"
---

# How Institutions Should Evaluate Crypto Custody Solutions

Choosing among crypto custody solutions is a requirements-and-evidence exercise, not a choice of technology label. Institutions should define the operations and threat assumptions they need to address, map who controls keys and transactions, and verify relevant safeguards against current documentation and testing. The appropriate comparison depends on the institution’s assets, workflows, responsibilities, and dependencies. This guide offers an evaluation framework; it does not recommend a provider or imply that any arrangement guarantees protection.

## Start with custody requirements and threat assumptions

Begin by describing the activity the custody arrangement must support. List the assets and networks in scope, transaction types, and expected operational volumes. Identify whether the institution expects routine transfers, occasional high-value movements, or workflows with multiple internal teams. These are requirements to verify against current, relevant documentation, not capabilities to infer from a broad service description. If a required asset, network, or transaction type is not documented clearly, record that as an open question rather than assuming compatibility.

Next, map a representative transaction from request to recordkeeping. Identify who initiates it, who reviews its purpose and details, who approves it, who authorizes signing, who executes or broadcasts it, and who monitors completion and reconciles the resulting records. These roles may be held by different people or organizations. The map should expose handoffs: for example, whether an internal approver relies on information supplied by another team, and whether a custody operator can execute an action without a separate approval. The point is to establish the actual path and decision authority, not merely to count approval steps.

Write down threat assumptions in operational terms. Include insider misuse, credential compromise, operational error, and service disruption. For each scenario, ask which part of the workflow could be affected, what control is expected to reduce exposure, who operates that control, and what evidence could demonstrate that it works as described. This does not require predicting every event. It makes the evaluation testable and helps distinguish a required safeguard from a preferred feature.

A wallet generally handles private keys or passcodes used to access and authorize crypto assets rather than storing the assets themselves. This technical explanation appears in an SEC staff investor bulletin; it is not a Commission rule, regulation, or legal determination. (claim_sec_wallet_not_assets) That distinction is useful when describing requirements: assess the management of access and authorization material, along with the operational arrangements around it, rather than treating a wallet label as a complete account of custody.

## Compare custody operating models

Compare operating models through responsibility boundaries. The labels “self-custody,” “third-party custody,” and “hybrid” are starting points; they do not, by themselves, establish who can take each action or how an institution retains access during disruption.

| Evaluation dimension | Questions to resolve |
|---|---|
| Key control | Who controls signing keys or access to them? Which people or systems can cause a signature to be produced? |
| Authorization | Who may request, approve, change, or override transaction policy? Are approval authority and execution authority distinct? |
| Workflow | Who reviews transaction details, signs, broadcasts, monitors, and reconciles? Where are the handoffs? |
| Operational responsibility | Which party maintains each process, handles errors, and responds to service interruption? |
| Dependencies | Which providers, people, software, infrastructure, subcontractors, and recovery processes are necessary for routine operation or recovery? |
| Disruption and exit | What access, records, responsibilities, and dependencies apply during an outage or contract termination? |

In a self-custody model, the user controls and is responsible for the private keys and recovery material needed to access the user’s crypto assets. Wallet designs can use seed phrases, hardware devices, multisignature arrangements, threshold signing, or other recovery models. (claim_sec_self_custody_responsibility) For an institutional assessment, translate that responsibility into operating questions: which internal roles can access or use relevant material, how duties are assigned, and which people and processes must be available to carry out approved operations. The model places responsibility with the user as described in the source; it does not by itself specify an institution’s internal controls or prove that a particular implementation is suitable.

In a third-party custody model, a custodian manages access to private keys on customers’ behalf; crypto exchanges are among the possible third-party custodians. Custody structure, customer rights, segregation, insurance, regulation, and insolvency treatment vary by provider and jurisdiction. (claim_sec_third_party_custody) Accordingly, ask which actions the custodian performs and which remain with the institution. Review current documentation for responsibility boundaries and do not infer segregation, insurance, regulatory status, or treatment in an insolvency from the general label. Questions about legal rights or jurisdiction-specific treatment require qualified advice and current authoritative evidence.

A hybrid arrangement may divide responsibilities across the institution and one or more external parties. Map each relevant key or access mechanism, authorization step, and operational dependency to a named responsible party. Then trace what happens if one participant, system, or service is unavailable. A division of duties can create additional handoffs and dependencies; do not assume that splitting control automatically removes recovery or concentration risks. The useful comparison is the concrete workflow and its responsibilities, not a model name in isolation.

## Evaluate key management and access controls

Review the key-management lifecycle as a sequence of functions: generation, storage, distribution, use, recovery, revocation, and destruction. NIST’s general key-management guidance covers these lifecycle functions. Blockchain-specific roles, regulations, custody models, and cryptographic modules require a separate risk assessment. (claim_key_management_lifecycle) The lifecycle gives evaluators a structure for finding gaps: a description of secure storage, for example, does not answer how material is generated, who can use it, or how access is revoked when responsibilities change.

For each lifecycle function, request an explanation of the process, the responsible role, and the evidence available to verify it. Useful questions include:

- **Generation:** What documented process governs generation, and who is permitted to initiate or oversee it?
- **Storage and distribution:** Where is keying material held or made available for use, and which people, systems, or services can access it? What dependencies are involved?
- **Use:** What process connects an approved transaction to signing authority? Which roles or systems participate, and what prevents an undocumented change in authority?
- **Recovery:** What procedures and material are required, who is responsible, and what testing evidence shows that the documented process has been exercised?
- **Revocation and destruction:** How are obsolete or no-longer-authorized material and access handled, and what records document completion?

These questions seek process evidence, not secret values or unnecessary exposure of sensitive material. Request architecture and policy descriptions that explain boundaries without asking an organization to disclose confidential key material. Evaluate identity controls, least privilege, separation of duties, and privileged-access monitoring as controls to verify. Ask how access is granted, changed, reviewed, and removed, and who reviews relevant activity. A technology label or general assurance statement is not proof that controls are appropriately configured or consistently operated.

Also examine how signing authority is distributed and how changes to that distribution are approved. Ask who can propose a policy change, who can authorize it, how the change is recorded, and what review occurs afterward. The exact design will vary; the evaluation should establish whether authority and change control fit the institution’s threat assumptions and workflow, rather than presume that any named method provides a particular level of protection.

## Assess transaction authorization and operational safeguards

Trace a transaction through review, authorization, signing, broadcast, and reconciliation. At each stage, identify the responsible person or system, the information checked, and the record produced. This makes it easier to locate ambiguous handoffs—for example, when the party that checks transaction details is also able to approve the same action, or when responsibility for monitoring completion is not assigned.

Evaluate documented controls such as approval thresholds, dual control, allowlists, limits, and exception handling where applicable. Ask what the control applies to, who can configure or change it, how exceptions are authorized, and where the resulting activity is recorded. Do not assume that a control’s presence in a feature list establishes its scope or operation. Compare the documented configuration and workflow with the institution’s own requirements.

Give special attention to changes that can alter future transaction behavior. Ask how address changes and policy updates are requested, reviewed, and approved; whether the relevant authority is distinct from routine transaction execution; and how changes are communicated to affected operators. For emergency actions, clarify who can invoke them, under what documented conditions, and how the action is logged and subsequently reviewed. For suspicious activity escalation, identify the reporting path, the receiving role, and how the institution will know that an issue has been acknowledged and addressed.

Request evidence of testing and review for transaction safeguards. Questions may include: which workflows were tested, when, what the test covered, what issues were recorded, and whether remediation remains open. Ask how overrides are logged and who examines those records. If testing evidence does not cover a workflow or condition the institution considers material, record the coverage gap; avoid treating an untested control as verified.

## Test resilience, recovery, and incident readiness

Review backup and restoration procedures, role succession, and the people, systems, and services on which recovery depends. Ask what the documented process is intended to restore: access, an operational role, a system function, or another part of the workflow. Identify prerequisites and dependencies, and clarify who is responsible for each action. A procedure is easier to evaluate when its steps, responsible parties, and evidence of completion are explicit.

Examine incident notification, escalation, containment, and communications processes. Ask who can report an incident, who receives the report, how escalation proceeds, and what information is shared with the institution. Where a service or external party is involved, clarify the responsibility boundary and dependency rather than assuming that one party handles every response task. The source claims do not establish a universal notification timetable or service commitment; assess any such commitment in current applicable documents.

Request evidence of exercises or independent testing, including scope, date, findings, and remediation status. Determine whether the evidence relates to the relevant workflows and dependencies, or only to a narrower component. An exercise can show that a process was tested within a stated scope; it cannot, by itself, establish that every future incident or recovery will succeed. Treat resilience as a set of arrangements and test results to inspect, not a promise that access or assets can always be recovered.

## Request evidence and scrutinize assurance claims

Evidence should match the claim being evaluated. Request current, relevant independent assurance reports and examine their scope, exclusions, coverage period, and remediation status. Ask which processes, systems, and responsibilities were covered, and note any parts of the institution’s intended workflow that fall outside that scope. A report with a different scope or period may not answer the specific question at hand.

Where available, review penetration-testing summaries and remediation information without treating testing as a guarantee. Ask for documented policies, control ownership, subcontractor dependencies, and material exceptions. For each item, record the date, scope, relevant operating model, and unresolved limitations. If the information is unavailable, incomplete, or too general to support the claim, describe that as an evidence gap rather than filling it with an assumption.

For statements about insurance, security, or service availability, request current documents and review their precise terms before relying on them. Do not infer coverage, responsibilities, or guarantees from a headline or general claim. Current contracts and policy terms matter for responsibility boundaries, subcontractors, insurance, service levels, and termination. The available claims here do not establish the terms of any particular provider, policy, or service; verify the documents relevant to the arrangement under consideration.

## Use a decision matrix and record unresolved risks

Define criteria before comparing alternatives. A practical matrix can assess operating fit, control evidence, resilience, integration requirements, and dependency concentration. Use consistent questions for each model or proposal, while allowing a criterion to be marked not applicable only with an explanation. One simple record can include the criterion, requirement, evidence reviewed, scope and date of that evidence, observed gap, proposed mitigation, accountable owner, and next review date.

For example, if an institution requires a defined transaction approval path, the record should identify the expected initiator, approver, signer, and monitor; the documentation that describes each role; and any unresolved ambiguity. If a recovery process depends on an external service, record that dependency and the evidence available about the process, rather than scoring resilience solely from a general assurance statement. These examples illustrate how to make the comparison auditable; they do not assert that a particular control design or provider is preferable.

Keep facts, assumptions, and judgments distinct. A documented control is not necessarily independently tested; an assurance report may cover only a limited scope; and a test result may have findings awaiting remediation. Record what was verified, what was not covered, and why an open issue is accepted, mitigated, or escalated. Avoid treating a missing document as proof that a control is absent, but do not treat an unsupported claim as equivalent to evidence.

Before selection, resolve or explicitly accept outstanding questions about responsibilities, dependencies, recovery limitations, and control exceptions. Escalate legal, regulatory, tax, insurance, and jurisdiction-specific questions to qualified advisers using current authoritative evidence; this guide does not determine requirements in any jurisdiction. Reassess the evaluation after material changes to assets, workflows, providers, or threat assumptions. A useful decision record states what was verified, what remains uncertain, who owns each open issue, and when it will be reviewed. This supports a requirements-based comparison without suggesting that a custody model or control set eliminates risk.

## Sources and references

- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
