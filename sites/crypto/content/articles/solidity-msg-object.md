---
title: "Solidity msg object: Meaning, Fields, and Context"
description: "Learn what the Solidity msg object exposes, how its common fields describe a call, and why sender, value, and data must be read in context."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity msg object"
owned_question: "What is Solidity’s `msg` object, what information does it expose to a contract, and how should developers interpret its main fields?"
risk_level: "medium"
---

Solidity’s `msg` object exposes information about the current call context, including the immediate caller, any native currency attached to the call, and the call’s input data. Read those fields as details of the current execution, not as persistent contract state or a guaranteed record of the original user.

## What the Solidity msg object represents

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. On Ethereum, a contract has persistent state and executable functions at an on-chain address. The `msg` object is not that stored state: it provides context for the call currently being handled. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)

Developers do not declare `msg` as an ordinary user-defined variable. Solidity provides it within contract code, where its fields can be read to understand aspects of the current interaction. Its presence does not, by itself, identify a human being or provide a complete history of the steps that led to the call.

## The main fields: `msg.sender`, `msg.value`, and `msg.data`

`msg.sender` is the address associated with the immediate caller in the current call context. If an externally owned account calls a contract directly, that account is the immediate caller. If another contract calls the function, the calling contract is the immediate caller instead. The field answers who called this function at this point in execution; it does not necessarily identify an earlier initiator.

`msg.value` is the amount of native currency attached to the current call. It is relevant when the function and call context allow value to be sent. It is not the contract’s balance, and its existence as a field does not mean that every function call carries currency.

`msg.data` is the input data supplied with the call. For a function invocation, it contains encoded call information rather than a ready-made list of named arguments. The receiving code interprets that data in the context of the function being invoked. For a developer reading source, the practical distinction is that call data is an encoded payload, not automatically a set of human-readable values.

The fields therefore answer different questions: `msg.sender` concerns the immediate caller, `msg.value` concerns currency attached to the call, and `msg.data` concerns the input payload. None should be confused with the contract’s persistent state.

## How call context affects `msg.sender`

To interpret `msg.sender`, trace the call that reached the function being read. A user may call one contract, and that contract may then call another. In the receiving contract, the immediate caller is the contract that made that later call. The original user is not automatically preserved as `msg.sender` across the contract-to-contract interaction.

This distinction matters whenever code uses the caller’s address to choose a behavior. The value of `msg.sender` refers to the immediate caller at that point in execution. Whether that is the intended address depends on the interaction’s call path. It should not be treated as proof of who initiated an earlier step or as proof of a person’s identity.

The same context-based reading applies to the other fields. Interpret `msg.value` and `msg.data` as information about the call currently being handled, rather than assuming they describe a previous call in a sequence.

## Common interpretation mistakes

Do not assume `msg.value` is meaningful in every function or that it always indicates a payment. Check the function’s purpose and the current call context before drawing conclusions from the field. A field being available does not mean every call uses it in the same way.

Do not treat `msg.data` as if it were already a decoded argument list. It is encoded input, and its meaning depends on the function being invoked and the receiving code’s interpretation. When reading a contract, distinguish the raw call payload from the values the function uses.

Do not assume `msg.sender` always names the original end user. A contract can be the immediate caller of another contract. Caller identity should be interpreted in the actual call path; this explanation does not prescribe an access-control design or recommend substituting another identity field.

Finally, the discussion here is conceptual, not a substitute for checking the Solidity documentation applicable to a project’s compiler version and execution context. Avoid extending these basic descriptions into claims about every possible call pattern.

## A compact example of reading `msg`

This illustrative fragment reads the immediate caller and the value attached to a call:

```solidity
function inspectCall() external payable returns (address caller, uint256 attached) {
    caller = msg.sender;
    attached = msg.value;
}
```

The returned `caller` is the immediate caller of this invocation. If another contract makes the call, that contract is the caller represented here. `attached` reports the native currency attached to this invocation; it is not the contract’s stored balance. Neither return value establishes that the caller is an end user or records a lasting payment by itself.

The fragment is an illustration of reading two fields, not a complete contract or an access-control pattern. When inspecting Solidity code, first identify which call is executing; then interpret `msg.sender`, `msg.value`, and `msg.data` in that context. This keeps the distinction clear between current-call information and persistent contract state.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
