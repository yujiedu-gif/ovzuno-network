---
title: "DAO explained: how proposals, votes, and execution fit together"
description: "DAO explained through the path from proposal to vote to execution, including how governance rules work and where human or technical controls remain."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["dao_governance"]
tags: ["dao"]
author: "editorial_team"
primary_keyword: "DAO explained"
owned_question: "How does a DAO turn member proposals and votes into governance decisions, and what determines whether those decisions are carried out?"
risk_level: "medium"
---

A DAO turns a proposal into a governance decision through rules for submitting proposals, participating in a vote, and determining whether the result authorizes a next step. Whether that decision is carried out depends on the DAO’s own contracts, policies, and execution arrangements. Some designs use smart contracts; others rely on people, multisignature execution, or a combination. A recorded vote alone does not establish that the requested action was completed.

## What a governance decision means in a DAO

Here, a governance decision means an outcome produced through a DAO’s decision process. The DAO’s rules determine what matters can be considered, who may participate, how an outcome is determined, and what that outcome permits. A vote should not be assumed to control matters outside the scope of those rules.

DAO governance can involve proposals, voting, delegation, token-based or share-based membership, reputation, and multisignature execution. These are options, not a universal checklist. A DAO’s contracts and policies determine which mechanisms it uses and how they connect. For instance, a community may vote on a proposal while a separate group or set of signers carries out the approved action. The existence of that vote does not show that the contract executes it automatically.

“Decentralized” does not specify a single allocation of decision rights. One design may distribute some parts of the process and retain other steps for people or designated signers. To understand a particular governance decision, trace who can propose, who can decide, and who or what can execute. The name or label applied to a DAO does not answer those operational questions.

## From proposal to an eligible vote

The process starts with a request for a decision. A proposal communicates what its author wants the DAO to consider, such as an action or change to a rule. The submission process may set requirements for eligibility or form, but those details cannot be assumed across DAOs. Check the specific DAO’s current procedures before treating a proposal as eligible for a vote.

Next, distinguish the proposal’s requested outcome from the process that can authorize it. The proposal describes an intended action; the DAO’s rules determine how it may be considered and whether a vote can lead to that action. Verify the proposal itself and the rules that apply to it, rather than relying only on a short summary or a screen in an application.

A decentralized application, or dApp, can combine a frontend interface with a smart contract running on a decentralized network. This distinction matters when following the proposal process: the interface presents information and may connect a participant to contract interactions, but it is not necessarily the full governance mechanism. Hosting, key management, and indexing can also remain dependencies outside the contract. When the precise action matters, compare what the interface shows with the governing contract or documented procedure.

At this stage, useful questions include: Who is permitted to submit? What information must a proposal contain? Is there a preliminary step before voting? Which contract or policy governs the proposal? The answers are system-specific. If the available documentation does not establish an answer, treat that as an unresolved process detail rather than filling it in from assumptions about other DAOs.

## How DAO voting rules shape outcomes

A vote’s meaning depends on the rules that define participation and approval. DAO governance may use voting, delegation, token- or share-based membership, reputation, or other arrangements. These possibilities do not establish how a particular DAO counts votes. Consult that DAO’s rules to determine who can vote, how voting power is assigned, how long voting remains open, and what result qualifies as approval.

Quorum and approval thresholds are examples of possible rules, not requirements common to every DAO. If the process includes a quorum, its rules define the participation condition. If it includes an approval threshold, the rules define the outcome needed to pass. Do not assume that either condition exists, or assign it a value, without verifying the applicable documentation or deployed rules.

Delegation is another possible feature, but its presence does not by itself explain the authority or weight of a delegated vote. The DAO’s own rules determine how delegation works within its process. Similarly, token-based, share-based, or reputation-based membership describes possible ways of structuring participation, not a universal method for assigning voting power.

A formal result should also be kept separate from broader community agreement. A vote records an outcome under the selected process. It does not, by itself, establish that every participant agrees, that all affected people took part, or that the proposal has been carried out. For a process review, record the formal result and separately identify any additional coordination or approval steps the DAO’s rules require.

## What happens after a proposal passes

After a proposal passes, identify what execution means in that DAO. Some decisions may be carried out through smart contracts; others may require people, multisignature execution, or a combination of mechanisms. Approval and execution are separate stages: the vote establishes an outcome under the voting rules, while the execution arrangement determines who or what must act next.

Follow the approved proposal to its specified action. Determine whether execution is automatic, requires designated signers, or depends on further coordination. If an administrator or additional approval has a role, passage does not establish that the permission was exercised or that the follow-up step occurred. The DAO’s own contracts and policies determine which steps apply.

A multisignature arrangement is one possible governance mechanism. Its presence should not be read as proof that a vote alone authorizes or completes an action: the connection between the vote and the signers’ next step depends on the design. Conversely, a proposal that calls for a smart-contract action does not show that the action succeeded merely because the vote passed. Verify the relevant execution step separately.

Ethereum protocol changes provide an example of coordination beyond a vote, not a universal rule for DAOs. Such a change can involve a proposal, technical review, implementation, coordination, and adoption across network stakeholders. A decision that depends on people and systems outside a voting mechanism may therefore require further work before the intended change takes effect.

To determine what happened, compare the proposal’s requested action with the relevant execution record or documented follow-up. Keep the conclusions distinct: the proposal passed under the rules; an authorized actor or contract attempted the action; and the intended action was completed. Evidence for one step does not automatically verify the next. Nor does a completed action, by itself, establish that it is permanent or irreversible.

## Where DAO governance can fall short

A practical review begins by tracing decision rights through the whole process: proposal submission, voting, and execution. Ask whether the same participants control all stages or whether a separate role, signer group, or contract is involved. A voting mechanism alone does not establish that voters control every important step.

Also distinguish contract behavior from the policies and coordination surrounding it. Smart contracts may carry out specified actions, while governance arrangements can also rely on people and documented procedures. A dApp may add dependencies through its frontend and supporting services. If an outcome relies on any such component, identify who or what is responsible for that step and what evidence would confirm it took place.

A governance process may also combine different mechanisms. Decred, for example, combines proof-of-work block production with proof-of-stake ticket voting that approves blocks and participates in rule-change governance. This is one hybrid architecture, not a template for other DAOs. The example underscores why a system’s specific documentation matters: the relationship between participation, decision, and execution is defined by its own design.

Finally, limit conclusions to what the available evidence establishes. General descriptions of governance mechanisms cannot show that a specific DAO’s procedures are secure, that its recovery arrangements work, or that it meets legal, tax, or compliance requirements. Those questions require current, authoritative evidence about the relevant system and circumstances. For the governance question itself, trace the applicable rule, confirm the vote result under that rule, and verify any distinct execution steps before describing the decision as carried out.

## Sources and references

- [What is a DAO?](https://ethereum.org/dao/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
- [PoS Voting Overview](https://docs.decred.org/proof-of-stake/overview/) — Decred Documentation; retrieved 2026-10-19.
