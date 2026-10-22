---
title: "Solidity function return value: meaning and basic usage"
description: "Understand a Solidity function return value: how outputs are declared, returned, and accessed, and why transaction receipts are not the same as returned data."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity function return value"
owned_question: "What does a Solidity function return value mean, how is it declared, and how can callers access it?"
risk_level: "low"
---

A Solidity function return value is data the function supplies to its caller. The function declaration specifies the output type or types, and the caller receives the result through the call interface. That returned data is distinct from a change to contract state and from information in a transaction receipt.

## What is a Solidity function return value?

A return value is the output of a function execution. In Solidity, the declaration identifies what type of output a function provides. A function can declare one output or several; the declared outputs determine what a Solidity caller can receive.

For example, a function might calculate a value and return it without changing the contract’s stored data. Returning a value, changing state, and emitting an event are different actions: an output is supplied to the caller, while a state change alters contract data and an event is a separate record that applications may process. A function’s return value is not automatically stored or emitted.

This distinction matters when reading code: a declared output describes data from the function’s execution, not a promise that the data will appear in a later transaction record.

## How to declare and return outputs

A function declares its outputs with `returns (Type)` after the parameter list. The following small example declares one unsigned-integer output and supplies it with an explicit `return` statement:

```solidity
function answer() public pure returns (uint256) {
    return 42;
}
```

Here, `uint256` is the declared output type. The expression after `return` supplies the value for that output. The type and returned expression need to be compatible.

A function can declare multiple outputs by listing their types, separated by commas. For example:

```solidity
function pair() public pure returns (uint256, bool) {
    return (42, true);
}
```

The returned values correspond to the declared types in order: first the `uint256`, then the `bool`. A caller handling multiple outputs must account for both positions, or use the relevant interface to select or ignore an output.

## Named and unnamed return values

Outputs can be unnamed, as in the examples above, or given names in the declaration. Names make the output variables available inside the function body:

```solidity
function answer() public pure returns (uint256 result) {
    result = 42;
}
```

In this example, assigning `42` to `result` supplies the function’s output. When execution reaches the end of the body, the assigned named output is returned implicitly. A function can also use an explicit `return` with named outputs; the important point is that the declared output still has to be supplied.

When checking a function, follow its execution paths and confirm that each one provides values matching the declared outputs. The declaration alone names the expected outputs; it does not supply them. For a beginner, the clearest approach is often to use an explicit `return` until named outputs and implicit returns are familiar.

## How callers receive a returned value

A Solidity caller can assign a function’s result to a compatible variable. For a single output, the idea is:

```solidity
uint256 value = otherContract.answer();
```

This is an illustrative Solidity call: `otherContract` must be an available reference to a contract exposing a compatible `answer` function. The assignment receives the output produced by that call; it does not, by itself, describe whether the call changes state.

For multiple outputs, a Solidity caller can use tuple assignment, matching the declared order:

```solidity
(uint256 number, bool flag) = otherContract.pair();
```

An off-chain application does not assign Solidity variables directly. It makes a call through its client or provider interface and receives the function’s result through that tooling. The exact representation and handling depend on the interface the application uses, so these examples do not prescribe a particular library or data format.

## Return values, transactions, and receipts

A function’s returned data is an execution result. A call that reads or simulates execution can expose that result to the caller. A transaction that invokes a function to change contract state is a different interaction: an Ethereum user can invoke a contract function by submitting a transaction, and the transaction lifecycle includes broadcast, block selection, execution, and subsequent confirmation or finality. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

The transaction receipt is not the function’s return value. A receipt can report whether execution succeeded or failed, but it should not be treated as a container for the function’s declared output. If an application needs output data from a state-changing transaction, it needs an appropriate mechanism or interface distinct from simply reading the receipt. A function’s return declaration does not automatically save or emit its output.

Keep the distinction simple: the declaration describes the function output, `return` supplies it, and the caller receives it through the call mechanism. State changes and transaction receipts answer different questions.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
