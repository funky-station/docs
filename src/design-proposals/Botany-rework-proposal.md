# Botany: Mutation and Progression Rework


| Designers | Implemented | GitHub Links |
|---|---|---|
| Seva | :x: No | TBD |

## Overview

Botany in SS14 has always been one of the more mechanically deep and expressive departments but its current design heavily favors speed and automation over experimentation and creativity.  

This proposal reworks core progression systems in Botany to focus on instability management and  organic stat growth, aligning the department more closely with Funky Station’s longer rounds and roleplay-driven pacing.  
  

The goal isn’t to make Botany slower in an unfun/punishing way, but to make progression feel more engaging and reactive. Where experimentation, observation, and risk-taking naturally lead to stronger or stranger plants over time.    

---

## The Current System

Right now, Botany progression revolves around mutation through applying Mutagen and Left 4 Zed.  

This creates a feedback loop where:

1. The botanist floods a plant with left 4 zed/mutagen until it gains every possible trait.  
2. Mutated problems are dealt with.  
3. The result is a close to perfect plant usually within minutes of the round starting.  

Once this stage is reached, the department effectively stops evolving, the start, mid, and endgame of botany is the same throughout.  

---

## Problems with the Current Model

While functional, this system has several design issues, both mechanically and narratively:

- Instant Power Curve: even limited by the amount of roundstart chemicals avaliable to a botanist, they can max out a plant’s stats in minutes.  
- No Progression: what botany can do at shift start is roughly if not exactly the same as what they can do late game, with the minor exception of exotic seeds. 
- Low Interaction: Aside from an inital interaction with chemistry, there is little to no consistent reason to interact with the rest of the station.  
- Limited Roleplay Value: Current mutation deisgn doesn't help create a story, it just produces numbers.  
- Fast, Flat Rounds: Funky’s rounds last on average 2 hours, but Botany runs out of meaningful gameplay after about 30 - 45 minutes.  

In short, the current design prioritizes efficiency over expression.  
It encourages spamming chemicals instead of planned experimentation.

---

## The Plan

The rework aims to solve these problems without discarding the core fun of Botany.  

The redesigned system introduces:
 
- Stat Growth: Core stats(mainly yield and potency) improve naturally through replanting stronger produce.  
- Instability and Risk–Reward: Instability affects how strongly a plant reacts to mutagen, letting players choose between safer stable mutations and more experimental mutations.  
- Subspecies Mutation: When a plant undergoes enough mutation, its produce has a chance to yield a subspecies produce. 
- Dna Manipulator: A machine which would replace swabbing, allowing for more controlled trait transfer.
- Multiple new plants and traits 

## Core Features

## Natrural stat Growth

### Concept

Plants now develop their stats(mainly yield and potency) naturally across generations.  
Instead of the mutation based stat increasing, botanists progress by replanting the best produce from each harvest.  

Instead of plants having a hard stat (for example potentcy), Each plant will have a base stat, and every produce it produces varies slightly around that numbers.  
When a botanist replants with higher stats, those values become the new baseline for the next generation leading to gradual improvement.  

### Example

A botanist grows a batch of wheat with a minimum potency of 1.  
The harvested produce ranges between 1 - 15 potency.  
They seed and plant the 15 potency wheat, raising the next generation’s baseline potentcy to 15.  
Each generation will have a higher and higher potenty, strengthening the line.  

### Why This Matters

This system replaces the mutation reliant stat increases with natural progression.  
It rewards attentive play and observation without making Botany overly complex.  


## Instability System

### Concept

Instability represents how volatile a plant reacts to exposure of mutagenic substances.  
It (propably)does not cause mutations on its own but instead determines how potent and unpredictable mutation results will be.  

Low instability makes mutations mild and predictable, while high instability amplifies both the chance and extremity of new traits.  
Instability rises through exposure to substances such as left 4 zed and can be reduced naturally over time or with stabilizing chemicals.  

| Instability Level | General Behavior |
|--------------------|------------------|
| Low | Predictable, mild mutation results. |
| Moderate | Noticeable mutation variety; traits appear more frequently. |
| High | Unstable mutation reactions; conflicting or rare traits appear. |
| Extreme | Chaotic results; volatile or hazardous traits may occur. |

### Gameplay Interaction

Instability defines the risk–reward curve for mutation:  

- Low instability → safe, predictable mutations.  
- High instability → stronger, rarer, but riskier mutations.  

This allows players to choose how much risk they want in their experiments — a natural balance between control and chaos.  


### Design Intent

The current mutation system is almost completely random, every mutation roll pulls from the full mutation table, (although each mutaiton is weighted)players have no control over what traits appear or how likely they are to occur.  

With the instability system, players can influence the direction of mutation by managing their plant’s instability level.  
While randomness still plays a part, instability effectively tips the scales of RNG in the player’s favor. 

---

## Subspecies Mutation

### Concept

When a plant undergoes enough mutation, its produce has a chance to create a subspecies produce instead of its normal produce.  


### Example

1. A botanist mutates an ambrosia plant.  
2. One of the yeild is an ambrosia deus.  
3. The botanist can now seed and plant this subspecies.  

### Design Intent

In the current system, hitting a subspecies mutation roll causes the entire plant to immediately transform into that subspecies. This makes acquiring rare species almost instantaneous.  

The proposed system slows this down and makes it more organic and thematic.  
Subspecies now emerge through the plants produce rather than instant full-plant transformation.  
This approach with the idea of gradual evolution and also helps with pacing and balance, ensuring powerful or exotic plants feel earned through continued mutation instead of instant success.

## Seed Splicer

### Concept

The Seed Splicer is a machine used to create advanced plant species that cannot be obtained through normal mutation, by combining two different seeds with a specific gene disk the machine produces a new specialized plant seed.

### Core Behaviour

To create a new seed, the botanist must: 
- Insert the two required seeds into the machine
- Insert the required gene disk
- Activate the machine
- After a processing period the machine produces the new seed

### Example

In this example the botanist wants to produce spacemans trumpet, after looking up the required parts in the guidebook, they would set out to gather them. In the case of spacemans trumpet these would be lily seeds, ambrosia seeds, and a gene disk containing the Ligneous mutation, after about a minute or so of processing the machine spits out an unmodified spacemans trumpet seed ready to plant. 

### Design Intent
In the current system, powerful plants can often be obtained quickly through repeated mutation rolls. While the suggested subspecies mutation system would slow this somewhat, rare plants could still appear early in a round. The Seed Splicer would add an adition step to aquiring the late game plants locking them behind plant and gene requirments.

This system isnt perfect, it relies on gene disks and mutation rng, while mutation rng is being changed in the instaiblity system it is still possible that a botanist gets lucky, making a lategame plant early into the round, However, this is acceptable, as occasional lucky outcomes helps create variety between rounds and keeps the game unpredictable. 


---

## Reagent extractor

### Concept

The reagent extractor is a  round start machine for Botany that rapidly converts harvested plants into their reagents. Botany often causes server lag due to entity spam from mass producing plants: high yield, auto harvesting setups combined with botanists waiting for an industrial grinder can lead to hundreds of plants piling up on the floor. This machine provides a way to process these plants efficently.

### Core Behavior

The reagent extractor will:

- Only accept produce from plants.

- Allow botanists to dump a plant bag’s contents directly into it.

- Process items over time at a similar rate to the standard grinder.


- Have an uncapped internal reagent capacity to prevent overflow or reagent spillage(we dont need more deparment wide puddles).

- Be unable separate reagents, so a ChemMaster is still required for sorting.


### Design Intent
The reagent extractor is designed to reduce lag by encouraging botanists to process their produce rather than letting it accumulate. While it may seem like just another QoL machine, its primarily designed to prevent entity bloat. Although it serves a similar function to the industrial grinder, its availability from round start helps enhance the roleplay experience by freeing up botanists’ time that would otherwise be spent manually processing plants either through the standard grinder or dragging onto a chem master(technically an exploit)(While Processing plants into chems should normally fall under the chemists role, most of the time the plants will sit on their counter for most of the round)

---
## DNA manipulator and Gene disks

### Concept

The DNA Manipulator and gene disks are concepts taken from 13's systems with some modifications.
Instead of relying on the opaque RNG-driven interactions of swabbing, the DNA Manipulator provides a clear and visible way for botanists to add, remove and edit traits on a plant.

All plant genetics are represented through a visible genome slot system: four trait slots (A, B, C, D) and one core-stat slot (X).
Gene Disks act as the medium for transferring traits between plants, storing genetic information extracted from seed packets


### Core Behavior


#### Genome Slot System

Every plant’s genome is divided into:

Trait Slots: A, B, C, D
– Used for mutations, chemical contents, special behaviours

Core Stat Slot: X
– Used for yield, potency, growth type, and other fundemental stats

Each slot contains a limited number of capacity points.
Mutated traits will take up slots on the plant’s genome, using at least one slot, with more powerful or complex traits occupying multiple slots across A, B, C, and D.
If adding a new gene to the plant causes a slot to exceed its capacity, it will be imposed with unviable, effectivly killing the plant.

X slot genes function differently to trait genes, the room X slot genes take up is dictated by the numerical value in which they hold, for example a yeild gene of 4 will only take up one space, while a high yeild of 10 will take up 2 - 3 slots on the X slot(the numbers are purely for example). These gene slot costs are only imposed when changing core stats through the dna manipulator, this is to leave natural growth as the main system for safley bettering the core stats of a plant.

This system exists as a middle ground between balance and RNG: traits are balanced by how many slots they consume, while the randomness of which specific slots they occupy introduces natural variance. This allows for occasional high-roll plants where efficient slot placement leaves room for additional traits. 

#### Gene disks

Gene disks are physical storage devices that hold extracted traits.
Botanists will start with a small number of empty disks roundstart, additional disks can be printed at science for a moderate cost, disks can be wiped at DNA manipulator.

Gene disks will be able to store most traits that the current swabbing system allows the transfer of, disks are reusable(Limiting the use of a stored trait would ultamtly just incentivise keeping copies of the seeds the traits were extracted from).

#### Extraction 

To extract a gene, the botanist will: 
- Insert a seed and empty gene disk into the Dna manipulator 
- select the gene(s) they want to extract(possible option to extract multiple genes onto one disk)
- hit the extract button, destroying the seed packet

#### Application

To apply a gene to a plant, the botanist will:
- Insert a seed packet and filled gene disk 
- hit the apply button, applying all genes on the disk to the seed

#### Genetic Scarring

Manipulating a plant’s genome through the DNA Manipulator can cause genetic scarring, representing damage to the plant’s genetic code caused by invasive modification.

Both adding and removing traits may introduce genetic scars. Each scar temporarily reduces the available genome capacity of the plant, limiting how many traits it can sustain at once. This prevents repeated genetic manipulation from allowing players to perfectly reconstruct plant genomes without consequence.

Genetic scarring is not permanent. As the plant line continues through successive generations, the genome gradually stabilizes and these scars begin to repair themselves. By replanting seeds and continuing the growth cycle, botanists can slowly restore the lost genome capacity.

This system ensures that while the DNA Manipulator allows powerful control over plant genetics, repeated editing carries a short-term cost that encourages players to stabilize their plant lines through continued cultivation and breeding. 



### Design intent

This system is designed to make trait transfer easy to understand for new players, removing the opaque expert level understanding that swabbing relied on. The intent is to also preserve botany's depth and skill curve through genome managment and optimisation. Newer botanists can participate immediately, while experienced players will have a curse to climb.  

### Considerations
This system will clash with the proposed systems present in the proposed botany changes by recon, taking up the role of the plant sequencer. 

---

## New Plants and Mutations

With the introduction of systems like the Seed Splicer and Instability, new plants and mutations will need to be added to take full advantage of these mechanics, for example only a handful of plants qualify for being locked behind the seed splicer. In a similar fashion there is currently a small pool of mutations, splitting them across the instability system would make each tier feel sparse. 

These lists will also serve as examples of how plants and mutations will be designed as development continues. 
The majority of plants added throught this rework will mostly be subspecies of existing plants, this is to utilise the seed splicer's role. 

### New Plants

#### Weeping Onion
A subspecies of onion, it contians tear gas and nutriment. 

Obtained through mutation. 

#### Coconut(Port from IMPstation)
Simply coconuts, can be thrown at people dealing minor stamina damage.

A base plant availible in the seed vend

#### Coco-not
Coco-not is a mutation of the coconut plant that plays on the expectation of what a coconut normally contains.

Despite appearing nearly identical to a normal coconut, Coco-nots do not contain coconut flesh. Instead, when opened they produce a random fruit or vegetable from a limited pool.

This plant would be acquired through mutation

#### Corpse Lily 
A flower which produces misamsa while the plant is alive. when harvested it produces corpse lily flowers, these flowers contain gastro toxin, and a small amount of nutriment.

These would be a base plant, likely locked behind a cargo purchase like exotic seeds. 

#### Corpse Bloom
A subspecies of the Corpse lily, this plant doesnt produce normal fruit, instead it will produce the rotting corpse of a random species.

This plant would be acquired via the seed splicer, the required parts:
- Corpse lily
- Blood Tomato
- gene disk: Hypertrophic Growth

#### High cap Potato 
A subspeices of the potato plant, normal potatoes can be made into a very small capacity power cell. The High cap potato itself is the powercell. Its powercapacity would be less of an actual high cap but more than a medium cap. 

This plant would be acquired from the seed splicer, the required parts:
- Potato
- Lemon
- Gene disk: Electrogenic Tissue

#### Blue Space Tomatoes

A highly unstable subspecies of the tomato plant that has developed strange bluespace properties. The tomatoes appear slightly distorted and may occasionally flicker in and out of focus, as if partially out of phase with reality.

When thrown, a Bluespace Tomato will teleport the target a short distance in a random direction instead of simply impacting them. They can also be eaten for teh same effect but on yourself. 

This plant would be aquired via the seed splicer, the required parts:
- Extradimensional Oranges
- Blue tomatoes
- Gene disk: Spatially Unstable

#### Carbean
A subspecies of the syndicate grown gatfruit. The Carbean plant produces vaugly rifle shaped bean pods capable of firing rifle-caliber beans.

The Carbean would be acquired throught the seed splicer, the required parts:
- gat fruit
- pea vine
- Gene disk: Ligneous

#### Fly Danceanita
A subspecies of fly amanita that appears to move rhythmically on its own, contains nutriment and happiness(the chem), when destroyed it emits a cloud containing happiness.

This plant would be acquired through mutating fly amanita.

### New Mutations
when designing new traits under this new system they should eb sorted into an instability tier, the genreal rule of thumb is
T1 - Minor Traits, usually small stat changes, resistances etc.
T2 - Medium Traits, Noticable changes to the plant, usually affecting behaviour of the plant.
T3 - Major Traits, powerful mutations that affect the plant and produce, these traits may proide strong benefits or introduce hazards.
T4 - Experimental mutations, the traits in this tier introduce unusual or unconventional behaviour that can drastically change how the plant or its produce function.

#### Pressure Immunity T1
The plant is able to grow without an atmosphere

#### Light Indifference
The plant grows normally at any light level.

#### Sap secretion T2
The produce are covered in sap, causing them to stick to peoples hands

#### Hypertrophic Growth T2
The plant consumes double the nutrients but the produce has increased Potentcy

#### Electrogenic Tissue T3
Plants with this trait will shock the person that harvest it

#### Rapid Bloom T3
The plant prioritizes rapid fruit production at the expense of a capped potency.

#### Spatially Unstable T4
When the plant is Harvested the produce will teleport a medium distance away

#### Bestial Germination T4
Upon harvesting, the plant would instead take the form of an animal, leaving the tray and roaming around, it will occasional create a produce of the orignal plant



