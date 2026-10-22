---
title: "Solidity interface example: define and call an external contract"
description: "Use this solidity interface example to declare a contract interface, call a compatible function, and understand return types and external-call caveats."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity interface example"
owned_question: "How do you define and use a Solidity interface to call a contract function, and what assumptions should the caller verify?"
risk_level: "medium"
---

A Solidity interface lets a caller describe an external contract function and invoke it through a contract address. The caller must use a declaration compatible with the deployed contract’s ABI—the encoding rules for function selectors, arguments, return values, errors, and events—and must not assume that matching signatures prove the target behaves as intended. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

## What a Solidity interface declares

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) In Solidity, an interface provides function declarations that describe how another contract can be addressed; it does not supply those functions’ implementation logic. The caller uses the declared types to form a call to the target address. That description is useful only if it matches the target’s actual interface.

A simple illustration is a read-style function that accepts an account address and returns an unsigned integer. The interface tells the caller the function name and the types expected at each end of the call. It does not establish what the returned integer means, whether the target enforces a particular policy, or whether the address points to the intended contract.

## Solidity interface example: a minimal contract call

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ICounter {
    function countOf(address account) external view returns (uint256);
}

contract CounterReader {
    ICounter public counter;

    constructor(address counterAddress) {
        counter = ICounter(counterAddress);
    }

    function readCount(address account) external view returns (uint256) {
        return counter.countOf(account);
    }
}
```

This example is illustrative, not a claim about any particular deployed contract. `ICounter` declares the external function signature: one `address` input and one `uint256` return value. The `view` modifier declares that the function is intended to read state rather than modify it. `CounterReader` converts the supplied address to the interface type, then invokes `countOf` through that typed reference.

The interface type provides the call description; it does not deploy `ICounter` or verify the address. For a state-changing call, the caller would use an interface declaration appropriate to the target function and invoke it from a non-view function. An Ethereum user account can invoke a smart-contract function by submitting a transaction to the deployed contract. [source](<https://ethereum.org/developers/docs/smart-contracts/>) The interface alone does not determine how the target changes state or whether the caller is authorized.

## Match the interface to the target ABI

Before relying on an interface call, check the target contract’s authoritative interface information and confirm that the function name, input types, output types, and relevant mutability match. Solidity’s ABI specifies how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>) A declaration that differs from the deployed interface can produce an incompatible call or an incorrect interpretation of returned data.

Verify the address separately. A source-level interface can be syntactically correct while the configured address points to a different contract, a different deployment, or no compatible implementation. Use deployment records or other reliable project information to check the intended network and target address. The interface declaration itself cannot establish either fact.

Even when the call is ABI-compatible, compatibility is not behavioral assurance. The ABI describes encoding, not the meaning or correctness of the implementation. Contracts can call or reuse independent on-chain components through public interfaces, but each dependency adds behavior, upgrade, permission, availability, and economic assumptions. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>) Review the target’s available implementation and documentation to understand what the function actually does and what assumptions its result requires.

## Handle return values and failed calls

The return type in the interface tells Solidity how to interpret the returned data. It should match the deployed function’s ABI. If the target does not return the data the caller expects, decoding may fail; if it returns a value that is correctly encoded but has different semantics than expected, the call may complete while the caller draws a wrong conclusion. A declared `uint256`, for example, is only a type—not a guarantee that the number represents a balance, count, or other particular measure.

External calls can also fail. A target may revert, and a failure can propagate to the caller unless the calling code uses a low-level call pattern and explicitly handles the failure result. This example uses a typed external call and does not add custom failure handling, so it should not be read as a complete error-management pattern. Decide what the surrounding application should do when a call fails, and avoid treating a returned value as trustworthy solely because execution completed.

## Checks before using an interface in production

Use a short verification sequence before integrating the call:

1. **Confirm the deployment.** Check the intended network and target address against reliable project or deployment records.
2. **Compare the interface.** Match the function name, inputs, outputs, and mutability to authoritative information for the deployed contract.
3. **Inspect the behavior.** Where implementation information is available, review the function’s state changes, access restrictions, and assumptions about external inputs.
4. **Exercise expected outcomes.** Test both the intended call and relevant failure cases using the compiler version and tooling selected for the project. Testing can check those cases; it does not by itself prove the target is safe or correct.

The practical boundary is simple: an interface makes a typed external call possible, while the caller remains responsible for verifying the target, compatibility, and meaning of the result. A matching declaration is a starting point for interaction—not proof of implementation or behavior.

## Sources and references

- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
