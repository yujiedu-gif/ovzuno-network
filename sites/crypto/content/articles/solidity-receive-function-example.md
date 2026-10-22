---
title: "Solidity receive function example: syntax, behavior, and tests"
description: "See a solidity receive function example, learn when Solidity invokes it, and review syntax, Ether-transfer behavior, and focused checks before adapting it."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity receive function example"
owned_question: "What does a Solidity receive function example look like, and what should developers verify when using one?"
risk_level: "medium"
---

For a Solidity developer, the minimal receive-function pattern is `receive() external payable {}`. It declares a function that can accept Ether when the contract receives a transfer with empty calldata. Before using it, verify the syntax against your project’s compiler version and test empty-calldata transfers separately from calls that include calldata.

## A minimal Solidity receive function example

```solidity
// Illustrative pattern only; confirm syntax with your project's compiler version.
contract EtherReceiver {
    receive() external payable {}
}
```

The function has no parameters or return values. `external` makes it callable from outside the contract, while `payable` permits it to receive Ether under the applicable call conditions. Its empty body contains no additional logic.

The snippet deliberately omits a compiler-version pragma: the evidence available for this example does not establish a specific version or compatibility range. In a project, compile using its declared Solidity compiler version and confirm that the syntax is supported there. Do not treat an illustrative snippet as a substitute for checking the compiler configuration used to build the deployed contract.

## When Solidity calls `receive`

Solidity selects a defined `receive` function for an Ether transfer whose calldata is empty. Calldata is the input data accompanying a call. The empty-calldata condition matters: a call that includes calldata does not use `receive` simply because it also transfers Ether.

Test these cases as distinct paths. One sends Ether with empty calldata; another includes calldata. Check which function the contract invokes and whether the outcome matches the intended behavior. This avoids assuming that every incoming Ether transfer reaches `receive`.

If a contract has no `receive` function, the result depends on its fallback setup. The example above does not show or define that setup, so it should not be read as saying that other incoming calls will succeed. Keep the dispatch question separate from the question of whether the contract has some other function capable of handling a call.

## What the example does—and does not—do

The `payable` declaration allows this function to accept Ether when invoked under the relevant call conditions. With an empty body, the example adds no sender-specific accounting and emits no event. A contract’s balance is not, by itself, a record in this snippet of which sender supplied which amount.

This is therefore a receive-function reference, not a complete deposit, withdrawal, or escrow design. Adding accounting, events, or other behavior changes what needs to be checked. A receive function’s declaration alone does not establish that additional logic is correct or appropriate for a particular contract.

## Checks to run before adapting the example

Use a focused review rather than treating the snippet as a complete payment feature:

1. **Compile for the project.** Build with the Solidity compiler version declared for the project, then review any compiler warnings. The example does not establish a universal version range.
2. **Test empty calldata.** Send a test transfer with empty calldata. Check whether it succeeds and whether the contract balance changes as expected.
3. **Test calldata separately.** Make a call that includes calldata and verify that it follows the intended dispatch path rather than assuming `receive` handles it.
4. **Recheck changes to the body.** If you add logic, assess its gas needs and external-call behavior with project-specific tests and review. Do not infer from the minimal example that any expanded receive function is inherently safe.

These checks answer the narrow implementation question: whether the compiler accepts the declaration and whether the contract behaves as intended for the two calldata cases. They do not amount to a security audit or establish the correctness of a larger payment design.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
