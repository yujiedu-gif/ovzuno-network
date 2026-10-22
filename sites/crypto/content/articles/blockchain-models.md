---
title: "Blockchain models: a guide to access, control, and visibility"
description: "Compare blockchain models by access, validation, governance, and transaction visibility, and see why public, private, permissionless, and permissioned labels can"
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "blockchain models"
owned_question: "What are the main blockchain models, and how do their access rules, control, and transaction visibility differ?"
risk_level: "medium"
---

Public, private, permissionless, and permissioned describe different aspects of blockchain participation—not four mutually exclusive types. To compare blockchain models, assess separately who can read data, submit transactions, validate activity, and change or govern the network. Those rules, along with the network’s data-visibility design, matter more than its label alone.

## What the term blockchain model describes

A blockchain model is the set of rules and arrangements that governs access, participation, validation, and control within a network. It describes how that network is organized; it does not, by itself, tell you whether a particular product or payment service is available, suitable, or operated in a particular way.

A useful comparison separates four questions:

- **Access:** Who can read the network’s data, connect to it, or use its services?
- **Participation:** Who can submit transactions or take part in maintaining the network?
- **Governance:** Who sets the rules and coordinates changes?
- **Visibility:** What transaction information can different participants see?

These dimensions can be combined in different ways. In particular, the ability to read information is not the same as permission to submit transactions or validate activity. For example, Ethereum full nodes independently verify blocks and transactions against protocol rules; that role describes validation, not by itself who can access an application or how its data is presented.

## Public and private describe who can access the network

**Public** generally indicates that network access or information is open beyond a designated group, subject to the network’s actual rules. The label alone does not establish that every person can perform every action. A network may permit broad reading while applying separate rules to transaction submission or validation.

**Private** indicates that access is restricted through an operator or governing arrangement. The restriction might concern reading, submitting transactions, participating in validation, or some combination. “Private” should therefore prompt a follow-up question: private for which activity, and controlled by whom?

Reading, transaction submission, and validation should be checked separately. A network can expose some records broadly but limit who may submit transactions. It can also allow a broader set of users to interact while limiting validation to designated participants. The access label alone does not resolve those distinctions.

Visibility is another separate question. Do not infer that a network is confidential merely because access is restricted, or that all information is visible merely because a network is public. The model’s documented data-handling rules determine what is visible and to whom; the label is not a complete description of those rules.

## Permissionless and permissioned describe participation rules

**Permissionless** describes participation that does not require approval from a designated gatekeeper for the relevant network role. It does not necessarily mean that every participant has identical capabilities, or that applications built on the network have no access controls.

**Permissioned** describes participation that requires authorization, credentials, or approval under the network’s rules. Permission can apply to different roles, including reading, submitting transactions, validating, or administering. A permissioned design does not, on its own, identify whether one operator or multiple organizations control the network.

These terms are often used as shorthand for who may help maintain a ledger, but that shorthand can obscure distinctions among roles. Network rules can assign reading, transaction submission, validation, and administration differently. A reader evaluating a system should identify the specific role being discussed rather than treating “permissionless” or “permissioned” as a complete access policy.

Permission also does not determine visibility. A permissioned network might provide broad data access within an approved group, or apply different visibility rules to different participants. A permissionless network’s label likewise does not specify every detail of the information available through its applications. Check the technical documentation for the actual data and access rules.

## How blockchain models combine in practice

The labels work best as two intersecting questions: **Who can access or read the network?** and **Who can participate in its operation?** The matrix is a conceptual guide, not a catalog of guaranteed network configurations.

| Access and visibility question | Participation question | What to verify |
|---|---|---|
| Is reading broadly available or restricted? | Is validation open or limited to approved participants? | The rules for reading, submitting transactions, and validating may differ. |
| Is access limited to a defined group? | Are multiple approved participants involved, or does an operator control key roles? | Identify who grants access and who controls each operational role. |
| Is information visible to network participants or a narrower set? | Who can submit or validate? | Confirm data visibility and participation rules separately. |

This framing explains why “public versus private” and “permissionless versus permissioned” are not interchangeable pairs. Public/private addresses access; permissionless/permissioned addresses participation rules. A network may be publicly readable while restricting validation, or limit access and also require authorization for participation. The particular combination depends on its documented design.

Do not treat the matrix as proof that a network has a specific configuration. It organizes questions to ask. For a real network, use its technical documentation to establish the rules for each role rather than inferring them from a general category or product description.

## Compare control, visibility, and operational trade-offs

To assess control, identify who admits participants, maintains the technical rules, and coordinates changes. A network’s governance arrangements may be distributed among stakeholders or concentrated in particular roles; the public or permissionless label alone does not settle that question. Check the documented decision process and the parties able to carry it out.

For visibility, distinguish information available to the public from information available only to approved participants. Then check what the network’s documentation says about transaction data and other records. A label is not evidence of confidentiality, and a description of broad access is not enough to establish that every participant sees every detail.

For validation, identify which participants check network activity and what rules they apply. As one specific example, Ethereum full nodes independently verify blocks and transactions against protocol rules. That example illustrates a validation role; it should not be generalized into claims about every network’s access, governance, or visibility.

A practical comparison can record four items for each network: reading access, transaction-submission rules, validation eligibility, and governance authority. Add a fifth item—documented visibility of transaction information—rather than assuming it follows from the first four. This makes operational dependencies easier to spot without ranking architectures or declaring one universally superior.

## What to verify before evaluating a payment use case

Before drawing conclusions about a network, consult current technical documentation and answer these questions:

1. Who can read network information, and are there restrictions by role?
2. Who can submit transactions, and what authorization is required?
3. Who validates activity, and what protocol rules apply to that role?
4. Who governs or coordinates changes to the network?
5. What transaction information is visible, and to which participants?

Keep those technical findings separate from claims about a payment product or service. A network’s architecture does not establish that a particular service is available, what it costs, how it handles recovery, or what legal, tax, regulatory, or compliance rules apply. Those claims need current, authoritative evidence appropriate to the specific product and jurisdiction, with qualified review where needed.

The central distinction is simple: access, participation, control, and visibility are related but separate properties. Treating them independently helps builders and decision-makers describe a blockchain model accurately and identify what must be verified before making further operational judgments.

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
