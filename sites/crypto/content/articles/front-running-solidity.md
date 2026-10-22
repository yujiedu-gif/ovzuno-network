---
title: "Front running Solidity: transaction-ordering risks in smart contracts"
description: "Learn how front running Solidity contracts can arise from transaction visibility and ordering, and review defensive design patterns and their limits."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "front running solidity"
owned_question: "How does front-running arise in Solidity-based dApps, and what design choices can reduce exposure to transaction-ordering attacks?"
risk_level: "medium"
---

Front-running risk in Solidity-based dApps arises when transaction visibility and execution order let an earlier transaction change the state or conditions a later one depends on. Solidity does not itself determine who can see a pending transaction or how a network orders transactions. Developers can reduce exposure by identifying order-sensitive state changes and matching controls to the application’s threat model. The evidence available for this article does not establish specific protections such as commit-reveal, deadlines, private submission, batching, or auctions, so none should be assumed to provide a guarantee.

## What front-running means for Solidity contracts

A transaction’s **ordering** is its position relative to other transactions executed against shared blockchain state. Front-running is a concern when a participant acts on information about a transaction and has a competing action executed first, changing the conditions or outcome for the original transaction. This differs from ordinary ordering: transactions must be processed in some order, but order alone does not establish that a harmful intervention occurred.

The broader term **maximal extractable value (MEV)** describes value that can be obtained by influencing transaction inclusion or ordering. Front-running is one ordering-related pattern, not a synonym for every form of MEV. The scope here is contract design, not instructions for exploiting a deployment or trading strategy.

Solidity defines contract behavior, but it does not alone define transaction visibility, inclusion, or ordering. Those depend on the network and transaction-submission path, as well as the application interacting with the contract. A dApp combines an onchain smart contract with a frontend, and supporting services can add dependencies. A contract review should distinguish what code controls from what a wallet, frontend, transaction provider, or network controls. [source](<https://ethereum.org/developers/docs/dapps/>)

## How transaction ordering can change contract outcomes

Some public-chain transactions may be visible before block inclusion. In the specific case of public-blockchain automated-market-maker swaps studied by the Bank for International Settlements, execution can be affected by public transaction visibility, ordering, pool depth, and price impact before inclusion. This is a bounded example, not a claim that every network or submission path exposes transactions in the same way. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

Consider a generic contract function that accepts a purchase only while a shared condition remains true. If one transaction changes that condition before another executes, the later call may revert, receive a different result, or proceed under changed terms, depending on the function’s code. The mechanism is state dependence: each execution reads the state left by earlier executions, so order can affect the result.

A swap is another illustrative case. Its result can depend on the pool’s state when the contract processes it. A transaction that executes earlier can change that state, which may alter a later transaction’s execution or output. The exact effect depends on the contract, pool design, network, and transaction parameters; the example is not a universal rule about all swaps.

## Common Solidity design exposure points

Start by examining functions where an action’s result depends on shared state at execution time. Examples include a first-come-first-served condition, a limited allocation, or a price or quantity calculated from current contract state. Ask what changes if another valid transaction executes immediately before the function call.

Next, inspect which parameters the user supplies and which outcomes the contract permits. A call with broad execution conditions may remain valid after intervening state changes; explicit limits can instead reject outcomes outside the stated bounds. The value of such a bound depends on how the contract checks it and how the application constructs the transaction. This observation does not establish a particular Solidity-specific control or guarantee.

Keep responsibility boundaries clear. Contract code can enforce state transitions and parameter checks, but it does not choose how a wallet signs or submits a transaction, what a frontend displays, or how a network includes transactions. Review those assumptions separately rather than attributing every ordering issue to Solidity itself.

## Defensive patterns and their trade-offs

A design review can begin with the general question of acceptable outcomes: which state changes should cause a call to proceed, and which should make it fail? Contract checks can enforce conditions that the code actually evaluates. But the evidence authorized for this article does not support detailed claims about the effectiveness, availability, or trade-offs of commit-reveal schemes, slippage bounds, deadlines, private transaction submission, batching, or auctions. Those approaches should not be described as established protections here without specific supporting evidence and system-level qualification.

One supported contract-level pattern is **checks-effects-interactions**. It orders contract logic by validating conditions, recording internal state changes, and only then interacting with external contracts. The pattern reduces a class of reentrancy risk; it does not make arbitrary contract code safe. Reentrancy is a distinct issue: an external call can transfer execution control to another contract, which may call back before the original operation is complete. It should not be conflated with transaction-ordering front-running. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>)

**Composability** means contracts can call or reuse independent onchain components through public interfaces. It can make a dApp more interconnected, while each dependency adds behavior, upgrade, permission, availability, and economic assumptions to the caller’s system. A review should include those dependencies rather than treating the contract in isolation. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

A mitigation must fit the application’s actual threat model: which actions are sensitive, what information is exposed, and what happens when state changes or execution fails. The allowed evidence does not establish that any specific defense prevents front-running across networks, transaction paths, or applications. Treat proposed protections as design choices requiring system-specific validation, not guarantees.

## How to assess a contract’s ordering risk

Use a focused review process:

1. **Map sensitive state transitions.** Identify functions that read shared state and can produce different outcomes depending on what executed first.
2. **Document environment assumptions.** Record the transaction-submission path the application expects and its assumptions about visibility, inclusion, and ordering. Treat these as environment-specific assumptions, not Solidity guarantees.
3. **Check conditions and failure behavior.** Verify which conditions the code actually enforces and what happens when intervening state changes make them false.
4. **Examine alternate sequences.** Consider cases where another state-changing call occurs before the action under review. This is a review question, not a claim that a particular testing method proves every possible ordering has been covered.
5. **Review the application path.** Compare contract assumptions with what the frontend and transaction-submission components request or communicate, and consider independent security review where appropriate.

The practical question is not simply whether a contract can be front-run. Ask which outcomes depend on ordering, what an earlier transaction can change, and which conditions the contract enforces before proceeding. Keep protocol behavior, application choices, and contract behavior distinct. Where the evidence does not support a claim about a proposed mitigation, do not infer protection from its name or intended purpose.

## Sources and references

- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
