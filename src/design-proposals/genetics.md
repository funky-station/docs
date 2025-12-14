## Overview

Genetics is a new medical science wing that lets researchers scan, sequence, and modify DNA to unlock mutations ranging from harmless accents and traits to powerful abilities. Every round, all mutations receive unique 32-base DNA sequences that must be discovered through experimentation on test subjects. Correctly sequencing a block activates the mutation, but excessive non-natural mutations cause genetic instability leading to harmful effects; rare mutations generate research points. While most mutations will be discovered through research on monkeys, some only naturally manifest in certain species or mob types, leading to experimentation with a wider assortment of station life. 

## Background

Science currently lacks depth in research variance, with minimal interaction involving live subjects or DNA manipulation. This proposal draws inspiration from SS13's genetics system but adapts it for SS14's codebase, emphasizing discovery, risk-reward experimentation, and integration with the proposed science overhaul's point types (e.g., biology points). Genetics will function as a wing of science, using monkeys, crew volunteers, or acquired specimens (e.g., from salvage, cargo, or scavenged pets) as test subjects.

## Features to be added

Genetics revolves around four key pieces of equipment: the DNA Scanner, DNA Scanner Console, DNA Injectors, and Handheld Genetic Analyzer. Mutations are prototype-based, and include many unofficial categories such as speech accents, quirks/disabilities, beneficial, harmful, and instability punishments.

### Core Mechanics
- **Round-Unique DNA Sequences**: At round start, each mutation prototype is assigned a unique block and 32-base sequence (A-T/G-C pairs). Sequences never repeat.
- **Genetic Instability**: Non-natural mutations add instability. Over 100: random severe negative mutation every 60–90s. Over 150: constant cellular damage. Instability is balanced to discourage spamming powerful mutations.
- **Mutation Discovery**: Sequencing a block reveals and activates the mutation station-wide. Common mutations generate minimal/no research points; rare mutations (unlocked via precursors) generate significant biology points, pacing higher rewards mid-to-late round.
- **Mutation Removal**: Mutadone removes most mutations. Select mutations can be flagged resistant to mutadone, sequencer, or "Scramble DNA" (30s cooldown, 25 cellular damage, resets non-resistant mutations).
- **Departure from SS13**: Monkeys cannot revert to humans (permanent visual punishment for instability; avoids conflicts with changeling/cargo systems involving corpses being a rare commodity).

### Equipment
- **DNA Scanner**: Pod for one occupant. Links to console via device network for scanning.
- **DNA Scanner Console**: UI shows vitals, mutation list, sequencer grid (click bases to guess; each click: 0.2 cellular damage), saved mutations, injector printing. Starts with 60 empty injectors (refillable via lathe). Filled injectors transfer mutations between consoles. Hidden mutations unlock via precursors (e.g., thermal resistance after heat/cold).
- **DNA Injector – Activator (blue)**: Single-use; activates existing mutation.
- **DNA Injector – Mutator (red)**: Single-use; adds/activates new block (increases instability if non-base).
- **Handheld Genetic Analyzer**: Portable; displays all blocks/revealed sequences, prints paper reports. Uses small power cell.

### Example Mutations (21 Implemented, Expandable)
- **Speech/Accents** (0 instability): Cowboy, Pirate, Russian, Stuttering, etc.
- **Quirks/Disabilities**: Pacifism, Narcolepsy, Blindness, Mute, etc.
- **Beneficial**: Alcohol Immunity, Supermatter Hallucination Immunity, Anaerobic Metabolism, etc.
- **Punishments**: Monkey Transformation (human-only, permanent, non-printable, sequencer, mutadone and scramble resistant).

Mutations apply/remove components dynamically. Balance focuses on removable effects (except instability punishments) with visible but non-permanent drawbacks.

## Game Design Rationale

- **Seriously Silly**: Experimenting on monkeys/kobolds/crew with mystery DNA sequences encourage absurd and serious roleplay, from forcing accents on unwilling subjects, chasing rare mutations in unique species or mob types, or dealing with upset monkeys who have gained sentience.
- **There is no Winning or Losing**: Instability risks balance powergaming mutations, and mutadone/scramble provide easy recovery before permanent consequences are suffered. Most mutations will be researched solely for the sake of contributing to scientific research points, not simply to hand out to crew. 
- **Maintaining Authenticity**: NanoTrasen experimenting on DNA fits corporate evil. The simplified sequencing mimic genetic base pairs. Genetic instability mutations such as those that polymorph players into another creature follow the Carpenter/Cronenbergesque aesthetic of Space Station.
- **Dynamic Environment**: Rare mutations require diverse subjects/stimuli, pulling in medical/cargo/salv.
- **Take Things Slow**: Paced by sequencing damage, instability, and precursor unlocks; extends science gameplay without rushing.
- **Maximizing Roleplay Potential**: Injectors enable trading mutations, and sequences can be discovered by analyzing crew and printing out their genetic sequences. Both of these should foster inter-department roleplay and cooperation.

## Roundflow & Player Interaction

- **Early Round**: Scan monkeys/crew with handheld for base sequences; discover low-point common mutations.
- **Mid Round**: Radiation/crew incidents provide new subjects; precursors unlock rarer mutations for research points.
- **Late Round**: High-point rare mutations discovered; injectors potentially distributed to crew for buffs/drama.
- **Every Round**: Core loop active throughout, slowing early science (plentiful undiscovered commons) and ramping late.
- **Desired Interactions**: Voluntary crew testing, injector trading, cross-dept subjects.

## Administrative & Server Rule Impact (if applicable)

- Minimal new workload: Fits existing griefing rules (no forced perma-harm without consent). Instability self-regulates abuse.
- Low grief risk: Removable mutations prevent round-removal; instability mutations require many deliberate choices and failure to recieve mutadone for at least a full minute of warnings. 
- Mechanical enforcement: Instability, resistant flags, and scramble cooldown prevent exploits.

# Technical Considerations

- **Performance Impacts**: Should be negligible; prototype-based mutations use lightweight components. Sequencing grid is client-side UI.
- **New Systems/UI/Refactors**:
  - New genetics component (per-entity DNA blocks/instability).
  - DNA Scanner/Console entities with device linking.
  - Console UI: Tabs for vitals, sequencer grid (clickable 32-slot base pair matcher), mutation list/storage, injector printer.
  - Handheld UI: Simple list view with print button.
  - Injector entities.
  - Round-start prototype shuffling for sequences.
- No major refactors; integrates with science lathes/research points. 
