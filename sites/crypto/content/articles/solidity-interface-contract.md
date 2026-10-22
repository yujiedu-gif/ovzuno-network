---
title: "Solidity interface contract: declarations and external calls"
description: "Learn what a solidity interface contract declares, how it differs from an implementation, and how Solidity uses it to make typed calls to another contract."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity interface contract"
owned_question: "What is a Solidity interface contract, what does it declare, and how is it used to call another contract?"
risk_level: "medium"
---

A Solidity interface contract is a type declaration that describes functions and events another contract is expected to expose. Solidity code can use that type to make a structured call to a contract at an address. The interface does not provide the called contract’s implementation or prove that the address behaves as declared.

## What a Solidity interface contract represents

A Solidity interface describes a contract boundary: the callable functions and event information that another piece of code expects to interact with. A deployed Ethereum contract has persistent state and executable functions at an on-chain address, and it can emit events for applications to process. An interface can describe selected functions and events from that surface without containing the target’s state or executable logic. [source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)

The practical value is that the caller can express an expectation in Solidity’s type system. Instead of handling an address alone, the caller can refer to a named function, its input types, and its expected return type. The interface makes that expectation visible in source code and gives the compiler a description to use when forming the call.

This description is not a runtime inspection of the target. A type conversion from an address to an interface type does not establish that the address is correct, that code is deployed there, or that any code at the address follows the declared behavior. The interface describes how the caller intends to interact; the target’s deployed code determines what happens when the interaction reaches it.

## What interfaces can declare—and what they cannot

An interface’s function declarations specify the callable shape: a function name, parameter types, return types, and relevant attributes such as visibility and mutability. The declarations do not provide function bodies. An interface can also declare events to describe event information relevant to the expected contract surface. These elements define what a caller can express through the interface, not how the target computes a result.

For example, `function readValue() external view returns (uint256);` declares a function named `readValue` that takes no arguments and is expected to return a `uint256`. The declaration does not say where a value is stored or how the target obtains it. The contract providing the function is responsible for its implementation.

An interface is also not a container for the target contract’s persistent variables. A function declaration may describe a way to request information, but it does not declare or create the target’s underlying data. Keeping this distinction clear prevents a common misunderstanding: an interface is not a partial implementation that becomes executable when assigned an address.

Nor does an interface independently prove that a target supports the declarations. It describes the caller’s expectations at the source-code boundary. Runtime behavior still depends on the actual address and the code reached by the call.

## How to use an interface for a contract call

A common pattern is to declare an interface, convert a target address to that interface type, and call one of its declared functions. This compact example is illustrative; it is not presented as a tested or deployed contract:

```solidity
interface IValueReader {
    function readValue() external view returns (uint256);
}

contract ReaderClient {
    function readFrom(address target) external view returns (uint256) {
        return IValueReader(target).readValue();
    }
}
```

`IValueReader(target)` gives the caller a typed reference for this interaction. It does not deploy an interface contract, move code to the address, or change the target. The next expression invokes the function as declared by the interface and treats the result as a `uint256`.

The interface signature also matters for the call’s representation. The Solidity ABI defines how function selectors and arguments are encoded between applications and EVM contracts, along with how return values, errors, and events are encoded. The interface and the deployed contract’s callable surface therefore need compatible encodings for the intended interaction. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

A function call written in a contract is not the same thing as a user’s top-level transaction. A user account can invoke a smart-contract function by submitting a transaction to the deployed contract. [source](<https://ethereum.org/developers/docs/smart-contracts/>) In either situation, the interface is a description used by the caller; it does not choose the target address or supply the function’s implementation.

The return declaration shapes how the caller handles the response, but it should not be mistaken for proof that the response is accurate or meaningful. The interface says what type the caller expects. It does not establish the target’s internal logic or the meaning of its returned value.

## Interfaces, inheritance, and implementations

An implementation is the contract code that supplies function behavior. An interface is a declaration of the functions and events that code may expect to encounter. A contract can use an interface as the basis for declaring that it provides the required functions, but the implementation still needs to supply the function bodies. Inheriting an interface does not turn its declarations into executable logic.

This relationship has two distinct uses. A contract author can use an interface declaration to state which functions an implementation must provide. Separately, a caller can use the interface type to describe calls to an existing address. The caller does not need to inherit from the target contract: it needs the relevant interface declaration and an address to call.

A compiler can check declarations within the source it compiles. That is a source-level compatibility check, not a guarantee about an arbitrary external address supplied later. The interface does not verify that the address points to the intended implementation or that the implementation’s behavior matches the caller’s assumptions.

This pattern is one part of smart-contract composition: contracts can call or reuse independent on-chain components through public interfaces. Each such dependency adds behavior and assumptions to the calling system. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>) An interface can make the boundary explicit, but it cannot remove the dependency or supply facts about the target that are not represented in the declaration.

## Call failures and practical limits

A typed call can still fail. The target may not provide a compatible function, or execution may fail while the call is being handled. Even when the call completes and data is returned, the interface alone does not prove that the result is correct or that the target acted as expected. The declaration governs the caller’s expectations; it is not a guarantee of execution success or target quality.

When integrating with a known contract, compare the interface declarations with the callable surface intended at the target address. Check that the interface and target use compatible ABI encodings, since the ABI governs how function selectors, arguments, return values, errors, and events are represented. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>) A mismatch can make an otherwise well-typed source call fail to match the intended interaction.

Keep the compile-time and runtime questions separate. At compile time, ask whether the caller’s code uses the interface consistently. At the call boundary, ask whether the intended address and deployed code correspond to that declaration. A successful type check answers the first kind of question; it does not independently answer the second.

Use an interface when code needs a typed description of another contract’s callable surface. Treat it as a declaration for the caller—not as an implementation, a runtime verification of the target, or a guarantee that an external call will behave safely or successfully.

## Sources and references

- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
