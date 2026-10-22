---
title: "Layer 2 blockchain projects: examples and how to assess them"
description: "Explore layer 2 blockchain projects through a neutral reference list, with criteria for checking architecture, Layer 1 relationships, and evidence."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 blockchain projects"
owned_question: "What are examples of Layer 2 blockchain projects, and how can readers distinguish them by architecture and relationship to their underlying Layer 1?"
risk_level: "medium"
---

The evidence available for this reference list does not identify individual Layer 2 projects or establish their current status, architecture, and relationship to an underlying Layer 1. It therefore cannot support a verified list of named projects. The criteria below show what evidence a project profile needs and how readers can distinguish documented architecture without treating a label as proof.

## What qualifies as a Layer 2 project in this list?

Include a project only when its technical documentation establishes a relationship to an underlying Layer 1 and explains the role that layer plays. A project name, promotional description, or use of the term “Layer 2” is not sufficient evidence of technical classification. The profile needs to connect the project to a specific base network and document how their roles relate.

For each candidate, look for clear answers to three questions: Where does transaction execution happen? Where is relevant transaction data made available? What does the underlying Layer 1 do in relation to settlement or security? These functions should be recorded separately rather than inferred from a general label. A modular architecture model, for example, distinguishes execution, settlement, consensus, and data availability as separate functions that can be assigned to specialized layers. [claim_four_functions] That model is a way to organize questions, not evidence that a particular project uses any given arrangement.

Keep the comparison unit precise. “Project” may refer to an organization or initiative, while “network” can mean the environment where activity takes place, “protocol” can refer to rules or interactions, and a “scaling technology” can describe an architectural approach. Do not treat these words as interchangeable if a project’s documentation uses them differently. Use the name and terminology the primary source uses, and flag ambiguity rather than resolving it by assumption.

Inclusion is descriptive, not an endorsement, ranking, or assessment of suitability. A project’s documented architecture does not establish that it is appropriate for a particular organization or application. Nor should a maturity label be treated as a complete security verdict: the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization, rather than proving that contracts, proof systems, bridges, or implementations are free of defects. [claim_stages_not_security_score]

## Examples of layer 2 blockchain projects

The authorized evidence for this article supplies no project-specific documentation. It does not name individual projects or establish their current status, architecture, or underlying Layer 1 relationship. Consequently, a verified examples list cannot be responsibly populated from this evidence. Supplying project names from memory would risk presenting unsupported or outdated descriptions as current facts.

A publication-ready directory should use a consistent profile for every entry. At a minimum, record:

- **Identity:** the exact project or network name used in its current primary technical documentation. Clarify whether the entry is an organization, network, protocol, or technology when the source distinguishes them.
- **Underlying Layer 1:** the specific base network identified by the project’s documentation. Do not infer this from a product name or from general ecosystem context.
- **Execution:** what the documentation says about where transactions or computation are processed. If the source does not specify this, mark it as unavailable rather than guessing.
- **Data availability:** what the documentation says about where transaction data or other relevant information is published or made available. Do not assume that a settlement relationship establishes the data arrangement.
- **Settlement and security assumptions:** describe the role the project assigns to the underlying Layer 1, and distinguish that stated role from any broader claim about security guarantees.
- **Status and evidence date:** include dated evidence that directly supports whether the project is deployed, in development, or undergoing a material transition.

These fields make entries comparable without implying that projects share equivalent designs. If primary documentation does not answer one of the questions, leave the field explicitly unknown or exclude the project until evidence is available. State the date on which the directory was checked and make clear that the list is not exhaustive unless a defensible method establishes exhaustiveness. No current date or status is asserted here because the allowed evidence does not establish one.

## Compare architecture and Layer 1 relationships

Compare projects by the functions their documentation assigns, not by their shared use of a category label. The modular architecture model separates execution, settlement, consensus, and data availability, while recognizing that specialized layers can receive different assignments. [claim_four_functions] Use those functions as a compact comparison checklist: identify the documented executor, data location, settlement role, and consensus relationship for each entry. If a project source does not disclose one of these roles, say so instead of filling the gap with a generic description of Layer 2 systems.

Next, separate a project’s stated security assumptions from independently established guarantees. Documentation may describe how a project relates to an underlying Layer 1, but the description alone does not establish every property of its transaction path or every failure condition. The authorized evidence provides no project-specific security proofs or assessments to compare. Avoid expanding a narrow architecture statement into a conclusion that the Layer 1 guarantees all project activity.

Shared labels also do not establish equivalent designs. Two projects might use the same terminology while assigning execution, data availability, or settlement differently; only project-specific technical evidence can resolve that comparison. Record the source, version or date when available, and the precise claim it supports. When documentation is ambiguous or silent, retain that limitation in the profile rather than presenting a clean but unsupported comparison.

Architectures and terminology can change. A profile should therefore be revisited when current documentation or dated technical records indicate a material change to execution, data handling, settlement, or the Layer 1 relationship. An older description can remain useful as historical information, but it should not be presented as a current account without evidence that it still applies.

## Verify project claims and current status

Begin with the project’s primary technical documentation. Find explicit statements about its underlying Layer 1, execution path, data handling, settlement role, and assumptions. Where the project refers to Layer 1 records or specifications, check those records for the specific claim being made. A summary page can identify what the project says; it does not by itself verify every architectural detail.

For status, seek dated evidence that directly identifies the relevant network or deployment and makes its status clear. Do not infer that a project is operating from the existence of a documentation page. Distinguish a live deployment, test environment, development effort, or material transition only when the evidence supports that distinction. If the source is undated or unclear, report status as unverified rather than supplying a likely answer.

Treat security assessments and operational claims as separate verification tasks. If a profile later includes an audit or other assessment, identify its author, date, scope, and limitations; do not use the existence of an audit alone to claim that a project is secure. A maturity framework also needs its own scope stated: the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization, not a complete security score. [claim_stages_not_security_score]

Availability, fees, yields, recovery mechanisms, and compliance or regulatory status likewise require specific, appropriately scoped evidence. No such project-specific claims are made here. In particular, do not turn an undated page or an architectural label into a claim about current availability, cost, recovery, or legal treatment.

The result is a verification-first directory method, not a ranking. With no named project documentation authorized for this article, the responsible reference list contains no named entries. Add examples only when evidence supports their identity, current status, architecture, and relationship to an underlying Layer 1; retain uncertainty wherever the documentation leaves a field unresolved.

## Sources and references

- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
