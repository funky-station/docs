# Power Utilisation

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

This document seeks to provide an outline for a more engaging interaction with power generation than the current "optimise and maximise everything" that comes from the PTP.

## Background

Currently the PTP results in engineers being encouraged to optimise and maximise every generator on the station to squeeze out just a bit more cash.

The PTP itself is also very odd in universe, given we are on the ass end of nowhere.
Who are we selling to? Why do they need so much power? How does bluespace work? Why can't we purchase power ourselves?
Especially so given the discussions about removing bluespace from faxes to instil the isolation feeling.

Additionally we now have active-idle power draw differences in forky.

## Features to be added

### Real throughput

Limit Substation and APC throughput, forcing additional substations and APCs to be produced for higher power consumption projects.
Going over the limit randomly causes the network to shut down "blowing a fuse" that must be repaired.

### Overloading cables

More than one "input device" (APC or Substation) should overload the circuit, causing both to de-power and blow a fuse. 
This can be done with an occasional check (once every 30 seconds or such) on the according network for a second input device.

### Over-powering generators

When a generator is unable to output the power it *can* produce (EG the SMES are full) then it has a chance to overload.
This scales in the threshold of surplus power according to the generator, and in what an "overload" means.
Some generators may damage themselves on an overload, others may explode an SMES it feeds into, more still may have alternate effects such as the tesla causing arcing shocks from APCs on the station.

### Larger Cells/Power bleeding

Some structures can be used to "bleed" excess power, increasing acceptable power variance.
These are not cheap, but would be intended to be built throughout the round to reduce the need for power ramping/maintenance, and can be discovered through research.

Additionally more SMES and Substation upgrades should be made available.
First on a structural level including the "advanced SMES" which has a larger basic power capacity.
Second on a component level are advanced components which have existed before, providing a secondary % increase to the efficiency of machines.

### Power use balance

Machines will be modified so that more advanced variants (e.g. hyper lathes) use much more power when engaged in addition to requiring secondary upkeep (EG cooling or lube) to prevent side effects.
This is intended to create situations where a dedicated APC and room may be required for the use of advanced machines.
This in conjunction with the wider construction reworks in making building more intensive, will increase proactive interaction between Science and Engineering, instead of the reactive repairs.

### Multitool connection

The multitool/connector will be given additional functionality to connect power sources with cables.
Cable connections in a similar manner already exist, this would simply give them a way to do it manually instead of automatically.
This provides engineering with a way to set up power systems within a moderate proximity of each other.

## Game Design Rationale

### Maintaining Authenticity

These design decisions are intended to create a more engaging power system than simply maximising power every game, instead creating a system that prioritises keeping power balanced and ramping up as the round continues.
This allows us to more closely reflect real power generation where there can be some deviation between power generation and power use, but generally it has to match fairly closely.

### Maximizing Roleplay Potential

This system promotes roleplay by encouraging the crew to communicate between departments.
Even if science wants to build a machine themselves, they still have to check with engineering for what acceptable power tolerances are, as failing to do so could cause station wide brownouts to occur.

### Taking it slow

Repairs will have to be performed properly instead of eventually tying all LV networks into one big super network, taking more time to effectively finish repairs.

## Roundflow & Player interaction

Over the course of a round it is expected that command will communicate with engineering, and the CE will direct their engineers accordingly.
As advanced machines are being built engineering will be required to step in and assist in power balancing and setup, including the possibility of expanding the generally ignored substation systems, and expanding battery capacity to more than a simple "incase power is attacked" system.

## Administrative & Server Rule Impact (if applicable)

This will have an effect from engineers not listening to the CE causing overloads that may affect the station.
Additionally it will likely create a secondary point of concern when it comes to CEs actually performing their duties and providing direction when it comes to power generation as a point of compliance.

# Technical Considerations

There will need to be an over-ride for cable-machine connection instead of the current "closest cable first" consistent connection that currently is in use.

APC absolute power limitations have already existed on wizden, so the code for them can be easily transferred to forky.
The same is true with component upgrades.

Substation power limitations can fairly easily be extrapolated from the APC system.

Overlapping network detection should be fairly straight forward too given it is not something that needs to be immediately detected the second it happens, though it can also be done that way with a network detection upon construction.

Network overloads would require the most intensive effort to detect possible power output, actual power output, and triggering events based off of that.


