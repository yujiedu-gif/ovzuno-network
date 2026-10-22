---
title: "Foundry Solidity Version: What the Setting Means"
description: "Understand the foundry solidity version setting in Foundry projects, how it relates to Solidity pragmas, and what it says about compiler selection."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "foundry solidity version"
owned_question: "What does “Foundry Solidity version” mean, and how is it specified in a Foundry project?"
risk_level: "medium"
---

“Foundry Solidity version” usually means the Solidity compiler version selected for a Foundry project, rather than a separate version of the Solidity language or of Foundry itself. In project configuration, the relevant setting is `solc_version` in `foundry.toml`; source files may also contain a Solidity `pragma` that constrains which compiler versions are acceptable. These declarations serve related but different purposes, so read them together when interpreting a build. [source](<https://getfoundry.sh/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

## What “Foundry Solidity Version” Refers To

Foundry is a toolkit for Ethereum-compatible development. Its tools have different roles: Forge builds and tests contracts, Anvil provides a local development node, and Cast supports command-line contract and RPC interaction. The phrase “Foundry Solidity version” generally refers to the Solidity compiler version used when Forge builds Solidity source code—not the version of the Foundry toolkit itself. [source](<https://getfoundry.sh/>)

The Solidity compiler is commonly called `solc`. A compiler version identifies the compiler implementation used to translate source code into build outputs. It is distinct from Solidity as a programming language: the language has types and syntax, while `solc` is software that processes source written in that language. [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

This distinction matters when reading a project. A Foundry release or toolchain version does not, by itself, tell you which Solidity compiler version a particular project build uses. Check the project’s compiler configuration and relevant source files rather than inferring the compiler from the name of the toolchain. [source](<https://getfoundry.sh/>) [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>)

## Compiler Version, `solc`, and the Solidity `pragma`

A Solidity `pragma` is a source-file declaration that constrains the compiler versions considered acceptable for that file. It is not, on its own, proof of which compiler produced a particular build. A pragma may allow more than one compiler version, so it can express a compatibility range rather than a single version selection. [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

The project-level compiler setting and source-level pragma therefore answer different questions. The `solc_version` setting identifies the compiler version specified for the project’s builds. A pragma states the compiler-version constraint written in a source file. To understand whether a build’s compiler selection fits the source, consider both declarations; neither should be casually substituted for the other. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

An exact compiler-version pragma can prevent a source file from being compiled automatically with a different compiler version that might introduce breaking behavior. But a pragma is still a constraint, not a record of the compiler that actually ran. The actual build context depends on the project’s configuration and the compiler used for that build. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

## Where Foundry Expresses the Solidity Compiler Setting

In a Foundry project, `foundry.toml` is where the `solc_version` configuration setting expresses the Solidity compiler version for builds. Treat this as project configuration: it names a compiler version for the project’s build context, while the `pragma` declarations remain in the Solidity source files. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

This is a description of the setting, not a step-by-step configuration procedure. The exact behavior and supported configuration options should be checked against the Foundry documentation applicable to the project and tool version. Foundry’s toolchain binaries and installation options can vary by release channel and version, so configuration details should not be generalized across versions without checking the relevant documentation. [source](<https://getfoundry.sh/getting-started/installation>)

## How to Read a Version Value in Project Context

When interpreting a project’s compiler version, use a short review sequence:

1. Look in `foundry.toml` for the `solc_version` setting. This is the project-level compiler-version declaration.
2. Inspect the `pragma` in each relevant Solidity source file. It states a compiler-version constraint and may permit a range.
3. Treat the compiler actually used for a particular build as a build-context fact. A configuration value or pragma alone should not be presented as independent proof of the complete build history. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

Keep the conclusion narrow. A compiler-version setting identifies a version choice in project configuration; it does not, by itself, establish that source code is compatible with every environment, suitable for deployment, or secure. The term explains compiler selection within a Foundry project, not which version a project should choose. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>)

In brief, “Foundry Solidity version” usually refers to the Solidity compiler version set for a project through `solc_version` in `foundry.toml`. A source-file `pragma` expresses an allowed compiler-version constraint. Reading both helps distinguish project configuration from source compatibility, without mistaking either declaration for a complete account of a particular build. [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>) [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>)

## Sources and references

- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Layout of a Solidity Source File](https://docs.soliditylang.org/en/latest/layout-of-source-files.html) — Solidity Documentation; retrieved 2026-10-19.
- [Foundry](https://getfoundry.sh/) — Foundry; retrieved 2026-10-19.
- [Installation](https://getfoundry.sh/getting-started/installation) — Foundry Documentation; retrieved 2026-10-19.
