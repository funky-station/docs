# Cyber-Horror Antagonist

| Designers | Implemented | GitHub Links |
|---|---|---|
| Dicerson (Writer/Designer) | :x: No | TBD |

Seeking Coder that actually knows how to code things (assuming the proposal is well-liked enough) and to help with specific numbers or refinements

## Overview

This proposal aims to add a new mid-round/primary antagonist type (similar in threat/scale to Changelings or Heretics) that fills a currently more or less vacant thematic niche (Cybernetic Horror/”Terminator”). It aims to fulfill this fantasy via a heretic/ling-like system of abilities and upgrades that it can purchase through use of points gained by fulfilling its primary objectives.

## Background

This proposal is not made in response to any problematic game states, rather with the intent to fulfill a thematic niche that is not present - ie Cybernetic or Robotic solo antagonists. Funky currently has Replicators and the Colossus, but both are rare, neither are truly standalone, and Replicators (while very fun) are a major round-ending threat snowball type conversion antag (similar to blob) while Cyber-Horrors aim to be more long-term, softer, and “ling-like” in that they emphasize discreet objectives which do not necessarily end the round. It is also a purely sci-fi/robotic themed antag, unlike the colossus which ties into the themes of the Cosmic Cult (it being a robot is almost entirely irrelevant/secondary, it could be a ghost or spirit or even an organic creature and it would not really change its nature or function)

## Features to be added

 - New type of Antagonist which can be rolled alongside other antagonists (Traitors, Thieves, Heretics, Lings, etc.), as part of a mid-round antagonist roll, or as the primary antagonist of a game mode (likely with other mid-rounds joining them in smaller numbers either at the beginning or truly mid-round)
 - This is a mecha monstrosity obsessed with achieving “Perfection” through self-modification. It emphasizes highly aggressive play, and can move quickly if the player is robust. Rather than posing as a crew member, like other antags, it instead poses as an arrivals cyborg with only 1 law: “Achieve Divinity”. It will have a button UI for selecting other lawsets, which do not actually constrain its behavior but will allow it to ‘feign’ having laws if it is asked or interrogated. It has no lawboard and cannot be relawed - only destroyed. It otherwise starts with the same model and modules as a normal borg, including the ability to “specialize”
 - This antag’s goal is achieved through dismantling other Borgs and/or advanced machines and using their parts to improve itself, stealing their modules and gaining special “points” it can spend to further unlock unique enhancements and upgrades similar to a Heretic’s knowledge points or a ling’s dna. It starts with 1 such point to select a single low-level tool it can utilize to achieve its first “kill”.
 - The Cyber-Horror can also gain points by a similar process performed on any Machine; though any given machine type can only provide points once (You gain no extra points from eating the other 5 tesla coils, or every lathe on the station, etc.); as well as "eating" live positronic brains and occupied MMIs (a savvy horror might kill a crew just to MMI and eat them).
 - As it progresses, it eventually reaches a point of no return; its sprite changes to reflect its antagonistic nature and it gains a new goal of “Assimilating” the station’s AI Core and achieving Mechanical Godhood. Once it does so it becomes a wholly Digital being with godlike powers and can roam around the station doing whatever it wants for exactly 2 minutes before it ascends to a higher plane of being (with the round continuing on as normal afterwards)
 - Generally speaking, the number of points required to reach this point is set such that at least 3-4 "kills" are mandatory (or enough unique machines to cripple the station in some way)
 - Examples of things this type can unlock: EMP button (that it is immune to), free (but long cooldown) EMAGs, free and more powerful versions of borg modules (regardless of actual specialization), Hands, personal storage, reflective shield bubble, self-repairing nanobots, various weapon-analogs (blades, energy guns, etc.), ability to change specializations/standard modules, change name, etc.
 - Notes on combating it; It can of course be outed if it is found to be ignoring obvious laws and someone ends up checking its actual lawset (or rather the fact that it appears to have no lawboard). While immune to its own EMP, it is not immune to EMP in general (and becomes flash immune only after achieving its “horror” form). It also shares the same resistances (and weaknesses) as normal borgs.

## Game Design Rationale

 - This Antagonist mostly fills a similar role to other current mid-rounds, being a dangerous, unpredictable source of chaos, confusion, and/or intrigue; intended to create paranoia or sheer terror in the crew through their pursuit of their ultimate aims.
 - Cybernetic or Robotic horrors fit very nicely into the general overarching sci-fi theme of any space based game setting, and ss14 is no different!
 - This antag can be played a variety of ways, though aggressive borg-on-borg violence is encouraged, thanks to its plethora of possible tools.

## Roundflow & Player interaction

 - This antagonist can be either roundstart or mid-round, and is intended to have a direct impact on gameplay for most of the crew at some point in its “growth”/progress towards its goals. Much like heretics or lings it starts off relatively slow, but unlike them has potential for progressing very quickly if played robustly (especially during already chaotic rounds)

## Administrative & Server Rule Impact (if applicable)

 - This antagonist is mostly limited by its objectives, and in some cases escalation rules; it can be a highly destructive antagonist - or it can hyperfocus on its objectives, consume the AI, and otherwise leave the station intact.

# Technical Considerations

 - This is a fully new antagonist, not native to SS13 or other servers (to my knowledge; hope I didn’t reinvent the wheel!) and thus would require a significant amount of coding and spriting work to implement.
 - Worse still, it’s effectively 3 different antagonists in one; with the player that rolls it getting to choose which type they play in a given round.
