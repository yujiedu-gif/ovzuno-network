---
title: "Solidity calling another contract: interfaces, execution, and failure behavior"
description: "Learn how Solidity calling another contract works through interfaces, including target addresses, arguments, return values, and how failed calls affect execution."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["interface", "external function call", "return values", "revert propagation"]
author: "editorial_team"
primary_keyword: "solidity calling another contract"
owned_question: "How does a Solidity contract call a function on another contract through an interface, and what execution and failure behaviors should a developer account for?"
risk_level: "medium"
---

A Solidity contract calls a function on another deployed contract by invoking it through an interface-typed reference to the target’s address. The caller passes arguments matching the declared parameter types and can use a return value if the call succeeds. If the target call reverts, failure ordinarily interrupts the caller’s current execution unless the caller uses an appropriate mechanism to handle it. The interface describes how to form and interpret the call; it does not verify the target’s identity or prove what its code will do.

## What happens when one Solidity contract calls another?

An ordinary external call is a function invocation from one contract to another contract at an address. It is not a direct connection between source files: the interaction occurs between deployed contracts during transaction execution. A user account can invoke a contract function by submitting a transaction to the deployed contract, and that contract can invoke another contract as part of its execution. [claim_eth_transaction_invocation]

The caller transfers execution control to the target for the call. The target’s code runs as the called contract, rather than as code in the caller’s contract context. This article covers that ordinary call pattern, not `delegatecall`, which is a distinct mechanism and outside the scope here.

Because control passes to another contract, the interaction is not necessarily a one-way sequence. The called contract may call back before the original operation is complete, creating an interaction the caller’s design must account for. This is a property to consider when reasoning about execution order, not a claim that every target will call back. [claim_external_call_control]

The call also crosses an encoding boundary. Solidity’s application binary interface, or ABI, defines how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. The interface declaration gives the caller a typed description for that boundary. [claim_solidity_abi]

## How an interface describes the external function

A Solidity interface declares the function signature that the caller expects to invoke. A signature specifies the function name and parameter and return types. The interface describes the callable shape, rather than supplying the function’s implementation.

For example, the caller may declare a function named `compute` that accepts a `uint256` and returns a `uint256`. When the caller uses that interface to form a call, the ABI rules determine how the selector and argument are encoded and how returned data is interpreted. [claim_solidity_abi]

A reference can be made by converting or otherwise treating a target address as the interface type. That type tells the caller how it intends to call the address. It does not establish that the address contains the intended contract, that the deployed code matches the interface, or that the function’s behavior has the meaning the caller expects. Those are separate assumptions about the address and implementation.

This distinction matters even when a call is syntactically valid. The ABI describes the shape and encoding of an interaction, not the identity or correctness of the code at the other end. A developer should therefore verify the expected target and interface using relevant project or deployment information rather than treating the type declaration as proof. [claim_solidity_abi]

## A minimal call flow: address, arguments, and return values

A basic typed call has four parts: identify the target address, refer to it through the interface type, pass arguments that match the declared signature, and handle the returned value. The example below shows only the pattern. It is illustrative, not a claim that this code has been compiled, tested, audited, or deployed.

```solidity
interface ITarget {
    function compute(uint256 input) external returns (uint256);
}

contract Caller {
    function request(address target, uint256 input)
        external
        returns (uint256 result)
    {
        result = ITarget(target).compute(input);
    }
}
```

In `request`, `target` is the address the caller will contact. `ITarget(target)` expresses the expected interface at that address. The `compute` invocation passes `input` as the function argument. Its declared type must match the interface signature used by the caller. Solidity’s ABI rules govern the encoding of the selector and arguments and the interpretation of returned data. [claim_solidity_abi]

If the call completes normally and provides return data in the expected form, the example assigns the decoded value to `result`. That assignment does not tell the caller what the number means. The developer must understand the target’s documented behavior and decide whether the returned value is appropriate for the caller’s next step. The interface gives a type-level expectation; it does not supply semantic guarantees about the implementation.

Before using an example in a project, check its syntax and behavior against the Solidity compiler version selected for that project. No compiler version is specified here, so the snippet should be read as an explanation of the call’s shape, not as a version-verified implementation. In particular, the interface declaration and call expression are not substitutes for checking that the deployed target has the intended code and behavior.

## What happens when the external call fails?

In an ordinary high-level call such as the example, a target revert ordinarily causes the caller’s current execution to revert as well. The shown function has no separate failure-handling branch. If the called function fails, the caller does not proceed as though it received a normal return value from that invocation.

Failure details should be described in terms of the calling mechanism and how its result is handled. Solidity’s ABI includes error encoding, but that fact alone does not determine how every caller exposes, changes, or handles failure information. Avoid assuming that all call forms have identical behavior. [claim_solidity_abi]

A low-level call pattern can expose a success result for the caller to inspect, but checking that result is not the same as confirming that the intended business operation occurred. The caller must decide what to do when a call fails and what evidence it needs before continuing. This article’s typed example leaves that decision implicit, so it should not be treated as a complete error-handling design.

Execution tools can help inspect nested call behavior. For example, Forge call traces can show nested contract calls, returns, reverts, emitted logs, deployments, and reported gas use during tests or scripts. A trace can help locate where execution stopped, but it explains an execution path; it does not by itself prove that the contract logic is correct. [claim_foundry_traces]

## Checks before relying on a contract interaction

Use a bounded review of the call boundary before depending on its outcome:

- **Target address:** Confirm that the address is the intended deployment using authoritative project or deployment documentation. An interface-typed reference does not authenticate the address.
- **Interface signature:** Compare the function name, parameter types, and return types with the expected interface. ABI compatibility concerns encoding and decoding, not the meaning or correctness of the target’s operation. [claim_solidity_abi]
- **Arguments:** Check that the values supplied represent the inputs the target expects. A type match alone does not establish that the input has the intended meaning.
- **Return value:** Determine what the target’s implementation says the returned data represents and how the caller will use it. Do not infer behavior from the return type alone.
- **Failure handling:** Decide whether a revert should stop the caller’s execution or whether the calling code needs an explicit way to detect and handle failure. The illustrative function has no separate handling path.
- **Execution control:** Account for control passing to the target and for the possibility of a callback before the original operation completes. [claim_external_call_control]

These checks help identify assumptions in an interface-based call. They do not establish security, correctness, recovery options, or compliance. A typed interface makes the expected call structure explicit; the address, deployed implementation, inputs, return interpretation, and failure behavior remain distinct matters for the developer to verify.

## Sources and references

- [Security Considerations](https://docs.soliditylang.org/en/latest/security-considerations.html) — Solidity Documentation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Understanding Traces](https://getfoundry.sh/forge/traces) — Foundry Documentation; retrieved 2026-10-19.
