# Pirates!

| Designers | Implemented | GitHub Links |
|---|---|---|
| Miiish | :x: No | TBD |

## Overview

Space pirates! A rough and tumble, perhaps even jolly, gang of miscreants who want nothing more than to plunder every last speso on-station. They are a midround ghost role, ranging from dangerous minor nuisances to major threats depending on their ship.

## Background
https://www.youtube.com/watch?v=90BFz_g0AgI&list=PLGZbuWTzf2mJRhrSLMS7Pm2pF8FDZkSXh

Pirates are cool. Pirates have a lot of unused content and were never really implemented into Space Station 14 wholesale, even though they're really cool. Did I say pirates are cool?

Everyone's always saying "aw man, I wish we had more interesting midround ghost roles for when that goshdarned validhunter totally gets me through no fault of my own," well look no further for Pirates are here! Grab your cutlass and flintlock, we're going plundering! This station looks awful undefended, and their crew will be easy pickings for our jolly band of ne'er-do-wells!

## Additions

### Pirates and their Objectives

Pirates spawn with little armor (EVA suits and/or improvised armor), minimal weaponry (1 ranged and 1 melee weapon per pirate, rolled in a pirate booty chest on the shuttle.)

The objectives for the pirates will be simple: Acquire X spesos (X is arbitrary, the point overall is to make it technically obtainable but it's realistically not gonna happen without major economic fuckery) for their booty chest, on-shuttle. Simple! How will they achieve these objectives? Plunder everything of value from the station and sell it on their shuttle. Value, in this case, means everything they're capable of carrying or dragging back to their ship. While they can technically do this with no violence, the crew are greedy bastards and will not allow for this.

### Shuttles / Ships

The pirate gamerules will operate on a table, rolling between these options (based on population) when the pirate event is rolled through the event scheduler.

#### Small Pirate Shuttle
Low (~25?) playercount to roll. 2 pirates in a small shuttle armed with minimal weaponry.

#### Medium Pirate Shuttle
Higher minimum playercount to roll. More dangerous pirates as well as a true Captain (there's more of them, which means more lead.)

#### Large Pirate Shuttle
Even higher minimum playercount to roll. More dangerous pirates (there may be more of them and perhaps they get some of the bigger guns.)

#### Skeleton Pirate Shuttle
Rarer (10%) chance for any previous shuttle to be far more decrepit and filled with skeletons rather than organics/IPCs.

## Changes

Currently, pirate entities are a bit outdated and could use some tidying to bring them more in-line with the current state of the game. Examples are the blunderbuss and flintlock, which use shotgun shells and anti-materiel rounds respectively. Even if the values don't need to be changed, these should probably have own ammotypes.

Overall, the foundation is already here in the files, it can just use some cleanup.

## Game Design Rationale

### Seriously Silly

Space Pirates with cartoonish attire and really shitty yet deceptively powerful weapons. Does more need to be said?

### Maintaining Authenticity

We're on a station god-knows where and the only external threats from outside parties are people wanting to blow up the station? Why blow up what you can *steal* instead? Other threats are too high-stakes. Corporate espionage, terrorist organizations, ideological warfare, extinct superpredators. These are just heavily armed thieves, plain and simple.

### Roundflow & Player Interaction

More antagonist variety is always good to keep players on their toes, not bored, and not metagaming. This also adds another interesting ghostrole to keep RR'd people invested and keep the round moving on-pace.

# Technical Considerations

Objectives may need a bit of finagling to get right with Spesos, and some station item values may need tweaked as a result of unexpected interactions. On the surface, there won't need to be much uprooting of any existing systems.

The old cargo sales computer can be used (one might even say plundered) as an easy way to sell loot.
