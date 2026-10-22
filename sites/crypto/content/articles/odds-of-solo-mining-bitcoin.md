---
title: "Odds of solo mining bitcoin: probability and expected timing"
description: "Learn how odds of solo mining bitcoin relate to a miner’s share of network hashrate, block-finding probability over time, and uncertainty."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["odds solo mining bitcoin"]
author: "editorial_team"
primary_keyword: "odds of solo mining bitcoin"
owned_question: "How can a Bitcoin miner estimate the probability and expected time of finding a block when mining solo, and what assumptions limit that estimate?"
risk_level: "medium"
---

A Bitcoin miner can estimate solo block-finding odds by comparing the miner’s hashrate with the network’s estimated total hashrate, then applying that share to a stated time interval. The result is a probability under simplifying assumptions, not a schedule or earnings estimate. Expected waiting time is an average, not a deadline.

## What solo block-finding odds mean

Solo mining means attempting to find a block without combining hashpower through a pool. In Bitcoin, mining is a process for constructing and proposing candidate blocks that meet the network’s proof-of-work condition. The odds question is narrower: given a miner’s share of total network hashing work and a period of time, how likely is it that the miner finds at least one block during that period?

Hashrate is the rate of hashing work. The relevant comparison is the solo miner’s hashrate divided by the estimated network hashrate. If a miner contributes one part out of every thousand parts of the network’s estimated hashrate, the estimated share is one-thousandth. This fraction describes relative hashing capacity; it does not mean the miner will find exactly one block in every thousand blocks.

A miner’s chance of finding a block depends on the miner’s hashrate relative to estimated network hashrate and the observation period. Solo-mining payouts have higher variance and longer expected gaps than pooled payouts at the same hash contribution. That describes a difference in payout patterns, not a way to predict when an individual block will be found.

## Estimate odds of solo mining bitcoin over a time period

A basic estimate treats each network block as an opportunity. Suppose the solo miner has the same chance of finding each opportunity throughout the selected interval, and treat those opportunities as independent. Define the inputs before calculating:

- **h**: the miner’s hashrate.
- **H**: the estimated total network hashrate for the period.
- **p = h/H**: the miner’s approximate share of network hashrate.
- **N**: the assumed number of network blocks during the interval.

Under this simplified model, the probability of finding at least one block in **N** opportunities is:

**1 − (1 − p)ᴺ**

For one opportunity, the model’s chance of not finding the block is **1 − p**. Across **N** opportunities, the chance of no discovery is **(1 − p)ᴺ**. Subtracting that value from one gives the chance of at least one discovery. The formula estimates whether a discovery occurs in the interval; it does not identify which block, if any, the miner will find.

For illustration, if the miner’s share were a small fraction **p**, the same expression could be evaluated using an assumed count **N** for a chosen interval. This is an illustration of how the variables relate, not a universal rule about how many blocks occur in a particular number of days. Without a justified block-count input, avoid turning the formula into a calendar estimate.

The inputs need to be compatible. The miner-hashrate figure and network-hashrate estimate should describe the same relevant time frame, and **N** must represent the assumed number of block opportunities during that interval. If the period is longer, the assumed number of opportunities changes too. A percentage without a stated interval and block-count assumption does not fully describe the event being estimated.

A numerical result also depends on the quality and timing of its inputs. Network hashrate is an estimate; a value observed at one time need not describe an entire future interval. No timestamped network-hashrate and block-production inputs are supplied for a current worked example here, so no current numerical odds are presented. This avoids giving a time-sensitive calculation the appearance of a stable Bitcoin parameter.

## Probability is not a block-finding schedule

The formula answers a bounded question: what is the modeled chance of finding at least one block in a chosen number of opportunities? It does not provide a date, countdown, or guarantee. A miner can find a block sooner than an average waiting-time estimate, or go substantially longer without finding one.

For a fixed share **p**, the geometric model’s expected number of opportunities until the first success is **1/p**. This is a mathematical average under the model, not a claim that discovery will occur after exactly that many opportunities. If an assumed average block rate is used to translate opportunities into time, the conversion also depends on that assumed rate and on the miner’s share remaining stable. Expected time remains an average over possible outcomes, not the point at which success is due.

Probability and expected waiting time answer different questions. The probability calculation asks whether at least one discovery occurs within a selected interval. Expected waiting time describes an average number of opportunities—or, with an assumed block rate, an average time—until the first discovery. Neither says that a miner will receive a block by a deadline. A probability estimate also does not establish guaranteed rewards or income.

A common interpretive mistake is to treat an average as a countdown. If an average estimate has passed without a discovery, that fact alone does not mean a block is now due. Conversely, a discovery can occur earlier than the average. The estimate concerns a range of possible outcomes rather than a predetermined sequence for one miner.

## What can change the estimate

The miner’s effective hashrate and the network’s total hashrate both affect **p**. If either differs from the assumed value, the estimated share changes. The number of opportunities **N** depends on the interval and on the assumed block production during it. The calculation should therefore be read as an estimate based on specified inputs, rather than as a timeless property of a miner or the network.

The formula assumes a stable share across the opportunities being modeled. If a miner’s effective hashrate or the network estimate changes during the interval, one fixed value of **p** may represent the period less well. The expression also treats each opportunity as having the same success probability and uses a chosen count of opportunities. Those assumptions make the calculation understandable, but they do not make it a real-time prediction.

The interval itself is an important part of the result. A chance calculated for one window cannot be presented as though it applied to a different window with no change to **N**. When evaluating an estimate, check whether the period is explicit, what block count was assumed for it, and whether the hash-rate inputs correspond to that same period. If these inputs are uncertain or mismatched, the result should be described as correspondingly approximate.

For careful reporting, keep four items visible: the miner-hashrate value, the network-hashrate estimate, the interval, and the assumed number of block opportunities. Note the timing of the estimates and avoid presenting extra decimal places as certainty. Precision in the arithmetic cannot correct uncertainty in the assumptions or the inputs.

## How to interpret a solo-mining estimate

Read the result as the modeled chance of at least one block discovery over a named interval under stated assumptions. Do not read it as the probability that a block will arrive at one particular time, or as a promise that an average waiting period will end in success. Keep probability separate from expected waiting time, and both separate from claims about earnings.

When comparing estimates, compare the inputs and intervals as well as the percentages. One estimate may use a different miner hashrate, network estimate, observation window, or assumed block count. If those details are missing, the figures may not address the same event. A clearly stated estimate tells readers what was assumed and what the result means; it does not turn uncertain network conditions into a fixed forecast.

The calculation is a way to understand how a miner’s relative hashrate relates to block-finding probability. It is not evidence of profitability or a recommendation to mine. Its most useful output is a bounded, qualified answer: an estimated chance for a defined interval, conditional on the stated share and block-opportunity assumptions.

## Sources and references

- [Mining - Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-21.
- [getnetworkhashps (Bitcoin Core 30.0 RPC)](https://bitcoincore.org/en/doc/30.0.0/rpc/mining/getnetworkhashps/) — Bitcoin Core; retrieved 2026-10-21.
