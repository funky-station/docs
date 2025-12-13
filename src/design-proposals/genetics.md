# Genetics and Mutations systems

## Overview

Genetics is a new medical/science feature that lets crew scan, sequence, and modify DNA to unlock mutations ranging from typical accents and traits to powerful and dangerous abilities.  
Every round, all mutations receive completely unique 32-base DNA sequences that players must discover through experimentation. Correctly sequencing a block activates the mutation; adding too many non-natural mutations causes genetic instability that can spiral into random harmful mutations that cannot be undone or even persistant cellular damage.

The system is built around four pieces of equipment. The DNA scanner and it's console, DNA injectors, and the handheld genetic analyzer.

## Core Gameplay Loop

1. Put a living test subject in the DNA scanner.
2. Use the DNA scanner console to view their partially hidden DNA blocks.
3. Click bases in the sequencer grid to guess the correct sequence (each click deals 0.2 cellular damage).
4. When a block is fully correct, the mutation activates automatically.
5. Save discovered mutations to the console's storage and print single-use injectors (activator to turn on an existing mutation, mutator to add a new one).
6. Too much instability = bad things happen.

## Key Mechanics

### Round-Unique DNA Sequences
- At round start every mutation prototype is randomly assigned a block (currently between 1–150) and a unique 32-base sequence (valid A-T / G-C pairs).
- Sequences never repeat.

### Genetics and Mutation Systems
- Inactive random mutations are genereated at round start. These are your base sequences.
- Added sequences contribute to genetic instability.
- Radiation or unstable mutagen exposure can also trigger random mutations.

### DNA Scanner and Console
- A test subject with the genetics component can be scanned to view which mutations are present. 
- The console contains a sequencer that allows you to attempt to solve a mutations sequence by matching base pairs. 
- When the sequence is successfully solved and discovered by a console for the first time, it is added to the station's discovered mutations
- Important sequences can be saved to individual consoles to be accessed later independant of a test subject.

### Genetic Instability
- Non-natural mutations add/subtract instability.
- Over 100 instability and you will have between 60 and 90 seconds until a random severe negative mutation occurs.
- Over 150 instability and you will recieve constant cellular damage. 

### Mutation Removal & Resistance
- Mutadone removes almost everything.
- Specific mutations can be flagged mutadone-resistant, sequencer-resistant, or scramble-resistant.
- “Scramble DNA” (30 s cooldown, 25 cellular damage) resets the entire genetics component except resistant mutations.

### Discovery Persistence
- Once a mutation is fully sequenced on a grid, its name is permanently revealed to every console and handheld analyzer on that grid. This could potentially be used to have the discovery of certain or rare mutations contribute to the station's research points. 

## Equipment

**DNA Scanner**  
A pod that holds one occupant. Occupants are inserted by dragging and dropping (2-second entry delay). The scanner links to a console via the device network.

**DNA Scanner Console**  
Full UI showing subject vitals, mutation list with partially hidden sequences, sequencer buttons, saved mutation storage, and printing controls. Starts with 60 empty injectors in stock which can be made into activators and mutators.

Empty injectors are lathe-printable trash items. They can be inserted into the console to refill it's stock. Filled injectors inserted into a console will save the mutation to that console. This can be used to transfer mutations between consoles.

Some mutations will remain hidden and unable to randomly appear in the round until unlocked by the console. For example, the thermal resistance mutation will unlock once you have discovered and saved the cold and heat resistance mutations. 

**DNA Injector – Activator (blue)**  
Single-use syringe that activates an already existing mutation in the target.

**DNA Injector – Mutator (red)**  
Single-use syringe that adds a new block and immediately activates it, increasing instability if it is not part of the target’s base genome.

**Handheld Genetic Analyzer**  
Portable scanner that instantly displays all blocks and current revealed sequences. Can print a formatted paper report with block numbers and sequences. Requires a small power cell.

## Important Departure from SS13-Style Genetics

Unlike SS13, monkeys **cannot** be turned back into humans. Instead, they will simply have fewer sequences to examine. This is for a few reasons:

- There is currently no safe, generic “spawn human” system in SS14.
- Reversing monkey transformations would interfere with changeling mechanics, cargo organ bounties, and other systems that treat human corpses as a limited resource.
- The monkey mutation is currently intended as a permanent, visual punishment for extreme instability rather than a reversible state.

## Example Mutations (21 currently implemented)

**Speech / Accents** (0 instability)  
Cowboy, Pirate, Russian, Southern, Stuttering, Frontal Lisp, etc.

**Quirks & Disabilities**  
Pacifism, Narcolepsy, Total Blindness, Mute, Chronic Snoring, etc.

**Beneficial**  
Alcohol Immunity, Supermatter Hallucination Immunity, Anaerobic Metabolism, etc.

**Instability Punishments**  
Permanent Monkey Transformation (hidden, mutadone/sequencer/scramble-resistant, non-printable, human-only).

All mutations are prototype-based and easy to add or tweak. Instability mutations will be added to cause more, generally visibily noticible consequences to overdoing it on mutations. 

## Round Flow Impact
- **Early round** - Geneticist begins work on available monkeys, scanning crew members with their handheld scanner to find missing parts of sequences.
- **Mid round** - Radiation exposures lead to random mutations in crew, giving the geneticist a chance to examine undiscovered mutations. Advanced and hidden mutations begin to unlock from discovering and saving their precursors. 
- **Late round** - Many beneficial and unique mutations are found and applied to crew. If rare mutations generate research points, geneticists may start trying to discover instability mutations just to contribute, to the detriment of many poor monkeys and kobolds. Species specific instability mutations will make some impossible to discover without living test subjects of that species, willing or otherwise.


## Balance & Safety

- 2 second injection time and break on damage/movement to prevent quick injections.
- Instability risks discourage spamming powerful mutations.
- Nearly all mutations, apart from instability mutations, are easily removable, preventing the player from feeling round-long loss of control over their character.

Mutations will be easy for anyone to add or remove but should remain balanced in design. Their instability and drawbacks should be carefully considered to self-regulate abuse. Negative mutations should not have severe or visual consequences to the player that last all round unless those mutations are preventable, such as via instability. Almost all mutations should be easily removable with no lasting effects. 

## Technical Notes

- Mutations simply apply the components provided in the prototype and remove them on mutation removal.
