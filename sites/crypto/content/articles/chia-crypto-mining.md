---
title: "Chia crypto mining: how proof of space and time works"
description: "Learn how chia crypto mining uses plotted storage, proof of space, and proof of time, and why the process is commonly called farming."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: []
author: "editorial_team"
primary_keyword: "chia crypto mining"
owned_question: "How does Chia’s proof-of-space-and-time consensus work, and what role do farmers’ storage and network time proofs play?"
risk_level: "medium"
---

Chia’s proof-of-space-and-time consensus uses plotted storage to provide proofs of space, alongside a time component; participants doing this work are commonly called farmers. The distinction from proof-of-work is useful, but the evidence available for this overview does not document Chia’s current protocol steps in enough detail to specify exactly how its plots, challenges, time proofs, or validation work. This article explains the supported distinction and identifies where Chia-specific details require current primary documentation.

## Why Chia farming is different from proof-of-work mining

Proof of work is a consensus model in which a participant solves a computational problem that is costly to solve but straightforward for other nodes to verify. The process consumes time, energy, and computational cycles, and the concrete algorithms, difficulty rules, and hardware differ by network. Chia is described here in terms of proof of space and proof of time instead. That difference in terminology signals a different consensus approach, not a claim that the two systems share the same participant workflow.

In Chia usage, participants are commonly called farmers, and the activity is commonly described as farming. “Chia crypto mining” remains a familiar search phrase, but the word “mining” can blur distinctions between protocols. Proof-of-work mining refers to the computational work used in proof-of-work systems; it should not be used as a precise description of Chia’s storage-based participation.

This distinction also limits what can be inferred. A general proof-of-work description does not explain how Chia stores plot data, processes challenges, or combines space and time proofs. Nor does the label “farming” establish that storage participation has no costs or that a participant will receive rewards. Those are separate operational and economic questions, and this mechanism overview does not make claims about them.

## How plots provide proof of space

A plot is described in the approved Chia overview as prepared data used by a participant to respond to network challenges. At a high level, the farmer’s storage provides plot data that may be matched against a challenge to produce a proof of space. The concept is that participation involves demonstrating available plotted space through a proof, rather than relying only on the proof-of-work model’s repeated search for a computational result.

The distinction between plot preparation and challenge response matters. Preparing plot data is not the same activity as checking that data against a particular challenge. The plan identifies plots as prepared files and challenge matching as part of proof generation, but the allowed evidence does not provide the current plot format, creation procedure, matching algorithm, or exact proof contents. Those implementation details should therefore not be treated as established here.

A useful comparison boundary is Filecoin’s Proof-of-Spacetime. That Filecoin-specific mechanism is designed to let a storage provider prove to its network that it continues to store a unique copy of committed data. It illustrates that storage-related proofs can be designed for particular protocol purposes, but it does not establish how Chia’s proof of space works. A reader should not transfer Filecoin’s mechanism or terminology to Chia without Chia-specific documentation.

Thus, the reliable high-level account is modest: plots are part of the storage side of Chia farming, and plot data is used in responding to challenges. Details such as how a plot is made, how often it is checked, which plot data qualifies, and what software performs each operation need to be verified against the relevant Chia documentation and software version.

## Where proof of time fits in Chia consensus

Proof of time is the time-related element named alongside proof of space in Chia’s consensus description. The plan calls for discussing a verifiable delay function, a computation designed to demonstrate an elapsed interval in a verifiable way. However, the allowed claims do not substantiate the specific Chia function, its inputs or outputs, who computes it, how it is verified, or how its result is combined with a proof of space. Those protocol details are omitted rather than inferred from another network’s design.

At the conceptual level, the two terms identify different roles: proof of space concerns the storage-based contribution, while proof of time supplies a time component to the consensus process. This does not mean a time proof demonstrates that a participant owns a particular storage device. The available evidence does not establish such a device-ownership claim, and a protocol proof should not be described as proving more than the documented property.

A verifiable delay function should not be treated as a synonym for proof of space. The concepts refer to different parts of the intended Chia explanation: one concerns a time-related computation, while the other concerns plotted storage. Without current Chia specifications, the exact relationship between the two, including their ordering and validation rules, remains outside the supported detail of this overview.

That limitation is important for readers tracing consensus. Naming two proof types does not, by itself, explain how a network selects or validates a block. The specific procedure must come from the protocol’s own current documentation. No proof-of-work rule can fill this gap: proof-of-work systems use their own computational problems, targets, and chain-selection rules, which are not general definitions of Chia’s proof-of-time process.

## What a Chia farmer does during a challenge

The participant-facing sequence can be described only at a high level from the evidence available. A farmer has plots, checks relevant plot data in relation to a network challenge, and may produce a proof of space if the data qualifies. The time component also belongs to Chia’s stated proof-of-space-and-time approach. The specific software steps, timing, proof submission process, and network acceptance criteria are not documented by the allowed claims, so this is not a step-by-step operating procedure.

A qualifying proof should also not be confused with a guaranteed reward. The evidence here does not establish that every challenge produces a reward, set an expected reward frequency, or support any estimate of earnings. It describes a consensus concept, not an outcome for an individual participant. The same caution applies to any statement about fees, current participation conditions, or economic value: none can be concluded from the mechanism alone.

The farmer’s role should also be kept distinct from the network’s broader validation and consensus roles. A farmer contributes proofs under the protocol’s rules; the exact parties and software that check those proofs, and how the network uses them, require current Chia-specific evidence. A general description of proof-of-work verification does not answer those Chia questions.

For a practical reading of Chia materials, check that each explanation identifies the relevant protocol or software version and separates plot preparation, challenge checking, proof creation, submission, and network validation. If a source describes only one stage, do not assume it establishes the full lifecycle. This is especially important when a high-level term such as “farming” is used without specifying which participant action it refers to.

## What this overview does not establish

This explanation does not establish current hardware requirements, plotting procedures, software configuration, fees, security practices, wallet or key handling, or recovery options. Each requires current, specific Chia documentation. It also does not assess profitability, expected rewards, or likely returns; describing consensus mechanics cannot substantiate those conclusions.

Nor does this overview make claims about regulation, tax, service availability, or compliance in any jurisdiction. Such claims would require authoritative, jurisdiction-specific evidence. The scope here is narrower: it distinguishes the named consensus concepts, explains the high-level role assigned to plotted storage and time proofs, and marks the Chia protocol details that need verification before being stated as operational facts.

## Sources and references

- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Filecoin Glossary](https://docs.filecoin.io/reference/general/glossary) — Filecoin Docs; retrieved 2026-10-19.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-19.
