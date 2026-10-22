---
title: "The DAO of DAOs: How Multiple DAOs Can Coordinate"
description: "Learn what the DAO of DAOs means, how multiple autonomous organizations can coordinate decisions, and what trade-offs arise in shared governance."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["dao_governance"]
tags: ["dao daos"]
author: "editorial_team"
primary_keyword: "the dao of daos"
owned_question: "What does “the DAO of DAOs” mean, and what governance patterns can enable multiple DAOs to coordinate while retaining separate decision-making authority?"
risk_level: "medium"
---

“The DAO of DAOs” describes coordination among distinct decentralized autonomous organizations (DAOs), not one standardized organization or governance system. Multiple DAOs can coordinate through delegated representation, joint proposals and votes, or shared working groups while retaining separate rules and decision processes. Which decisions are shared—and who can approve or carry them out—depends on the arrangement’s governing rules.

## What “the DAO of DAOs” describes

A DAO of DAOs is a useful description for a network or federation of separate organizations coordinating on matters that affect them jointly. It differs from a single DAO divided into internal teams: in a multi-DAO arrangement, the participants are distinct organizations, each potentially operating under its own membership and governance rules.

The phrase does not identify one required technical structure. DAO governance can involve proposals, voting, delegation, token-based or share-based membership, reputation, or multisignature execution. These are possible governance mechanisms, not a universal checklist, and their presence alone does not establish that several DAOs have formed a federation. Actual rights and execution paths depend on the DAO’s contracts, policies, and legal context. [source](<https://ethereum.org/dao/>)

A practical starting point is to ask what the participating organizations have actually agreed to coordinate. They might define a narrow shared matter while keeping other decisions local. Without that boundary, calling a group a “DAO of DAOs” says little about its authority or how its decisions work. The term is a conceptual label here, not a technical specification or a claim about legal status.

This distinction also prevents a common analytical shortcut: a group of teams within one organization is not necessarily the same thing as several organizations coordinating. To assess whether the latter is happening, look for evidence that participating entities retain their own decision rules and have established a process for decisions that cross their boundaries. A shared discussion space or a common project goal alone does not establish who has authority to decide.

## How DAO DAOs can coordinate decisions

Several patterns can support joint decisions. They can be used separately or combined, but each requires explicit rules about the scope of shared authority.

**Delegated representation** lets a participating DAO authorize one or more representatives to speak or act for it within a defined mandate. The essential questions are who grants the mandate, what it covers, and whether the representative’s action binds the DAO or only communicates its position. Delegation should not be assumed to transfer all decision-making authority.

**Joint proposals and votes** provide a process for participants to consider a shared proposal and record their decisions. A design must specify who may submit proposals, who is eligible to vote, how the result is determined, and what follows from approval. DAO governance models can include proposals, voting, delegation, and different membership approaches, but the details depend on the organization’s contracts and policies. A generic description cannot establish a particular network’s voting rules or the weight assigned to each participant.

**Shared working groups** provide a forum for members or delegates from several DAOs to deliberate, negotiate, and develop recommendations. A group’s ability to recommend a course of action is different from authority to approve or execute it. The governing rules need to say whether a working group is advisory, delegated, or empowered to take a defined action. If authority is delegated, the mandate should identify its limits and how the participants can review or revise it.

In any of these patterns, distinguish deliberation from authorization and execution. Discussion and negotiation may happen off-chain; a vote or other approval may be recorded through a governance process; and implementation may require a separate action. Ethereum protocol-change processes, for example, involve proposal, technical review, implementation, coordination, and adoption across network stakeholders. That illustrates a coordination sequence, not a template for every DAO network. [source](<https://ethereum.org/governance/>)

When evaluating a real arrangement, follow the sequence rather than relying on labels. Ask where a proposal begins, how the relevant participants consider it, how approval is determined, and what action implements the outcome. The approval mechanism and the implementation mechanism may be different. A recorded approval should not be treated as proof that an authorized actor has carried it out.

## Where authority and accountability sit

To understand a particular arrangement, trace a shared decision from proposal to review. Identify who may propose it, who approves it, whether anyone can veto it, who executes it, and who can review or revise the result. If the rules do not answer these questions, the label “DAO of DAOs” does not fill in the missing authority structure.

Then separate shared authority from local authority. A joint process may cover only an agreed set of issues; the participating organizations may keep their other choices within their own processes. The boundary matters because a shared vote should not automatically be treated as authority over every participant or every issue. Look for a defined scope, and check whether the process itself can change that scope.

Look closely at mandates and representation. If delegates act for participating DAOs, check how those delegates are selected and what authority they receive. If a vote is intended to represent organizations rather than individuals, check how the rules translate participant-level decisions into a collective result. Do not assume that equal representation, equal voting weight, or a particular approval threshold exists unless the rules state it.

Accountability can become unclear when a decision spans organizations. A proposal may be approved collectively but implemented by only one participant, or a delegate may convey a position without authority to bind the group. The arrangement should clarify who is responsible for communicating the decision, carrying out any authorized action, and reporting on what happened. Governance arrangements alone do not establish legal status or liability; those questions require evidence beyond the governance label.

A useful review separates three roles: the participant that authorizes a representative, the body or process that approves a shared decision, and the actor that implements it. These roles can overlap, but they do not have to. If one actor performs several roles, the governing documents should still make the authority for each step understandable. This is a governance-analysis checklist, not a claim that a particular structure is legally accountable in a specified way.

## Trade-offs in multi-DAO governance

Coordination can make a joint decision more deliberate, but every added step creates questions about participation and authority. A process involving multiple organizations must define how each can contribute, how their views are combined, and what happens when they disagree. Delegation can reduce the need for every participant to handle every discussion directly, but it makes the delegate’s mandate and accountability especially important.

A shared process can also create practical influence that differs from formal voting rights. For example, participants who shape proposals or coordinate implementation may affect the outcome even if formal approval lies elsewhere. This is a design consideration, not a claim that any particular DAO network concentrates power. To evaluate it, compare the written authority with the steps required to put a decision into effect.

Disagreement needs an explicit path. A design might specify another round of deliberation, a revised proposal, a limited scope for action, or that a participant can decline to join a particular decision. These are possible design choices, not universal rules. If the governing documents do not describe deadlock, exit, or rejection, do not assume that the arrangement has a reliable process for those situations.

Representation and participation also involve a trade-off. A process may give each organization a direct voice, or it may use delegates; either way, the rules should explain how a participant’s view enters the shared decision. A process that is easy to describe in principle may still leave unresolved how a disagreement between a delegate and the organization they represent is handled. The answer must come from that arrangement’s rules, not from the general idea of delegation.

Transparency depends on what the process records and communicates. A recorded vote can show an outcome, but it does not by itself explain the deliberation, the scope of a delegate’s authority, or how an approved decision was implemented. Check which parts of the process are visible and how the arrangement communicates changes or follow-up actions. A public record of one stage should not be mistaken for a complete account of all stages.

Finally, distinguish resilience to disagreement from a claim that disagreement can always be resolved. A design can state a route for further discussion or for a participant to withhold participation, but the existence of a written route does not establish that all parties will accept the outcome. The evaluation task is to determine what the rules actually authorize when coordination fails, rather than to assume consensus or a particular remedy.

## Questions to ask when evaluating a DAO network

Use the arrangement’s governing documents, public rules, and relevant proposal records to check:

- **Participants and scope:** Which DAOs participate, and which issues are covered by shared governance?
- **Decision rights:** Who may propose, vote, delegate, veto, execute, or review a shared decision?
- **Representation:** What mandate does each representative receive, and how can it be changed or withdrawn?
- **Local authority:** Which decisions remain with each participating DAO rather than the joint process?
- **Implementation:** Who communicates and carries out an approved decision, and where can readers verify that step?
- **Disagreement:** What do the rules specify for deadlock, a rejected proposal, or a participant that does not join a shared decision?
- **Revision:** How can the coordination rules or scope themselves be changed?

Treat answers as specific to the arrangement under review. The phrase “DAO of DAOs” does not establish a standard voting method, shared legal status, or guaranteed ability to resolve disagreement. The useful question is whether the documents clearly connect each shared decision to its mandate, approval process, implementation, and review—while preserving the authority the participating organizations have kept for themselves.

Keep evidence matched to the claim being evaluated. A governance overview may describe possible mechanisms, while a current governing document or proposal record is needed to substantiate how a particular arrangement operates. If a key rule is absent or unclear in the material reviewed, record that limit rather than supplying a presumed threshold, veto right, dispute process, or legal conclusion.

A concise assessment can therefore map each shared decision to four elements: its scope, the authorized participants, the approval path, and the implementation or review path. Compare that map with the powers each organization has retained locally. This approach keeps the analysis centered on coordination across distinct DAOs without treating the phrase as a standardized structure or implying that one governance pattern fits every network.

## Sources and references

- [What is a DAO?](https://ethereum.org/dao/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
