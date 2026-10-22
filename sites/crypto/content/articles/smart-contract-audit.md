---
title: "Smart contract audit: scope, process, findings, and limitations"
description: "Learn what a smart contract audit typically examines, how findings and remediation are reported, and why an audit cannot guarantee a contract is secure."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["smart contract security review", "audit scope", "audit findings", "remediation"]
author: "editorial_team"
primary_keyword: "smart contract audit"
owned_question: "What does a smart contract audit examine, how are findings handled, and what can an audit report establish about a contract’s security?"
risk_level: "high"
---

A smart contract audit is a scoped review of specified contract code and its assumptions, intended to identify and document security concerns. It can support understanding of the code that was reviewed, but it cannot establish that a contract is defect-free or that an entire application or protocol is safe. To interpret a report, check exactly what was reviewed, what findings remain, and whether fixes were examined afterward.

## What a smart contract audit is—and what it is not

An audit report records conclusions about a particular review, not a universal security guarantee. A contract’s code and data are deployed onchain, and its functions can be invoked through transactions; the report’s conclusions therefore depend on the code and materials actually examined. On a blockchain, smart-contract execution is expected to produce the same result for participating nodes, with results recorded onchain. That deterministic behavior does not itself establish that the programmed behavior is correct or safe. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/>)

An audit also should not be treated as a broad assessment of a project’s business model, governance, or every component users interact with. For example, an onchain contract cannot directly obtain offchain facts unless an oracle or transaction mechanism supplies them. Reviewing contract logic alone does not establish the quality, freshness, availability, or trustworthiness of such external inputs. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

## Set the audit scope before review begins

The report’s scope defines the boundary of its conclusions. Before review starts, project operators should make the intended review materials identifiable: the code repository and version, contracts included, relevant dependencies, and assumptions the system relies on. Those details let a reader connect findings to a specific object of review rather than assuming the report applies to every version or component.

The report should also be read for what it excludes. An audit of specified code does not automatically cover offchain services, integrations, deployment settings, or later changes. If a component or assumption is not identified as included, do not infer that it was examined. Likewise, a conclusion about one code version should not be transferred to a changed version without evidence that the change was within the review.

This boundary matters because contract behavior may rely on external information or components. An oracle, for example, connects offchain data or services to onchain contract logic; the contract’s ability to use that input does not establish the input’s reliability. The relevant question is whether the report says those dependencies and assumptions were part of the review, rather than whether the project has an audit document at all. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

## How reviewers examine smart contracts

A useful review begins with intended behavior and the assumptions that behavior depends on. The reviewer needs to understand what the code is meant to do in order to assess whether implementation and expected behavior align. The evidence available here does not establish one required audit methodology, nor does it support treating particular tools or test types as universal. A report should therefore be read according to the methods it actually discloses.

For any described review activity, distinguish the work performed from the conclusion a reader might wish to draw. A finding may document a concern identified in the reviewed materials; the absence of a finding is not proof that no concern exists. The report’s scope and disclosed methods are essential context for interpreting either result.

## Read audit findings and remediation carefully

A finding is a reported issue or concern, not a verified fix. Reports may organize findings using severity labels or other descriptions, but formats can vary. Read the report’s own definitions and supporting explanation instead of assuming that a label has the same meaning across reports. Consider what the finding says about impact and conditions, and whether the stated evidence fits the project’s response.

Then follow the issue through remediation. Check whether the project responded, what code changed, and whether the report documents review or retesting of that change. A statement that an issue was addressed is not, by itself, evidence that the change was independently examined. If the report does not say whether a fix was checked, treat that point as unverified rather than assuming it was.

Finally, compare the code version named in the report with the code currently deployed or maintained. A report’s conclusions attach to its stated scope; the report should not be used to imply review of later changes or different code. This version check is especially important when a report is being used to understand present-day risk rather than the historical review.

## What an audit cannot establish

An audit cannot guarantee defect-free code, prevent future vulnerabilities, or establish overall protocol safety. An audit maturity framework, where used, may measure decentralization and trust minimization rather than provide a complete security score; a stage label should not be treated as proof that contracts or implementations are bug-free. [source](<https://l2beat.com/stages>)

Residual risk remains when scope is incomplete, code changes, or dependencies and assumptions lie outside the reviewed materials. A contract may also depend on external facts supplied through an oracle, while the report’s conclusions concern only what its scope and methods address. These limits mean an audit is one piece of evidence about specified materials—not a forecast of future behavior or a finding about every connected system. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

An audit report also does not establish legal compliance, regulatory approval, or financial performance. Those are different conclusions and should not be inferred from technical review language. If a decision requires expertise outside the report’s technical scope, seek appropriately qualified advice.

## Questions to ask when using an audit report

Before relying on a report, check:

- **Which code was reviewed?** Find the repository, version, commit, or other identifier stated in the report.
- **What was in scope?** Read the list of reviewed components, assumptions, and exclusions rather than inferring broad coverage.
- **What methods and evidence are described?** Interpret the report based on work it documents, not on assumptions about standard practice.
- **What happened to each finding?** Separate open, addressed, and retested issues according to the report’s wording; do not treat a claimed fix as verified without evidence of review.
- **Does the reviewed code match the code of interest?** If the deployed or maintained version differs, the report alone does not establish what the changes mean for security.

A report can help explain what a review found within its stated boundary. Its value depends on that boundary, the evidence it records, and how clearly it distinguishes findings from confirmed remediation. Keep those limits visible: the report supports a scoped conclusion, not a guarantee about all code, dependencies, or future operation.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
