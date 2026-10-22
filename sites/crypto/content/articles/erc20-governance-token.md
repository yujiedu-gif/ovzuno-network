---
title: "erc20 governance token: how token standards and voting relate"
description: "Learn how an erc20 governance token may connect token holdings with protocol decisions, and why the token standard alone does not define voting rules."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "erc20 governance token"
owned_question: "How can a protocol use an ERC-20 token in governance, and which voting rules and limitations are separate from the token standard?"
risk_level: "medium"
---

An **ERC-20 governance token** is a fungible token that a protocol may use as an input to its own decision process. ERC-20 defines common token functions and events; it does not define who can propose, how voting power is counted, what threshold passes a proposal, or how a decision is carried out. To understand participation, inspect the protocol’s governance documentation and the contracts it identifies rather than relying on the token’s label or balance alone.

## What does the ERC-20 standard define?

ERC-20 is a common interface for fungible tokens. Its functions and events cover matters such as total supply, balances, transfers, allowances, approvals, and the reporting of transfers and approvals. This interface helps applications interact with token contracts in a consistent way.

That scope is deliberately narrower than governance. The ERC-20 interface does not specify proposal creation, voting eligibility, vote counting, quorum, delegation, or enforcement of a decision. Nor does it establish a token’s issuance policy, backing, market value, regulatory treatment, or implementation safety. Those are not consequences of ERC-20 conformity. [claim_erc20_interface]

A protocol can build governance features that read or otherwise use token-related information, but those features belong to the protocol’s own design. For example, the protocol may use balances as one input to voting power, or it may define a separate delegation process. The token interface alone cannot tell a reader which design applies.

This distinction matters when a project describes a token as a “governance token.” The phrase may describe an intended use, but the practical rights and process depend on the rules implemented and documented by that protocol. A token balance is not, by itself, a complete description of a holder’s ability to participate or affect an outcome.

## How can an ERC-20 governance token relate to voting?

A governance system needs a rule for translating some eligible input into voting power. One possible design uses token balances; another may count delegated balances or apply a distinct calculation. The available evidence here does not establish a particular protocol’s method, so readers should treat any project-specific description as something to verify rather than assume.

Delegation is a design choice, not an ERC-20 feature. A protocol may allow a holder to assign voting power to another participant while retaining the tokens, or it may use a different arrangement. The relevant documentation should explain what delegation changes, who can delegate, and whether the protocol’s rules connect delegation to token ownership or voting periods.

Proof-of-stake terminology illustrates why “stake” should not be treated as a universal voting rule. In the general proof-of-stake model, cryptocurrency is committed as stake and can influence a participant’s consensus weight. That describes consensus participation, not automatically governance voting in a separate application. Protocol-specific selection, delegation, custody, reward, penalty, and withdrawal rules vary. [claim_nist_pos_stake]

Participation models also differ in who may take part in maintaining a ledger. Networks can be permissionless, with participation in block publication open, or permissioned, with authorized operators maintaining the ledger; access to reading or submitting transactions can also be restricted. These are network-access distinctions, not ERC-20 governance rules. A protocol’s governance process may impose its own participation requirements, which should be checked separately. [claim_permission_models]

## Which rules shape token-based governance?

Proposal eligibility determines who can put an item forward and under what conditions. A protocol might define a threshold or another qualification, but the ERC-20 standard does not prescribe either. Documentation should state whether the proposal process is open, token-gated, delegated, or subject to another stated requirement.

The voting rule should identify the voting period, what counts as an eligible vote, and how approval is determined. Quorum means a required level of participation, if one is specified; an approval threshold describes the support needed for a proposal to pass. These are protocol-level parameters, not functions or events required by ERC-20. If they are not clearly documented, the token standard cannot fill in the missing information.

Token-based voting also does not automatically mean that influence is evenly distributed or representative of every user. The way voting power is calculated and distributed matters. A protocol may use balances, delegation, or other rules, but the evidence must support any claim about the resulting distribution. Readers should avoid inferring practical influence from the existence of a token alone.

Passing a vote and carrying out its result are separate questions. A governance system may record a decision on-chain, while a later action depends on a separate execution process or on operators taking action. A different design can connect approval to contract execution. Do not assume one path: find out what the documentation says happens after the voting period and who or what is responsible for implementation.

Some projects combine different participation mechanisms. Decred, for example, is one documented hybrid architecture: proof-of-work produces blocks, while proof-of-stake ticket voting approves blocks and participates in rule-change governance. This example shows that a system can assign distinct roles to different mechanisms; it is not a general template for ERC-20 governance or evidence that another protocol uses the same process. [claim_decred_hybrid_roles]

## What should readers verify in protocol documentation?

Use a traceable reading path from the proposal stage to the final action:

1. **Locate the governance specification.** Identify the protocol’s stated process and the contract references associated with it. A token name or summary page is not a substitute for the rules.
2. **Check the voting-power calculation.** Determine what the protocol counts, when it measures eligibility, and whether delegated power is included. If the documentation does not answer these questions, mark the method as unresolved.
3. **Read the proposal and voting conditions.** Look for eligibility, voting period, quorum, and approval rules. Distinguish each condition rather than treating “the vote passed” as a complete description.
4. **Follow the execution path.** Establish whether an approved proposal triggers a contract action, requires another authorized step, or is only a recorded decision. The documentation should identify the process and relevant actors.
5. **Review control and recovery disclosures.** Find what the protocol says about upgrades, administration, security, and recovery. A disclosed control is useful information, but disclosure alone does not prove that the design is safe or that a recovery process will succeed.

When technical descriptions and governance summaries differ, the discrepancy is a limitation to report, not a reason to infer a rule. Protocol documentation can clarify intended behavior, but the ERC-20 interface itself remains limited to token interaction mechanics.

## What are the limits and risks of token governance?

Governance outcomes depend on more than token mechanics. The rules can concentrate or distribute decision-making power, and the actual execution path may involve additional controls. The available evidence does not establish the voting-power distribution, security properties, or recovery arrangements of any particular ERC-20 governance token. Those conclusions require protocol-specific documentation and contract evidence.

Smart-contract execution is deterministic in the sense that participating nodes must derive the same result, with execution results recorded on the blockchain. That property concerns consistent execution of the specified code; it does not establish that the code expresses a fair or safe governance process, or that a proposal’s assumptions are sound. [claim_nist_deterministic_execution]

Finally, holding a token does not by itself prove a legal right, financial return, or guaranteed influence. This article does not determine regulatory treatment, tax obligations, availability, fees, yields, or compliance. Those questions require jurisdiction- and fact-specific evidence and are outside what the ERC-20 standard can establish.

The practical takeaway is to separate the token interface from the governance system: ERC-20 describes common fungible-token mechanics, while each protocol defines whether the token connects to proposals, voting power, delegation, thresholds, and execution—and how those rules are limited or controlled.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [PoS Voting Overview](https://docs.decred.org/proof-of-stake/overview/) — Decred Documentation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
