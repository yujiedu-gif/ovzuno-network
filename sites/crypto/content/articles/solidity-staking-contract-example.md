---
title: "Solidity staking contract example: mechanics and safety limits"
description: "Follow a Solidity staking contract example through deposits, withdrawals, and reward accounting, with assumptions, edge cases, and security limits clearly explained."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: ["staking contract architecture", "Solidity staking rewards", "smart contract security"]
author: "editorial_team"
primary_keyword: "solidity staking contract example"
owned_question: "How can a minimal Solidity staking contract account for deposits, withdrawals, and reward claims, and what assumptions and risks must be addressed before deployment?"
risk_level: "high"
---

A minimal Solidity staking contract can record each account’s deposited principal, calculate rewards from explicit accounting rules, and let users withdraw principal or claim rewards through separate functions. The example below is an accounting illustration—not a tested or production-ready contract—and its reward logic depends on funding, timing, and token behavior that a real implementation must define.

## What this staking example is designed to demonstrate

The pattern separates three concepts: principal a user deposited, rewards the contract owes under its rules, and tokens the contract actually holds. Keeping these distinct makes it easier to reason about whether a withdrawal is limited to recorded stake and whether a reward claim is backed by available funds.

This guide uses a single ERC-20-like token for both staking and rewards to keep the example narrow. It does not implement a particular protocol’s staking process. Proof-of-stake systems use committed cryptocurrency as stake, but selection, custody, withdrawal, reward, and penalty rules vary by protocol; a contract’s accounting is not a substitute for those protocol rules. [source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>)

The code omits access control, pause and recovery mechanisms, reward funding, upgradeability, and protections for unusual token behavior. Those omissions are intentional: the aim is to explain the accounting shape, not suggest that these features are unnecessary. Before adapting the pattern, developers need independent review and tests appropriate to the intended implementation.

## Solidity staking contract example: state and accounting model

The following compact example illustrates a time-based reward calculation. It assumes a trusted operator funds the contract with enough reward tokens and sets a reward rate expressed in the token’s smallest units per staked token unit per second. It also assumes ordinary token transfers behave as requested. Those are assumptions, not guarantees provided by this code.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount)
        external returns (bool);
}

contract IllustrativeStaking {
    IERC20 public immutable token;
    uint256 public rewardRate; // smallest reward-token units per stake unit per second
    uint256 public lastUpdate;
    uint256 public rewardPerStakeUnitStored;
    uint256 public totalStaked;

    mapping(address => uint256) public stakeOf;
    mapping(address => uint256) public userRewardCheckpoint;
    mapping(address => uint256) public rewards;

    constructor(IERC20 token_, uint256 rewardRate_) {
        token = token_;
        rewardRate = rewardRate_;
        lastUpdate = block.timestamp;
    }

    function rewardPerStakeUnit() public view returns (uint256) {
        if (totalStaked == 0) return rewardPerStakeUnitStored;
        return rewardPerStakeUnitStored
            + (block.timestamp - lastUpdate) * rewardRate / totalStaked;
    }

    function earned(address user) public view returns (uint256) {
        return rewards[user]
            + stakeOf[user]
                * (rewardPerStakeUnit() - userRewardCheckpoint[user]);
    }

    function _update(address user) internal {
        rewardPerStakeUnitStored = rewardPerStakeUnit();
        lastUpdate = block.timestamp;
        if (user != address(0)) {
            rewards[user] = earned(user);
            userRewardCheckpoint[user] = rewardPerStakeUnitStored;
        }
    }

    function deposit(uint256 amount) external {
        require(amount > 0, "zero amount");
        _update(msg.sender);
        stakeOf[msg.sender] += amount;
        totalStaked += amount;
        require(token.transferFrom(msg.sender, address(this), amount), "transfer failed");
    }

    function withdraw(uint256 amount) external {
        require(amount > 0 && amount <= stakeOf[msg.sender], "invalid amount");
        _update(msg.sender);
        stakeOf[msg.sender] -= amount;
        totalStaked -= amount;
        require(token.transfer(msg.sender, amount), "transfer failed");
    }

    function claim() external {
        _update(msg.sender);
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "no rewards");
        rewards[msg.sender] = 0;
        require(token.transfer(msg.sender, amount), "transfer failed");
    }
}
```

`stakeOf` records each user’s principal, while `totalStaked` is the aggregate used as the denominator for reward allocation. `rewardPerStakeUnitStored` accumulates rewards per unit of stake, and `userRewardCheckpoint` marks the last point already credited to each account. `rewards` stores the user’s accrued but unclaimed balance.

The core accounting invariant is that a user cannot withdraw more principal than `stakeOf[user]`; `totalStaked` should change by the same amount as user stakes. Reward calculations also need a clear rounding policy: integer division truncates fractions, so small allocations may not be credited exactly. This sample does not define a mechanism to recover or redistribute rounding dust.

## How deposits, withdrawals, and reward claims work

On deposit, the contract rejects zero, updates the caller’s reward checkpoint using their existing stake, then increases the user and aggregate stake before requesting the token transfer. Updating first prevents the new deposit from being treated as if it had earned rewards during the preceding interval. However, if the token transfer fails, the transaction reverts, including the accounting changes.

This ordering is an illustrative tradeoff, not a blanket security recommendation. An external token call can transfer control to another contract, so the exact sequence and any reentrancy protections require review. Solidity’s checks-effects-interactions pattern calls for validating conditions, recording internal changes, and only then interacting externally; it reduces a class of reentrancy risk but does not make arbitrary contract code safe.

On withdrawal, the function checks the requested amount against recorded principal, updates reward accounting, reduces the user’s stake and the aggregate, then transfers the principal. The rewards mapping is separate, so withdrawing principal does not itself claim rewards. A user can withdraw and claim in separate calls; the sample does not provide a combined exit function.

On claim, `_update` first brings the user’s accrued amount current. The function then zeroes the stored reward before transferring tokens. That ordering avoids leaving the same stored amount available for a later claim if the transfer succeeds, but the example does not include a reentrancy guard or establish safety for every possible token implementation.

Repeated calls and zero amounts have explicit outcomes: deposits and withdrawals reject zero; withdrawals above recorded stake fail; claims with no positive stored reward fail. The formula’s multiplication and division can also produce rounding effects, and its reward total grows with elapsed time and configured rate. A production design would need to define how rate changes, empty-stake periods, reward exhaustion, and funding are handled.

## Security review before adapting the code

First, verify the assumptions about the token. The example treats a successful `transfer` or `transferFrom` return as evidence that the requested amount moved. It does not measure actual balance changes or address tokens with atypical transfer behavior. If the token’s behavior differs, the recorded stake can diverge from assets held.

Second, determine who can set or change the reward rate and how rewards are funded. This sample sets the rate once and has no funding function or balance check. A calculated reward is only an accounting amount; the contract may not hold enough tokens to pay it. Reward availability must be designed and checked rather than inferred from the formula.

Third, test invariants and edge cases, including repeated deposits and withdrawals, zero stake, the transition from zero to nonzero total stake, rounding, elapsed time, and insufficient reward balance. Review external-call behavior and decide whether the implementation needs reentrancy protection, access controls, a pause mechanism, or a recovery path. None is included here, and no specific safeguard is established by this illustrative code.

If a design adds third-party delegation or protocol-level validator participation, that introduces rules beyond this example. For Ethereum, ETH deposited through a third party adds custody, smart-contract, operator, and product terms outside base protocol staking. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

## What the example does not establish

The example does not establish a yield rate, guarantee that rewards will be available, or show that a particular staking arrangement is secure. It only demonstrates one possible way to represent deposits and accrued rewards. Actual security, recovery options, and operational controls depend on the specific code and environment.

Before deployment, replace the illustrative interface and accounting assumptions with requirements for the intended token and system, then obtain appropriate technical review and test the implemented behavior. This article does not address protocol selection, provider comparisons, deployment steps, or legal and tax treatment.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
