# Command Item Overhaul


| Designers | Implemented | GitHub Links |
|---|---|---|
| MasterElzoi | :x: No | TBD |

`Designers` 

Assisted in brainstorming ideas
- Delta_
- Kouhadyne (editor of this doc as well teehee)
- Flux (sinister)
- Higwaz
- thatonemoon
- Trixxedheart
- Dimesequals9
- (if I missed you please DM me on discord so i can add)

`Implemented` Not implemented.


## Overview

Adds/removes many Command items to incentivize leadership and disincentivize job+ activities.

## Background

Command members often find themselves being Job+. A large part of this is that Command items do not incentivize leadership in any way. The hypospray is Doctor+, as it is simply an improved syringe. The WT55 is Secoff plus, it is the highest DPS gun crew has access to. The RD suit is a science suit that lets you do artifacts without risks, etc. Additionally, command can find themselves lacking any items or tools to incentivize a management role. This doc outlines things to be added/removed to give to Command roles, and incentivize them to lead their department. While these changes could easily go into individual PR's, it is reformatting a lot about Command so i think a design doc is justified.

## Features to be added

- All Command members: RMC-style megaphone. This item would be mapped into Command lockers. It simply makes Command members text bigger when held, allowing staff to more clearly see what command members are saying.
_________________________________________________________________________________________________________________________________________
- CMO: "Medical overseer tablet." This item is contingent on others existing, but it would replace the hypospray. This would allow for two things. It would be a handheld crewmon (which the cmo already has access to). Additionally it functions as the "Holoband projector". This allows you to triage patients. Medhuds (for crew) instead of seeing healthbar status, would see patient priority assigned by the CMO. High priority, low priority, cryo, surgery, morgue, infected. You would set via radial wheel, click on a person with a small do-after to assign the status. The holoband projector would also include the option to remove their status once treated on the radial wheel. Remove the syringe gun. (nukie agent visor left unchanged)
_________________________________________________________________________________________________________________________________________
- Science:  Research tablet: The Research Director can flag research to be researched as it becomes available, this notifies scientist that the RD wishes this particular research to be unlocked. Research tablet can remotely access things to be researched. Scientists can choose other researches regardless of what is marked, but the mark always shows while it is available. Reduce RD hardsuit explosion resist to 25%
_________________________________________________________________________________________________________________________________________
- Engineering: A handheld Atmos monitoring console alongside their power handheld monitoring console. Kill advanced magboots. Kill CE roundstart advanced tools. Chief engineer designation tablet. Functions similarly to a Wanted PC, instead using station beacons as selectable options. It says a message on the comms such as "CE has designated (X beacon) area for repairs. Engineers are to report to the area." 
_________________________________________________________________________________________________________________________________________
- Cargo: mostly fine. Resource monitoring console, linked to silos (already approved PR upon inspection), however this could be included as a second tab on the digiboard.
_________________________________________________________________________________________________________________________________________
- Security: wt55 would be removed. Head of Security mask (replaces swat mask) includes a toggleable megaphone, which makes the HoS's text bigger than other peoples allowing it to be identified easier, functions like the handheld ones mentioned above. It also has a unique whistle sound effect to help rally secoffs. The HoS is given a security overseer tablet. This would have a device that allows you to announce things to sec on sec comms only with a loud notification sound, and have a portable wanted list console.
_________________________________________________________________________________________________________________________________________
- Service: Service techfab to be added. It is only in the HoP's office, to allow more central coordination of service.
_________________________________________________________________________________________________________________________________________
- Captain. Portable announcement console. Literally just an announcement console in tablet form.

## Game Design Rationale

As previously stated, Command players do not have the tools, nor incentive to Command their respective departments. As such command often relegate themselves to job plus, because we give them the tools to do so. These new items are intended to flip this over, making them no more efficient at their job than a normal worker, but giving them many tools to direct and command their respective departments. The items here are centered around giving command more vectors to communicate with their departments. Giving out information to them forces interaction, and potential conflict when the information or orders given aren't to the crews liking. This also sets a more defined power structure, aiming to separate command and their staff more in terms of who should be running things. The bigger text along with more communication methods, aims to imply to normal staff that NT gives them these tools because they value the heads of staff more, even when command is making a wrong call. It additionally enforces the idea that NT would not send their staff to the frontlines to do such dangerous things in sci or sec or engi, and instead wishes their lesser important normal staff to do so.

## Roundflow & Player interaction

It comes into play pretty much instantly for command members. These tools are designed to be used throughout the round. Command members won't have fancy toys to do job+ activities anymore, all they are left with is their management tools. Players should be using these tools to actually be command. Its important to mechanically hammer home to players what a command personnel's job is, which i believe these items will do. They are centered around communication, which enforces the idea that your job is to communicate to your staff. The features are designed in a way that it's pretty hard to interact with them in an incorrect manner. Any incorrect use would mostly just surmount to IC incompetence, which is another good vector for conflict.

## Administrative & Server Rule Impact (if applicable)

- Adding more vectors for announcements always has the issue of potential misuse, at least not to a degree that isn't already in the game


# Technical Considerations

- Unlikely to be any performance impacts
- Several UI's would need to be implemented. 
- A radial wheel input to designate patient status for the holoband projector. 
- A custom UI for sec only announcements from the security overseer tablet
- A UI for CE's beacon repair tablet. This should look like a station map, with a list of beacons on the right, when a beacon is clicked on it is marked for repairs.
- A UI containing a list of researches so the RD can designate priorities.
- Reformatting some traitor steal objectives
- Spriting for the new items