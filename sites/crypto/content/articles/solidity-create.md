---
title: "Solidity create: Deploy a Contract from Another Contract"
description: "Learn how Solidity create deploys a contract from another contract, how to pass constructor arguments, and what to check when deployment fails."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity create"
owned_question: "How does Solidity’s CREATE operation deploy a contract from another contract, and how can developers verify the result?"
risk_level: "medium"
---

Solidity’s `CREATE` operation lets a contract deploy another contract by executing its creation bytecode; the new contract’s constructor runs as part of that creation. To verify the result, check the returned contract reference and address, then inspect the deployed contract’s expected state in the intended development or node environment. The available evidence here does not establish the exact address-derivation formula or specific failure conditions, so this guide avoids stating those details as protocol facts.

## What Solidity CREATE does

A deployed smart contract is a program in blockchain state that can be invoked through transaction requests. In Solidity, a contract can initiate creation of another contract; this is different from an ordinary call to a function on an already deployed contract. The new contract’s constructor executes during creation, using the initialization code and constructor data supplied for that deployment.

The immediate creator in this pattern is the contract executing the creation expression. If a user calls a factory contract and that factory creates a target contract, the factory—not the user’s account—is the target’s immediate creator. This distinction matters when reviewing the deployment flow and the address reported by the result.

The `CREATE` operation is distinct from `CREATE2`, which is outside this guide’s scope. Do not apply assumptions about one creation operation to the other.

## Solidity create: Build a minimal deployment example

The following is an illustrative pattern, not a tested or production-ready deployment recipe. The available evidence does not specify a Solidity compiler version or establish that this particular snippet was compiled. Before using code, select and record a compiler version, compile the example in the intended environment, and review any compiler diagnostics.

```solidity
// Illustrative only; no compiler version has been tested here.
pragma solidity ^0.8.0;

contract Greeting {
    string public message;

    constructor(string memory initialMessage) {
        message = initialMessage;
    }
}

contract GreetingFactory {
    function createGreeting(string memory initialMessage)
        external
        returns (Greeting deployed)
    {
        deployed = new Greeting(initialMessage);
        require(address(deployed) != address(0), "creation failed");
    }
}
```

The expression `new Greeting(initialMessage)` requests creation of a `Greeting` instance. The argument is passed to the target’s constructor, where it initializes `message`. In this example, the function returns a typed contract reference, `deployed`; the address can be obtained with `address(deployed)`.

The `require` illustrates a defensive check before the function returns. It does not prove the deployment succeeded in every possible execution environment, nor does it validate the target contract’s behavior. Because the code has not been tested against a stated compiler and execution setup, treat it as a syntax illustration. Compile and test an equivalent example before publication or use.

## How the new contract address is determined

For a `CREATE` deployment, the relevant creator is the contract that executes creation. The created contract receives its own address; it does not inherit the factory’s address. Thus, in the example, `address(deployed)` refers to the new `Greeting`, while `address(this)` inside the factory would refer to the factory itself.

The approved evidence for this article does not include an authoritative specification of the exact `CREATE` address-derivation formula or the nonce details needed to calculate it. Therefore, do not rely on a hand-calculated address based on this guide. Read the actual returned address and confirm it in the intended development or node environment. This keeps verification tied to the result of the execution rather than an unsupported prediction.

A contract deployment is a transaction-level state change. On Ethereum, deployment uses a transaction containing compiled contract bytecode and constructor data, consumes gas, and creates a contract at a new address after successful inclusion. That transaction-level description is separate from the factory’s source-code expression: the factory’s execution requests creation as part of its own execution flow.

## Handle creation failures and verify deployment

A factory should not use a returned contract reference as though it were valid without checking the creation result. The example checks that the address is nonzero before returning. Keep this check proportionate: it is a guard on the returned reference, not a general proof of correctness or security.

Use a verification sequence suited to the environment:

1. **Compile the target and factory.** Record the compiler version and inspect diagnostics. The example’s pragma is illustrative and does not establish which compiler was actually used.
2. **Exercise the factory call.** Supply constructor input and confirm that the creation flow completes in the chosen development or node environment.
3. **Inspect the returned reference.** Confirm that the factory returns a nonzero address, then record that address as the target contract’s address.
4. **Check expected state.** Read the target’s `message` value and compare it with the constructor input. This checks a specific observable outcome, not every possible behavior.
5. **Review execution status.** A transaction can be included while reporting failed execution, so inclusion alone is not enough to conclude that a state-changing interaction completed successfully.

Creation can fail, but the evidence available for this article does not enumerate the exact `CREATE` failure cases or specify their return behavior in detail. Avoid treating the illustrative `require` as a complete account of failure semantics. Consult the relevant Solidity and EVM technical references for the exact rules before building failure-sensitive logic.

## Review risks before using a contract factory

The small example demonstrates only how a factory can supply a constructor argument and return a contract reference. It does not establish that the factory is appropriate for a production system, that the constructor input is trustworthy, or that the resulting contract is secure. Programmed behavior depends on the code and its inputs; those require separate review.

Review authorization and input handling in both the factory and target contract. Test the expected creation path and relevant failure cases under the intended compiler and execution environment. The OWASP Smart Contract Security Verification Standard provides a structured framework for designing, building, and testing EVM-based smart contracts and decentralized applications, but its published standard is an early version and should be supplemented with project-specific threat modeling and review.

A successful deployment check answers a narrow question: whether the intended creation flow produced a contract reference and observable state in the environment examined. It does not, by itself, establish that the application behaves correctly in all cases or that the contract is secure.

## Sources and references

- [Deploying Smart Contracts](https://ethereum.org/developers/docs/smart-contracts/deploying/) — ethereum.org; retrieved 2026-10-19.
- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
