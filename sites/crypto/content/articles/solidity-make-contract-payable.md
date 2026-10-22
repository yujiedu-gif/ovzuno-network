---
title: "How to solidity make contract payable: functions and value handling"
description: "Learn how to solidity make contract payable by declaring payable functions, handling incoming native currency, and checking receive and fallback behavior."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: ["payable function Solidity", "receive function Solidity", "fallback function Solidity", "msg.value"]
author: "editorial_team"
primary_keyword: "solidity make contract payable"
owned_question: "How do you enable a Solidity contract to receive native cryptocurrency, and what should you check when adding payable functions?"
risk_level: "medium"
---

To enable a Solidity contract to receive native cryptocurrency through a function, declare that function `payable`. For a call with empty calldata, a defined `receive` function can serve as the receiving entry point; a `fallback` function handles calls that do not match another function. Before relying on either path, verify which calls it accepts and how the contract handles the value. The examples below illustrate patterns, not production-ready code.

## What `payable` means in Solidity

`payable` is a function declaration that permits the function to receive native cryptocurrency along with a call. It does not, on its own, specify whether the contract keeps, records, or forwards that value. Those outcomes depend on the function’s program logic.

In an Ethereum transaction that invokes a contract function, the submitted instruction can include value and contract-call data. The called function can access the amount sent through `msg.value`. A payable declaration permits a call to carry value; it does not mean that a caller must send a nonzero amount, or that the contract has implemented a payment workflow. [source](<https://ethereum.org/developers/docs/smart-contracts/>) [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Keep the boundaries clear. The contract’s declaration and code define how its entry point processes a call. The application or wallet that prepares a transaction and the user who authorizes it have separate responsibilities. A frontend can communicate what a call is intended to do, but an interface alone does not establish that the underlying contract behaves safely. [source](<https://ethereum.org/developers/docs/design-and-ux/dex-design-best-practice/>)

## How to solidity make contract payable

For a named function, put `payable` in the function declaration. This small example adds the received amount to a state variable:

```solidity
// Illustrative pattern only. Confirm compiler version and project settings.
pragma solidity ^0.8.0;

contract Example {
    uint256 public totalReceived;

    function contribute() external payable {
        totalReceived += msg.value;
    }
}
```

Here, `contribute` is the payable entry point, and `totalReceived` is the example’s chosen record of cumulative receipts. This simple total does not track individual contributors or explain how funds should later be used. A project must choose its state and business rules to match the behavior it intends to implement.

A caller must send value with the transaction for `msg.value` to be nonzero. If the function is meant to require payment, payable alone does not express the required amount: the contract must contain logic that checks the amount and defines what happens when the condition is not met. Similarly, the declaration does not say that the amount corresponds to a particular action or entitlement.

Treat the pragma in the sample as illustrative rather than a recommendation. Solidity source files can declare a compiler-version range, but that pragma constrains acceptable compiler versions rather than selecting the compiler. For a real project, identify the compiler version and settings used to build the code, then check syntax and behavior against that version.

When reviewing the function, trace the value from entry to outcome. Does the code update state, retain value in the contract, or invoke another contract? Is the recorded amount consistent with the intended handling? The declaration opens a path for a value-bearing call; it does not answer these design questions.

## Choose between `receive` and `fallback`

A contract may use special functions to define behavior for calls that do not invoke an ordinary named function. A `receive` function is the entry point for a call with empty calldata when it is defined. A `fallback` function handles a call that does not match another function. If either path is intended to accept value, its declaration must permit value.

Illustrative signatures:

```solidity
receive() external payable {
    // Define handling for a call with empty calldata.
}

fallback() external payable {
    // Define handling for an unmatched call.
}
```

Use `receive` when the intended case is a call with empty calldata. Use `fallback` when the contract needs to specify what happens to a call that does not match another function. If the design includes both, make their distinct purposes and outcomes explicit; do not assume that one declaration covers every call pattern.

The declarations above show the shape of the entry points, not a complete handling strategy. In particular, a payable signature does not record the amount or decide what to do with it. Add and review the required logic for each path. Confirm the special-function syntax and behavior against the selected Solidity version rather than assuming a sample applies unchanged to every compiler version or configuration.

## Check value handling before deployment

Review each payable path as a distinct route into the contract. A short, focused checklist can surface questions the declaration itself does not resolve:

- **Which calls should be accepted?** Name the expected entry point and call pattern. Decide whether the function accepts any amount or checks a project-defined condition, and verify that the code implements that decision.
- **How is the amount accounted for?** Follow `msg.value` through the function. Check whether the code records it, leaves it in the contract, or attempts to forward it, and whether state updates match the intended outcome.
- **What is the access rule?** Check the relevant entry point itself. If the function is meant to have restricted access, verify that the check applies to the payable path rather than only to a separate function.
- **What happens on failure?** Review the branches that handle rejected conditions and any external interaction. Confirm that the function’s failure behavior is deliberate and that its state changes fit the intended outcome.
- **What call cases need exercising?** Test the named payable function, an empty-calldata call when `receive` is defined, and unmatched calls when `fallback` is defined. Include cases that should be accepted and cases that should be rejected under the contract’s own conditions.

Use tests to check the specified call paths, but do not treat passing tests as proof that the contract is secure. Keep this checklist within its scope: it concerns payable declarations and value handling, not a comprehensive contract audit. Confirm the code against the exact compiler version and project configuration, and make sure any application interface describes the call’s expected behavior without presenting that description as evidence that the code is safe.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Decentralized exchange (DEX) design best practices](https://ethereum.org/developers/docs/design-and-ux/dex-design-best-practice/) — ethereum.org; retrieved 2026-10-18.
