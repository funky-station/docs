# Short, Properly Capitalized Title

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds".

## Background

RPDs and RCDs have long cheapend the construction experiance for engineering. The Flatpack simularly has long existed in a place that has almost entierly removed the need for actual machine construction in science.

This PR is the first in a multi-step process to give engineering an advantage in constructions with tools, while also replacing the need for RPDs and RCDs and flatpack machine.

## Features to be added

### RCD/RPD, flatpacks.

The RCD and RPD will be removed as its existing use cases are replaced with the new tools and "use" systems.

The flatpacker will be removed from research, and its board made un-craftable. 
It will still exist as something to be spawned for testing/admin use, but not for in-round use.
This part of the construction rework will not be including the removal of flatpacks that are shift-start or ordered via cargo.

### Item "use"

Item useage within the radial menus in this PR will alow for quick placement of blueprints for construction.
It will not place the item itself as RPD/RCDs currently do.

#### Machine Boards

Machine and computer boards will be given a "use" that alows you to place a machine or computer frame blueprint depending on type used.

#### Pipes

Pipes as a recource, printed at a standard lathe they cost .5 of a metal sheets for each pipe and stack up to 30. Size will be 1x2.
You can "use" the pipe stack in your hand to set the kind of pipe your going to lay, curved, split, straight, ect.
Pipe construction will include a wrenching to finalise the pipe's positioning.
These will fit within the materials bag.
Welding will fix broken pipes, but will not return pipes to steel sheets. This will be done in the recycler with a 45% return rate.

#### Engineering Circuits

All "engineering circuits" will be changed to a 1x1 size and include: Power Circuits (APC, SMES, Substation), Doors (Various doors),Timers (Brig timers, Regular timers, Clocks), Atmospheric (Air alarms, Vents, Pumps, Filters, ect).
You can "use" the circuit in your hand in order to select the type of device you wish to place quickly, such as using a door circuit and being able to select a windoor, airlock, or 

#### Walls

The "use" of steel will bring up a radial menu for placing a veriety of "standard" wall types along with lights.

#### Windows

The "use" of glass will bring up their veriety of windows (reinforced, plasma, uranium, ect) with directional, angled, and full options.

#### Grills

The "use" of rods will bring up the diffrent forms of grills to be placed. (Rods will also be added to the materials bag whitelist)

### Tools

The lathe in engineering will be exchanged for an "engineering lathe".
It will have the standard recipies of the basic lathe.
It will also have the ability to make engineering tools.

#### Circuit pouch/Machine pouch/Tool belt

The circuit pouch will be a 1x2 pouch with storage inside of 2x3.
This storage will be whitelisted to "engineering circuits" which are circuits that engineering commonly uses.
It will spawn in engineering lockers, the engie clothing vend, and be craftable in the textile lathe.

The machine pouch will be a 1x2 pouch with storage inside of 2x4.
It will hold machines parts such as manipulators, matter bins, capaciters and machine circuits. (Note, this PR does not decrease Machine Circuit sizes).
It will spawn in the roboticist locker, the roboticist vend, and be craftable in the textile lathe.

The toolbelt will be moved into the textile lathe and price changed to cloth.

#### Hull Axe and Crowbar

The hullaxe will be added as an upgraded form of crowbar for engineers.
It will take up the same 1x2 space as a crowbar, deal slight structural damadge, and will be able to remove hull to reveal space simular to the fire axe.
It will have the same time to pry as the current crowbar.
It will spawn in "filled engineering" toolbelts and the engie vend.

The jaws of life will also be given "hull prying" functionality.

The crowbar will be given a longer do-after as a "lesser tool".

#### Power drills, Screwdrivers, wrenches

The "power drill" will be given the current time to work as the Screwdriver and Wrench.
It will be given a 2x2 size.
It will be given an exchangeable battery for preforming jobs.
It will spawn in "filled engineering" toolbelts and the engie vend.

The existing power drill research will be changed to a "compact power drill" with a 1x2 size.

The screwdriver and wrench will be given a longer do-after as a "lesser tool".

#### Wire cutters and Scissors

Wire cutters will be given an innate LV insulation (the rubber grips arent just for looks).
They will still spawn in maints and toolboxes.
They will spawn in "filled engineering" toolbelts and the engie vend.

The jaws of life will also have HV insulation.

Scissors will replace the "common" wirecutters in tool vends, belts, and general maps.
They will be slower than regular wire cutters.

#### Welders

Industrial welders replace engineering's welders, and are made to be "standard" speed.

Advanced industrial welders are made to be faster, and carry more than Industrial Welders.

Welders will be given a longer do-after as a "lesser tool".

#### Insuls/Budget insuls/Arc Gloves

Budget insuls no longer exist in the tool vend. 
They can be crafted with a pair of gloves and plastic, providing LV resistance and turning the gloves white.

Insuls continue to exist as they have, but will provide MV resistance.
They will no longer spawn round-start in the tool room.

Arc-gloves slow down do-afters when worn but provide HV resistance.

## Game Design Rationale

RPDs and RCDs cheapen the construction experiance and currently exist due to disatisfaction with the construction menu.
By providing "quick use" option with the relevant materials this rework hopes to eradicate the need for them, without the final UI rework being needed.
The Circuit pouch, reduced engineering circuit size, and increased versitility in circuits will also satisfy the RCD's current place in combating the bulkyness of existing circuitry.
After implimentation this may eventualy be able to be reduced to just "circutry" as a recource for engineering and construction.
The hull axes also target this as they provide a way for engineers to remove hull tiles with the removal of RCDs without there only being the fire axe.

The flatpacker was built for servers with shorter rounds where science would never have time to make anything they researched.
We however have 2 hour rounds where science often finishes research and has little to do.
The removal of the flatpacker may not entierly solve this, but it is a start on it.
The addition of "use" to circuits will also alow them to skip over the construction menu that was a complaint in the flatpack removal feedback.
As per the feedback in the past about flatpack removal, this part of the construction rework will not be implimenting full flatpack removal across all parts of the roundstart and cargo experiance.

The pipe change's reason is fairly straight forward.
People *usualy* cant bend sheets of steel by hand to make make pipes that are air tight. 
Additionaly they cant bend those sheets by hand to make functioning circutry that will seperate diffrent kinds of gasses, pump it in a direction, or much else.
Lastly the change to pipes as a recourse alows it to effectively interact with the new "use" system without overloading steel, and makes them cheaper to craft and hold.

For the tools it enables engineering to have an advantage in construction and deconstruction, without directly taking away those abilitys from other roles.
They can simply use better tools that are afforded to them as they were hired to do those things.
When you want to rework the medical bay, the bar, or a shuttle you *can* do it without engineering, but its faster to have an engineer come over and lend a hand in the project.

## Roundflow & Player interaction

This PR will slow down the engineering experiance in some aspects, mainly where the RPD and RCD are concerned, such as in the construction of complicated atmos networks and wall repairs, but accelerate the "intended" form of doing it via the "use" radials.
It will also lead to a greater use of materials from engineering, encouraging interactions with cargo throughout the round.

This will make large scale engineering projects go much smoother when done in conjunction with engineering, encouraging their interaction, while still be possible for non-engineers to do themselves though less efficiently.

Additionaly science will be encouraged to do more machine construction throughout the round, slowing them down a little bit and providing them with more interactions with other departments.

## Administrative & Server Rule Impact (if applicable)

This should have no additional administration impact when compared to current systems.

# Technical Considerations

This will utilise existing systems and code such as the radial menu, however it will require interaction between that system and the construction blueprint system.

Some construction objects will have to be tweaked to provide an extra step, such as with pipe devices, or to change the required circuit.
