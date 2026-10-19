---
title: "Foundry Solidity Tutorial: Build, Test, and Deploy Locally"
description: "Create a small Solidity contract with Foundry, test it with Forge, deploy it to a local Anvil node, and verify the resulting state without exposing a real key."
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["smart-contracts-dapps"]
tags: ["Solidity Foundry tutorial", "Foundry smart contract tutorial", "forge init Solidity", "forge test tutorial", "deploy Solidity with Foundry"]
author: "editorial_team"
primary_keyword: "foundry solidity tutorial"
owned_question: "How can a developer create, test, and deploy a minimal Solidity project with Foundry?"
risk_level: "high"
---

This **Foundry Solidity tutorial** creates one small `Counter` contract, tests it with Forge, deploys it to a local Anvil node, and reads and changes its state with Cast. It stays on localhost: no public-network funds, production key, token, or external deployment is required.

Foundry changes quickly. The workflow below was checked against the official documentation on October 19, 2026. Record your installed versions and consult the current command help before using the same steps later.

## What this tutorial builds

The project contains:

- `src/Counter.sol`: a contract that stores a number;
- `test/Counter.t.sol`: deterministic and fuzz tests;
- Forge for compilation and tests;
- Anvil as a disposable local Ethereum node; and
- Cast for JSON-RPC reads and signed local transactions.

The contract is deliberately simple. Passing this tutorial proves that the local toolchain and deployment loop work. It does not prove that a production contract is secure. [What smart contracts are](/articles/what-are-smart-contracts/) provides the execution model, while [smart contract architecture](/articles/smart-contract-architecture/) covers authority and dependency boundaries.

## 1. Install and verify Foundry

Foundry's official installer is Foundryup. Follow the current command on the official installation page for your platform rather than copying an old installer URL. After installation, open a new shell if the binary directory was added to your `PATH`, then run:

```bash
foundryup
forge --version
anvil --version
cast --version
```

Foundryup installs Forge, Cast, Anvil, and Chisel. It can install stable, nightly, or version-specific builds. For a reproducible project, record the exact Forge and Solidity compiler versions in the repository or build log rather than assuming `latest` will remain equivalent.

If your environment requires downloaded-binary verification, follow Foundry's current artifact-attestation instructions. Do not run an installation pipe blindly in a privileged shell. Review the official URL, use an ordinary user account, and apply your organization's software-supply-chain policy.

## 2. Initialize the project

Create and enter a new project directory:

```bash
forge init foundry-counter
cd foundry-counter
```

A standard project includes `src/`, `test/`, `script/`, `lib/`, and `foundry.toml`. The initialized example may already contain a counter contract, test, and deployment script. For this tutorial, replace the contract and test with the versions below so the behavior is explicit.

Inspect the configuration before building:

```bash
forge config
```

Do not copy a mature project's `foundry.toml` without understanding it. Compiler version, optimizer settings, remappings, file permissions, RPC aliases, and filesystem access affect reproducibility and security. Keep secrets outside the file and outside version control.

## 3. Write the minimal contract

Create or replace `src/Counter.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Counter {
    uint256 public number;

    function setNumber(uint256 newNumber) external {
        number = newNumber;
    }

    function increment() external {
        number += 1;
    }
}
```

Solidity recommends an SPDX license identifier and a version pragma in each source file. The pragma checks that the selected compiler falls within an allowed range; it does not install or select that compiler. Decide whether a caret range is appropriate for your project. A production build may pin an exact compiler and settings for reproducible bytecode.

The compiler creates an automatic getter for the `public` state variable. `setNumber` and `increment` change state and therefore require transactions when called on a node. The example has no access control because its only purpose is demonstrating the toolchain. Do not treat it as a template for valuable state.

## 4. Write Solidity tests

Create or replace `test/Counter.t.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";

contract CounterTest is Test {
    Counter internal counter;

    function setUp() public {
        counter = new Counter();
    }

    function test_InitialNumberIsZero() public view {
        assertEq(counter.number(), 0);
    }

    function test_IncrementAddsOne() public {
        counter.increment();
        assertEq(counter.number(), 1);
    }

    function testFuzz_SetNumber(uint256 value) public {
        counter.setNumber(value);
        assertEq(counter.number(), value);
    }
}
```

Forge tests are Solidity functions. The official test guide documents `setUp` as the optional function run before each case and public or external functions beginning with `test` as discoverable tests. Forge Std's `Test` contract supplies assertions and the `vm` cheatcode interface.

The fuzz test accepts values generated by the runner and checks that every tested value can be stored and read back. Fuzzing explores inputs, but it is not a proof of correctness. Production tests should cover authorization, boundaries, expected reverts, events, invariants, stateful sequences, external dependencies, and upgrade behavior where applicable.

## 5. Build and test

Compile the project:

```bash
forge build
```

Then run the tests:

```bash
forge test
```

All three tests should pass. If one fails, increase verbosity:

```bash
forge test -vvv
```

Higher verbosity can show logs and execution traces. Read the first relevant revert and the call path instead of changing code until the test turns green. A compiler error usually identifies the source file, line, and mismatch. A test failure means the compiled behavior did not satisfy the assertion for that case.

Confirm which compiler and configuration Forge used in the build output. Commit the source, test, configuration, dependency lock information, and toolchain version needed to reproduce the result. Build artifacts alone are not a durable source of truth.

## 6. Start Anvil and deploy locally

Open a second terminal in the project directory and start the local node:

```bash
anvil
```

Anvil prints an RPC URL, development accounts, and development private keys. These credentials are intentionally public and safe only for disposable local or test environments. Never fund an Anvil default account on a public network and never reuse its mnemonic or keys.

Keep Anvil running. In the first terminal, set local shell variables using one of the development keys printed by your own Anvil process:

```bash
LOCAL_RPC=http://127.0.0.1:8545
LOCAL_KEY=<ANVIL_DEVELOPMENT_PRIVATE_KEY>
```

Deploy the contract:

```bash
forge create src/Counter.sol:Counter \
  --rpc-url "$LOCAL_RPC" \
  --private-key "$LOCAL_KEY" \
  --broadcast
```

Forge documents `forge create` for deploying one contract. The `--broadcast` flag publishes the transaction; without it, the operation is a simulation. This tutorial uses a disposable local key on a local node. For any shared or public network, avoid command-line private keys because they can leak through shell history, process listings, logs, or automation output. Use an approved signer or keystore workflow instead.

Copy the `Deployed to` address from the successful output into a temporary variable:

```bash
COUNTER=<DEPLOYED_CONTRACT_ADDRESS>
```

## 7. Read and change state with Cast

First confirm that bytecode exists at the address:

```bash
cast code "$COUNTER" --rpc-url "$LOCAL_RPC"
```

A value other than `0x` indicates code is present. Read the generated `number()` getter:

```bash
cast call "$COUNTER" "number()(uint256)" --rpc-url "$LOCAL_RPC"
```

The first value should be zero. Send a local state-changing transaction:

```bash
cast send "$COUNTER" "setNumber(uint256)" 42 \
  --rpc-url "$LOCAL_RPC" \
  --private-key "$LOCAL_KEY"
```

Read again:

```bash
cast call "$COUNTER" "number()(uint256)" --rpc-url "$LOCAL_RPC"
```

The decoded value should now be 42. The send output provides a transaction hash and receipt fields. This closes the local loop: source, compilation, test, deployment, transaction, receipt, and resulting state. [A local Solidity contract tutorial](/articles/solidity-tutorial-local-contract/) explains the same lifecycle without depending on one toolkit.

Stop Anvil when finished. Its in-memory chain and deployed state are disposable unless you deliberately save and reload state.

## Troubleshoot the local loop

If deployment fails, verify one boundary at a time. Confirm that `forge build` succeeds, Anvil is running, `cast chain-id --rpc-url "$LOCAL_RPC"` returns the expected local chain, and the chosen development account has a balance. If `cast code` returns `0x`, check that `COUNTER` contains the address from the current Anvil session rather than a previous restart. If a call cannot decode, compare its signature and return type with the compiled ABI.

Do not solve a connection problem by changing contract logic. Capture the command, tool versions, RPC URL class, chain ID, transaction hash, and error while keeping keys out of logs. This evidence usually identifies whether failure belongs to compilation, signing, RPC transport, execution, or decoding.

## Before moving beyond localhost

A public testnet or production deployment adds responsibilities that this tutorial intentionally omits:

- pin and review the Foundry, Solidity, and dependency versions;
- expand tests to cover permissions, failures, invariants, and adversarial behavior;
- review storage, external calls, upgrade rights, and administrative keys;
- use a controlled signer rather than a plaintext command-line key;
- verify chain ID, RPC endpoint, fees, constructor arguments, and deployment address;
- simulate before broadcasting and retain the deployment receipt;
- verify published source and compiler settings independently; and
- obtain review appropriate to the value and risk of the contract.

[Blockchain deployment architecture](/articles/blockchain-deployment-architecture/) covers nodes, keys, network access, and operations beyond the contract file. A successful local **Foundry Solidity tutorial** run is a development milestone, not a production security claim.

## Sources and references

- [Installation](https://getfoundry.sh/getting-started/installation) — Foundry Documentation; retrieved 2026-10-19.
- [Writing Tests](https://getfoundry.sh/forge/writing-tests) — Foundry Documentation; retrieved 2026-10-19.
- [Anvil](https://www.getfoundry.sh/anvil/index.html) — Foundry Documentation; retrieved 2026-10-19.
- [Deploying and Verifying](https://getfoundry.sh/forge/deploying) — Foundry Documentation; retrieved 2026-10-19.
- [Layout of a Solidity Source File](https://docs.soliditylang.org/en/latest/layout-of-source-files.html) — Solidity Documentation; retrieved 2026-10-19.
