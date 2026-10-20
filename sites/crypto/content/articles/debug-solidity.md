---
title: "How to Debug Solidity Smart Contracts: A Practical Workflow"
description: "Learn a repeatable workflow for debugging Solidity contracts: reproduce the failure, inspect compiler output and revert data, trace execution, and verify the fix."
date: "2026-10-20"
draft: false
content_type: "guide"
topics: ["smart_contracts_dapps"]
tags: ["Solidity debugging", "debug Solidity smart contracts", "Solidity debugging tools", "debugging smart contract tests", "Solidity stack traces", "debugging EVM transactions"]
author: "editorial_team"
primary_keyword: "debug solidity"
owned_question: "How do you debug Solidity smart contracts?"
risk_level: "medium"
---

# How to Debug Solidity Smart Contracts

Debugging Solidity is a process of investigating a particular failing test or transaction. Start by recording the case, then use the available output and execution views to examine it. Keep conclusions limited to the test, script, or transaction actually inspected: a trace explains execution, but does not prove correctness.

This guide focuses on diagnosing a failure. It does not cover choosing a tool for a particular team, auditing a contract for security vulnerabilities, recovering funds, or deploying and operating a production contract.

## Start with a reproducible failure

Before changing code, capture the failure in a short record:

- **Target:** the failing test name or the transaction or call being examined.
- **Expected result:** what the test or caller was meant to observe.
- **Actual result:** what happened, including any reported failure.
- **Inputs and context:** the arguments and relevant caller, state, and block assumptions used in the case.
- **Build and test setup:** the compiler version, configuration, and test environment.

Reduce the case to the smallest test or call that still reproduces the issue. Remove unrelated actions or assertions one at a time, checking whether the failure remains. If removing a setup action makes it disappear, retain that action in the reproduction while investigating its role. A reduced case is useful only if it still exhibits the original failure.

For example, consider a hypothetical test that expects a call to update a stored value but observes a different value afterward. Preserve the test name, input, expected and actual values, compiler version, and configuration. Then simplify the setup without removing actions necessary to reproduce the discrepancy. This example illustrates a diagnostic method; it does not assert a particular Solidity behavior or cause.

Foundry tests are Solidity functions conventionally stored in `.t.sol` files. Foundry provides setup, unit, fuzz, invariant, and fork-testing facilities. Exact flags, cheatcodes, defaults, and APIs depend on the installed Foundry version. Check the documentation for the release used by the project rather than assuming that a command or behavior applies across versions. [1]

## Read the compiler and test output

First identify what kind of failure the output reports. Is the project failing to compile, is a test reporting a failure, or is the observed result different from what was expected? Record the exact output and the test name or other identifier for the case. Avoid treating a report as an explanation of the cause unless it provides evidence for that explanation.

Use the output to narrow what to inspect next, and keep the test setup and build configuration in view. If a compiler version or configuration changes between runs, record the difference. Without a stable reproduction, it may be unclear whether a changed result reflects a code edit or a changed setup.

When a test reports an unexpected result, compare the stated expectation with the value or behavior the test actually observed. Review the test’s setup and the actions leading to that observation. Treat a reported location or test name as a starting point for investigation, not as proof that the underlying cause lies exactly there.

## Inspect reverts and execution traces

If the output includes revert information, record what it reports and whether it is available in a form you can interpret. If revert data is missing or undecoded, note that as a limitation; do not infer from the absence of readable data that no failure occurred or that the cause is known.

Forge call traces show nested contract calls, returns, reverts, emitted logs, deployments, and reported gas use during tests or scripts. Trace formatting and verbosity flags vary by release. A trace can help explain the execution represented in its output, but it does not prove correctness. [2]

Read the trace as an account of one execution. Start at the outer call and follow the nested calls. Note where calls return or revert, and compare the recorded path with the test’s expectation. Logs and reported gas use are observations in that trace; interpret them in the context of the case rather than treating them as a complete explanation on their own.

In a hypothetical case where a test completes an outer call but later reports an unexpected value, a trace may help show which nested calls occurred and where they returned. That can narrow the next question to investigate, but does not by itself establish why the value differed. If a trace shows a revert, use the information it actually reports, and preserve any uncertainty it leaves unresolved.

When a trace does not provide enough detail for a specific question, the Forge debugger can inspect one selected test, script, or transaction at opcode level through an interactive debugging view. Debugger commands and interface depend on the installed Foundry release. [3] Use it to examine the selected execution more closely, while keeping the reproduction and its setup available for context.

Confirm that the trace or debugger view corresponds to the test, script, or transaction under investigation. If the available output does not resolve the issue, record what is missing and return to the reproduction and its assumptions. Do not fill gaps in the evidence with a guessed explanation.

## Check state, callers, and assumptions

Review the conditions under which the failing case ran. Check the caller identity, balances, storage values, timestamps, and block context used by the test or call. Compare observed conditions with the test’s assumptions, and distinguish values that were verified from values that were merely expected.

Also review setup code, mocks, fixtures, and external-call behavior. These are part of the case being examined because they affect the conditions established for that test. If changing a fixture or mock changes the observed result, record that fact. Do not assume that a mock behaves identically to an external contract unless that equivalence has been established for the particular behavior under investigation.

Consider whether the result depends on prior state or transaction ordering. Preserve relevant preceding actions in the reproduction when they are needed to establish the case. A result observed under one setup does not, by itself, describe a different starting state or sequence.

A concise assumption checklist can help keep the investigation concrete:

1. Who is the caller in the failing case?
2. Which balances and storage values are present before the relevant call?
3. What timestamp and block context does the case use?
4. Which setup actions, fixtures, or mocks establish those conditions?
5. Does the outcome depend on a prior action or transaction order?
6. Which conditions were observed, and which remain assumptions?

The purpose is to make the limits of the reproduction visible, not to imply that every uncertainty has been resolved.

## Use debugging tools without over-relying on them

Use the project’s test runner and compiler output to establish and reproduce the failure. Then inspect the execution evidence available for that case: a call trace, an interactive debugger, or transaction trace data where available. Check current project documentation for the installed tool’s supported commands and configuration. Foundry trace formatting and debugger commands or interfaces are release-dependent. [2][3]

These views answer different diagnostic questions. Test output identifies the case and its reported result; a call trace shows execution details such as nested calls and reverts; and the Forge debugger provides an opcode-level interactive view of one selected test, script, or transaction. Use each view only for what it reports, and interpret it alongside the recorded setup.

A trace explains the execution it represents; it does not prove correctness. Likewise, a result from a local test establishes what that test reported under its particular conditions. Do not generalize a single test or trace to executions that were not examined, or describe debugging output as a comprehensive security assessment. If an output is incomplete, state that limitation rather than treating it as evidence that an unreported event did not occur.

## Verify the fix and preserve the evidence

After making a change, return to the original reproduction. Add or update a regression test that captures the failure, then run the relevant tests with the recorded compiler and configuration. Compare the outcome with the original record: does the case now produce the intended result, and does the test still check the behavior that originally failed?

Review the changed behavior and the dependent call paths relevant to the issue. If the failure disappears only after the setup or build configuration changes, the reproduction does not yet isolate the effect of the code change. Keep the conditions stable when comparing before and after results, or document the differences.

Preserve the reproduction steps, expected and actual results, compiler version, configuration, relevant test output, trace or debugger observations, change made, and remaining uncertainty. This record lets another developer repeat the case and assess the same evidence without relying on undocumented assumptions.

Before closing the debugging task, check that:

- The original failure is reproducible under the recorded setup.
- The regression test captures the behavior that failed.
- Verification used the recorded compiler and configuration, or documents any differences.
- The explanation is supported by the output or trace, with unresolved gaps stated.
- Conclusions are limited to the test or transaction that was examined.

This workflow makes an investigation repeatable and its conclusions easier to assess. It does not turn a result for one case into a conclusion about every possible execution.

### Sources

1. [Foundry Documentation: Writing Tests](https://getfoundry.sh/forge/writing-tests)
2. [Foundry Documentation: Understanding Traces](https://getfoundry.sh/forge/traces)
3. [Foundry Documentation: Debugger](https://getfoundry.sh/forge/debugger)

## Sources and references

- [Debugger](https://getfoundry.sh/forge/debugger) — Foundry Documentation; retrieved 2026-10-19.
- [Understanding Traces](https://getfoundry.sh/forge/traces) — Foundry Documentation; retrieved 2026-10-19.
- [Writing Tests](https://getfoundry.sh/forge/writing-tests) — Foundry Documentation; retrieved 2026-10-19.
