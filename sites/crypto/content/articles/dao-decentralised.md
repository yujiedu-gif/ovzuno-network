---
title: "DAO Decentralised: How to Assess Distributed Governance"
description: "Learn how to assess whether DAO decentralised governance distributes authority across proposals, voting, execution, and administrative controls."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["dao_governance"]
tags: []
author: "editorial_team"
primary_keyword: "dao decentralised"
owned_question: "What does “DAO decentralised” mean in practice, and how can readers assess where a DAO’s governance is genuinely distributed versus concentrated?"
risk_level: "medium"
---

“DAO decentralised” is best treated as an assessment question, not a yes-or-no label: trace who can propose, vote on, execute, and administer decisions, because authority may be distributed differently at each stage. A formal vote alone does not show who can change the rules or carry out the result. The available evidence supports a practical framework for examining those stages, but it does not establish the controls of any particular DAO; those require project-specific documentation and verifiable records.

## What “DAO decentralised” means for governance

For governance, decentralisation concerns how decision-making authority is assigned and constrained. It is not a universal technical score, and the available evidence does not establish one threshold that makes a DAO “decentralised.” Instead, ask which participants or groups can take each consequential action and what conditions limit their authority.

A DAO may use proposals, voting, delegation, token-based or share-based membership, reputation, or multisignature execution. These are possible governance mechanisms, not evidence by themselves that authority is broadly distributed. Actual rights and execution paths depend on the DAO’s contracts, policies, and legal context. ([source](<https://ethereum.org/dao/>))

Separate at least four stages: proposing a change, deciding whether to approve it, implementing an approved decision, and administering the mechanisms that allow those actions. A process can distribute one stage while concentrating another. For example, an open proposal process does not by itself tell you who can execute a change or control the rules governing future proposals. These questions need to be checked separately rather than inferred from the DAO label or a single participation mechanism.

## Trace a decision from proposal to execution

Start with one consequential proposal and follow its documented path. This makes the assessment concrete: it shows which actors have authority at each step, instead of relying on general descriptions of the project’s governance.

**Proposal.** Find the rules or documentation describing who may submit a proposal and what conditions apply. Check whether a proposal can be changed, withdrawn, or blocked before a vote. If documentation does not identify those permissions, record that the stage is unclear rather than assuming that submission is open to everyone.

**Voting.** Identify who is eligible to participate, how voting or delegation works, and what threshold is needed for a decision. A description of voting options is not enough to establish how influence is distributed in practice. The available evidence identifies possible approaches—including delegation and different membership models—but does not prescribe a universal voting design or show the distribution of power in any specific DAO. ([source](<https://ethereum.org/dao/>))

**Execution.** Determine what happens after approval. Is the result carried out automatically under contract rules, or does another actor or group need to approve or implement it? Smart-contract execution is designed so participating nodes derive the same result, with execution results recorded on the blockchain; that property describes execution consistency, not who has authority to initiate or authorize a change. ([source](<https://csrc.nist.gov/glossary/term/Smart_contract>))

**Administration.** Look for separate authority over the mechanisms used to propose, vote, or execute. Governance mechanisms can include multisignature execution, but the presence of a multisignature process alone does not reveal who controls it or how it relates to a vote. Check the documented rights and, where available, implementation evidence before drawing conclusions. ([source](<https://ethereum.org/dao/>))

For each stage, note the authorized actor, the relevant rule or condition, what evidence supports the finding, and anything you could not verify. This compact record makes gaps visible and prevents a documented vote from being mistaken for proof that every stage is equally distributed.

## Check where control may be concentrated

A useful assessment asks whether an actor or group can independently alter, delay, block, or carry out a decision. Treat these as questions to investigate, not claims about the controls a particular DAO necessarily has. The authorized evidence does not specify that any particular DAO has administrator keys, upgrade permissions, pause controls, or a particular delay mechanism.

Compare written governance descriptions with verifiable permissions or records when available. Documentation can explain the intended process; implementation evidence can help show which actions particular accounts or contracts are permitted to perform. Proposal and execution records can help connect an approved decision to an action. These forms of evidence answer different questions, so one should not substitute for another.

Also distinguish the governance process from the application interface people use to interact with it. A decentralized application can combine a smart contract on a decentralized network with a frontend user interface, while supporting services such as hosting, key management, or indexing may remain centralized dependencies. Therefore, an interface’s appearance does not establish who controls the underlying governance rules or supporting operations. ([source](<https://ethereum.org/developers/docs/dapps/>))

If the project’s explanation and the available technical evidence do not align—or if permissions cannot be verified—state that limitation directly. Do not turn an undocumented control into a presumed safeguard, or treat a project’s description as independent confirmation.

## Interpret evidence and limits

Use a layered record rather than a single label. Project documentation can describe intended rules; contract permissions, where verifiable, can show technical authority; and proposal and execution records can show how particular decisions proceeded. Each piece of evidence has a limited scope. A record of one completed decision does not, by itself, establish how every future decision will work.

Write findings in feature-specific terms: for example, whether proposal submission, voting, execution, or administration appears distributed, concentrated, or unverified. Avoid a single score unless a defined and supported method justifies it; the evidence available here provides no universal scoring standard or comparative ranking. Governance rights and execution paths depend on the particular DAO’s contracts and policies, so conclusions should be limited to the materials examined. ([source](<https://ethereum.org/dao/>))

Treat the assessment as time-sensitive. A change to a contract, policy, or operational process may change who has authority. If you cannot verify current materials or the relevant implementation details, say so rather than inferring that a past record proves the present arrangement.

## Questions to resolve before relying on DAO governance

Before relying on a governance process for a decision, answer these questions from current, project-specific evidence:

- Who can submit or modify proposals, and what conditions apply?
- Who can vote or delegate, and what rules govern approval?
- What actor or process carries an approved decision into effect?
- Who administers or can alter the mechanisms used at those stages?
- Which permissions or operational dependencies remain unclear or unverified?
- What happens when participation is inactive, a decision is contested, or a required threshold is not reached?

The available evidence does not establish what a particular DAO does when participation is insufficient or a decision is contested; resolve those questions from that project’s rules and records. Legal questions also require separate, qualified review: the cited governance evidence notes that actual rights and execution paths depend in part on legal context, but it does not provide legal conclusions. ([source](<https://ethereum.org/dao/>))

The practical conclusion is deliberately narrow: “DAO decentralised” should prompt a stage-by-stage investigation of authority, not an assumption based on a name, vote, or mechanism. The result is strongest when it distinguishes what is documented, what can be verified, and what remains unknown.

## Sources and references

- [What is a DAO?](https://ethereum.org/dao/) — ethereum.org; retrieved 2026-10-19.
- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
