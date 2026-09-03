# Blacksmithing

| Designers   | Implemented | GitHub Links |
|-------------|---|---|
| ALooseGoose |  :x: No | TBD |

## Overview

This PR proposes a new role and mechanics for Cargo to expand their role in material production, the Blacksmith.
This also hopes to add a method of gaining currently unreproducable items station side, without the means to go through purchasing, and instead crafting directly on the station.

## Background

Right now the current way that materials are made is through Salvage with them fultoning back huge boxes full of materials all at once.
This process seems questionable at best. There's no way a group that are stranded at space are able to just print out sheets of metal and glass. Surely there should be a more difficult process behind this.
This isn't inheretly bad, Salvage have their own problems that are outside the scope of this PR regardless. This simply tries to open up more authentic ways of production and overhaul the method of which materials are produced.
It achieves this through the main way of adding more of a process to making materials. This makes it feel more involved and intentional rather than just a mindless process.

On top of this, there is currently no way to obtain items, such as hardsuits and guns, without purchasing them.
For equipment such as lasers, this isn't the case and feels incredibly hypocritical as a mechanic. Of course, certain items like Syndicate Contraband makes sense, but you'd imagine Nanotrasen would have a method of creating Nanotrasen equipment.
This proposes a solution to this by adding a dedicated role akin to science that creates these items.

## Features to be added

The Blacksmith would have to be implemented. This would require the respective workstations mapped onto the stations Cargo Departments.
The Blacksmith is a Cargo role with Cargo access, and Blacksmith access. Unlike Cargo Technician, they do not have Logistics access to incentivize them to stay to their role
They would not have Salvage access either, as it is not needed for their job.
Only 1 to 2 slots for Blacksmiths should ever be on station at a time, similar to the balancing of Paramedics and Roboticists.
Below I list the different machiens that Blacksmiths would use/go into detail on the changes to existing machines/items that would be made.

### Ore Processor Overhaul
The Ore Processor remains in the game as a functional item, alongside it's industrial variant.
Instead of producing completely processed materials, they only produce Refined materials. They would be useless from this point onwards to Salvage, and would need to be sent back.
Coal would not have any Refined variants, and Diamonds would be refined instantly into their processed form like they already do.
The Industrial Ore Processor would be converted to operating on Wood instead of Coal, as Coal will have a much more important use as described below.

### Blast Furnace and Arc Furnace
The Blast Furnace is the first item that the Blacksmith needs. This works similarly to a lathe. Uniquely, it wouldn't be powered from electricity, but from Coal instead.
Coal would be inserted like a Generator, and it would allow the Blast Furnace to operate.
You can insert Refined Ores into this to print out Molten Ore at a 1:1 Ratio.
This would have an Arc Furnace variant which would be unlocked with the Hyper Convection research, and wouldn't need Coal to operate, but needs to be powered. On top of this, it produces heat and makes the air around it hot.

### Molten Ore
Molten Ore is simply produced from the Blast Furnace as show above. There is a key detail to it though.
Molten Ores cannot be handled by regular people. If you hold Molten Ore in your hands, your character will scream and drop it immediately.
Thrown Molten Ore will deal considerable Burn Damage to whoever it hits as well.
Finally, storing Molten Ore in a bag or coat that isn't specially designed to do so will cause it to melt the item and eventually cause it to break, dropping all items in it to the ground and ashing it, not before setting the wearer on fire.
There would be Flame Proof Ore Bags to store Molten Ore safely (which would work functionally identical to plant bags) and Flame Proof Gloves to hold these. Combat/Blood-Red Combat Gloves would also be able to hold them, as due to their descriptions.

### Auto-Hammer and Industrial Auto-Hammer
Molten Ore would need to be inserted into the Auto-Hammer to cool down. Inserting a stack of Molten Ore will cause it to begin working.
This has a lot of speed variants. 1x Speed is the default. It works at normal speeds and is rather slow but there is no risk behind it. 2x speed works double as fast, but has a small chance each hit for the Auto-Hammer to break. 4x Speed is the maximum and works much faster, but has a much higher chance for the Auto-Hammer to break.
If the Auto-Hammer breaks at any point, then the Ores are launched around the room, 1 for every Ore in the Stack, hitting and burning anyone caught in its path, and the Auto-Hammer needs to be repaired. This will require the maintenance panel to be open, the Auto-Hammer to be unanchored, and then Welded.
The Industrial Auto-Hammer has more faster speeds but is more risky. It has an option for 8x and 12x Speeds as well, but if the Industrial Auto-Hammer breaks, it will blow up, the severity of the explosion being proportional to the speed it was on, adding a risk vs. reward gamble.

### CastFab and the Assembler
The CastFab would be a unique Fabricator that produces casts. The majority of these at Shift-Start would be medieval esque gear, such as swords, daggers, shields and chainmail armor.
Through the shift, as research is done, more Casts for various items would be added to it. Pistols, Hardsuits, and stronger items, would be added to it through research.
All these Casts would have 3 parts to it. Guns would have a cast for the Reciever, Handguard, and Stock. Hardsuits would have a cast for the Lower half, Upper half, and helmet. Etc.
3 of these items can be inserted into the Assembler, and the player would then need to play a minigame to fabricate it. It would be similar to skill checks, such as Dead by Daylight. The more of them the player succeeds, the higher chance of success.
Before this you would need to insert the correct Molten Ores into the Assembler to allow it to work. Otherwise, you would not be able to craft the item. This would just simply be item storage and nothing special. Similar to the likes of a Material Silo.

## Game Design Rationale

### Seriously Silly
The addition of a Blacksmith allows for interesting character roles and gameplay.
On top of this, the new gear the Blacksmith would be able to produce would be both practical and silly.
Imagine being arrested by a Security officer that charged at you dressed fully as a knight?
While it has practical use, it can still be very silly.

### There is no winning or losing
While the items would be practical, they wouldn't be incredibly overpowered, or at least very expensive to produce.
On top of this, for the character, this is just their 9 to 5.
This also opens up interesting methods for Antags to use the gear that they can produce though this to their advantage.
Of course, for specific gear like guns, the casts can always be locked behind the SecFab if necessary, or the other specific departmental lathes.

### Maintaining Authenticity
Materials do not get produced as easily as the game makes it out to be.
Sure, this is a Sci-Fi setting. But you'd imagine there's still more of an involved process other than mining to produce, say, a stack of steel.
While this doesn't completely overcomplicate the process and make it incredibly realistic, it does try to keep the feeling of authenticity and adding a more involved process.

### Take things slow
For a 1-hour round, the Ore Processors work just fine. But for 2 hours, that opens more doors.
Of course, already you can consider this slow as it is contingent on Salvage sending materials, however the process of producing them is not.
This makes the process slower and instead of making it so that everything is sent in bulk and in bursts, the station has a steady stream of materials being produced that would carry them over to the next Salvage shipment.

### Maximizing Roleplay Potential (Avoid QoL Slop)
This is, quite literally, the exact opposite definition of QoL slop. It makes the process much more difficult and involved.
With a new role on station dedicated to making these materials as well, and with them being able to produce more equipment previously completely unproduceable items as well as unqiuely added items, it would make interactions with this role very interesting.

### Dynamic Environment
From someone making their own division of Knights to being Security's best friend, this role would allow for lots of different things to happen.
With good downtime where there are no materials to process as well, it can allow for lots of interactions for the player while taking a break.

## Roundflow & Player interaction

While not too impactful at shift-start, as salvage send materials, they would have a lot to do.
To make their gameplay more interesting, the machines would not be set up from the start of the shift.
They would have all the materials in their workshop to make all the needed machines, but they wouldn't come premapped. They would need to build them up from the ground.
As Salvage send more items through, the core parts of their role begins to show. They then get constant work through being able to forge materials and items for the station.
They would also have bounties that they would be responsible for creating, such as bounties for Swords or Shields.
They would slow down the production of materials heavily, incentivizing budgeting in Science or the sacrifice out of Cargo's pockets to purchase materials directly.
Players can interact with Blacksmiths to ask for items, or the Blacksmith can offer to produce items for others. On top of this, items produced by the Blacksmith, depending on how well they pass the skill checks, can be sold for a generally good price. 

## Administrative & Server Rule Impact (if applicable)

Powergaming in this role could be possible through creating Armor and Swords, so there may be issues there.
Otherwise, there is little to no applicable administrative impact. Such issues are already applicable nigh everywhere else if you try hard enough.

# Technical Considerations

Lots of systems are already implemented for this, but would require general changes to ensure they work as intended.
The Molten system would need to be added to ensure that the Molten Ore interactions work as intended.
The Auto-Hammer and Assemblers would need to be built from the ground up as no systems would carry over from existing items.