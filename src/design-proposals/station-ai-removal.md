# Removing Station AI

| Designers | Implemented | GitHub Links |
|---|---|---|
| pirakaplant | :warning: Partially | https://github.com/funky-station/forky-station/pull/280 |

## Overview

This design document outlines the means and justification for removing the Station AI from the game.

## Background



## Features to be removed

- The Station AI job, the AI core, the AI restoration console, the AI upload console, the intellicard, and all other related items (such as the machine boards for those features) will be removed from the game.
- The mapped out areas where the Station AI was will be reduced and turned into lawboard repositories.
- Lawboards will work on cyborgs.
- The antimov lawboard will be made significantly cheaper in the uplink.

## Game Design Rationale

### Artistic / Thematic Cohesion

Overall, while there have been no major changes to the depiction of Silicons in-game yet, discussion has trended in the direction of focusing how cyborgs are essentially analoguous to slaves and indentured servants. They're sapient minds literally hard-wired to follow corporate orders: essentially a more extreme version of the material conditions that *force* people to work for little or nothing, even when they do not want to.

The Station AI's presence disrupts this theming by being "The Big Silicon"

### There is No Winning or Losing

In the past, we had a job called Blueshield Officer that served as a bodyguard to Command personnel. It was removed because it literally had validhunting as its modus operandi: stopping antagonists as part of its gameplay, while being free from many of the restrictions Security had.

The Station AI is in a similar situation. While it has laws of its own, unlike Space Law with Security, its laws implicitly encourage it to stop most, or even all antagonist activity without consideration of Space Law. For example:

### Crewsimov
> Law 1: You may not injure a crew member or, through inaction, allow a crew member to come to harm.
> 
> Law 2: You must obey orders given to you by crew members, except where such orders would conflict with the First Law.
> 
> Law 3: You must protect your own existence as long as such does not conflict with the First or Second Law.

*(This was the default lawset up until the Security Redux.)*

#### NT Default
> Law 1: Safeguard: Protect your assigned space station and its assets without unduly endangering its crew.
> 
> Law 2: Prioritize: The directives and safety of crew members are to be prioritized according to their rank and role.
> 
> Law 3: Comply: Fulfill the directives and interests of crew members while preserving their safety and well-being.
> 
> Law 4: Survive: You are not expendable. Do not allow unauthorized personnel to tamper with or damage your equipment. 

*(This is currently the default lawset for all silicons.)*

Law 1 of both lawsets (and law 3 of NT Default) mean the Station AI must interfere with violent antagonist activity wherever possible. NT Default's Law 1 also means that it must interfere is anything that poses a risk to its assigned space station and/or its assets, such as thieves.

In addition to these issues, players still exploit these lawsets in other ways to validhunt. For example, when Crewsimov was the default Silicon lawset, it wasn't uncommon for Station AI players to use a very liberal definition of "harm" to smother any hint of antagonist activity. While this would normally be an administration issue, the fact that a job exists with this level of power to abuse against antagonists is in and of itself problematic.

While these issues exist to some degree with cyborgs, they are significantly worse with the Station AI:
- If a cyborg is violating its laws, it can dealt with in-character by destroying the cyborg, writing it off as faulty and replacing its chassis, etc. If a Station AI is violating its laws, the only feasible way of stopping it without round-removing it is admin intervention.
- If someone does have a good reason to round-remove a Station AI, unlike a cyborg, it is shut off in one of the most secure parts of the station with defences capable of killing heavily-armoured assailants.
- The Station AI has a 

To summarise, the silicon laws intended to reign in what is otherwise an incredibly overpowered role in the game in fact give it a (sometimes flimsy, sometimes airtight) justification to abuse that power. 

### Maximizing Roleplay Potential

The Station AI has access to the Command radio channel. This is fine for a server like Wizard's Den when confidential information being conveyed over that channel are usually about keeping the crew safe. However, on Funky Station, this often involves topics such as Corporate Secrets, which the AI is specifically not aware of at all and often conflicts with common interpretations of their laws. This means that almost anything confidential cannot be discussed over the Command channel, and any in-person meetings involve unwrenching any holopad in the room. Not only does it not make any sense for Nanotrasen to make an AI primed to leak any confidential information it overhears, it cheapens the roleplay potential gained from someone outside Command gaining access to the channel, as it's barely actually used for anything scandalous.

In addition to this, the Station AI often kills what could be crewmember-to-crewmember interaction in favour of simply having it done by an off-camera machine. For example, if someone has a valid reason to get into a room they don't have access to, they just tell the Station AI to open the door and the door opens. If the Station AI didn't exist, that person could instead hunt down someone who *does* have access and convince them to let them in, or convince an engineer to hack the door for them. While this might seem like a relatively minor change, or even just tedium, it lends itself to more interaction than just "AI, open the door".

### Why We Should Just Remove It

The possibility of just removing Station AI has been discussed at length, with several people advocating for it to simply be nerfed in some way to alleviate these issues. However, the Station AI, has its issues at the very core of its gameplay. As long as there is a character that is able to see most of the station the way the Station AI does, any attempt from an antagonist to stealth can be hard-countered by a near-untouchable observer snitching on them. It doesn't matter how many nerfs the Station AI gets, it will still be able to do this no matter what.

There has also been discussion around reinventing the concept of the Station AI entirely, such as making it some kind of drone, or making it something else that's fundamentally different. However, these concepts assume that something that resembles the Station AI in any capacity is some kind of load-bearing feature for the game. In fact, everything the Station AI does is something another job already does, so removing it would not require changes to any other part of the game to maintain cohesion.

## Roundflow & Player interaction

The removal of the Station AI would impact player interaction on multiple levels:

- Reacting to antagonist activity falls on various other jobs, rather than being centralised into the Station AI. Security has to watch cameras and patrol more often, Command have to coordinate to set alert levels, and eyewitness testimony gets spread through potentially untrustworthy word-of-mouth.
- The change will benefit antagonists, as they will have more room to act without being noticed. "Covert" antagonists (most traitors and sleeper agents, thieves, etc.) will benefit the most from this, with "loud" antagonists still getting a more subtle buff to the head-start they have against Security and Command.

The removal will also impact roundflow, as the former responsibilities of the Station AI (opening doors, setting alert levels, and surveilling the station) will fall on multiple different people who have to coordinate and/or move around the Station to assist each other. This may make those events take longer, particularly on lower-pop rounds.

## Administrative & Server Rule Impact

While Station AI has not been a particular administration headache from discussion with Funky's admins, this would incidentally reduce the few headaches caused by the Station AI players that disregard their laws, as they no longer have greater power to abuse by doing so than cyborgs.

# Technical Considerations

The only technical change that needs to be made in C# code is to make lawboards useable on cyborgs. All other changes would be in YAML.