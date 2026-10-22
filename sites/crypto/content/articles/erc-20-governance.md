---
title: "erc 20 governance: How Token-Based Protocol Decisions Work"
description: "Learn how erc 20 governance can use token balances for protocol voting, how proposals reach execution, and why the ERC-20 standard does not define governance."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["ERC-20 governance token", "token voting", "on-chain governance"]
author: "editorial_team"
primary_keyword: "erc 20 governance"
owned_question: "How can ERC-20-compatible tokens be used in protocol governance, and what does token-based voting enable or fail to guarantee?"
risk_level: "medium"
---

ERC-20-compatible tokens can serve as inputs to governance systems that separately define who may propose, how voting power is counted, and what happens after a vote. The ERC-20 standard defines a fungible-token interface for supply, balances, transfers, allowances, approvals, and related events; it does not define governance. A balance alone therefore does not establish voting rights or control over a protocol.

## What ERC-20 defines—and what it leaves open

ERC-20 is a common interface for fungible tokens. It includes functions for checking total supply and balances, transferring tokens, and approving another address to spend up to an authorized amount. The standard also specifies `Transfer` and `Approval` events. These functions and events let compatible applications and contracts interact with token balances and movements through a shared interface. [claim_erc20_interface]

The standard does not prescribe how proposals are created, who can submit them, how votes are counted, what quorum is required, whether holders may delegate, or how a successful proposal is executed. Those are governance rules, not token-interface rules. A contract can follow ERC-20 without including governance functionality.

This distinction separates two roles that are often discussed together. The token contract maintains the interface and token-related records. A governance system may consult those records or use a related mechanism to assign voting power and process proposals. That system may consist of other contracts, off-chain procedures, or a combination. The interface alone does not establish which arrangement applies, or whether token holders have any decision-making role.

## How erc 20 governance typically moves from proposal to action

A token-based governance process is best understood as a sequence of implementation choices rather than a feature guaranteed by ERC-20.

First, rules define proposal eligibility. A system may set conditions for who can submit a proposal and what the proposal must contain or satisfy. The token standard does not establish those conditions. To understand them, identify the governance documentation and the specific contracts or procedures that enforce them.

Next, the system determines voting power. It might use token balances, or it might count power assigned through delegation. The implementation also needs a rule for the relevant balance or delegation state: for example, the state used when voting begins or when an individual vote is cast. ERC-20 supplies token-related interface functions, but it does not select a voting-power formula or measurement point.

During voting, the governance system records votes and applies its own outcome rules. Those rules may specify a participation minimum, an approval threshold, or other conditions. Terms such as “quorum” and “threshold” should be read according to the system’s documentation rather than assumed to have identical meanings across implementations.

A recorded result is not the same thing as executed action. The final stage depends on what the governance system connects to the vote. In one possible design, a successful outcome authorizes a contract action. In another, the vote may be advisory or may require an off-chain step before anything changes. A delay before action is also an implementation choice, not a property of ERC-20.

For a technical review, trace the full path: proposal submission, eligibility checks, voting-power calculation, vote recording, outcome determination, and any action that follows. A description of voting without an explanation of the execution path leaves the practical effect of the result unsettled.

## Voting power, delegation, and participation trade-offs

With direct voting, a holder uses the voting power that the governance system assigns to that holder. With delegation, a holder assigns voting power to another participant if the system supports that mechanism. Neither arrangement is required by ERC-20. The governance rules determine whether delegation exists, how it is recorded, and what power it conveys.

The timing and accounting details can materially affect how a vote is interpreted. A design may specify when balances count, how transfers during a voting period are treated, and whether delegated power can be changed or reclaimed. It may also specify the participation needed for a proposal to qualify and the support needed for it to pass. These are system-specific parameters; they cannot be inferred from a token’s ERC-20 compatibility.

Token-weighted voting also has a basic representational limitation: voting power associated with tokens is not itself a measure of how many people participate or whether the outcome represents a broad constituency. A system’s count can reflect its defined token-based rules without demonstrating broad participation. The rules should therefore be evaluated as rules for allocating and counting influence, not as proof that participation is representative.

The technical question is not simply whether a system “uses token voting.” It is what the voting-power source is, when it is measured, how votes are aggregated, and which conditions determine an outcome. Documentation that does not answer those questions limits what can be concluded about how influence is allocated.

## What a governance vote can—and cannot—control

A vote can affect only what the system’s permissions and procedures allow it to affect. If the result is connected to an authorized contract action, the action’s scope depends on that contract and the system around it. If a vote is advisory or relies on an off-chain process, the vote itself may not change contract state. The label “on-chain governance” is not a substitute for examining the actual path from result to action.

It is also important to distinguish the decision mechanism from the subject being decided. A token-based vote does not, by itself, establish that holders control every contract, application component, service, operator, or organization associated with a protocol. The relevant authority may be distributed among different contracts and procedures, or the vote may cover only a defined set of actions. ERC-20’s interface does not resolve that question.

A sound description should therefore identify the actual scope of a vote and the mechanism that carries out its result. If a proposal passes but execution depends on a separate actor or procedure, that dependency is part of the governance design. Do not treat a counted vote as proof that every related component will change automatically.

## Questions to check when evaluating a governance design

Use primary project documentation and authoritative technical records to investigate the following points:

- Which token contract and governance mechanisms are involved, and what does each one do?
- What is the source of voting power, and when is it measured?
- Who may propose, and what eligibility conditions apply?
- How are quorum, approval thresholds, and other outcome conditions defined?
- Is voting direct, delegated, or both? What rules govern the assignment and measurement of delegated power?
- After a proposal passes, what specifically happens? Does a contract act, does another party need to take a step, or is the result advisory?
- Which permissions and procedures determine the scope of actions that a vote can affect?

Then compare the documented rules with the described execution path. If proposal rules, vote counting, or post-vote action are unclear, treat the effect as unresolved rather than assuming token holders have binding authority. ERC-20 compatibility establishes a token-interface relationship; governance rights and their limits must be established separately for the system being evaluated.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
