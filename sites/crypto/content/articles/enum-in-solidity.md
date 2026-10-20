---
title: "Enum in Solidity: What It Is and How to Use It"
description: "Learn what an enum in Solidity represents, how to declare and use enum values in a smart contract, and what to consider when handling defaults and conversions."
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["smart_contracts_dapps"]
tags: ["Solidity enum type", "enum values in Solidity", "Solidity enum example", "enum state variable Solidity", "Solidity enum conversion"]
author: "editorial_team"
primary_keyword: "enum in solidity"
owned_question: "What is an enum in Solidity, and how is it used in a smart contract?"
risk_level: "medium"
---

# What Is an Enum in Solidity?

An **enum in Solidity** is a user-defined type whose possible values are a finite, ordered set of names declared in the contract. Enums are useful when a value must represent one choice from a bounded set—for example, whether a record is `Open`, `Closed`, or `Settled`. Instead of treating those states as unrelated numbers or arbitrary text, an enum gives them named members that code can compare and assign.

Each member has an integer position determined by its place in the declaration, starting at zero. That ordering is relevant when interpreting conversions or when code and external applications rely on the numeric representation. A newly declared enum variable has the first declared member as its default. These details make the declaration more than a list of labels: it defines the valid choices and their order for that type.

This guide explains how to declare and use a Solidity enum, how to reason about its default and integer conversions, and what to review before using one in a contract. The example is illustrative, not a complete production implementation.

## What an enum means in Solidity

Solidity is a statically typed language with several categories of types, including value types, reference types, mappings, arrays, structs, enums, function types, and contract types. An enum is one of Solidity’s user-defined types. Its declaration establishes a finite set of named values, and a variable of that type represents one of those values.

For example, this declaration defines three members:

```solidity
enum Status { Open, Closed, Settled }
```

The names describe the options available through `Status`. Their positions follow the declaration order: `Open` is position zero, `Closed` is position one, and `Settled` is position two. In Solidity code, it is usually clearer to refer to a member by name—such as `Status.Closed`—than to make a reader infer its meaning from a number.

An enum is a fit for **bounded categories or states**: the permitted set is finite and known when the type is designed. It is not a general-purpose representation for arbitrary or unbounded data. If users need to supply values not known in advance, or if the set is expected to be open-ended, consider whether a different representation is more suitable.

The declaration answers a type-modeling question: “Which named values can this variable represent?” It does not, by itself, answer questions such as who can change the variable, which transitions are permitted, or what should happen when a particular state is reached. Those are separate contract behaviors that must be expressed and reviewed in the surrounding code.

## How to declare and use an enum

A contract can declare an enum and use it as the type of a state variable. Functions can compare that variable with named members and assign a different member when their logic calls for a change.

```solidity
pragma solidity ^0.8.20;

contract Example {
    enum Status { Open, Closed, Settled }

    Status public status;

    function close() external {
        if (status == Status.Open) {
            status = Status.Closed;
        }
    }
}
```

This compact example has four relevant parts:

1. **The declaration:** `Status` names the enum type, and the braces list its available members in order.
2. **The state variable:** `status` is declared as `Status`, so the example models that variable using the enum rather than an unrelated type.
3. **The comparison:** `status == Status.Open` checks whether its current value is the named `Open` member.
4. **The assignment:** when that condition is true, the function assigns the named `Closed` member to the variable.

The function does not assign a number directly. It uses names at the point of comparison and assignment, which makes the intended state easier to read. The type declaration supplies the finite set of choices; the function supplies one piece of behavior that uses those choices.

The example has deliberately narrow behavior. It shows an assignment when the current value is `Open`, but it does not define a complete state machine, establish who should be permitted to call the function, or specify all behavior for every possible state. It should not be read as a production-ready contract or as a security guarantee. Before using a similar pattern, a project must decide what each state means and what contract logic should apply to each state.

### Trace the example before extending it

A useful review exercise is to trace the variable’s value through the example without assuming that the function always changes it:

- At declaration, `status` has the first member’s default value, `Status.Open`.
- On a call to `close`, the condition compares the current value with `Status.Open`.
- If the condition is true, the assignment changes the value to `Status.Closed`.
- If the condition is false, the conditional block does not perform that assignment.

This trace separates the enum’s type-level choices from the function’s control flow. The enum says which named values exist. The `if` statement says when this particular function performs its assignment. Other functions could use the same type but implement different behavior, so reviewing the declaration alone is not enough to understand a contract’s state handling.

When building a larger example, make the state meaning and transition logic explicit rather than assuming that the enum enforces them. For each function that reads or writes the enum variable, ask which members it expects, what it does for each relevant value, and whether it can leave the variable unchanged. Those questions help expose incomplete behavior without implying that an enum automatically supplies transition rules.

## Enum defaults, ordering, and conversions

### The first member is the default

A newly declared enum variable defaults to its first listed member. With `enum Status { Open, Closed, Settled }`, a newly declared `Status` variable therefore starts as `Status.Open`. In the example, that means the initial value of `status` is `Status.Open` before a function changes it.

This is an important modeling detail. The first member is not merely the first label a reader sees; it is also the enum’s default value. When choosing member order, consider whether the first member is an appropriate default for a newly declared variable. If it is not, do not rely on the declaration to communicate a different initial state: review how the contract’s code establishes and handles its intended values.

### Positions follow declaration order

Enum members map to integer positions beginning at zero. The position changes when the declaration order changes. For the example, the correspondence is:

| Member | Position |
|---|---:|
| `Open` | 0 |
| `Closed` | 1 |
| `Settled` | 2 |

The names are useful for reading Solidity source, while the positions explain the ordering and conversion relationship. Do not assume that a position is a stable external identifier just because it is associated with a named member. If code or an integration depends on positions, that dependency needs deliberate design and review, particularly before changing the declaration.

### Integer-to-enum conversion has a range condition

An explicit conversion from an integer to an enum requires the integer to be within that enum’s valid range. For an enum with three members, the positions shown above describe the members’ valid range. A conversion should therefore be reviewed as a boundary-sensitive operation rather than treated as an arbitrary way to assign a value.

For example, when reviewing a conversion involving `Status`, ask:

- Which integer values can reach the conversion?
- Are those values within the range represented by the declared members?
- What happens at the lowest and highest valid positions?
- Can an input or intermediate value fall outside that range?

These are verification questions, not a substitute for checking the exact language behavior for the selected compiler version. Solidity documentation notes that compiler-version details matter for language limits and behavior. Check the official documentation that corresponds to the compiler version used by the project before relying on syntax or conversion details. This article does not claim that any particular conversion has been compiled or tested.

## When enums are appropriate—and their limits

An enum is a reasonable candidate when all permitted choices form a finite set that can be named in advance. A short status such as `Open`, `Closed`, and `Settled` is the kind of bounded model the type can express. The names also let contract code compare values in terms of the model rather than requiring readers to interpret bare positions.

A different representation may be worth considering when values are user-defined or the permitted set is expected to change. An enum declaration fixes the available names and their order for that type. Adding members changes the set; reordering them changes their positions. Code or integrations that assume particular members or positions may therefore need review when the declaration changes. This is a reason to examine dependent code and interfaces—not a claim that every change has the same effect in every project.

Enums also have a narrower role than a complete state machine. They describe a finite set of values, but do not specify which transitions are allowed. In the example, the function implements one conditional assignment. The enum itself does not establish that only a certain caller may make the change, nor does it define how all other states should be handled. Access control, validation, and transition behavior must be considered in the surrounding contract design; the enum alone does not provide them.

An application that communicates with an EVM contract uses the contract ABI for encoding function selectors, arguments, return values, errors, and events. The application must use an ABI that matches the deployed bytecode and interface. If an enum is exposed through a contract interface, include that interface relationship in the review. Do not infer that an application’s interpretation of a value is correct merely because its source uses a familiar member name; verify that the ABI corresponds to the deployed contract and the interface the application intends to use.

## Practical checklist

Before applying a Solidity enum, work through these questions:

1. **Is the set genuinely finite and known?** If the values can be user-defined or are expected to keep changing, reconsider whether an enum matches the data being represented.
2. **Are the member names and meanings clear?** Choose names that distinguish the intended choices, and document meanings that might otherwise be ambiguous.
3. **Is the first member an acceptable default?** A newly declared enum variable defaults to its first listed member. Check that this default is understood in the context where the variable is declared.
4. **Have you reviewed declaration order?** Members map to positions starting at zero. Look for code or integrations that depend on those positions before adding or reordering members.
5. **Does the surrounding code define the behavior?** Review each read and assignment, including how relevant or terminal states are handled. Do not treat the enum declaration as the transition policy or access control.
6. **Are conversions bounded and verified?** Check that integer values reaching an explicit conversion fit the enum’s valid range, and review the relevant boundary cases.
7. **Does the compiler version match the language assumptions?** Verify exact syntax, limits, and behavior against official Solidity documentation for the selected compiler version. The example’s pragma is illustrative and should not replace checking the compiler configuration used by a project.
8. **Does an external application use the right interface?** If the enum is part of a contract interface, verify that the application uses an ABI matching the deployed bytecode and interface.
9. **Have the complete-contract cases been tested?** Test boundary cases and conversions in the context of the complete contract. A small illustrative snippet cannot establish how a larger system behaves.

In short, a Solidity enum is a user-defined type for a finite, ordered set of named values. Declare it when the choices are bounded, use named members in state variables and conditions, and account for the first-member default and integer positions. Then review the surrounding transitions, conversions, compiler-version behavior, and any external interface assumptions separately: the enum models the choices, but it does not supply those additional rules.

## Sources and references

- [Types](https://docs.soliditylang.org/en/latest/types.html) — Solidity Documentation; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
