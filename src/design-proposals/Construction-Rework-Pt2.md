# Construction Rework Part 2

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

This document covers the implementation of an expanded blueprint and hologram system for construction.
While less useful in the current system where you can construct and deconstruct walls and basic structures in seconds, its implementation allows for a smoother transition to more indepth construction.

## Background

Currently unless you start esoterically drawing with crayons on the ground there is no way to properly show others what you want built in an area.
This document will be covering a variety of solutions to this issue to be implemented separately or together.

## Features to be added

### Mental images
"Mental images" come from the current construction system.
These are only visible to the person who places them, and can be used to build what you are looking to construct.

### Construction Outlines

"Construction outlines" are more advanced forms of "mental images".
They are visible to everyone but otherwise work exactly as "mental images"

### Construction Chalk
Construction chalk has 2 modes.
The first mode is to left click on a "mental image" to make it a white "construction outline" with a quick do-after.
The second mode lets you mark items for deconstruction with a red "destruction mark" (an X on the object) with a short do-after.
Both of these are visible to all crew.
The "construction outlines" and "destruction marks" can be erased by alt clicking them, though it produces a short do-after.
Additionally they can be erased via the use of space cleaner spray (why would you clean a construction zone?).

### Construction Spraypaint
The "construction spraypaint" is available to the Chief Engineer or via research.
This device has 2 modes.
In the first mode the device turns all "mental images" from the user in a short range into blue "construction outlines".
In the second mode the device will allow for the user to mark items for deconstruction from a range.

This device is intended to allow the CE to take a larger designation and leadership role on construction sites rather than their current vague orders method.
When used in conjunction with the following device it can also be used to enact large scale repairs in the case of large scale destruction.

### Construction Checklist

The "construction checklist" creates a list of supplies needed for each "mental image" or "construction outline" selected.
When images or outlines are completed or removed, they update on the construction checklist.
There would also be a button to reset the list accordingly.

EG you go to a construction site and select the following images/outlines:

To Build:
1. Windows X5
2. Walls X18
3. Wooden tables X4
5. Wooden chairs X8

Resources:
1. Glass X10
2. Steel X72
3. Wood X24
4. Rods X8

When you build a window it will update the window and glass numbers accordingly to Windows X4 and Glass X8

### Blueprint (Most complicated to implement)
A "Blueprint" contains the "standard structure" of the station, making for a fast way to check what needs repairs and what is not "up to standard".
Use of the "blueprints" places a "mental marker", of which 2 can be placed. 
Once both markers are placed a "mental image" of the station hull in working order will appear to guide repair.
Once the hull is constructed (or the blueprint is used again) it will then produce a "mental image" of the pipes and cables.
Lastly once those are placed (or the blueprint is used again) it will then produce a "mental image" of the walls, doors and windows.

A final stage that produces the furniture, exact floor tiles, ect will not be included as they are not structural components.

## Game Design Rationale

### Maximizing Roleplay Potential
These changes push forward the ability for general crew to utilise the station's engineers more to construct rooms and modify areas to their liking.
As it is now the difficulty in communicating what you want done creates serious problems that lead to many non-engineers simply constructing what they want themselves.
With these changes it creates a way to effectively communicate these changes to alow for the plans to be fully realised with minimal miscommunication.

### Maintaining Authenticity
In the real world, you would set up blueprints and ways to communicate what it is you want done in constructions, not just "oh yea put some tables *waves hand* and take down those walls "waves hand".
Additionally a station would always keep construction blueprints on hand in case of repairs.

## Roundflow & Player interaction

Generally these will come into effect throughout the round whenever construction or repairs are needed.
Ideally it will result in the Chief Engineer marking repair zones for the construction effort after major damage.
Additionally it should result in small groups of engineers working together on certain construction projects, and otherwise helping out departments as requested.

## Administrative & Server Rule Impact (if applicable)

The only concern would be egregious spam of the implemented construction tools.
That is however less worrisome as someone spamming crayon or spray painting as it can be taken down without tools.

# Technical Considerations

The two biggest technical considerations will be the implementation of "Construction Outlines" which should be relatively easy as it utilises existing methods, and the "Blueprint" which would be far more intensive.


