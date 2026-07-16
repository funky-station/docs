# Command Design

| Designers | Implemented | GitHub Links |
|---|---|---|
| SOP workgroup, written by scrambleking | :x: No | TBD |

## Overview

This document will be covering the wider focus of the command's themes as Leaders, Teachers, and Corporate Elites.

The HoS/Warden dynamic will not be covered in this document given it requires a more indepth rework to how they currently function.

The introduction of HD "the service side of HoP" is covered in https://github.com/funky-station/docs/pull/96.

XO "the second in command/paperwork" side of HoP is covered here.

Additionally this document will be proposing defensive measures for each command member in accordance to their departmental themes as requested in the original document.
This is to support the "Corporate Elite" themes.

## Background

Currently command work on a level that is verging on being Role+ in many departments.
This is due to a variety of their tools simply making them better at those given jobs than their work force.

## Features to be added

<details>

<summary> CMO (This section may change with the release of status-med) </summary>

### Current Tools

Hypo : Altered, current form does not support a supporting/overview position.

Surgery gloves/Tools : Removed as surgery is a time intensive process that the CMO should not be encouraged to perform.

Syringe Gun : Removed, chemicals are fiercely powerful, even more so if used from a range.

Hand Held Crew Monitor : Altered for additional functionality

### Altered Tools

Hypo (Stabilising Injection) : Altered to inject a new chemical that clears existing chemicals, stops bleeding, and minorly regenerates badly injured patients, with a slightly larger heal on airloss and bloodloss.
Auto recharges on a time based charge system.
This provides the CMO with a tool to assist in emergency situations and mistakes without encouraging them to take over medical entirely.
Additionally this still makes it a potent tool for antagonists to obtain.

### New Tools

Room Tags : An nameplate/displayboard system to designate rooms by number, doctor, ailment, or more.

### Defensive Measures

Hypo (Causlikos Spray) : Alternate mode for the Hypo, also consuming charges.
The spray is similar to a spray bottle, however the chemicals slow the target on contact for a short amount of time, dealing minor caustic damage and blinding them for a second.
Given the loss of the Hypo and Syringe Gun as defensive options, the CMO will require a new minor defensive tool which this fulfils.

</details>

<details>

<summary> RD </summary>

### Current Tools

Tool Drill : Removed, serves no purpose

Portal Device : Altered, currently primarily used to circumvent movement on large maps.

Suit : No Change

### Altered Tools

Portal Device (Recall Device) : Altered for the first placement to lock in a destination, and the second use to place a short term portal to said destination.
The portal only lasts for a few seconds, allowing others to follow, but no travel back to the initial location, nor for a sustained route.
Removes using the portal device as a tool to teleport into random locations.
Removes the use of it in circumventing the design of large maps.

Additionally, change anomalies to automatically "unanchor" when going critical. Allowing a prepared RD to "recall them" away from (or into) dangerous locations.

### New Tools

Hand Held Research Console : A research console that is hand-held, allowing the RD to research from wherever they are.
Add a separate tab with functionality to track where points are being generated, possibly in graph form.

### Defensive Measures

Recall portal and Suit are judged as enough defence.

</details>

<details>

<summary> CE </summary>

### Current Tools

Advanced Tools : Removed, no advantage aside from allowing them to just be a better engineer

CE Belt : No Change, it's just a large belt, no shame in storage room

CE Suit : Additional Functionality

CE Boots : No change, getting to the scene faster to direct engineers is within theme

RCD/RPD : No change, Removed on RCD/RPD overall removal

Handheld Power Monitor : Altered for additional functionality

### Altered Tools

Handheld Power Monitor (Handheld Engineering Monitor) : Additional tabs added for atmos, nuclear reactor, and supermatter monitoring.

### New Tools

Construction Spray Paint : Shares placed blueprints as Construction Outlines.
Marks items for demolition.
Allows the CE to effectively direct construction projects.
([See Also](https://github.com/funky-station/docs/pull/124))

Remote Cell Charger : Allows the CE to slowly recharge cells in the area.
Perfect for battery based tools and workplace lights.

### Defensive Measures

Fulfilled by the atmos axe

</details>

<details>

<summary> QM </summary>

### Current Tools

Digiboard : Altered for additional functionality

Suit : Unchanged

### Altered Tools

Digiboard : Add silo monitor link capabilities.

### Defensive Measures

Satisfied by knuckle dusters

</details>

<details>

<summary> XO </summary>

Extra note:
The Executive Officer (XO) is the second in command/paperwork side of HoP, split to a separate role with oversight of the Internal Affairs involving the altered Magistrate and IAA positions.
They generally have a strong connection to the contract-law the station runs on, and accordingly support the station as HoP had previously done before.
In line with their paperwork and Contract/Legal themes, they still retain the standard duties you would normaly recognise as being within the old HoP's perview, such as setting access and firing/hiring individuals.

### Current Tools

They will generally inherit all the tools of the HoP, which are appropriately within the theme given their position.

</details>

<details>

<summary> Captain/CL (NTR) </summary>

Extra Note:
In order to better support the Captain being in charge of the station and the Corporate Liaison (CL, previously NTR) just visiting for inspection we plan on the following changes.
First is that the CL will have their own shuttle that they came/come in on instead of their own room/rooms on the station.
Second is having the CL come in later in the shift, possibly as a guaranteed event role, to better represent in game how they do not always exist.


These are appropriately within the theme given their position, and as such will only have minor changes.

CL:

Handheld Fax: Removed. It is not required given their change in responsabilities, and with the death of faxes being bluespace it no longer makes sense.

Cane Sword: Re-Implimented

Laser Pistol: Re-implimented

Command Glasses: Re-implimented

NTR Stamp: Re-designed for their new title

These should also start on the NTRs person, instead of being inside a dedicated locker.

Captain:

No changes to equiptment required, though the CTM equivilent will need to, again, be placed in their locker.

</details>

## Game Design Rationale

Reasoning is scattered within the relevant parts, but overall this is to support the idea that command personnel are there to command, teach, and overwatch the common workers.
Should there be a horrific mistake command should generally be able to step in if required to stop a mistake from becoming even worse.
These themes are also reinforced in https://github.com/funky-station/docs/pull/112 with the various paperworks there.

The intent of the "defensive item" modifications are to highlight that NT care far more about command over the common crew without providing a level of power that would encourage valid hunting.

## Roundflow & Player interaction

Through these modifications command members should be placed into a more focused position for taking command over their departments instead of taking the jobs of their employees.
Additionally it should help assist them in being the focus on training as it is far more efficient to teach the new players how to do things in your department as opposed to doing it yourself.

## Administrative & Server Rule Impact (if applicable)

The overall administrative impact should not be overly changed from existing systems.

Rule wise considerations will have to be made for command properly commanding and teaching new players, but these rules do already exist to an extent and so any changes will likely be minor.

# Technical Considerations

UI elements will need to be modified for the various hand held console modifications.

Portal code would need minor modifications to impliment a one-way portal system for their hand-held device.

Addition to critial anomoly code to un-anchor when it triggers the criticality sequence.

Tracking of points over time for the relevant R&D server.

This may impact server performance via CE's hand held console, though implimentation can be altered to a mode selection should this prove an issue.
