---
title: "Solidity bool default value: what an unassigned Boolean contains"
description: "Learn the Solidity bool default value for unassigned state variables, how local-variable initialization differs, and why declaration context matters."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity bool default value"
owned_question: "What value does a Solidity bool have before it is explicitly assigned, and how does that depend on where it is declared?"
risk_level: "low"
---

An unassigned Solidity `bool` declared as a contract state variable has the language-defined initial value `false`. A function-local `bool` is different: do not assume that the state-variable default applies to it. Check the declaration’s context and the documentation for the Solidity version in use before relying on initialization behavior.

## Solidity bool default value for state variables

A state variable is declared in a contract, outside a function body. It represents part of the contract’s state, rather than a temporary value declared inside a function. For the question covered here, the key rule is that a state-variable `bool` starts as `false` if no other initial value is supplied.

For example:

```solidity
pragma solidity ^0.8.0;

contract Example {
    bool public enabled;
}
```

In this illustrative declaration, `enabled` is a state variable and is not given an explicit initializer. Its initial value is `false`. The pragma states a compiler-version range; it does not identify one exact compiler release. For a version-specific conclusion, check the applicable Solidity language documentation. This example illustrates the declaration context and rule; it is not presented as compiled or tested code.

A language-defined starting value is not the same as a value that remains unchanged forever. Contract code can assign a different value during construction or later execution. When reading a particular contract, distinguish “what value does this declaration start with?” from “what value does the contract hold after its code has run?”

Solidity state variables also have defined storage-layout rules. Those rules describe how state variables are arranged in storage, but a storage-layout question is separate from identifying the initial value of a Boolean. Do not treat layout details as a substitute for checking the initialization rule that applies to the declaration.

## Why local bool variables are different

A local variable is declared within a function or another local scope. It is not a contract state variable, so the state-variable default should not be applied to it by assumption. In particular, an example showing a state declaration such as `bool enabled;` does not establish the behavior of a similarly written declaration inside a function.

For local variables, consult the Solidity documentation for the relevant language version and follow the compiler’s requirements. In code you are reading, look for an explicit assignment before the local variable is used. If the applicable version’s rule is not known, do not infer that an uninitialized local `bool` is `false` merely because an unassigned state-variable `bool` starts that way.

This distinction is about declaration context, not the spelling of the type. The same type name can appear in different places in a contract, and the place where a variable is declared determines which language rules need to be checked. Keep the categories separate when explaining, reviewing, or modifying code.

## How to read an unassigned Boolean in contract code

A short inspection can clarify which question you need to answer:

1. **Find the declaration.** Determine whether it appears at contract scope or inside a function. The former is state; the latter is local.
2. **Check for an explicit initializer.** A declaration may assign a value where it is written, so it may not be an unassigned declaration at all.
3. **Look for later writes.** Review the constructor and relevant execution paths for assignments that can change a state variable or initialize a local variable before it is read.
4. **Trace the read.** Identify where the Boolean is used and which assignments can occur before that point.
5. **Confirm the Solidity version.** Use documentation for the applicable compiler version when the behavior depends on a version-specific language rule.

This sequence separates the initial value from the contract’s later state. A state variable’s initial value answers only how it begins under the language rule. A later assignment can change that value, so a declaration alone does not tell you what the contract holds at every point in its execution.

For a local variable, the practical check is different: determine whether it is initialized before use under the relevant compiler rules. Do not replace that check with the state-variable default. When the version or declaration context is unclear, resolve those details before drawing a conclusion about the value.

## What the default does not tell you

The value `false` by itself does not explain what a Boolean is intended to represent, whether contract logic later changes it, or whether the surrounding logic is correct. It is an initialization fact for the specified state-variable context—not a conclusion about the meaning or suitability of a flag.

Nor does an initial value alone establish the current value in a deployed contract. The current value depends on the applicable contract and what has happened in its execution. The narrow rule about an unassigned state-variable `bool` should not be expanded into a claim about every declaration or every point in a contract’s life.

For a clear answer, first classify the declaration as state or local, then check for an explicit initializer and subsequent assignments. If language-version behavior is material, consult the Solidity documentation for that version. This keeps the `false` default in its proper scope and avoids treating a local variable as though it were contract state.

## Sources and references

- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
