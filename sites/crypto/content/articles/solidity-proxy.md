---
title: "Solidity proxy: how call routing and upgrades work"
description: "Learn how a solidity proxy routes calls to an implementation, how delegatecall affects storage and execution context, and what to review before upgrades."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["proxy contract", "upgradeable smart contract", "implementation contract", "proxy storage", "delegatecall"]
author: "editorial_team"
primary_keyword: "solidity proxy"
owned_question: "How does a Solidity proxy route calls to an implementation contract, and what are the main storage and upgrade risks?"
risk_level: "high"
---

A Solidity proxy lets an application call one contract address while the proxy routes execution to logic held in a separate implementation contract. In a delegatecall-based design, that implementation’s code runs against the proxy’s storage context. This indirection can support changes to logic without changing the address users call, but it makes storage compatibility and control over implementation changes central review concerns. Routing, initialization, and upgrade rules depend on the particular design.

## What a Solidity proxy does

A proxy is a contract that serves as an entry point for calls; an implementation contract supplies code that the proxy can route execution to. The proxy and implementation have distinct addresses and roles. In an upgradeable arrangement, an application typically targets the proxy address, while the proxy’s routing mechanism determines which implementation handles the call.

This separation can allow a system to change the logic used at an address without asking applications to call a different address. It does not establish that every proxy is upgradeable, that an upgrade is safe, or that users can assume the implementation remains unchanged. Those properties depend on the proxy’s actual routing and control mechanisms.

On Ethereum, an externally owned account can invoke a contract function by submitting a transaction to the deployed contract. In a proxy arrangement, the application’s transaction is directed to the proxy, and the proxy then routes execution according to its design. The application also needs an ABI that matches the deployed contract interface and network address. An ABI, or application binary interface, specifies how function selectors and arguments, return values, errors, and events are encoded between applications and EVM contracts. It describes the interface, not which implementation a proxy currently selects. [source](<https://ethereum.org/developers/docs/smart-contracts/>) [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

## How calls reach the implementation

A simplified call path helps separate the application’s destination from the code that handles the request:

1. The application prepares a function call using the interface it expects.
2. The transaction or call reaches the proxy address.
3. The proxy’s routing mechanism directs execution to the implementation selected by that design.
4. The implementation’s code handles the call in the context established by the proxy mechanism, and the result is returned through the proxy path.

In a delegatecall-based arrangement, the essential point is that the code comes from the implementation while execution uses the proxy’s storage context. State read or written during that delegated execution is therefore associated with the proxy rather than the implementation’s own storage. This differs from calling the implementation directly, which executes against the implementation contract itself.

Do not infer every message or call detail from the phrase “proxy.” The available evidence supports the proxy-storage distinction but does not specify the exact treatment of caller identity or transferred value for every proxy design. Those details should be verified in the specific routing code and its documentation. Likewise, the general pattern does not identify a particular fallback procedure, implementation-selection mechanism, or upgrade authorization rule.

## Proxy storage and implementation compatibility

A proxy’s storage context makes the implementation’s assumptions about state locations important. Solidity follows deterministic layout rules for state variables, including slot packing, inheritance, arrays, mappings, and structs. That layout is part of the contract’s external storage interface. [source](<https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html>)

If a new implementation interprets existing storage differently, it can read values from unexpected locations or write where other state is stored. Compatibility review therefore needs to examine the actual layouts and inheritance structure, rather than relying only on matching variable names or function signatures. Compiler version, inheritance, custom layouts, proxy use, and language changes can affect the precise analysis, so reviewers need the relevant source and build details for the contracts under review.

Initialization should be treated as a separate design question. The proxy and implementation are distinct contracts, so a reviewer should determine which contract’s state is initialized, how initialization is invoked, and how the design handles unintended repeat initialization. The allowed evidence does not establish one universal initialization pattern or safeguard. Check the specific contracts and their documented behavior instead of assuming that deploying a proxy automatically establishes the intended state.

## Upgrade authority and failure modes

An upgrade changes which implementation supplies logic, but the mechanism and authority for changing that selection vary by design. Reviewers should identify who or what can alter the implementation reference and how the deployed controls restrict that action. A proxy pattern alone does not promise a particular approval process, delay, reversibility, or recovery path.

For one specific case, OpenZeppelin’s documented proxy-based upgrade model requires initializer discipline and compatible storage layout across implementations to avoid takeover or corrupted state. This is a constraint of that model, not a claim that all proxies use the same mechanics or protections. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>)

Three failure scenarios illustrate why the authority and process matter. If someone can change implementation selection without the intended authorization, calls may reach logic the application or users did not expect. An authorized upgrade can still introduce faulty behavior. And upgrade controls that are misconfigured or inaccessible can prevent an intended change or recovery. These are risks to investigate, not conclusions about any particular deployment.

A role check, upgrade function, or written procedure is not, by itself, proof that controls are correctly configured or that an upgrade will succeed. The review must connect the documented process to the actual code and authority that can change the implementation.

## A review checklist for proxy-based contracts

Use these questions to trace the design without assuming that a proxy label guarantees particular properties:

- **Call destination:** Which address does the application target, and does its ABI match the deployed interface and network address?
- **Implementation selection:** What mechanism routes calls to an implementation, and how can the selected implementation be identified?
- **Upgrade authority:** Who or what can change that selection, and what code enforces the relevant authorization?
- **Storage compatibility:** Have existing and proposed layouts been compared, including inheritance and applicable compiler and build details?
- **Initialization:** Which contract’s state is initialized, how is initialization reached, and what behavior prevents or handles repeat initialization in this design?
- **Upgrade process:** What sequence does the project document, and do the deployed contracts and controls match it?
- **Review evidence:** Are tests, access controls, and upgrade procedures documented and available for review? Their presence can inform the assessment, but does not prove correctness or security.

The practical distinction is that the proxy is the call entry point, while the implementation provides code that can execute against proxy state. An upgrade changes the logic selected for that path; it does not erase the need to check the routing mechanism, state layout, initialization behavior, and authority to make the change. Because those details are pattern-specific, conclusions should be limited to the contracts and controls actually examined.

## Sources and references

- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
