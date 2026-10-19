---
title: "What Is a Crypto Mining Rig? Compute, Power, Cooling, and Control"
description: "Understand the components of a crypto mining rig, including hashing hardware, controllers, power delivery, cooling, networking, pool connections, and telemetry."
date: "2026-10-19"
draft: false
content_type: "definition"
topics: ["mining-consensus"]
tags: ["cryptocurrency mining rig", "mining rig components", "ASIC mining rig", "GPU mining rig", "mining hardware system"]
author: "editorial_team"
primary_keyword: "crypto mining rig"
owned_question: "What is a crypto mining rig, and how do its compute, power, cooling, and network components work together?"
risk_level: "medium"
---

A **crypto mining rig** is the complete system that performs proof-of-work hashing and connects that computation to a blockchain or mining pool. It includes more than processors. A usable rig needs hashing hardware, a controller and firmware, power conversion and delivery, cooling, a network interface, mining-protocol software, and telemetry.

The term covers both modular frames and integrated appliances. Both receive work, search hashes, report results, remove heat, and expose operating measurements.

## A mining rig is a complete hashing system

NIST describes proof-of-work mining as repeated computation used to find a hash that satisfies a target. The chips perform that search, but other subsystems keep the search meaningful and continuous. A controller prepares or receives work, assigns it to hashing devices, collects candidate results, and submits qualifying results upstream.

Power supplies convert facility input into the voltage rails the electronics require. Fans, ducts, heat sinks, liquid loops, or immersion systems carry away the heat. Network hardware connects the controller to a node, proxy, or pool. Firmware coordinates all of these parts and reports their state.

A rig is therefore a data path and an energy path. The data path runs from block template or pool job to controller, hashing device, share, and upstream server. The energy path runs from facility power through conversion and compute into heat that the cooling system must reject. A failure in either path stops useful mining.

## ASIC and GPU rigs package compute differently

An application-specific integrated circuit, or ASIC, is designed around a particular hash function or family of related work. Commercial ASIC miners often package hash boards, a controller, power interfaces, fans or liquid connections, and Ethernet in one chassis. Their algorithm support is fixed by hardware design, so model and network compatibility must be checked before use.

A GPU rig is more modular. It usually combines a motherboard, processor, memory, storage, several graphics cards, risers or direct slots, one or more power supplies, a frame, and an operating system with mining software. GPUs can execute different programs, but that flexibility does not make every algorithm efficient or supported. Driver, operating-system, and miner-software compatibility become part of the system boundary.

Efficiency is algorithm- and workload-specific; flexibility is not a universal advantage. [What Bitcoin mining is](/articles/what-is-bitcoin-mining/) explains why specialized SHA-256 hardware dominates that network without turning this definition into a buying guide.

## The controller turns pool jobs into device work

Bitcoin's developer documentation describes mining software receiving template information and constructing work for hashing hardware. In a pooled deployment, a pool server or proxy normally supplies jobs and a target for submitted shares. The rig controller expands each job into many candidate headers by changing permitted fields and distributes non-overlapping search ranges to chips or workers.

Stratum V2 formalizes distinct roles for a mining device, pool server, and optional proxy. Its Mining Protocol requires upstream software to allocate unique portions of the search space so devices do not waste power duplicating the same work. The device reports shares that satisfy the pool target. A share demonstrates contributed work for pool accounting but may not meet the much harder network target required to create a block.

When a new previous block arrives, the current search can become stale. The controller must receive updated work quickly, stop obsolete assignments, and keep devices supplied. Network delay, an overloaded proxy, pool disconnection, controller faults, or clock problems can therefore reduce useful output even when the hashing chips remain powered.

## Power delivery and cooling are part of the rig

Hashing converts electrical input into computation and heat. The power subsystem includes the facility circuit, cord and connector, power-supply unit, distribution inside the rig, and voltage regulation near the compute devices. Each part must match the exact model and continuous load. Electrical design and installation belong to qualified personnel working under applicable local code; a component overview is not a wiring instruction.

Cooling begins at the chip and ends where heat leaves the room or fluid loop. An air-cooled rig relies on heat sinks, fans, clear intake and exhaust paths, and sufficient room ventilation. Liquid-cooled equipment adds pumps, cold plates or immersion fluid, plumbing, heat exchangers, leak control, and coolant telemetry. Blocking one link in the heat path can cause throttling, errors, or shutdown.

BITMAIN's S21 Pro version 10 is one example of an integrated appliance: its specification connects a named SHA-256 model with model-specific wall power, input requirements, environmental limits, forced-air noise, and RJ45 networking. Those details illustrate why a "mining rig" cannot be sized from hashrate alone. They do not transfer to another model or constitute a product recommendation.

## Telemetry reveals the failure domain

A rig should report signals from each subsystem:

- **Compute:** device and board hashrate, active chips, hardware errors, frequency, and throttling.
- **Pool path:** accepted, stale, duplicate, low-difficulty, and invalid shares; job age; endpoint latency; disconnects.
- **Thermal:** inlet, outlet, chip or board temperature; fan speed; pump flow; coolant temperature.
- **Power:** measured wall power, supply alarms, voltage or current telemetry where supported, and unexpected resets.
- **Control:** firmware version, configuration changes, controller load, clock state, and reboot history.
- **Facility:** room conditions, ventilation or heat-rejection state, and smoke, leak, or access alarms.

The combination narrows diagnosis. Normal chip temperature with zero shares can indicate a pool, network, configuration, or controller problem. Rising temperature with falling hashrate can indicate blocked airflow, a fan failure, insufficient heat rejection, or thermal throttling. Reboots under load can point toward power delivery, protection, firmware, or hardware faults. Telemetry identifies a direction; it does not replace the manufacturer's troubleshooting procedure.

## A rig specification is not an operating result

Keep four value types separate:

1. **Rated or allowed value:** a boundary on the nameplate or manual, such as input range or maximum environmental condition.
2. **Typical value:** a representative manufacturer figure under stated test conditions.
3. **Local measurement:** wall power, temperature, noise, or device hashrate observed for one installed unit.
4. **Pool estimate:** hashrate inferred statistically from accepted shares over a time window.

The S21 Pro page explicitly presents several performance figures as typical and allows stated variation. A pool estimate can vary more because share discovery is probabilistic. Comparing a five-minute pool estimate with a laboratory typical value can therefore suggest a fault where none exists. Use consistent time windows and compare device telemetry, pool shares, and measured power together.

A rig also does not determine profitability by itself. Network difficulty, reward rules, transaction fees, asset price, energy tariff, cooling overhead, pool fees, downtime, maintenance, and depreciation all vary. Technical capability and economic viability should be measured separately.

The concise definition of a **crypto mining rig** is thus a coordinated proof-of-work system: compute hardware searches hashes, a controller and protocol supply jobs and collect shares, power infrastructure feeds the workload, cooling removes its heat, networking connects it upstream, and telemetry exposes whether each layer is working. [How to set up crypto mining](/articles/how-to-set-up-crypto-mining/) turns those components into a controlled commissioning sequence, while [proof of work](/articles/what-is-proof-of-work-in-blockchain/) explains the consensus role of the result.

## Sources and references

- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Stratum V2 Protocol Overview](https://stratumprotocol.org/specification/03-protocol-overview/) — Stratum V2; retrieved 2026-10-19.
- [Stratum V2 Mining Protocol](https://stratumprotocol.org/specification/05-mining-protocol/) — Stratum V2; retrieved 2026-10-19.
- [S21 Pro Specification](https://support.bitmain.com/hc/en-us/articles/31321354157593-S21-Pro-Specification) — BITMAIN Support; retrieved 2026-10-19.
