# Implementing a SuperMatter Antagonist

| Designers | Implemented | GitHub Links |
|---|---|---|
| SIU |  :x: No | TBD |

## Overview

What I am proposing is implementing a SuperMatter Antagonist that would function in two primary ways. It would display NT negligence for increased efficiency and acquiring of cash. As well as functioning as an antag built around exploiting and loopholing space law, and NT SOP around it, to be in a good position to conquer the station.

## Background

Admittedly there isn’t too much background beyond the idea seeming interesting. However it would function as a way to give magistrate, lawyer, and similar roles more unique job performances relating to this antagonist, as well as encouraging security to squint and try to see if this antagonist is overstepping the lines.

## Features to be added

The first of the two major features to be added: The Chrystaline Supermatter, is a sort of bee/hive themed semi-conversion, SOP tangled cult antagonist. Essentially the idea is that Nanotrasen implements this Chrystaline SuperMatter because it’s a little cheaper to produce than normal Supermatter. As well as increasing the productivity of Engineering staff that are influenced by it, as long as SOP is followed. At the crux of it, this antagonist is built to rules lawyer that SOP into giving it a LOT of wiggle room.
	Its main abilities would be to convert crew, distribute commands, and generate LUDICROUS amounts of power. To the point it may cause wire burns when it decides to stop operating outside of its SOP.
	Infected crew abilities would be construction of crystalline metallic hive material, and deconstruction capabilities, as well as inbuilt capabilities for all available utility goggles, tools, and a quick and easy to access map. As well as the ability to construct traps, I.e Holofan based atmos traps, shock traps, stuff like that, Additionally combat related capabilities would be heavy incendiary and radiation damage via stingers and brawling, plus an electric stun to snag crew once it starts violating SOP. These are done through natural means. There’d be a crafting station for crafting some more advanced tools I think, probably crystalline and goopy.
	The main goal would be empowering the Chrystaline Supermatter enough that it can hatch into a queen, not a true round end immediately, but it’s equivalent to the all hands on deck requirement of the monolith or final ritual being activated given it’s good at converting and ashing. If greater than 85% of the crew or the station’s tiles are converted, then that’s the round end, with the station becoming a hive that sells power to NT.
	The Second of the two major features would be Chrystaline SuperMatter SOP, encouraging the CE to appease it, and encouraging it to stay within SOP whilst generating absurd amounts of power, treating it and any hive members as crew as long as SOP is maintained.  That SOP stating things like: if more than 30% of the crew is a part of the hive, it may not make any conversions, as well as something like: hive material must not interfere with crew operations. Things of that nature. As well as SOP relating to just keeping the Chrystaline SuperMatter appeased, but not aggressively conquering. Encouraging Magistrate, security and Lawyers to interact with, and roleplay out effective HOA agreements with that hive.

## Game Design Rationale

  I will admit I probably have made several mistakes in this as it is my first time writing one of these. But the idea here is to encourage more command/security and crew tension, as well as general roleplay shenanigans you can  get up to with an antagonist that is weak at first and has to comply with SOP, but builds up to a good spot to escalate past the limits of SOP. If the Antag wants to actually comply with SOP, they probably can if they really wanted to, and do their antagonism by the book. As a conversion antagonist, there is technically a win/lose state unfortunately, but I aimed for it to be more roleplay oriented as it’s a conversion antagonist that isn’t valid at roundstart due to snowballing a little, and trying to get stronger within SOP till it can burst free. Plus the silliness of just: Nanotrasen and a hivemind rules lawyering each other is amusing to think about.

## Roundflow & Player interaction

  This feature by nature of being an occasional Supermatter replacement, would be a scaling round start antagonist, that starts from engineering and escalates from there, it shouldn’t happen every round, and I don’t think it would always speed up a round, but it would add a push and pull between engineering/Chrystaline Supermatter, command, security, and the crew at  large.
	I have admittedly reiterated this several times, but I would like the Chrystaline Supermatter to be interacted with through a lens of nitpicking at it to make sure it stays within SOP, managing the power it produces, selling it, as well as being used to perform silly skits occasionally via rules lawyering, whilst also being a credible engineering based threat. This would be enforced mechanically by it being an antagonist, but also having an SOP to enforce and thus make it so it isn’t a valid target at first.

## Administrative & Server Rule Impact 

- Does this feature introduce any new rule enforcement challenges or additional workload for admins? it involves SOP, so yes, it would require some admin oversight to make sure people don’t rush the supermatter whilst it’s behaving. So that is a factor, but generally SOP is well managed.
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes? It provides the form  of griefing of just sprinting at the hive, or people griefing the hive by acting out of SOP. But funky is behaved enough. I think i’m confident people can manage it.
- How are the rules enforced mechanically by way the feature will be implemented? Admittedly, this is semi reinforced mechanically by rushing a supermatter on your own that’s defended being a bad idea, no matter how early on it is.

# Technical Considerations

- Are there any anticipated performance impacts? Maybe lighting based if it’s using supermatter lighting, not sure how bad lighting is on the frames though
- Does the feature require new systems, UI elements, or refactors of existing ones? it would likely  require a fork of certain cult, AI, and supermatter code.
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types) as an antagonist, probably needs custom UI elements to distinguish what the hive wants the crew under its control to do. Probably a radial menu to place Little crystaline markers on the map to show where it wants people to go, as well as a separate menu to manage the various little traps, crafting stations, stuff like that. The crafting station would probably just use the protolathe UI for crafting.
