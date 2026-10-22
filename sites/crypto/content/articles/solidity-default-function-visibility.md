---
title: "Solidity Default Function Visibility: What Developers Need to Know"
description: "Learn what Solidity default function visibility means, whether functions need an explicit visibility specifier, and how to check behavior for your compiler version."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["Solidity visibility specifiers", "external and public functions in Solidity", "private and internal functions in Solidity"]
author: "editorial_team"
primary_keyword: "solidity default function visibility"
owned_question: "What does Solidity default function visibility mean, and must a function’s visibility be declared explicitly?"
risk_level: "medium"
---

Solidity does not have one safe default function visibility that readers should infer when a specifier is missing. For the source in front of you, identify the compiler version and declaration context, then check that version’s documentation and compiler diagnostics. Visibility describes which contract code can call a function; it does not establish authorization or make blockchain information confidential.

## What Solidity function visibility controls

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) In Solidity, function visibility describes the scope from which a function can be called. The four visibility specifiers are `public`, `external`, `internal`, and `private`.

This is a boundary on callable scope, not a complete permission system. A declaration’s visibility does not, by itself, answer whether an otherwise permitted caller should be allowed to carry out a particular operation. It also does not make the function’s code or associated blockchain data secret. Treat visibility and any separate authorization checks as distinct questions.

For example, a function marked `private` is limited by Solidity’s visibility rules to the contract where it is defined. That restriction concerns calls from contract code; it should not be read as a confidentiality guarantee about information recorded on a blockchain. The visibility label tells a reader about code access, not who can observe the chain’s data.

## Solidity default function visibility: is there an implicit default?

For a function declaration being compiled with a modern Solidity compiler, do not assume that omission silently assigns a visibility. The relevant rule depends on compiler version and declaration context, so check the documentation and diagnostics for the compiler actually used. The available evidence does not establish a complete historical timeline or every exception across Solidity versions; no universal rule for all past releases should be inferred here.

A source-file pragma can constrain the compiler versions that are acceptable, but it does not select the compiler that actually performs the compilation.  Consequently, a pragma by itself may not tell you which compiler version produced a particular build. Identify the configured or recorded compiler version, then verify whether it accepts the exact declaration and what diagnostic it reports.

This answers the practical meaning of “default” in the question: do not rely on an omitted specifier as an implicit choice. For a particular file, the compiler’s version and the declaration’s context determine what to verify. If you are reading older source, consult the documentation for the version relevant to that source rather than applying a modern rule retroactively.

## How the four visibility specifiers differ

The specifiers identify different callable scopes:

- `public` functions can be called from outside the contract and from within it.
- `external` functions are intended for calls from outside the contract.
- `internal` functions can be called within the defining contract and by derived contracts.
- `private` functions are restricted to the contract in which they are defined; derived contracts do not gain access through inheritance.

This comparison helps interpret a declaration, but it does not choose a visibility for a particular design. In particular, `public` does not mean that every operation is authorized for every caller: any authorization conditions are a separate matter. And `private` is not a way to hide code or on-chain data from observers. These limits keep the terms focused on callable scope rather than broader security or privacy conclusions.

An illustrative reading exercise is to compare `function readValue() public` with `function updateValue() internal`. The first declaration labels its function as callable externally and internally; the second restricts its callable scope to the defining contract and derived contracts. These examples illustrate the visibility labels only. They do not establish what either function does, what conditions it checks, or whether a design is suitable.

## What to do when a function omits visibility

When a declaration appears without a visibility specifier, use a bounded verification process rather than guessing:

1. Identify the compiler version actually used, not only the version range stated in a pragma.
2. Locate the exact declaration and note its context.
3. Consult the Solidity documentation for that compiler version and inspect the diagnostic produced for the declaration.
4. Verify the visibility that the source explicitly states, and consider any separate authorization logic independently.

If the compiler rejects the declaration, use its diagnostic to understand the issue for that version. If the declaration comes from an older codebase, verify it against version-appropriate documentation before deciding what omission means. The evidence here does not support a universal statement about every historical compiler behavior, so the compiler and context remain essential checks.

For new or maintained source, an explicit visibility specifier makes the intended callable scope visible in the declaration. Confirm it using the project’s configured compiler. This avoids treating omission as an implicit permission, an authorization rule, or a privacy feature.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
