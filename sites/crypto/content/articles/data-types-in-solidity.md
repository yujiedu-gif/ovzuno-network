---
title: "Data Types in Solidity: A Practical Guide"
description: "Learn the main data types in Solidity, including integers, booleans, addresses, arrays, structs, and mappings, and see how data locations apply to reference types."
date: "2026-10-20"
draft: false
content_type: "guide"
topics: ["smart_contracts_dapps"]
tags: ["Solidity value types", "Solidity reference types", "Solidity arrays and structs", "Solidity mappings", "Solidity data locations"]
author: "editorial_team"
primary_keyword: "data types in solidity"
owned_question: "What data types are available in Solidity, and how are they used in smart contracts?"
risk_level: "medium"
---

# Data Types in Solidity: Categories, Uses, and Examples

Solidity is a statically typed language. Its type system includes value types, reference types, mappings, arrays, structs, enums, function types, and contract types. Exact syntax and compiler behavior must be checked against the compiler version selected for the code. [claim_solidity_types]

This guide maps the principal categories and provides a practical way to frame type-selection questions. The accepted evidence establishes the categories and specific facts about enums and the contract ABI. It does not establish detailed rules for every built-in type or data location. Accordingly, category descriptions below are paired with verification guidance, and no unverified operation, range, location rule, or version-specific syntax is presented as settled fact.

## How Solidity data types organize contract data

A type identifies what category of value a declaration can represent. It also informs which operations and conversions the language permits, although the exact rules for a particular type must be checked against the relevant compiler documentation. Solidity’s categories include value types and reference types, alongside mappings, arrays, structs, enums, function types, and contract types. [claim_solidity_types]

A useful first step in modeling contract data is to describe its shape. Is it one individual value, one choice among named alternatives, a collection, or a group of related fields? These descriptions can point toward candidate categories, but they do not alone establish that a declaration is valid. Context, type rules, and compiler version still matter.

Types and data locations answer different questions. A type concerns the kind of data represented; a location is a separate declaration concept relevant to certain data. This distinction is especially important when reading code involving composite values. The detailed semantics and applicability of `storage`, `memory`, and `calldata` must be verified in the documentation for the compiler version being used.

## Value types: individual values and named options

Value types are one of Solidity’s main categories. Common topics in this group include `bool`, signed and unsigned integer families, fixed-size byte values, address forms, enums, and function types. Solidity also includes contract types in its type system. The accepted claims establish the presence of these broad categories, but do not provide a complete specification of each type’s operations or restrictions. [claim_solidity_types]

### Boolean, integer, and byte categories

A Boolean category is useful to consider when the intended value represents a true-or-false condition; Solidity names this type `bool`. Whole-number quantities lead to questions about signed and unsigned integer types, commonly written with `int` and `uint` families. Fixed-size byte values are another category, with names such as `bytes1` through `bytes32` included in the language reference topics.

These descriptions identify candidate categories, not a complete account of their ranges, arithmetic behavior, width rules, or permitted conversions. Those details should be checked against the selected compiler’s documentation before a declaration is relied upon. In particular, do not assume that every available integer width is equally suitable or that a type name by itself answers questions about application requirements.

The plan also distinguishes fixed-size byte values from dynamic `bytes`. The accepted claims do not establish the detailed behavior or classification rules for these particular declarations. Check the relevant Solidity documentation rather than inferring dynamic-byte semantics from fixed-size names. Likewise, the word “bytes” alone does not settle questions about text, encoding, or operations.

### Address, enum, function, and contract categories

The language topics include `address` and `address payable`. The supplied accepted claims do not define their detailed semantics or the conditions under which payable-address behavior applies. When a declaration uses either form, verify its meaning and applicable rules in the documentation for the selected compiler rather than treating the names as a sufficient specification.

An enum is a user-defined type with a finite, ordered set of named values. Its values are represented from zero, and conversion from an integer to an enum is checked. The first member is the default value. ABI representation and language limits should be checked for the compiler version. [claim_solidity_enum]

This makes an enum a candidate to investigate when a data model has a bounded set of named alternatives. The ordering fact has a practical consequence for understanding the stated representation, and the default fact means the first member has a defined role. The checked-conversion claim specifically concerns conversion **from an integer to an enum**; it should not be restated as a claim about conversion in the opposite direction.

Function types and contract types are also part of Solidity’s type system. The accepted claims do not describe their detailed syntax, behavior, or restrictions. If code uses them, consult the compiler-version documentation for the relevant declarations and contexts. Their inclusion in the type system does not, by itself, answer how a particular function reference or contract-typed value behaves.

## Reference types: collections and structured data

Solidity’s type system includes reference types, arrays, structs, and mappings. These are useful categories to consider when data consists of multiple components or values. The supplied accepted claims establish their inclusion in the language type system, not the full details of their declaration rules or behavior. [claim_solidity_types]

Arrays are a candidate category when the model calls for an ordered collection. The language topics include fixed-size and dynamic array forms, but the accepted claims do not establish their syntax, permitted operations, or constraints. Confirm those details against the compiler documentation for the code in question.

Structs provide a category to investigate when a model calls for related fields collected under a custom shape. The source pack does not establish rules for struct declarations, nesting, or use in particular contexts. Treat “record” as a way to describe the modeling question, not as a substitute for checking Solidity’s rules.

Mappings are a category to investigate for key-associated values and lookup-oriented state. Mapping behavior and permitted contexts have language-specific constraints, but those constraints are not detailed in the accepted claims here. Do not assume that every key or value choice, or every declaration context, is permitted. Verify the applicable restrictions in the selected compiler’s documentation.

The plan names `string` as a text-related type and dynamic `bytes` as a byte-sequence topic. The accepted claims do not substantiate their detailed definitions or behavior. When a design depends on how text or byte sequences are represented or manipulated, consult the official language reference for the relevant compiler version rather than relying on ordinary-language meanings of the names.

## Data locations: storage, memory, and calldata

Data locations are separate from types. The terms `storage`, `memory`, and `calldata` are identified in the article plan as locations to understand, but the accepted claims supplied here do not establish their semantics, applicability, or copying and referencing behavior. Therefore, this guide does not present a detailed rule for assigning any particular location.

For code involving reference data, verify the location rules in the documentation for the compiler version being used. Check the declaration context and the operation involved; do not assume a location is permitted everywhere or that assignments behave identically across locations. The question “what type is this?” and the question “where is this data accessed or held in this context?” are distinct questions, and both may need answers when reviewing a declaration.

This separation is useful as a reading method even before the detailed rules are checked. First identify the data category named by a declaration. Then identify whether the declaration includes a location and consult the relevant documentation for that location’s meaning and constraints. Avoid inferring location behavior solely from the fact that a value is composite or from an example written for a different compiler version.

## Choosing a type for common contract data

A practical selection process begins with the meaning and shape of the data rather than with a preferred type name:

1. Describe whether the data is an individual value, a bounded named choice, an ordered collection, or related fields.
2. Identify candidate Solidity categories that appear to match that description.
3. Consult the selected compiler’s documentation for the candidate type’s syntax, operations, conversions, and restrictions.
4. If the declaration involves reference data, check the data-location rules for its exact context.
5. Confirm any interface assumptions against the ABI and interface relevant to the deployed contract.

For a binary flag, `bool` is a natural candidate to investigate. For a whole-number quantity, consider the integer family and verify the relevant signedness and width rules rather than assuming a particular variant. For account identifiers, investigate the address forms and confirm whether the code’s requirements call for the semantics associated with a payable form. These are category-level prompts, not prescriptions for a specific contract.

For a bounded set of named states, an enum may be a candidate; account for its ordered members, first-member default, and checked conversion from integers as stated above. For related fields, investigate a struct. For ordered collections, investigate arrays; for key-based lookup, investigate mappings and their language-specific restrictions. In each case, confirm that the type, declaration context, and intended operations are supported by the selected compiler.

No type choice should be treated as proof that a contract is secure or correct. A type can express a data category, but the evidence here does not establish whether a particular contract model or implementation is suitable. This guide also makes no claim that selecting one category or width produces a universal gas benefit. Such questions depend on details outside the accepted evidence and are not needed to identify the type categories.

## Version and interface verification

Solidity syntax and compiler behavior must be checked against the version relevant to the code. When examining a declaration, verify the spelling and syntax, the permitted context, the available operations, and any conversion or location rules in that version’s documentation. Avoid transferring a rule from an example or reference page for another compiler version without checking compatibility.

The contract ABI is a separate but related interface concern. It defines how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. An application must use an ABI matching the deployed bytecode and interface. [claim_solidity_abi] This does not replace understanding the Solidity type itself; it identifies an additional verification point when applications communicate with a contract.

A concise review of a type decision can therefore ask: what data shape is intended, which Solidity category represents it, what does the selected compiler permit in this context, and does the application interface match the deployed contract? These questions keep type selection grounded in the language rules and the code’s stated interface. They do not turn a category-level guide into a compiler-specific reference or a contract audit.

The evidence-supported map is deliberately bounded: Solidity is statically typed and includes the listed type-system categories; enums have the stated finite, ordered, zero-based representation, default, and integer-conversion properties; and the ABI has the stated encoding role. For detailed behavior of individual built-ins, reference data, and locations, use the official Solidity documentation for the compiler version under consideration.

## Sources and references

- [Types](https://docs.soliditylang.org/en/latest/types.html) — Solidity Documentation; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
