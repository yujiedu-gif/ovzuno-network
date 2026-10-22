---
title: "Solidity abstract contract constructor: declaration and inheritance"
description: "Learn how a solidity abstract contract constructor is declared, when it runs through inheritance, and how derived contracts provide its arguments."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["abstract contracts in Solidity", "Solidity constructors", "constructor inheritance"]
author: "editorial_team"
primary_keyword: "solidity abstract contract constructor"
owned_question: "How does a constructor declared in a Solidity abstract contract run, and what must a derived contract do to initialize it?"
risk_level: "medium"
---

A Solidity abstract contract can declare a constructor, but it is not deployed on its own. When a concrete derived contract is created, its constructor must supply any required arguments to the abstract base constructor, and the base initialization runs as part of creating that derived contract. Exact syntax depends on the Solidity compiler version, which the available evidence here does not establish; check the language documentation for the version used by your project before applying an example.

## What makes a Solidity contract abstract?

An abstract contract is a contract that is incomplete for deployment as a concrete instance. It may provide some behavior while leaving other behavior for a derived contract to implement. On Ethereum, a smart contract has code and data in blockchain state at a specific address; an abstract contract’s role in inheritance is to contribute that code and its initialization requirements to a concrete contract.

For this topic, the important distinction is between a contract’s source-level role and a deployed instance. An abstract base can specify initialization through a constructor even though the base itself is not the separately deployed object. The concrete derived contract is the one created onchain, with the inherited initialization included in that creation.

## Solidity abstract contract constructor: declaration and execution

A constructor is special initialization logic associated with creating a contract instance, rather than an ordinary function intended for later calls. An abstract contract may declare one and require constructor parameters. The derived contract must ensure those parameters are provided when the concrete contract is created.

The base constructor executes in the construction of the derived instance; it is not a separate deployment of the abstract base. This lets the base establish values that its inherited logic needs, while the derived contract can provide those values from its own constructor parameters or from arguments fixed in the inheritance declaration. The exact forms available and their syntax are compiler-version matters, so do not assume that an example written for one Solidity version will compile unchanged under another.

A useful mental model is an initialization chain: the concrete contract is created, and the constructors required by its inheritance hierarchy are initialized as part of that creation. The abstract contract contributes a required step in that chain. It does not become an independent contract address merely because it declares a constructor.

## How derived contracts pass constructor arguments

Here is a schematic illustration of the relationship, not a tested code sample or a version-verified syntax reference:

```solidity
abstract contract Base {
    uint256 internal setting;

    constructor(uint256 initialSetting) {
        setting = initialSetting;
    }
}

contract Example is Base {
    constructor(uint256 chosenSetting) Base(chosenSetting) {}
}
```

The intended point is that `Base` requires an argument, and `Example` forwards a value when it initializes the base. A project might instead provide fixed values in the inheritance declaration, depending on the language version and the desired design. With forwarded values, the derived constructor can accept an input and pass it to the base; with fixed values, the inheritance declaration supplies the base argument directly. Both approaches express how the abstract base receives its initialization input, but the exact legal syntax must be confirmed against the project’s compiler version.

Do not infer from this schematic that it has been compiled or that it captures every inheritance form. The allowed evidence for this article does not verify constructor grammar, the precise ordering rules for multiple base constructors, or a particular compiler release. Consult the official Solidity documentation corresponding to the compiler version you intend to use, and compile an example in that version before relying on it.

## Common inheritance mistakes to check

When a derived contract fails to compile around an abstract base constructor, check whether the base’s required arguments have been supplied along the inheritance chain. Also check that the final contract provides any behavior left abstract by its parents. Supplying constructor arguments does not by itself make an incomplete contract concrete.

Next, verify the compiler version and the syntax used to pass arguments. A code fragment may be conceptually clear but still use syntax unsupported by a project’s chosen compiler. Treat compiler diagnostics as version-specific feedback, not as proof that a different syntax form is valid.

Finally, distinguish construction from later interaction. A constructor is part of creating the instance; it is not an ordinary function that a user calls again after deployment. The core rule is therefore straightforward: an abstract contract can declare initialization requirements, and the concrete derived contract must satisfy them when it is created. The exact source syntax should be checked against the compiler version in use.

## Sources and references

- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
