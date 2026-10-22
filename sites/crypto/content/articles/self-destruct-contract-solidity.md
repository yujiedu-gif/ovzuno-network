---
title: "Self destruct contract solidity: EVM behavior and current rules"
description: "Learn what self destruct contract solidity means under current EVM rules, including code and storage behavior, balance transfers, and the creation-transaction caveat"
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Solidity selfdestruct", "EIP-6780", "contract deletion semantics"]
author: "editorial_team"
primary_keyword: "self destruct contract solidity"
owned_question: "What does `selfdestruct` do in Solidity under current Ethereum execution rules, and what code, storage, and balance effects should developers account for?"
risk_level: "high"
---

In Solidity, `selfdestruct` invokes an EVM operation that transfers the executing account’s balance; it should not be assumed to erase a contract. The available evidence here does not establish EIP-6780’s current Ethereum rules, its same-transaction creation exception, or the precise effects on code and storage. Developers should verify those details against the protocol rules for the network and execution context they are reviewing.

## What `selfdestruct` means in Solidity and the EVM

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. That general definition does not prescribe one network’s execution or deletion rules. Nor does the Solidity keyword, by itself, establish what a chain will do when the operation executes. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

For Ethereum smart contracts, deployment and execution are constrained by gas, and contracts cannot directly retrieve off-chain facts without an oracle mechanism. These constraints are separate from the question of what `selfdestruct` does to a contract’s account. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

The term “deletion” can obscure distinct questions: whether an operation transfers balance, whether code remains available, and whether stored data remains. Evidence for one effect does not establish the others. The allowed evidence does not document the opcode’s beneficiary handling or its code and storage effects, so those particulars should not be inferred here.

## How EIP-6780 changed contract deletion semantics

The article’s requested account of EIP-6780—including the rule for contracts that were not created in the same transaction and the exception for contracts created and self-destructed within that transaction—is not established by the allowed evidence. It would therefore be inaccurate to state those details as confirmed protocol behavior in this draft.

The same evidence boundary applies to whether the rule is active on a particular Ethereum network or fork. A reviewer should consult that network’s applicable protocol specification and implementation documentation before concluding that code or storage persists, or that a same-transaction exception applies. Ethereum behavior should not be generalized to other chains or layer 2s without their own evidence.

## What happens to code, storage, and balance

Treat balance movement, code availability, and stored state as separate items to verify. The evidence authorized for this article does not specify whether `selfdestruct` transfers the entire balance, how the beneficiary is selected, whether code or storage is removed, or how later calls and state reads behave. Those effects depend on execution rules that must be checked directly rather than derived from the operation’s name.

A general point about smart-contract execution is that participating blockchain nodes must derive the same result, with execution results recorded on the blockchain. That describes deterministic execution in general; it does not supply the missing opcode-specific result for a particular network. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

For a technical review, record the questions separately: What account executes the operation? What balance movement do the relevant rules specify? What do those rules say about code and storage after execution? What do subsequent calls observe? Do not treat an answer to one as proof of the others.

## Reviewing self destruct contract solidity in existing code

Start by locating every reachable use of `selfdestruct` in the source and identifying the execution path that can invoke it. Then establish the target chain and its active rules for the relevant execution. The evidence available here does not substantiate specific Solidity compiler warnings, inherited or delegated-call behavior, or how creation and destruction within one transaction are treated; verify those points in current language and network documentation before relying on them.

Next, compare the code’s assumptions with its observable behavior. If a comment, test, or integration expects a contract to disappear, storage to be cleared, or funds to be recovered, treat that expectation as unverified until the applicable rules establish it. A test result is only useful for this question when its network rules and execution context match the behavior under review.

For structured security review, the OWASP Smart Contract Security Verification Standard provides a framework for designing, building, and testing EVM-based smart contracts and decentralized applications. It is an early version and should be supplemented with project-specific threat modeling and review; it does not replace protocol documentation for determining opcode semantics. [source](<https://owasp.org/projects/smart-contract-security-verification-standard>)

## Risks, limits, and evidence to verify

Older examples or comments may describe deletion-related behavior without establishing that the same rule applies to the network and execution context under review. Confirm the applicable protocol specification and implementation documentation, and check the relevant Solidity documentation for syntax and compiler-specific guidance. The allowed evidence does not resolve those sources’ current contents or establish a universal rule.

This explainer therefore does not confirm EIP-6780’s precise behavior, the same-transaction creation exception, or the resulting code, storage, and balance state. It also does not establish that assets can be recovered, that a contract is secure, or that any implementation is legally or tax compliant. Those conclusions cannot be inferred from the Solidity construct alone.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
