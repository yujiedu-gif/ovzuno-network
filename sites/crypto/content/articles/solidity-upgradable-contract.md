---
title: "Solidity upgradable contract: proxy design, storage, and risks"
description: "Learn how a solidity upgradable contract uses a proxy and implementation, why storage compatibility matters, and which authority and security risks to review."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Solidity upgradeable contracts", "proxy pattern", "implementation contract", "storage layout"]
author: "editorial_team"
primary_keyword: "solidity upgradable contract"
owned_question: "How do Solidity upgradeable contracts route calls through a proxy, and what design and operational risks should developers evaluate before changing an implementation?"
risk_level: "high"
---

A Solidity upgradable contract typically keeps a proxy address in place and routes calls to a separate implementation contract that supplies the logic. Before changing that implementation, developers should verify how the proxy delegates execution, how existing state is laid out, who can authorize the change, and what the project’s specific procedures provide. These details depend on the proxy pattern and contract design; “upgradeable” is not a guarantee that an upgrade is safe or reversible.

## What makes a Solidity contract upgradeable?

A contract is upgradeable when its architecture provides a way to change the logic used for calls while preserving an address through which users or other contracts interact. A common design separates a proxy from an implementation: the proxy is the persistent entry point, while an implementation contains executable logic. Rather than editing deployed bytecode in place, an upgrade changes which implementation the proxy uses. The exact mechanism depends on the chosen pattern.

This arrangement must be designed in advance. A contract without a mechanism and authorization path for changing its logic cannot be made upgradeable simply by editing its Solidity source after deployment. Deploying a different contract creates a different instance; it does not, by itself, change the behavior of the original address.

The distinction matters for reviewers: the proxy and implementation are separate components with different responsibilities. The proxy provides the route into the system and, in common patterns, holds persistent state. The implementation provides the code that handles calls. The contract’s particular design determines how those responsibilities are connected.

## How the proxy and implementation contract work

In a typical delegated call flow, a user or another contract calls the proxy. The proxy forwards execution to its selected implementation using delegated execution. The implementation’s code then handles the request in the proxy’s context, so the state associated with the proxy is used rather than treating the implementation as an ordinary destination contract. Exact behavior depends on the proxy pattern and implementation.

Conceptual call-flow description:

```text
Caller
  │ calls the stable contract address
  ▼
Proxy
  │ forwards execution to the selected implementation
  │ using delegated execution and the proxy's state context
  ▼
Implementation
  │ supplies logic for this call
  ▼
Result returned through the proxy to the caller
```

This differs from a regular external call to an implementation. With a regular call, the implementation executes as the called contract; in a delegated proxy design, the intended arrangement is for implementation logic to operate through the proxy’s context. Reviewers should confirm that the actual code and selected pattern behave as expected rather than relying on a diagram or label alone.

A call to a contract function is not an upgrade. Changing the implementation is a separate privileged operation that updates the proxy’s routing or implementation-selection mechanism. The authorized account or process, the stored implementation reference, and the exact operation are design-specific. This article describes that distinction, not a framework-specific upgrade procedure.

## Solidity upgradable contract storage compatibility

Storage layout describes how a contract’s persistent state variables map to storage locations. In a proxy design, new implementation logic may read or write state associated with the proxy. If the new logic assumes a different layout from the one already used, it may interpret existing values incorrectly or affect the wrong state. This is why changing source code is not enough to establish that an upgrade is compatible.

Solidity’s storage layout follows rules for slots, packing, inheritance, arrays, mappings, and structs. The precise result depends on the compiler version and the contract’s inheritance and layout choices. Proxy-based upgrade guidance therefore calls for compatible storage layouts across implementations, together with disciplined initialization, to reduce the risk of takeover or corrupted state. These constraints are not a substitute for reviewing the specific contract and upgrade pattern. ([source](<https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable>))

Before a proposed change, compare the old and new layout assumptions and review the actual compiler output for the relevant versions and configuration. Pay particular attention to inheritance and variable ordering, as well as pattern-specific rules. A review should establish which existing values the new code expects at each relevant location; a source-level diff alone may not answer that question. The available evidence does not establish a universal safe set of storage edits, so compatibility must be assessed for the actual implementation pair.

Initialization also requires pattern-specific review. A proxy and an implementation are distinct contracts, and the upgrade design must ensure that the intended state is initialized in the intended context. Do not assume that a constructor or a familiar initialization convention behaves correctly for every proxy architecture; verify the specific pattern’s requirements and how the deployed system applied them.

## Upgrade authority, governance, and security risks

An upgrade changes the logic that users reach through the proxy, so a reviewer needs to identify who or what can authorize that change. Authority may be assigned to an account, a multisignature arrangement, a governance process, or another mechanism, but the appropriate description depends on the project’s design. Check the actual authorization path and who can grant, revoke, or exercise the relevant permissions; do not infer governance controls from the presence of a proxy alone.

Risks to evaluate include compromised authorization credentials, incorrectly restricted upgrade functions, a proposed implementation that behaves differently than intended, and operational mistakes during a change. These are review categories, not claims that a particular system has suffered them or will necessarily suffer them. A proxy makes the upgrade authority part of the system’s security boundary because that authority can affect the logic used at the proxy address.

Composability adds another review consideration: contracts can call or reuse independent on-chain components through public interfaces, but each dependency adds behavior, availability, upgrade, permission, and economic assumptions. A reviewer should therefore consider whether the proposed implementation relies on other contracts, and whether changes or permissions in those dependencies affect the system being reviewed. ([source](<https://ethereum.org/developers/docs/smart-contracts/composability/>))

Do not treat the words “audited,” “governed,” or “upgradeable” as proof of a specific security property. Evidence about audits, authorization, recovery, compliance, or incident response must come from documentation for the particular system. The allowed evidence here does not establish that any given contract has an audit, a recovery path, a rollback mechanism, or a compliance status.

## Checks to perform before changing an implementation

Use this checklist to frame a technical review, not as a deployment recipe or assurance of safety:

- **Confirm the route and authority.** Identify the proxy, the implementation it currently selects, the proposed replacement, and the exact authorization path required to change that selection.
- **Verify identity and intended behavior.** Check that the proposed implementation is the one intended for the target proxy and that its behavior has been reviewed against the change being proposed.
- **Compare storage assumptions.** Review old and new layouts, inheritance, variable ordering, compiler output, and the proxy pattern’s specific compatibility requirements. Confirm how initialization is handled in that design.
- **Review permissions and dependencies.** Establish which accounts or processes can authorize upgrades and whether external contracts introduce additional upgrade, permission, availability, or economic assumptions.
- **Check project-specific procedures.** Review the tests, compiler version, tooling, and upgrade process documented for the actual system. Confirm whether monitoring, incident response, pausing, or rollback mechanisms exist; do not assume they are available.

These checks help distinguish what the architecture supports from what the project has actually implemented and documented. Without project-specific evidence, the existence of a proxy cannot establish that a proposed change is compatible, authorized correctly, tested, recoverable, or safe.

## Sources and references

- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
