---
title: "ERC 20 governance token: meaning, voting, and limits"
description: "Learn what an ERC 20 governance token is, how ERC-20 functionality relates to voting, and why participation rights depend on project rules."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "erc 20 governance token"
owned_question: "What is an ERC-20 governance token, and how can it be used to participate in protocol governance?"
risk_level: "medium"
---

An ERC-20 governance token is a fungible token that a project may use as part of its decision-making process. ERC-20 functionality and governance rights are separate: a token’s designation does not, by itself, establish who may vote, how voting power is measured, or whether a decision is carried out. Those details depend on the project’s rules and implementation.

## What an ERC 20 governance token is

ERC-20 describes a common interface for fungible tokens. A governance token, by contrast, is a project-defined token that may be used in decisions about a project or protocol. The phrase “ERC-20 governance token” therefore combines two ideas: a token interface and a possible use within a project’s governance arrangements. It does not mean that the interface itself creates governance rights.

Governance is the process by which a group makes or coordinates decisions. The methods can vary: a project might use proposals, voting, delegation, token-based membership, share-based membership, reputation, or multisignature execution. These are possible governance approaches, not automatic features of an ERC-20 token. Which approach a project uses, and what authority participants have, depends on its contracts, policies, and context. ([source](<https://ethereum.org/dao/>))

## How ERC-20 functionality and governance differ

The distinction is between what a token interface describes and what a governance system decides. Token functionality concerns operations involving the token. Governance rules address participation, decision-making, and how a decision proceeds. A project can connect these parts, but the connection must be established by its own design; the token label is not enough to infer it.

For example, a project might make token-based membership part of its governance process. That description alone does not tell a reader whether holding tokens permits voting, whether votes are delegated, or whether a vote changes the protocol. The same caution applies to proposal rights: the fact that a project uses a governance token does not establish who can submit a proposal or what conditions apply.

Some governance arrangements distribute authority through named roles. In role-based access control, permissions are assigned to roles, and administrators can grant or revoke those roles, creating an authority structure that must itself be secured. A project using such controls may therefore have an operational authority path that differs from, or supplements, token-holder voting. ([source](<https://docs.openzeppelin.com/contracts/5.x/access-control>))

## How token-based voting may work

A project’s rules may describe a sequence in which participants submit proposals, eligible participants vote, and a decision is recorded or acted on. The available governance methods include proposal and voting processes as well as delegation, but the precise steps and authority depend on the project’s contracts and policies. ([source](<https://ethereum.org/dao/>))

Voting weight is another implementation question. A project could define how token holdings relate to participation, but the permitted evidence here does not establish a universal method for measuring balances, counting votes, setting a quorum, or recording balances at a particular time. Do not assume that any one mechanism follows from ERC-20 or from the phrase “governance token.” Check the project’s own rules for those details.

Likewise, a vote’s outcome and its execution are distinct questions. A governance process may include multisignature execution, among other methods, but the general existence of that option does not show that a particular project uses it, or that a vote automatically triggers a change. ([source](<https://ethereum.org/dao/>))

## What holders should verify in a specific project

To understand what participation means in a particular project, compare its current governance documentation with the rules and controls that implement decisions. Look for clear answers to these questions:

- **Participation:** Who can vote, and who can submit a proposal?
- **Voting power:** How does the project determine the weight of a vote?
- **Delegation:** Can authority or voting power be delegated, and what does delegation change?
- **Decision requirements:** What participation or approval conditions does the project specify?
- **Execution:** What happens after a vote, and which people, contracts, or processes carry it out?
- **Administration:** Who can grant or revoke roles, or otherwise change relevant permissions?

These are verification prompts, not claims that every project has the same rules. In particular, documentation that describes a vote should not be treated as proof that a vote directly executes a change. The project’s actual implementation and authority structure matter.

## Limits and risks of governance-token participation

A token’s use in governance does not establish that influence is evenly distributed, that every holder has equal practical influence, or that a vote controls every project decision. Delegation, role-based permissions, and other governance methods can shape how authority is exercised, but their effects depend on the specific arrangement. ([source](<https://ethereum.org/dao/>)) ([source](<https://docs.openzeppelin.com/contracts/5.x/access-control>))

Governance controls also have their own risks. Named roles can form an authority graph because administrators may grant or revoke permissions; that authority structure must be secured. Readers should therefore consider both the stated voting process and the permissions that can affect it, without assuming that token ownership alone captures the full decision-making process. ([source](<https://docs.openzeppelin.com/contracts/5.x/access-control>))

The central distinction is straightforward: ERC-20 does not itself define governance rights. A project may use a token in governance, but participation depends on separate rules and implementation. To evaluate a specific project, verify who can propose and vote, how the project defines voting power, what administrative authority exists, and how any decision is carried out. This general explanation does not determine legal or tax treatment or establish project-specific security, fee, yield, recovery, availability, or compliance claims.

## Sources and references

- [What is a DAO?](https://ethereum.org/dao/) — ethereum.org; retrieved 2026-10-19.
- [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control) — OpenZeppelin Documentation; retrieved 2026-10-19.
