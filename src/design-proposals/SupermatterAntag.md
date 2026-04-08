# Implementing a SuperMatter Antagonist

| Designers | Implemented | GitHub Links |
|---|---|---|
| SIU + Snippet from Joaco545 |  :x: No | TBD |

## Overview

  What I am proposing is implementing a SuperMatter Antagonist that would function in two primary ways. It would display NT negligence for increased efficiency and acquiring of cash. As well as functioning as an antag built around exploiting and loopholing space law, and NT SOP around it, to be in a good position to conquer the station.

## Background
 it would function as a way to give magistrate, lawyer, and similar roles more unique job performances relating to this antagonist, as well as encouraging security to squint and try to see if this antagonist is overstepping the lines. Links to relevant conversations: https://discord.com/channels/1276640157511979008/1276653734767755294/1491577740263166183

## Features to be added

  The major feature to be added: The Chrystaline Supermatter, is a sort of bee/hive themed semi-conversion, deal tangled cult antagonist. Essentially the idea is that Nanotrasen implements this Chrystaline SuperMatter because it’s a little cheaper to produce than normal Supermatter. As well as increasing the productivity of Engineering staff that are influenced by it, as long as the deals it makes are followed. At the crux of it, this antagonist is built to rules lawyer deals made with it into giving it a LOT of wiggle room. Its main abilities would be to convert crew, and silicons, distribute commands, and generate LUDICROUS amounts of power. To the point it may cause wire burns when it decides to stop operating outside of its deals completely.  The Infected crew abilities would be construction of crystalline metallic hive material, and deconstruction capabilities, as well as inbuilt capabilities for all available utility goggles, tools, and a quick and easy to access map. As well as the ability to construct traps, I.e Holofan based atmos traps, shock traps, stuff like that, Additionally combat related capabilities would be heavy incendiary and radiation damage via stingers and brawling, plus an electric stun to snag crew once it starts violating the deals it makes. These are done through natural means. There’d be a crafting station for crafting some more advanced tools I think, probably crystalline and goopy. The main goal would be empowering the Chrystaline Supermatter enough that it can hatch into a queen, not a true round end immediately, but it’s equivalent to the all hands on deck requirement of the monolith or final ritual being activated given it’s good at converting and ashing. If greater than 85% of the crew or the station’s tiles are converted, then that’s the round end, with the station becoming a hive that sells power to NT. The bow that ties this together, is the reccomendations that the CTM would give, encouraging the CE to appease it and strike bargains, as well as working with security, lawyers, and magistrate to establish deals treating it as crew, encouraging it to stay within the deals it makes whilst generating absurd amounts of power, treating it and any hive members as crew as long as those deals are maintained.  Those deals able to state things like: if more than 30% of the crew is a part of the hive, it may not make any conversions, as well as something like: hive material must not interfere with crew operations. Things of that nature. As well as the deals relating to just keeping the Chrystaline SuperMatter appeased, but not aggressively conquering. Encouraging Magistrate, security and Lawyers to interact with, and roleplay out effective HOA agreements with that hive.
  Infected would likely have glowing yellow eyes that can be hidden in the early stages, as well as taking on more blatant crystaline bee related traits in the mid-late stages of this antagonist, although if it hasn't broken it's deals, even if they get blatant features like that, they would still not be valid. Communication for the supermatter can only be done on an antag radio, until communications servers get subverted, at which point it can talk on the infected servers. It can see through it's tiles, infected crew, as well as eventually cameras if the camera routers get assimilated. In general, the supermatter can infect machines to use them in the same way the AI can. Able to upgrade those machines to perform better using some of it's power to use in bargaining as well.

## Optional Features

 When cameras are subverted, the AI and supermatter can see eachother's cursors when looking around. Gingerbreads in the mid-late stage look like they're made of suppermatter. Moths Go full bee mode at the early stage, Arachnids go wasp mode.

## Game Design Rationale

 The idea is to encourage more command/security and crew tension, as well as general roleplay shenanigans you can  get up to with an antagonist that is weak at first and has to comply with the deals it makes with command, but builds up to a good spot to escalate past the limits of the deals it makes. If the Antag wants to actually comply with the deals, they probably can if they really wanted to, and do their antagonism by the book. As a conversion antagonist, there is technically a win/lose state unfortunately, but I aimed for it to be more roleplay oriented as it’s a conversion antagonist that isn’t valid at roundstart due to snowballing a little, and trying to get stronger within it's deals till it can burst free. Plus the silliness of just: Nanotrasen and a hivemind rules lawyering each other is a bonus.

## Roundflow & Player interaction

  This feature by nature of being an occasional Supermatter replacement, would be a scaling round start antagonist, that starts from engineering as a SM and 1-3 infected engineers and escalates from there, it shouldn’t happen every round, and it would add a push and pull between engineering/Chrystaline Supermatter, command, security, and the crew at large. I would like the Chrystaline Supermatter to be interacted with through a lens of nitpicking at it to make sure it stays within it's deals, managing the power it produces, selling it, as well as being used to perform silly skits occasionally via rules lawyering, whilst also being a credible engineering based threat. This would be enforced mechanically by it being an antagonist, but also having deals made, and training to enforce and thus make it so it isn’t a valid target at first.

## Administrative & Server Rule Impact 

- Does this feature introduce any new rule enforcement challenges or additional workload for admins? It involves CTM, so yes, it would require some admin oversight to make sure people don’t rush the supermatter whilst it’s behaving.
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes? It provides the form  of griefing of just sprinting at the hive, or people griefing the hive by acting out of it's deals. 
- How are the rules enforced mechanically by way the feature will be implemented? This is semi-reinforced mechanically by rushing a supermatter on your own that’s defended being a bad idea, no matter how early in the round it is, it is crew so AI will defend it.

# Technical Considerations

- Are there any anticipated performance impacts? Possibly lighting based if it’s using supermatter lighting, if lighting impacts the frames.
- Does the feature require new systems, UI elements, or refactors of existing ones? it would likely  require a fork of certain cult of both varieties, AI, and supermatter code.
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types): as an antagonist, needs custom UI elements to distinguish what the hive wants the crew under its control to do. As well as a custom navmap managed by the supermatter, likely a radial menu to place Little crystaline markers on the map to show where it wants people to go, as well as a separate menu to manage the various little traps, crafting stations, as well as natural tools. The crafting station would just use the protolathe UI for crafting.
