---
title: "Governance in decentralised autonomous organisations daos: proposals, voting and execution"
description: "Explore how decentralised autonomous organisations daos handle proposals, voting and execution, and what design limits and governance risks to assess."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["dao_governance"]
tags: ["DAO governance models", "on-chain governance", "off-chain governance", "smart contract execution"]
author: "editorial_team"
primary_keyword: "decentralised autonomous organisations daos"
owned_question: "How do decentralised autonomous organisations coordinate proposals, voting, and execution, and what governance limitations should participants assess?"
risk_level: "medium"
---

DAO governance is best understood as a process, not as a vote alone: participants may propose and discuss a change, decide under rules chosen by that organization, and then rely on a contract or people to carry it out. The rules and execution path differ between organizations, so readers should verify each stage rather than assume that a recorded result automatically becomes action.

## The governance lifecycle in decentralised autonomous organisations daos

A governance process can be mapped in four stages: proposal, deliberation, decision, and implementation. These are useful analytical steps, not a universal protocol. The relevant rules may appear in smart contracts, written procedures, interfaces, or other organization-specific arrangements.

**Proposal** is the point at which someone asks for a change or decision. The process may set conditions for who can submit a proposal and what information it must contain. **Deliberation** is the review and discussion that helps participants understand the request and its consequences. It may take place in an interface, community forum, or another channel; the location alone does not determine whether the discussion has formal authority.

**Decision** is the stage where an eligible group or mechanism records an outcome. Governance can use proposals, voting, delegation, token-based or share-based membership, reputation, or multisignature execution, among other models. These are possible approaches, not defaults that apply to every DAO. **Implementation** is the step that changes a contract, system, policy, or operational practice. It may happen automatically under contract rules or require people to take further action.

The stages can involve different participants and controls. A person may be able to discuss a proposal without being able to submit one; a vote may be open to a particular set of participants; and carrying out the result may require separate permissions. A recorded vote documents an outcome within the relevant process, but does not by itself show that the result is binding, technically executable, or already implemented.

## Who can propose, deliberate, and decide

The first evaluation task is to identify the organization’s actual participation rules. Ask who can submit a proposal, who can comment, who can cast or delegate a vote, and what conditions must be met for a decision to proceed. Do not infer those rights from a project’s name, interface, or use of the word “DAO.” Governance approaches can differ in membership and approval structure, including token-based, share-based, reputation-based, and multisignature arrangements.

Voting weight and decision eligibility are separate questions. A process might let participants vote directly, allow delegation, or use a different approval mechanism. To assess influence, inspect the written or coded rules that define who counts, how votes are treated, and whether a result triggers any further action. The existence of delegation, for example, does not establish who delegates to whom or how much practical influence is concentrated; those are implementation-specific facts to verify.

Quorum—the minimum participation condition a process may require before treating a vote as valid—is another design question, not a universal DAO feature. If quorum or a threshold appears in a process, verify its definition and how it interacts with the proposal and decision rules. Do not assume that a high turnout, a passed vote, or a large number of recorded participants resolves concerns about unequal influence or access.

Useful participation checks include whether proposal access is restricted, whether voters can delegate, whether decision rules are clearly stated, and whether participants can distinguish discussion from a formal decision. Potential concerns such as concentrated voting power, limited participation, or barriers to proposing should be evaluated against the specific rules and available evidence, not asserted as characteristics of every DAO.

## On-chain and off-chain governance mechanisms

“On-chain” means that some governance activity is represented or processed through a blockchain system. “Off-chain” means that activity takes place outside that system. Neither label, by itself, tells you who has authority or whether a decision will be implemented.

A blockchain-based governance process may record proposals or votes, but what the record establishes depends on the system and its rules. A recorded vote can provide evidence that a particular result was registered under a process; it does not establish that the vote was fair, that all relevant participants were included, or that an implementation step followed. Nor does the presence of a smart contract mean that every part of the organization’s governance occurs on-chain.

Off-chain discussion or signaling can inform a decision without directly changing blockchain state. For example, participants may discuss a proposed change outside the contract that will eventually execute it. Treat that discussion as distinct from a formal decision unless the organization’s own procedures connect the two. An interface may present discussion, voting, and contract interaction together, but the interface is not necessarily the authority that defines the underlying process.

A hybrid process can connect off-chain discussion or a recorded decision to a multisignature arrangement, administrator, or other execution control. This makes it important to identify the handoff: what outcome is recognized, who receives it, and what action is required next? A stated community preference and an executable instruction are not necessarily the same thing.

## From an approved decision to execution

After a decision, determine whether a contract carries it out automatically or whether a person or group must act. Smart contracts can form part of a decentralized application, while the application may also rely on a frontend interface and supporting services. This distinction helps separate the code that acts from the interface that presents information or the people who perform an operational step.

If implementation depends on signers or administrators, inspect the permission structure and the procedure for using it. A multisignature arrangement may be part of a governance model, but its presence alone does not show what actions it can authorize or how it relates to a vote. Similarly, an administrator’s existence does not establish the scope of that administrator’s powers. Verify the specific contract, policy, or operating procedure before drawing conclusions.

Timelocks and emergency powers should be treated as implementation-specific controls. The evidence available here does not establish that a particular DAO uses either mechanism, how long a delay might last, who can invoke an emergency power, or whether an intervention can reverse an action. If a process claims to have these controls, check their documented scope, authority, and relationship to ordinary governance rather than assuming they guarantee safety or recovery.

Track the outcome through to completion. A vote may pass while a required transaction remains unsubmitted, a signer does not act, or a technical step does not succeed. Conversely, an organization’s procedures may allow an execution path that is separate from a community vote. The key verification question is not only “What was the result?” but also “What system or authorized actor was supposed to implement it, and what evidence shows that happened?”

## Governance risks and design questions

A practical review should examine each stage independently. At proposal, ask who has access and what requirements apply. During deliberation, ask where participants can inspect the request and distinguish informal discussion from an official process. At decision, inspect eligibility, voting or approval rules, delegation, and any stated participation threshold. At execution, identify the contract or actor responsible and the permissions that govern the action.

Then consider failure modes without assuming they are present. Could proposal access be too limited for participants to raise concerns? Could participation or delegation concentrate influence? Is it clear how a disputed result is handled? Does the process explain what happens if an implementation step fails or an urgent intervention is proposed? These are questions for evaluating a particular design, not conclusions that follow from the label DAO.

Technical controls and governance procedures are related but distinct. A contract may enforce a specified rule, while the rule itself reflects choices about participation and authority. Conversely, a discussion or vote may express a decision without supplying the technical permissions needed to execute it. Neither a blockchain record nor a governance process alone establishes that all risks have been addressed.

Finally, keep claims about legal status, regulation, or compliance separate from technical descriptions. This explainer does not determine those matters for any organization or jurisdiction. The bounded assessment is procedural: identify who can propose, who can deliberate and decide, how decisions connect to execution, and what documented controls or unresolved limitations apply at each handoff.

## Sources and references

- [What is a DAO?](https://ethereum.org/dao/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
