# Construction Rework Part 1

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

This part is intended to initiate the rework of construction and the removal of RCDs, PRDs, and flatpacks. This part is planned in such a way that it can avoid the requirement of the UI rework through "use" radial systems.

## Background

RPDs and RCDs have long cheapened the construction experiance for engineering. The Flatpack similarly has long existed in a place that has almost entirely removed the need for actual machine construction in science.

This PR is the first in a multi-step process to give engineering an advantage in constructions with tools, while also replacing the need for RPDs, RCDs and flatpack machine.

## Features to be added

### RCD/RPD, flatpacks

The RCD and RPD will be removed as its existing use cases are replaced with the new tools and "use" systems.

The flatpacker will be removed from research, and its board made un-craftable. 
It will still exist as something to be spawned for testing/admin use, but not for in-round use.
This part of the construction rework will not be including the removal of flatpacks that are shift-start or ordered via cargo.

### Item "use"

Item usage (with z or left click inside your hand) within the radial menus in this PR will alow for quick placement of blueprints for construction.
It will not place the item itself as RPD/RCDs currently do.

#### Machine Boards

Machine and computer boards will be given a "use" that alows you to place a machine or computer frame blueprint depending on type used.

#### Pipes

Pipes as a resource, printed at a standard lathe they cost .5 of a metal sheet for each pipe and stack up to 30. Size will be 1x2.
You can "use" the pipe stack in your hand to set the kind of pipe you're going to lay, curved, split, straight, ect.
Pipe construction will include a wrenching to connect it to the pipe network.
These will fit within the materials bag.
Welding will fix broken pipes, but will not return pipes to steel sheets. 
This will instead be done in the recycler with a 45% return rate.

Additionaly atmospheric devices such as filters, pumps, ect. will require an Atmospheric Circuit to construct.

#### Engineering Circuits

All "engineering circuits" will be changed to a 1x1 size and include: Power Circuits (APC, SMES, Substation), Doors (Various doors),Timers (Brig timers, Regular timers, Clocks), Atmospheric (Air alarms, Vents, Pumps, Filters, ect).
You can "use" the circuit in your hand in order to select the type of device you wish to place quickly, such as using a door circuit and being able to select a windoor, airlock, or glass airlock.

#### Walls

The "use" of steel will bring up a radial menu for placing a veriety of "standard" wall types along with lights.

#### Windows

The "use" of glass will bring up their variety of windows (reinforced, plasma, uranium, ect.) with directional, angled, and full options.

#### grilles

The "use" of rods will bring up the diffrent forms of grilles to be placed. (Rods will also be added to the materials bag whitelist)

### Tools

The lathe in engineering will be exchanged for an "engineering lathe".
It will have the standard recipes of the basic lathe.
It will also have the ability to make engineering tools.

#### Circuit pouch/Machine pouch/Tool belt

The circuit pouch will be a 1x2 pouch with storage inside of 2x3.
This storage will be whitelisted to "engineering circuits" which are circuits that engineering commonly uses (as listed in the Engineering Circuits section).
It will spawn in engineering lockers, the engie clothing vend, and be craftable in the uniform printer.

The machine pouch will be a 1x2 pouch with storage inside of 2x4.
It will hold machine parts such as manipulators, matter bins, capacitors and machine circuits. (Note, this PR does not decrease Machine Circuit sizes).
It will spawn in the roboticist locker, the roboticist vend, and be craftable in the uniform printer.

The toolbelt will be moved into the uniform printer and price changed to cloth.

#### Hull Axe and Crowbar

The hullaxe will be added as an upgraded form of crowbar for engineers.
It will take up the same 1x2 space as a crowbar, deal slight structural damadge, and will be able to remove hull to reveal space simular to the fire axe.
It will have the same time to pry as the current crowbar.
It will spawn in "filled engineering" toolbelts and the engie vend.

The jaws of life will also be given "hull prying" functionality.

The crowbar will be given a longer do-after as "lesser tools".

#### Power drills, Screwdrivers, wrenches

The "power drill" will be given the current time to work as the Screwdriver and Wrench.
It will be given a 2x2 size.
It will be given an exchangeable battery for performing jobs.
It will spawn in "filled engineering" toolbelts and the EngiVend.

The existing power drill research will be changed to a "compact power drill" with a 1x2 size.

The screwdriver and wrench will be given a longer do-after as "lesser tools".

#### Wire cutters and Scissors

Wire cutters will be given innate LV insulation (the rubber grips aren't just for looks).
They will still spawn in maints and toolboxes.
They will spawn in "filled engineering" toolbelts and the EngiVend.

Scissors will replace the "common" wirecutters in tool vends, belts, and general maps.
They will be slower than regular wire cutters.

#### Welders

Industrial welders replace engineering's welders, and are made to be "standard" speed.

Advanced industrial welders are made to be faster, and carry more than Industrial Welders.

Welders will be given a longer do-after as a "lesser tool".

#### Insuls/Budget insuls/Arc Gloves

Budget insuls no longer exist in the tool vend, and their place will be taken by improvised insulated gloves. 
They can be crafted with a pair of gloves and plastic, providing LV resistance and turning the gloves white.
These gloves would give a significantly longer do-after while worn and take up a 2x2 space due to their unwieldy improvised nature.

Insuls continue to exist as they have, but will provide MV resistance.
They will no longer spawn round-start in the tool room.

Arc-gloves slow down do-afters when worn but provide HV resistance.
This does not apply to the CE's Arc Gloves.

## Game Design Rationale

RPDs and RCDs cheapen the construction experience and currently exist due to dissatisfaction with the construction menu.
By providing "quick use" option with the relevant materials this rework hopes to eradicate the need for them, without the final UI rework being needed for the G menu as a whole.
The Circuit pouch, reduced engineering circuit size, and increased versatility in circuits will also satisfy the RCD's current place in combating the bulkiness of existing circuitry.
After implementation this may eventually be able to be reduced to just "circuitry" as a resource for engineering and construction.
The hull axes also target this as they provide a way for engineers to remove hull tiles with the removal of RCDs, without there only being the fire axe.

The flatpacker was built for servers with shorter rounds where science would never have time to make anything they researched.
We however have 2 hour rounds where science often finishes research and has little to do.
The removal of the flatpacker may not entierly solve this, but it is a start on it.
The addition of a "use" function to circuits will also alow them to skip over the construction menu that was a complaint in the flatpack removal feedback.
As per the feedback in the past about flatpack removal, this part of the construction rework will not be implementating full flatpack removal across all parts of the roundstart and cargo experience.

The pipe change's reason is fairly straightforward.
People *usually* cant bend sheets of steel by hand to make make pipes that are air tight. 
Additionaly they can't bend those sheets by hand to make functioning circuitry that will seperate diffrent kinds of gasses, pump it in a direction, or much else.
Lastly the change to pipes as a recourse alows it to effectively interact with the new "use" system without overloading steel, and makes them cheaper to craft and hold.

For the tools it enables engineering to have an advantage in construction and deconstruction, without directly taking away those abilities from other roles.
They can simply use better tools that are afforded to them as they were hired to do those things.
When you want to rework the medical bay, the bar, or a shuttle you *can* do it without engineering, but it's faster to have an engineer come over and lend a hand in the project.

## Roundflow & Player interaction

This PR will slow down the engineering experience in some aspects, mainly where the RPD and RCD are concerned, such as in the construction of complicated atmos networks and wall repairs, but accelerate the "intended" form of doing it via the "use" radials.
It will also lead to a greater use of materials from engineering, encouraging interactions with cargo throughout the round.

This will make large scale engineering projects go much smoother when done in conjunction with engineering, encouraging their interaction, while still be possible for non-engineers to do themselves though less efficiently.

Additionaly science will be encouraged to do more machine construction throughout the round, slowing them down a little bit and providing them with more interactions with other departments.

## Administrative & Server Rule Impact (if applicable)

This should have no additional administration impact when compared to current systems.

# Technical Considerations

This will utilise existing systems and code such as the radial menu, however it will require interaction between that system and the construction blueprint system.7

Some construction objects will have to be tweaked to provide an extra step, such as with pipe devices, or to change the required circuit.
