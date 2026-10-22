---
title: "Crypto Layer 2 Projects: How Their Architectures Relate to Base Chains"
description: "Understand crypto layer 2 projects through their base-chain relationship, execution model, data availability, and settlement or proof design."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["layer 2 blockchain", "rollup", "data availability", "settlement layer"]
author: "editorial_team"
primary_keyword: "crypto layer 2 projects"
owned_question: "What makes a crypto project a layer 2, and how can readers compare its relationship to the underlying blockchain?"
risk_level: "medium"
---

A crypto project qualifies as a layer 2 only through its architectural relationship to an underlying blockchain: readers need to identify which functions it performs away from that base chain and what role the base chain retains. To compare designs, examine where transactions execute, where their data is available, and how results are connected to or validated through the underlying chain. The “layer 2” label alone does not establish a project’s security, fees, or recovery options.

## What qualifies as a layer 2 project?

“Layer 2” describes an architecture, not simply a fast network or a marketing category. A useful first test is whether the system separates transaction execution from an underlying blockchain while retaining a defined relationship to that blockchain. A rollup, for example, separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. This is a description of a particular architectural pattern, not proof that every project using the layer 2 label follows it. [source](<https://ethereum.org/developers/docs/scaling/>)

Several terms help make that relationship precise:

- **Base layer or Layer 1:** The underlying blockchain to which a system connects. The name alone does not tell you which functions it provides.
- **Execution:** Processing transactions and calculating their resulting state changes. The key question is where this happens.
- **Data availability:** Whether participants can obtain transaction data needed to check summarized state changes. This is a separate question from where execution occurs.
- **Settlement:** The role a chain plays in recording or recognizing outcomes. A project’s documentation should specify what its base chain does rather than relying on the word “settlement” as a catchall.
- **Proof or challenge mechanism:** A described method for establishing or disputing whether a state transition is correct. The general layer 2 label does not identify which method, if any, a project uses.

These functions need not be assigned to one layer in every architecture. In the monolithic-versus-modular model, a monolithic base layer performs execution, settlement, consensus, and data availability together, while a modular stack can assign those functions to specialized layers. That distinction is a framework for reading architecture, not a claim that every deployed system cleanly fits one side of the comparison. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

Project terminology can vary, and a label is not a substitute for a functional description. Start with current technical documentation and translate its statements into specific answers: which chain is named, where execution occurs, where data is published or otherwise available, and what the documentation says about settlement or proof. If the document does not answer one of those questions, retain that uncertainty rather than filling it with assumptions about the category.

## Crypto layer 2 projects and their base-chain relationship

Identify the base chain first. Then list the functions the project says that chain performs and the functions it assigns elsewhere. For a rollup, the documented pattern is execution away from the base layer and publication of transaction data to Ethereum, with Ethereum consensus establishing the published record. That relationship does not mean that execution itself takes place on Ethereum. [source](<https://ethereum.org/developers/docs/scaling/>)

The functional map matters more than a project’s shorthand description. For each system, separate at least three statements: where transactions execute, where the data needed to assess the state transition is made available, and how the outcome relates to the base chain. If the source says only that a project “uses” a particular chain, that statement does not resolve which of these functions the chain supplies.

Also distinguish a chain’s role from the layer 2’s own execution environment. The base chain may be described as providing consensus or recording published data, while transaction processing happens elsewhere. Those are different responsibilities. Avoid turning a narrow description—such as data being posted to a chain—into a broader conclusion about every settlement, verification, or recovery condition. Those points require separate, project-specific evidence.

Data availability is especially important to state precisely. In L2BEAT’s terminology, a rollup uses a Layer 1 for consensus and data availability; systems that publish data elsewhere add external data-availability assumptions and are classified differently. This is a terminology framework, not a conclusion about a particular project until its data path and dependencies have been checked. A project’s own category label should not override evidence about where its data is published. [source](<https://l2beat.com/glossary>)

A reader can therefore describe the base-chain relationship without ranking projects: “The documentation identifies chain X as the base layer, assigns execution to environment Y, and says transaction data is published to Z.” If the source does not specify settlement or validation, say so. This wording separates what is documented from what remains unresolved.

## Compare execution, data availability, and settlement

Use the same questions for each project, and preserve the boundaries between them. A consistent comparison prevents one well-described feature from standing in for an entire architecture.

**Execution:** Determine where transactions are processed and where resulting state changes are calculated. Then look for the documented validation method. A statement about the execution location alone does not tell you how correctness is checked. Ethereum documentation describes full nodes as independently verifying blocks and transactions against protocol rules rather than relying entirely on another node. That describes an Ethereum node role; it should not be treated as evidence about a separate project’s own execution or verification process. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

**Data availability:** Find where transaction data is made available and what participants are expected to rely on to obtain it. A rollup in the terminology above uses a Layer 1 for data availability, whereas systems that publish data elsewhere add external data-availability assumptions and are classified differently. Record the actual documented data path rather than inferring it from a project’s name or branding. If the source does not explain access to the relevant data, list that as an open question instead of asserting that data is available in a particular way. [source](<https://l2beat.com/glossary>)

**Settlement or proof design:** Identify what the documentation says connects outcomes to the underlying chain. It may describe publication, commitments, or a proof-related process, but each term needs its own explanation and project-specific support. Do not assume that all layer 2 systems use the same settlement method, or infer a particular challenge or validity mechanism from the category label. If the source does not say how a result is established or disputed, mark the mechanism as unspecified.

A comparison table can keep the questions distinct:

| Dimension | What to record | What not to assume |
|---|---|---|
| Base-chain relationship | Named chain and the functions assigned to it | That “uses” means the chain provides every core function |
| Execution | Where transactions are processed and how results are described as checked | That execution location alone establishes correctness |
| Data availability | Where relevant transaction data is published or made available | That a project’s label proves where data resides |
| Settlement or proof | Documented connection between outcomes and the base chain | That all layer 2 projects use the same proof or challenge design |
| Evidence gaps | Unanswered questions, conditions, and dependencies | That missing details can be supplied from category-wide assumptions |

This table produces an architectural comparison, not a security score or project ranking. Two projects may both use the layer 2 label while assigning functions differently or depending on different chains and components. The shared label therefore does not establish that their designs or assumptions are equivalent.

## Verify project claims and important limitations

Prefer current technical documentation and keep conclusions close to the evidence. Record the document’s date or version when available, and check that it describes the system being compared. A project’s documentation can describe an intended architecture; the description alone is not an independent assessment of whether the system operates as described.

For every major claim, ask what it actually establishes. A statement that execution occurs away from the base layer does not, by itself, specify the data-availability arrangement. A statement that data is posted to a chain does not, by itself, describe every settlement or proof detail. And a statement about a general architecture does not establish a project’s specific dependencies or behavior. Keeping these claims separate avoids drawing a broader conclusion than the documentation supports.

Look for changes and limitations in the specific design. A project may assign different functions to different layers, and its documentation may describe dependencies or leave exceptional conditions unresolved. When information is missing, label the gap clearly. Do not treat a broad architecture category as evidence that a system has a particular recovery path, availability level, or security property.

The same boundary applies to fees, yields, service availability, and compliance status: none follows from the layer 2 label alone. They are separate questions requiring current, project-specific evidence, and they are outside what an architectural classification can establish.

A careful final comparison can be concise: name the base chain identified in the documentation; state where execution occurs; describe where relevant data is made available; summarize only the documented settlement or proof mechanism; and list what remains unclear. This gives readers a meaningful basis for comparing crypto layer 2 projects without turning technical categories into recommendations or treating incomplete evidence as certainty.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
