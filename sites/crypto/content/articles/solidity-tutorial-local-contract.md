---
title: "Solidity Tutorial: Write, Test, and Deploy a Local Contract"
description: "Build a version-pinned Solidity project with Foundry, test a minimal contract, deploy it to a local Anvil node, and verify read and write calls."
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["smart-contracts-and-dapps"]
tags: ["Solidity beginner tutorial", "write a Solidity contract", "test Solidity locally", "deploy Solidity contract to Anvil", "Foundry Solidity tutorial"]
author: "editorial_team"
primary_keyword: "solidity tutorial"
owned_question: "How can a developer write, test, and deploy a minimal Solidity contract in a local learning environment?"
risk_level: "high"
---

This **Solidity tutorial** builds a complete but deliberately small local workflow: create a version-pinned Foundry project, write a `Counter` contract, test its initial and updated state, start an isolated Anvil chain, deploy with a disposable development account, and verify read and write calls. Nothing in the tutorial requires a public RPC endpoint, faucet, browser wallet, API key, seed phrase, or real funds.

The contract is a learning artifact, not production code. It has no access control, upgrade strategy, economic model, or external integrations. Read [what smart contracts are and how they execute](/articles/what-are-smart-contracts/) before continuing if bytecode, state, transactions, and gas are unfamiliar.

## What this tutorial builds

The finished project has four relevant files:

```text
solidity-local-lab/
├── foundry.toml
├── src/Counter.sol
├── test/Counter.t.sol
└── lib/forge-std/
```

`Counter.sol` stores one unsigned integer. Its constructor sets the initial value. Any caller can later set a new value, and the contract emits an event describing the change. The tests check the initial value, a normal update, and arbitrary values supplied by Foundry's fuzz runner.

Foundry separates the workflow into tools. Forge initializes, compiles, tests, and deploys projects. Anvil provides a local Ethereum-compatible JSON-RPC node. Cast reads contracts and sends transactions from the command line. This tutorial keeps every write on `127.0.0.1`.

## Create and pin the project

Install Foundry using its current official instructions, then record the installed version rather than assuming every reader has the same release:

```bash
forge --version
cast --version
anvil --version
```

Create a new project:

```bash
forge init solidity-local-lab
cd solidity-local-lab
```

`forge init` creates example source, test, and script files and installs `forge-std`. Keep the generated Git metadata and dependency lock information. Delete or replace only the example `Counter` files described below.

Set an exact compiler version in `foundry.toml`:

```toml
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
test = "test"
solc_version = "0.8.30"
```

The code below also uses `pragma solidity 0.8.30;`. An exact pragma prevents the file from silently compiling with a different Solidity release. If `0.8.30` is not installed, Foundry can normally obtain the configured compiler, but a restricted or offline environment may require installing it first. Do not loosen the pragma just to make a build pass. Choose an available reviewed version, update both locations, and commit the change.

Record the Foundry version and preserve `foundry.toml`, dependency commits, and lockfiles so another developer can reproduce the environment. Compiler pinning controls one variable; it does not prove the source is safe.

## Write the minimal contract

Replace `src/Counter.sol` with:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

contract Counter {
    uint256 public value;

    event ValueChanged(
        uint256 indexed previousValue,
        uint256 indexed newValue,
        address indexed caller
    );

    constructor(uint256 initialValue) {
        value = initialValue;
    }

    function setValue(uint256 newValue) external {
        uint256 previousValue = value;
        value = newValue;
        emit ValueChanged(previousValue, newValue, msg.sender);
    }
}
```

The first line declares the license identifier used by tooling. The pragma selects one compiler version. `Counter` is the contract type, and `value` is persistent onchain state. Marking it `public` makes the compiler generate a read function named `value()`.

The constructor runs once during deployment. It accepts the initial value and stores it. `setValue` is `external`, so a transaction can call it. The function reads the old value, writes the new one, and emits an event with both values and the caller.

There is intentionally no owner check. Any local account can update the value. That makes the access model obvious and provides a useful question for the production checklist: who should be allowed to call each state-changing function?

## Write focused tests

Replace `test/Counter.t.sol` with:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {Test} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";

contract CounterTest is Test {
    Counter internal counter;

    function setUp() public {
        counter = new Counter(7);
    }

    function testInitialValue() public view {
        assertEq(counter.value(), 7);
    }

    function testSetValue() public {
        counter.setValue(42);
        assertEq(counter.value(), 42);
    }

    function testFuzzSetValue(uint256 newValue) public {
        counter.setValue(newValue);
        assertEq(counter.value(), newValue);
    }
}
```

Forge recognizes Solidity functions whose names start with `test`; test files conventionally end in `.t.sol`. `setUp` runs before each test and deploys a fresh contract, so one test's state does not leak into the next.

The first test checks constructor state. The second checks one expected update. The fuzz test asks Forge to generate many `uint256` values and verifies the same invariant each time: after a successful call, stored state equals the input. Fuzzing broadens input coverage, but this invariant is intentionally simple. A production contract needs tests for authorization, reverts, events, boundaries, interactions, invariants, forks, and failure recovery.

## Compile and run the tests

Run formatting, compilation, and tests as separate gates:

```bash
forge fmt --check
forge build
forge test -vv
```

`forge fmt --check` reports formatting drift without rewriting files. `forge build` invokes the pinned compiler and writes artifacts under `out/`. A contract artifact contains items such as the ABI used by clients and the creation or runtime bytecode used by the EVM. Do not commit generated output unless the project has a deliberate artifact policy.

`forge test -vv` compiles the project and executes the Solidity tests in an isolated test EVM. The command should report three passing tests and no failures. If it selects a different compiler, stop and inspect `foundry.toml`, the pragma, environment overrides, and command-line flags.

Increase verbosity only when needed:

```bash
forge test -vvv
```

Higher levels expose traces that help locate a revert or failed assertion. A green test suite means the encoded assertions passed under that environment. It does not mean every requirement was tested.

## Start an isolated local chain

Open a second terminal in the project directory and run:

```bash
anvil
```

Anvil starts an in-memory development node, normally at `http://127.0.0.1:8545`, with instant mining and prefunded development accounts. Its terminal output includes addresses and disposable private keys. The default mnemonic and keys are publicly known. They are safe only for an isolated local chain and must never control real assets or be reused on a public testnet or mainnet.

Keep the Anvil terminal running. In the first terminal, confirm the node responds:

```bash
cast chain-id --rpc-url http://127.0.0.1:8545
cast block-number --rpc-url http://127.0.0.1:8545
```

A fresh default Anvil instance normally reports its local chain ID and an initial block height. Treat the values printed by your process as authoritative; options can change them.

## Deploy and interact locally

Copy one disposable private key from the running Anvil terminal into a shell variable for this terminal session only. Do not paste a real wallet key, save the value in source control, or reuse it outside this local node:

```bash
export ANVIL_DEV_KEY='paste-one-anvil-development-key-here'
```

Deploy the contract with an initial value of `7`:

```bash
forge create src/Counter.sol:Counter \
  --rpc-url http://127.0.0.1:8545 \
  --private-key "$ANVIL_DEV_KEY" \
  --constructor-args 7 \
  --broadcast
```

Deployment is a transaction containing the compiled creation bytecode and encoded constructor argument. On success, the command prints a transaction hash and a new contract address. Store that address in a local shell variable:

```bash
export COUNTER_ADDRESS='paste-deployed-contract-address-here'
```

Read the generated `value()` function. This is a read-only RPC call and does not create a transaction:

```bash
cast call "$COUNTER_ADDRESS" \
  'value()(uint256)' \
  --rpc-url http://127.0.0.1:8545
```

It should decode to `7`. Now send a state-changing transaction:

```bash
cast send "$COUNTER_ADDRESS" \
  'setValue(uint256)' 42 \
  --rpc-url http://127.0.0.1:8545 \
  --private-key "$ANVIL_DEV_KEY"
```

Read again:

```bash
cast call "$COUNTER_ADDRESS" \
  'value()(uint256)' \
  --rpc-url http://127.0.0.1:8545
```

The result should be `42`. Compare the write receipt, block number, sender, contract address, gas used, and status. This connects the source-level call with the transaction lifecycle explained in [how a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/).

When you stop Anvil, its in-memory chain disappears unless you explicitly dump state. Restarting produces a new local environment and the earlier contract address no longer refers to the same deployment. That disposability is useful for learning and repeatable tests.

## Know what is still missing for production

Do not change the RPC URL and treat this exercise as a public deployment procedure. A production contract requires at least:

- written requirements and threat modeling;
- explicit authorization for every privileged operation;
- tests for expected, boundary, adversarial, and integration behavior;
- dependency and compiler review;
- static analysis and independent security review appropriate to the value at risk;
- deployment simulation and bytecode or source verification;
- hardware or institutional key management rather than shell variables;
- multisignature, delay, pause, and recovery design where appropriate;
- monitoring, event indexing, incident response, and upgrade or migration procedures; and
- legal and operational review for any financial or user-facing function.

The tutorial's open `setValue` function is a deliberate example of missing authorization. The local account is disposable, the funds are simulated, and the node has no public consensus. Those properties make the environment convenient, not representative of production security.

A sound learning loop is: pin the environment, read every line, format, compile, test, start a clean local node, deploy with a disposable key, inspect the receipt, read state, send one controlled write, and restart from scratch. Only after that loop is reproducible should a developer add access control, external contracts, tokens, payments, upgrade logic, or public-network configuration.

## Sources and references

- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Foundry](https://getfoundry.sh/) — Foundry; retrieved 2026-10-19.
- [Tests](https://getfoundry.sh/forge/tests) — Foundry; retrieved 2026-10-19.
- [Anvil](https://www.getfoundry.sh/anvil/index.html) — Foundry; retrieved 2026-10-19.
- [Deploying Smart Contracts](https://ethereum.org/developers/docs/smart-contracts/deploying/) — ethereum.org; retrieved 2026-10-19.
