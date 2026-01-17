# Atmospheric Reserves Computer (ARC) and Gas Economy Design Document

## Status
**Proposal**

## Overview / Core Goal

Introduce a realistic gas economy where gases are no longer infinite or free. All gas usage, loss, and production ties into a dedicated departmental budget called AIR (Atmospheric Integrity Reserve).

This creates meaningful trade-offs:
- Wasteful practices (overpressurizing pipes, unnecessary venting, poor pipe design, large breaches) cost station funds directly.
- Encourages efficient atmos gameplay: better pipe layouts, recycling loops, in-house basic gas production, careful management.
- Prevents early/mid-game exploits for infinite cash and energy while providing starting leeway.
- Forces late-game coordination with Cargo for exotic/rare gases instead of self-sufficient infinite production.

Gas becomes a purchasable commodity with per-mol pricing, managed through the ARC, a specialized console tied to Cargo ordering systems but focused on atmos needs.

## The ARC (Atmospheric Reserves Computer)

- New computer placed in Engineering/Atmos areas (near main distribution loop/gas storage).
- Specialized Cargo Request Computer variant dedicated to gas procurement and budget oversight.
- Linked to gas extractors (miners) that supply purchasable gases.
- Key features:
  - View and manage AIR budget balance.
  - Purchase gases directly from linked extractors (configure output pressure, moles-per-second rate).
  - Emergency money case: pull cash from an emergency case if AIR depleted and station distro is low.
  - UI shows current reserves in extractors, extractor status, cost per mol.

## The AIR Budget (Atmospheric Integrity Reserve)

- Separate departmental fund for gas-related expenses.
- Prevents atmos mismanagement and experimentation from bankrupting the entire engineering department.
- Starts with generous buffer for round start and early game.
- Income sources:
  - Initial round-start allocation.
  - Periodic department budget payouts.
  - Typical cargo activity.
- Spending occurs on:
  - Every mole of gas purchased via ARC.
  - Typical cargo catalog items.
- Isolates risk: catastrophic breach costs AIR money, not whole station budget, but repeated issues can force emergency transfers or budget requests.

## Gas Pricing and Valuation

All gases have monetary value per mole (values to be tuned based on testing):
- Oxygen (O₂): $0.10 / mol
- Nitrogen (N₂): $0.01 / mol
- Single tile of breathable air mix (roughly 21% O₂ / 79% N₂ at 101 kPa) = $3 in raw cost.
- Waste and common gases (CO₂, Water Vapor) remain cheap.
- Other gases (N₂O, Plasma, etc.): higher values.
- Prices make basic air meaningful but affordable early; exotic gases require late-game Cargo interaction.

## Changes to Gas Sources / Extractors

- Gas miners / extractors no longer provide infinite free gas.
- Internal finite reserves (equivalent to 10-50 full canisters depending on type/tier).
- Depleted reserves stop production until ARC purchase replenishes them.
- ARC controls extractor output: set pressure, flow rate (moles/second) to avoid overproduction waste.
- Ends exploits like infinite plasma/oxygen for TEG overclocking or frezon/healium spam.

## Tool / Item / Machine Adjustments

- Canisters / Portable tanks: filling draws from paid reserves (via pipes or ARC-linked fill ports).
- Gas recyclers / electrolyzers: more important for in-house O₂ production from station air or waste loops (reduces ARC spending).
- Distro loops / pipes: efficiency critical; leaks or bad designs bleed budget.
- No free/infinite sources remain; station-produced air ties back to initial paid gases or recycling.

## Gameplay Implications

- Early game: forgiving startup budget for basic setup and minor spacing.
- Mid game: forces optimization, recycling, minimizing loss.
- Late game: exotics require Cargo collaboration.
- Antag / events: breaches, fires, deliberate venting drain AIR quickly, force command attention.
- Balance: poor atmos play hurts station funds and requires active management.
- Fun factor: introduces resource-management style gameplay to atmos.

## Detailed Gameplay & Station-Wide Implications

Implementing the ARC, AIR budget, and priced gases fundamentally alters how atmospherics functions and how the station as a whole operates. These changes remove the ability for atmos to generate infinite money and energy, shifting the department from a passive powerhouse to an active, resource-constrained guardian of the station's atmosphere. The effects ripple outward, touching every department and round phase in ways that demand careful balancing through live playtesting.

At its core, this system changes the atmos mindset from "set it and forget it" to deliberate stewardship. Gases now carry real economic weight: every mole purchased, every leak tolerated, every unnecessary vent or overpressurized pipe translates to AIR funds spent. Basic station air remains relatively forgiving - nitrogen is cheap, oxygen costly but manageable with recycling and electrolyzers - allowing room for honest mistakes, minor spacing events, or even deliberate waste in controlled scenarios (e.g., testing a new loop or emergency purging). However, repeated or large-scale waste (major hull breaches, prolonged fires, careless distro overproduction) can drain the AIR budget noticeably, creating tension without immediately bankrupting the department. The starting buffer and emergency money case provide leeway for early experimentation and recovery, but sustained inefficiency forces active intervention: better pipe layouts, closed recycling loops, conservative flow rates, and in-house O₂ production to stretch reserves.

This shift has profound station-wide consequences. Previously, atmos could subsidize the entire station through infinite gas production - overrunning TEGs for endless energy with zero downsides or selling exotic gases for easy spesos. That would end entirely. Atmos will no longer act as an infinite money printer or self-sustaining power source; instead, its success now follows Cargo's performance rather than leading it. A thriving Cargo department generates the funds needed to replenish AIR and purchase precursors for mixing, enabling atmos to scale into advanced gas production, crystallizer, HFR and SM experimentation, or high-output burns. A struggling or inactive Cargo leaves atmos constrained: stuck on basic air, limited experimental gases, and cautious power generation. This interdependence is intentional rather than an oversight - it prevents any single department from dominating the economy and encourages cross-station coordination, deals, and communication that were previously one directional.

Game progression will naturally feel markedly different as a result. Early rounds remain accessible with a generous startup allocation, letting atmos establish basics and handle any early spacings without panic. Mid-game introduces real walls: extractor reserves deplete, forcing optimization and recycling to avoid constant ARC purchases. Late-game exotic gases and large-scale projects become rewards for a healthy station economy, not early exploits. Power generation via TEGs or other gas systems transitions from free infinite energy to a budgeted, late-round endeavor that requires careful fuel management and Cargo support to sustain.

Antagonist play and events gain new weight. Deliberate breaches, plasma floods, or prolonged fires are no longer just engineering annoyances - they represent direct economic attacks that can force command attention, emergency fund transfers, or budget requests. This makes atmos disasters high-stakes team events, demanding coordinated response rather than "eh, just max distro."

These changes create meaningful new trade-offs and dependencies that will take time and live testing to fully balance. New players may find budget tracking and reserve management intimidating at first. Low-pop rounds could stall gas mixing projects and even refilling of spaced areas if Cargo underperforms. Overly punitive waste penalties risk frustrating experimentation or punishing honest errors. Balancing the exact pricing, starting buffer size, and emergency mechanisms will take careful observation in live games - some rounds may feel tighter than intended, others too lenient. Yet these are solvable issues, and addressing them thoughtfully will yield a version of atmospherics that actually carries genuine mechanical and narrative weight. Rounds will play out differently: more interdependent, more consequential, with air no longer an afterthought but a scarce, valuable resource whose management can shape the station's fate.

## Feedback Requested

This is a proposal to overhaul the gas economy with the **Atmospheric Reserves Computer (ARC)**, **AIR budget**, priced gases, and finite extractors - making gases a real, budgeted resource rather than infinite/free.

Particularly looking for feedback on:
- Does this give atmospherics (as handled by Engineers or whoever plays the systems) a stronger, more focused identity with real stakes and consequences, separate from just being "Engineering's side gig"?
- Do the boundaries, budget isolation, and Cargo interdependence create healthy cooperation and productive tension between departments (especially Engineering, Cargo, and Command) without excessive frustration or gridlock?
- How aggressive should basic gas pricing be (e.g., nitrogen/CO₂/water vapor very cheap for survival basics, oxygen moderate, plasma significantly expensive to gate advanced play)?

All input appreciated - especially from players who run Atmos/Engineering/Cargo regularly.
