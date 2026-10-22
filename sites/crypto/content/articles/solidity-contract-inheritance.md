---
title: "Solidity Contract Inheritance: Base Contracts, Overrides, and Order"
description: "Learn how solidity contract inheritance passes declarations from base to derived contracts, handles constructors and overrides, and resolves multiple inheritance."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Solidity inheritance", "base contract", "derived contract", "multiple inheritance", "method resolution order"]
author: "editorial_team"
primary_keyword: "solidity contract inheritance"
owned_question: "How does contract inheritance work in Solidity, including constructor execution and method resolution when contracts inherit from multiple base contracts?"
risk_level: "medium"
---

Solidity contract inheritance lets a derived contract reuse and extend declarations from one or more base contracts. To understand the result, trace which declarations are available to the child, how base constructors are invoked during construction, and how the compiler resolves overridden functions through the inheritance graph. These rules are version-sensitive, so verify syntax and behavior against the compiler version used for the code.

## What Solidity contract inheritance means

A **base contract** is a contract named as a parent in another contract’s inheritance declaration. A **derived contract** is the child that inherits from it. Inheritance is a source-code relationship: it allows a derived contract to use declarations from its bases under Solidity’s rules. It is different from composition, in which contracts reuse or call independent on-chain components through public interfaces. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

That distinction matters when tracing behavior. Inheritance does not, by itself, mean that the derived contract creates a separately deployed instance of each base and calls it. Instead, inherited declarations contribute to the derived contract’s compiled implementation. The exact result depends on the declarations, their accessibility, and the applicable compiler rules.

A declaration’s presence in a base does not necessarily mean that derived code can access it directly. When reviewing a hierarchy, check visibility and the specific declaration rather than treating “inherited” as synonymous with “available everywhere.” The source relationship identifies where code and declarations come from; it does not answer every question about their use.

Inheritance also does not itself establish an upgrade arrangement. Proxy-based upgradeable contracts, for example, have requirements concerning initializer discipline and compatible storage layouts across implementations. Those are upgrade-related constraints, not consequences that can be inferred from inheritance alone. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>)

## What a derived contract inherits—and what it does not

Start with the derived contract’s direct bases, then inspect the declarations it relies on in each base. Trace state variables and functions through the hierarchy, checking whether each declaration is visible to the derived contract and whether another declaration overrides it. A name appearing in a base contract is not sufficient evidence that the child can use it directly; accessibility and compiler rules govern that question.

Keep the source-level relationship distinct from a runtime interaction between contract instances. Inheritance brings declarations into the derived implementation according to language rules. Composition instead involves a contract reusing or calling an independent on-chain component through an interface. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>) This difference helps reviewers determine whether a behavior should be found in the child’s inheritance tree or in a call path to another contract.

The resulting hierarchy is not a complete description of a deployed system. For example, storage compatibility across implementations matters in proxy-based upgrade designs, and shared ancestry alone does not establish that compatibility. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>) Treat inheritance as one part of the code structure, not as proof of deployment configuration or upgrade behavior.

## Constructors and initialization order

A base constructor participates in constructing the derived contract; it is not simply a later call to a separately deployed base instance. A reviewer should identify the constructors along the hierarchy and trace how required arguments are supplied through the inheritance declaration or constructor invocation supported by the project’s Solidity version.

Constructor invocation syntax and ordering must be checked against that version. Do not turn an example from one compiler release into a universal rule. A careful review records the compiler version, lists the bases and their constructors, and follows the actual argument expressions in the source. If an inherited base itself has a base, continue tracing rather than stopping at the child’s direct declaration.

The available evidence for this article does not establish a particular constructor ordering rule or support a version-pinned example. Therefore, a source review should consult Solidity’s documentation for the exact compiler release and confirm the syntax and behavior used by the project. That limitation is preferable to guessing at constructor order from the visual order of names in a declaration.

## Overriding inherited functions

An **override** is a derived implementation that replaces an inherited function implementation under Solidity’s rules. It is not overloading, which uses a different function signature, and it is not a separate external call to another deployed contract. Keep those concepts distinct while tracing what implementation the derived contract provides.

The keywords and requirements for `virtual` and `override` depend on the Solidity language rules for the relevant version. When reviewing a function, find its declaration in the base contract and check whether that declaration permits overriding. Then inspect the derived implementation and its override declaration. Do not assume that seeing one keyword is enough to establish the full relationship or that requirements remain identical across compiler versions.

Multiple inheritance can make this check more involved. If different branches provide implementations of the same function, the derived contract’s declaration may need to identify the relevant base contracts. The precise requirement depends on the hierarchy and the compiler version. Trace each branch and verify the rule rather than inferring it from the function name alone.

An override changes which implementation the hierarchy provides for that function. It does not transform inheritance into a call to an independent contract. If the behavior instead depends on a separate component, analyze that interaction as composition. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

## Multiple inheritance and method resolution

Multiple inheritance means that a derived contract names more than one base. Those relationships can form a graph, including shared ancestors. **Method resolution** is the language process for determining which inherited implementation applies when declarations appear along multiple branches. Solidity’s documented rules govern that result; a reader’s intuition about the order of base names is not a substitute.

To analyze a function, first map the direct bases and the bases they inherit from. Next, locate each declaration of the function in that graph and note where a branch introduces an override. Finally, inspect the derived contract’s own override declaration and check whether it names bases as required. This process makes competing implementations and shared ancestors visible instead of reducing the hierarchy to a simple list.

Avoid relying on a slogan such as “the first base wins” or “the last base wins” without checking the compiler’s specified method-resolution rules. The behavior must be verified for the exact Solidity version and the actual shape of the hierarchy. The evidence available here does not establish a detailed, version-pinned linearization algorithm or a validated code example, so it would be misleading to present one ordering formula as universal.

A reviewer can still make progress without assuming an ordering rule: draw the inheritance graph, annotate each relevant function declaration, and then compare the source to the language documentation for its compiler version. If a method has multiple candidate implementations, treat the override declaration and compiler requirements as essential evidence of which implementation the derived contract selects.

## Review an inheritance hierarchy safely

For a bounded source review, record the compiler version first. Identify the derived contract’s direct bases, then follow any relevant ancestors. For each declaration the child uses, check visibility and whether an override appears on any branch. For constructors, trace the supplied arguments through the hierarchy and verify the version-specific invocation rules. For a function with competing implementations, map the declarations and confirm the resolution requirements against the compiler’s documentation.

Keep this review separate from broader conclusions. Inheritance analysis explains how declarations relate and which implementation language rules select; it is not an audit and does not establish that the resulting code is safe. Where a system composes independent contracts, each dependency introduces behavior, upgrade, permission, availability, and economic assumptions that are separate from inheritance resolution. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Likewise, do not infer upgrade compatibility from a shared base or familiar inheritance structure. Proxy-based upgrades require attention to initializer discipline and compatible storage layout across implementations. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>) The practical review task is to trace the hierarchy accurately, then assess any deployment, upgrade, or dependency questions on their own evidence rather than treating the inheritance graph as a guarantee.

## Sources and references

- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
