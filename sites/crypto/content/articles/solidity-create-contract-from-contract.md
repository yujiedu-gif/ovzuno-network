---
title: "Solidity Create Contract from Contract: A Practical Implementation Guide"
description: "Learn solidity create contract from contract with a minimal factory example, constructor arguments, deployment checks, and key failure considerations."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity create contract from contract"
owned_question: "How do you implement contract deployment from another contract in Solidity?"
risk_level: "medium"
---

A Solidity contract can deploy another contract during a transaction by creating an instance of a known contract type with `new`. The new instance has its own address and state. A factory can return that instance or record its address so the calling application can locate it. The example below shows the basic pattern and how to check the result; it is illustrative, not a claim that the code was executed or tested.

## What contract creation from another contract means in Solidity

A contract is code and data representing its state. On Ethereum, a user account can invoke a contract function by submitting a transaction to the deployed contract. That function may, in turn, create another contract as part of the transaction’s execution. In this arrangement, the first contract is the deploying contract, and the newly created contract is the child.

A **factory** is a contract that provides a way to create instances of another contract. It can collect constructor arguments, initiate creation, and make the resulting instance easier for an application to find. “Factory” describes an organizational pattern, not a rule that every application needs a separate deployment contract.

The child is a separate contract, with its own on-chain address and persistent state. The factory may store or return a reference to it, but that does not make the child’s state part of the factory’s state. A contract can also call or reuse another on-chain component through a public interface; each added component brings its own behavior and assumptions, so the combined behavior needs to be considered rather than inferred from the factory alone. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

## Solidity create contract from contract with a minimal factory

This example defines a child contract with one constructor parameter and a factory function that creates the child with `new`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Child {
    uint256 public value;

    constructor(uint256 initialValue) {
        value = initialValue;
    }
}

contract ChildFactory {
    function deploy(uint256 initialValue)
        external
        returns (Child child)
    {
        child = new Child(initialValue);
    }
}
```

`Child` declares a state variable named `value` and a constructor that assigns it when a new instance is created. `ChildFactory.deploy` passes `initialValue` to that constructor. The named return variable, `child`, receives the newly created instance, so the function returns a typed reference to it.

The pragma `^0.8.20` expresses a permitted compiler-version range; it does not select or install a compiler. Before using an example in a project, confirm that its syntax and build settings match the compiler version chosen for that project. Pinning an exact compiler version can prevent a source file from being compiled automatically with a different compiler version that may introduce breaking behavior, but a version pin does not establish that the contract is correct or secure.

This simple pattern is appropriate to explain creation of a known Solidity contract type. It does not cover deployment tooling, production factory architecture, or specialized address-derivation schemes. Those are separate design questions.

## Pass constructor arguments and record the deployed instance

Constructor arguments go inside the parentheses after the child contract’s type: `new Child(initialValue)`. If a child needs more initialization data, its constructor can accept additional parameters, and the factory can pass corresponding values when it creates the instance. The factory should validate inputs that matter to the child’s intended configuration; successful creation by itself does not prove that the supplied values meet the application’s requirements.

The example returns a typed `Child` reference. A caller that needs to invoke the child’s interface can use that reference in its Solidity code. If the application only needs to identify or retain the destination, it can use the instance’s address. An address identifies the on-chain location; the contract interface describes how calls, arguments, return values, errors, and events are encoded. Applications need an ABI that matches the deployed contract interface and network address.

A factory can also record each created address in its own state or emit an event when it creates a child. These choices serve different lookup needs. Stored addresses are part of the factory’s state and can be read through its interface. Events can be processed by applications, provided they use the correct contract interface to interpret the event. Neither approach changes the fact that the child has its own state.

When choosing what to expose, consider the caller’s task: return a reference when the immediate caller needs the instance, store addresses when the factory must maintain its own on-chain list, and emit an event when applications need an observable creation record. These are implementation options, not universal requirements. The example uses only a return value, so it does not demonstrate storage or event handling.

## Check deployment outcomes and handle failure

A direct `new` expression makes child creation part of the enclosing factory call. If the child’s constructor cannot complete, the ordinary direct creation path does not produce a successfully completed factory call. The caller should handle transaction failure through its application’s normal error path rather than assuming an instance exists.

Validate relevant inputs before creation. For example, a factory can check a value against the child’s documented requirements before passing it to the constructor. The right condition depends on the application; the example intentionally does not invent a universal rule for `initialValue`.

After a successful transaction, check the application-visible result. Confirm that the returned reference identifies the instance, then read the child’s expected initial state through its interface. If the factory stores an address or emits an event, check that the recorded or emitted value corresponds to the instance created in that call. A successful transaction is not a substitute for verifying that the child’s configuration is the one the application expected.

Treat failure cases as part of implementation review. Tests can exercise accepted inputs, rejected inputs, constructor argument propagation, and the child’s initial state. If creation is expected to fail for a particular input, verify that the surrounding application receives and handles that failure as intended. A structured verification framework can organize checks for EVM contracts and decentralized applications, but its existence does not establish that a particular factory is secure or that its tests cover every relevant behavior. [source](<https://owasp.org/projects/smart-contract-security-verification-standard>)

## Choose between new and lower-level creation mechanisms

For a known contract type, `new` is the straightforward Solidity expression shown here: it creates that type and supplies constructor arguments. `CREATE` and `CREATE2` are lower-level alternatives, but their behavior and address derivation require separate, version-appropriate verification. This guide does not specify those mechanisms or make a recommendation about when to use them.

Keep the decision tied to the implementation you are building. If the task is simply to create a child of a known type and return it, the example illustrates that path. If the requirement depends on details not shown here, such as a particular address-derivation behavior, verify those requirements against authoritative documentation before writing or relying on the code.

## Test the factory and verify the child contract

A practical check of the example should follow the creation path from input to observable result:

1. Call `deploy` with an accepted constructor argument and confirm that the returned reference identifies a nonzero address.
2. Read `value` from the child and check that it reflects the argument passed through the factory.
3. If the implementation adds input validation, exercise both accepted and rejected inputs and check the expected result for each.
4. If the factory stores addresses or emits a creation event, verify that the value recorded or reported matches the child created by that call.
5. Confirm that the application uses the child’s matching interface when it calls functions or interprets events.

These checks target the factory’s behavior, not every possible property of the factory or child. Solidity documentation cautions that using Solidity does not by itself guarantee correctness or security: software, compiler, and platform bugs remain possible, and practices such as review and testing are recommended. Keep the compiler and build configuration explicit, review the child’s constructor and the factory’s input handling, and avoid treating a successful deployment as proof that the broader application behaves as intended.

## Sources and references

- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
