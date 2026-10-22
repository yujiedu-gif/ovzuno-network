---
title: "How upgradable smart contracts openzeppelin use proxies"
description: "Understand how upgradable smart contracts openzeppelin use proxies, how upgrades affect storage and control, and which design risks developers should assess."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["OpenZeppelin proxy", "proxy contract", "implementation contract", "storage layout", "upgrade authorization"]
author: "editorial_team"
primary_keyword: "upgradable smart contracts openzeppelin"
owned_question: "How do OpenZeppelin-based upgradeable smart contracts use proxies to change contract logic, and what must developers account for in their design?"
risk_level: "high"
---

OpenZeppelin-based upgradeable contracts use a proxy as the address applications call and an implementation contract as the source of logic. An upgrade changes which implementation the proxy uses, so later calls can run different code while the proxy remains the interaction point. Developers must account for storage compatibility, initialization, and the authority that can approve changes. The details depend on the chosen architecture and version; the OpenZeppelin name alone does not establish how any specific deployment works.

## What makes an OpenZeppelin-based contract upgradeable?

A proxy is a contract that acts as the call-facing address in an upgradeable design. An implementation is a separate contract that contains the logic used to process those calls. The proxy architecture also needs an explicit mechanism for selecting or changing the implementation. Upgradeability is therefore a property of the overall design, not an automatic feature of Solidity contracts or a consequence of using a particular programming language.

The distinction between address and logic matters to applications. The proxy can remain the address an application uses while the code applied to later calls changes. But an unchanged address does not mean that every application or integration will automatically understand a changed interface or behavior. An implementation change may affect how users and other contracts interact with the system.

OpenZeppelin’s upgrade patterns and tools are version- and architecture-dependent. A technical review should identify the exact proxy pattern and library version, then consult documentation for that combination. Do not infer a particular proxy type, upgrade path, or validation capability from the library name alone.

Upgradeable designs also sit within a broader application stack. Smart-contract composability means contracts can call or reuse independent on-chain components through public interfaces. Each dependency adds behavior, upgrade, permission, availability, and economic assumptions to the calling system. A proxy-based contract may itself be one such dependency, so an upgrade can matter to components that rely on its interface or behavior. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

## How a proxy routes calls to implementation logic

Conceptually, a call reaches the proxy, which routes execution to the selected implementation. The implementation supplies instructions; the proxy is the address whose state those instructions use in a delegated call. This separation is central to the design: code and persistent data do not simply move together when the implementation reference changes.

An upgrade changes the implementation reference used by the proxy. After the authorized change takes effect, later calls are processed by the new implementation against the proxy’s existing state. The proxy address may remain the same, but that does not mean the upgrade automatically migrates, checks, or preserves the meaning of every stored value. Reviewers need to understand how the new code interprets the existing state.

This model is useful for asking precise questions: Which address receives application calls? Which implementation supplies the active logic? Which contract’s storage is used during execution? What mechanism changes the implementation reference? Answers must come from the actual architecture and its version-specific documentation, not from a general description of proxies.

The implementation and proxy also have different change implications. Replacing or changing the logic can affect future behavior without changing the call-facing address. Conversely, the continued presence of the same address does not itself show that the new logic is compatible with previous state or user expectations. Those are separate technical questions for review.

## Storage layout and initialization risks

Storage compatibility matters because new implementation logic must interpret the proxy’s existing data consistently. If a change makes the new logic read values from incompatible locations or interpret them differently, the contract can behave incorrectly. OpenZeppelin’s upgrade documentation identifies initializer discipline and compatible storage layout across implementations as requirements for proxy-based upgradeable contracts; failures can lead to takeover or corrupted state. [source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>)

Initialization is a related but distinct issue. Proxy state is not initialized simply because an implementation has a constructor: the implementation and proxy are separate contracts, and the state used through the proxy belongs to the proxy’s context. Proxy-based designs commonly need an initialization mechanism that acts on proxy state. The precise initializer pattern and safeguards depend on the architecture and version. Consult the matching OpenZeppelin documentation rather than carrying instructions over from a different release.

For a proposed implementation change, ask whether existing state retains its meaning, whether new state is introduced compatibly, and whether initialization can occur only as intended. A reviewer should also identify the exact version-specific storage rules and any validation tooling relevant to the chosen pattern. A tool’s existence or a successful check is not, by itself, proof that an upgrade is safe; the supported pattern, scope of checks, and remaining assumptions must be understood.

Do not treat storage review as a one-time concern limited to the first implementation. Each future logic change depends on the state already held by the proxy. The operational decision is whether the proposed code and its initialization assumptions can use that state as intended. Evidence for this decision should match the exact architecture, compiler and library versions, and proposed change; general statements about upgradeability are not a substitute.

## Who can authorize an upgrade—and what that means

Upgrade authorization is a design decision. The authority may be assigned to an account, a role, or a governance process, but the mechanism and its controller must be established from the specific system. Role-based access control can assign distinct permissions to named roles and use administrators to grant or revoke roles, creating an authority graph that must itself be secured. [source](<https://docs.openzeppelin.com/contracts/5.x/access-control>)

A person, account, or process able to authorize an implementation change may be able to alter future contract behavior, subject to the architecture and controls in place. This is a technical capability, not a conclusion about whether a system is decentralized, secure, compliant, or protective of users. A role name or governance label alone does not show who can act, what approval is required, or what constraints apply.

For review, trace the authorization path from the upgrade operation to the ultimate authority. Identify which permission is checked, who controls that permission, and how grants or changes to it are governed. The general role model does not establish how a particular deployment configures access or whether its controls are effective. Do not turn a general library mechanism into a claim about a project’s live authority structure.

This control question also affects how an upgrade is understood over time. The active implementation is not the only relevant fact: reviewers need to know who or what can change it later. The answer is deployment-specific, and should not be guessed from the proxy’s address, the implementation’s source code, or a library’s general documentation alone.

## Review checklist before relying on an upgradeable design

Use these questions to structure a technical review, not as a deployment procedure:

- **Architecture:** What exact proxy pattern and OpenZeppelin Contracts version are involved? Which address is used by applications, and which implementation supplies the active logic?
- **Call and state behavior:** How does the chosen design route calls, and whose state does the implementation logic use? Confirm this from documentation for the actual pattern.
- **Initialization:** How is proxy state initialized, and what version-specific safeguards apply? Do not assume an implementation constructor initializes proxy state.
- **Compatibility:** How does the proposed implementation preserve the meaning and arrangement of existing state? What exact documentation or tooling applies to this pattern and version, and what does it leave unchecked?
- **Authorization:** Which account, role, or governance process can approve an implementation change? Trace how that authority is controlled rather than relying on labels.
- **Operations and claims:** Treat monitoring, response, recovery, availability, and fees as deployment-specific questions. Require evidence before making claims about them; the general architecture does not establish those properties.

The outcome of this review should be a clear account of the proxy-to-implementation relationship, state and initialization assumptions, and upgrade authority. It is not a conclusion that an architecture is safe, nor an assessment of any particular project. Consult current documentation for the exact version and pattern, and obtain independent technical review before relying on or changing a production design. Legal, tax, and compliance conclusions are outside this technical explanation and should not be inferred from proxy behavior.

## Sources and references

- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control) — OpenZeppelin Documentation; retrieved 2026-10-19.
