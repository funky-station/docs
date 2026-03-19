# Old Station Redux

| Designers | Implemented | GitHub Links |
|---|---|---|
| hereelabs (GH) / spongiformwebsley (DC) | :x: No | TBD |

## Overview

Old Station returns as a Telescience based side game. Ghosts are prompted to join a party, and will be sent onto a variant of an old, derelict station, tasked with making contact with the main station, using Telescience. The crew of Old Station will go through many dangerous dungeons, before finally sending the station to close proximity of the main station where the rest of the round is taking place. This side game will allow players to focus their feelings after being removed from the main round towards something constructive, rather than something negative.

## Background

A year or so ago, Old Station was added to Funky Station. This side game gave players a chance to return to the station, as fresh new characters, with tools and materials that they earned, rather than were just handed. While it was well received, it was not variantized, meaning that there was little replayability. 

## Features to be added

When a player is a ghost without a body to return to, and they have been alive for X minutes (at least 25), they will be prompted to join a party for Old Station. Once the party fills up, it will begin after 1 minute. If more than 6 players join the party, it will become a raffle, and 6 players will be chosen out of the players. The game will create a new map, load a variant of the main Old Station map, and the players will be able to leave their Cryogenic Sleepers.

A basic telescience setup alongside a randomized disk will be present on every station, the disk containing the id of a new Oldstation Dungeon prototype. Once the disk is loaded into the console, a portal will appear, and the crew will enter it to the dungeon. Every dungeon will contain a Oldstation Disk spawner, and depending on the ordering, the disk will either contain the next disk in the order, or a special final disk which will then send the entire grid to the main map, far away from the main station.

## Game Design Rationale

### Take Things Slow & Maximizing Roleplay Potential

Old Station is a slow burn side game. While players can always return to the side game should they all fail, the dangers of every dungeon will require players to plan their steps thoughtfully, thus giving them time to not only make a good game plan, but also to build their characters that they were assigned. Medical supplies are far from infinite, they are scarce, and require all players to think before they act.

It is entirely possible for Old Station to not be completed before the players can return to the main station, and that's okay. It fills the time many spend waiting for a destructive or influential ghost role with a constructive and fun side game. And, if it isn't something you're interested in, you can always not join the party.

## Roundflow & Player interaction

Old Station is mostly irrelevant of the main round, only coming into play once a player is removed from the round. In a sense, Old Station is it's own mini round, but once (and if) the players are able to return to the main station, it gives an opportunity for the new characters that players have built up over the past hour or so to shine. Old Station characters are blank slates, and give people opportunities to play a character they may never have thought to before.

The characters are all from a time long past, and as such they may not be privvy to modern technologies, or changes in things like Space Law or SoP. A prankster might not be knowledgeable to how rough Security has gotten in the past few years, and will be punished much farther than they expected. This may lead other members of the Old Station crew to either jump to their defense, or maybe they will allow this injustice, to said pranksters chagrin.

## Administrative & Server Rule Impact

Since Old Station no longer spawns on the same map as the station, it shouldn't be a concern. It might be worth adding a rule against stalling, since someone could definitely just stay on Old Station doing nothing for a whole round.

# Technical Considerations

There are a few concerns I have regarding how the Telescience aspects may come into effect. Since Old Station has it's own map, the telescience dungeons / adventure zones may need to be their own each, as well. Maybe the Telescience console needs to load the disk, which can mask the loading of the adventure zone? It may have a safety feature to ensure the portal is not closed until everyone has left the dungeon / adventure zone.

The ghost role party / raffle system should be nonintrusive. An action appearing in the top right prompted by a sound would be wise, though it may make Old Station not as present in the mind of ghosts as it should be. Another way this could be done, is to rework the Ghost Roles menu to include static ghost roles. I could see a world where the Ghost Bar and Old Station have their own section, but it would require a lot of work.
