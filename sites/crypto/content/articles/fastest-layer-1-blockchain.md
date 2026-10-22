---
title: "Fastest layer 1 blockchain: how to assess speed claims"
description: "Learn how to assess fastest layer 1 blockchain claims by distinguishing throughput, latency, and finality, and checking whether measurement conditions are comparable"
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "fastest layer 1 blockchain"
owned_question: "What does “fastest Layer 1 blockchain” mean, and how can reported speed claims be compared fairly?"
risk_level: "medium"
---

“Fastest Layer 1 blockchain” is not a single measurable result. To assess the claim, identify whether it refers to throughput, latency, or finality, then check the workload, measurement window, and counting method behind the figure. Without matching definitions and conditions, speed numbers are not a fair basis for comparison.

## What “fastest” means for a Layer 1 blockchain

A Layer 1 refers in common crypto usage to the base blockchain network and its protocol; it is not a separately standardized technical category.  For speed comparisons, “fastest” should be treated as a question about specified performance measures rather than a universal rank.

**Throughput** describes the rate at which a system processes transactions over a stated period. It is often expressed as transactions per second, or TPS, but the number is interpretable only when the source defines what it counts and the period it covers.

**Latency** is elapsed time between two specified events. For a transaction, possible endpoints include its submission, its inclusion in a block, or a later consensus event. A latency figure without start and stop points is ambiguous: two sources may both say “confirmation time” while measuring different intervals.

**Finality** describes when a transaction or state is treated as settled under a network’s rules, according to the definition and threshold used by the source. It is not automatically equivalent to appearing in a block. The allowed evidence does not establish one finality definition or threshold for all Layer 1 networks, so use the particular network and measurement source’s definition.

These measures answer distinct questions. A throughput result does not by itself establish how quickly an individual transaction is included or when it is considered final. Blockchain scaling work may seek higher transaction speed and throughput without sacrificing decentralization or security, but that is a design objective—not a single score or proof that a particular system achieves all three. [source](<https://ethereum.org/developers/docs/scaling/>)

A speed claim also needs a scope. It may concern a particular transaction type, workload, network configuration, or observation period. Without those boundaries, readers cannot tell whether a number describes an observed rate, a test result, or a modeled capacity.

## How to read Layer 1 throughput figures

Throughput figures can represent different kinds of evidence. **Theoretical capacity** is a stated or modeled maximum under assumptions. **Benchmark throughput** reports what a test produced under its test conditions. **Observed throughput** describes activity recorded over a stated interval. These categories are not interchangeable: a capacity estimate does not show that the same rate occurred in live network activity.

Next, check what the source counts. A transaction might be submitted to the network, included in a block, executed, or described as successfully completed. These are distinct measurement boundaries. A rate based on submissions is not necessarily comparable to one based on executed transactions, and a source’s label alone may not reveal which boundary it uses.

The workload matters as well. A test with one transaction type or mix does not automatically represent other activity. Record the measurement window and configuration alongside the result. A brief peak-rate interval answers a different question from a longer observation period, while an average and a peak should not be treated as equivalent unless the source explains how they were calculated.

When a report omits its workload, configuration, time period, or counting rule, treat the figure as incomplete evidence. Do not fill in missing conditions by assuming that the number represents typical performance or maximum capability.

The reason for this care is that blockchain systems differ in participation, consensus, privacy, finality, and governance. A blockchain can be described generally as a distributed ledger using cryptographically linked transactions, validation, and conflict-resolution rules to maintain a shared history, but that description does not provide a universal formula for counting TPS. [source](<https://csrc.nist.gov/pubs/ir/8202/final>) A comparison must therefore report not only the number but also how it was produced.

## Latency, confirmation, and finality are different

Latency has meaning only relative to a defined start and endpoint. “Submission to block inclusion” and “submission to finality” are different intervals. If a source reports confirmation latency, check whether confirmation means inclusion, a later network event, or another stated threshold. If the source does not define the endpoint, the claim is difficult to compare.

Confirmation and finality should not be used as synonyms without evidence that the source defines them that way. A transaction’s appearance in a block is one possible measurement event; finality depends on the network’s consensus rules and the source’s stated meaning of settled. Different sources may use different thresholds, so a lower reported time does not necessarily mean that two networks reached the same type of endpoint sooner.

For each reported time, record the event that starts the clock, the event that stops it, and any confirmation or finality threshold. Also note the source’s measurement window and whether it reports a typical observation, a summary, or a particular case. If those details differ between figures, present them separately rather than claiming a direct latency comparison.

This method also prevents a common interpretation error: treating one quick event as a complete measure of transaction performance. Inclusion, execution, and finality refer to different stages or boundaries when the source distinguishes them. A short interval measured to one endpoint cannot stand in for a longer interval measured to another.

## A like-for-like checklist for speed claims

Before citing or using a Layer 1 speed figure, capture the following information:

1. **Metric and unit:** Is the claim about throughput, latency, or finality? What unit, definition, and threshold does the source use?
2. **Counting boundary:** Does throughput count submitted, included, executed, or completed transactions? For latency, what events start and stop the clock?
3. **Workload:** What transaction type or mix is represented? Is the result a modeled capacity, a benchmark, or activity observed on the network?
4. **Conditions and time window:** What configuration and period does the figure cover? Does the source describe a peak, average, or other summary?
5. **Source and method:** Does the source identify the data and method sufficiently for readers to inspect how the number was obtained? Are limitations stated?
6. **Comparability:** Do the figures being compared use compatible definitions, workloads, conditions, time windows, and measurement boundaries?

If one or more answers are missing, state the gap. The number may still describe what its source reports, but the omission makes a like-for-like comparison uncertain. Do not treat a collection of differently measured figures as evidence of a universal fastest network.

Reproducibility is a useful check, not a substitute for a matching metric. A result may be inspectable yet still differ from another result in workload or endpoint. Conversely, two sources may use similar labels while measuring different things. Make the comparison boundary explicit before drawing a conclusion.

## Speed trade-offs and evidence limits

Throughput alone does not describe decentralization, reliability, security, or user experience. Node count by itself does not establish operator independence, geographic diversity, implementation diversity, or the distribution of block-production power. [source](<https://csrc.nist.gov/pubs/ir/8202/final>) These are separate questions; a TPS result does not answer them.

A throughput claim also does not establish that activity is consistently available or that every transaction type experiences the same latency. Those conclusions require evidence about the relevant conditions and endpoints. Do not infer fees, availability, security, compliance, or future performance from a speed metric alone.

Scaling work can separate transaction execution from the base layer while posting data or commitments to that layer, allowing batches to use it for consensus and settlement. [source](<https://ethereum.org/developers/docs/scaling/>) This is relevant when interpreting the measurement boundary: a figure must make clear what work it counts and where it occurs. It does not, by itself, establish a comparable Layer 1 speed result, so keep the metric and architecture scope explicit rather than treating unlike measurements as equivalent.

In practice, use “fastest” only with a stated metric and scope—for example, the highest reported throughput under a named method, workload, and measurement window. If the source does not provide enough detail to verify that scope, describe the result as an unqualified claim, not proof of a universal fastest Layer 1 blockchain.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [NIST IR 8202: Blockchain Technology Overview](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
