# Roundflow & Transportation

| Designers | Implemented | GitHub Links |
|-------|-----|-----|
| Teasq | :x: | TBD |

## Overview

The purpose of this document is to redesign 3 facets of Funky's current roundflow:
1. arrivals/joining a round late
2. the build-up to the end of the round - specifically how we could reshape service's roleplay/gameplay and expectations
   towards the end of the round
3. and the end of round itself.

## Background

1. Currently, late joining via the arrivals shuttle is a very underwhelming experience that adds very
   little to a round and creates a colossal logic gap: if the station is a far-off, isolated research outpost,
   why can arrivals easily transport people to the station on a regularly scheduled basis>
   (oftentimes transporting nobody)? This eliminates the sense of isolation being on this far-off station is
   meant to evoke, and isn't logically consistent with how difficult it is to call for off-station reinforcements.
2. There is oftentimes no build-up to the end of the round without direct antagonist interference, the round merely
   progresses silently until the 1h50m mark, at which point the shuttle announcement is made and people prepare
   to leave the station behind and climb aboard an evac shuttle that detaches them from the consequences of the
   events of a round.
3. Lastly, the primary focus of this document, is the evac shuttle and the interactions surrounding it.
   Beyond being detached from the actual events of the station, its arrival is very sudden and its
   departure is swift (3 minutes). While this does achieve a concrete ending to a round, it does so in away that is
   unengaging and unfulfilling. You are forced to drop everything you are doing and make way to evacuation, leaving
   everything you and others have achieved behind.

## Features to be added

There are several changes required to alleviate or solve the issues mentioned above, which I will compile in a list for
convenience:

### Mapping
1. Arrivals &Departures. This will replace arrivals and evac as separate entities, and instead unify them into a new
   area named Arrivals & Departures, which would ideally be a large airport-like area, with various docking ports to
   accommodate shuttles or emergency evacuation in case it needs to be called.
2. The arrivals shuttle. The arrivals shuttle would no longer exist, instead being replaced by various cryosleep areas
   around the station: in arrivals & departures and dorms (and potentially more that I cannot think up currently).
   This is logically consistent with what the station is:
   an isolated outpost wherein the workers are contracted to work aboard for set periods of time - an easy example
   being oil rig work, or the Nostromo from Alien.
   That is, after all, why long-term accommodations like a high-capacity power grind, a
   hydroponics area, a service area AND staff and dorms exist. These stations are, by design, made to be lived
   in for extended periods of time.

### Roundflow & Player Interaction
1. The round-end announcement. This would replace the evac shuttle's "10 minute until departure" announcement.
   The primary purpose of it would be to indicate the final act of the round, encouraging everyone to finish their
   work and prepare to wind down. The shift would at this point effectively be over, and people would be on break.
   This is when the final service event, detailed below, would happen. After 10 minutes, a final announcement would be
   made alongside the round-end screen, effectively ending the round after 3 or so minutes.
2. Service events. (outlined here: https://github.com/funky-station/docs/pull/96) An event would ideally be designed to
   line up at the end of a round, to create a round-end "happy hour" or pizza party and creating a more
   diegetic build-up to the end of the round. This encourages people to wind down at the end of a round, and
   builds up a sense of community while simultaneously reinforcing service's role as the bread and circus role. This
   also provides people with an opportunity to hand out medals of exemplary service (See the often forgotten medal case
   in the captain's office).

### Gameplay
1. Cryopods. Upon exiting a cryopod, a player will be injected with the same contents as medi-pens and space-pens,
   to help kickstart the worker's systems and protect them from potentially harmful workplace environments around
   the cryopod area. An animation will be played to show a cryopod coming from the floor, ejecting the player
   and disappearing again. This explains how the station can somehow accommodate such a large workforce.

### Spriting
1. Cryopods. Cryopods will be resprited to accommodate the cryopod changes.

## Game Design Rationale

### Seriously Silly
These changes allow a greater chance of meaningful roleplay interactions near the end of the round, by effectively
killing the mad dash to evac that every round currently suffers from and replacing it with a banquet/pizza part/celebration.
This provides a wonderful chance for players to wind down and roleplay, get a last chance to sow chaos, give out
medals and awards, or to simply roleplay out the consequences of what has transpired during the round.

### Maintaining Authenticity
This deepens the feeling of isolation the station is meant to evoke. There are no regularly scheduled shuttles going
to or from the station, and workers do not arrive to the station as they already live there in cryosleep.
The only time emergency evacuation is called is when there is an actual emergency present or the station's situation
has become genuinely untenable and must be abandoned.

### Dynamic Environment
The round ending in a less railroady fashion and the inclusion of round-end service events
inherently promotes more dynamic ends to rounds.
It keeps players invested up until the round end screen by keeping the focus where it
should always have been: ***the station***. The round ending no longer forcibly decouples players from the station,
but instead maintains focus on the most dynamic stage of the game and forces everyone to live with the consequences of
what has transpired during the round.

## Administrative & Server Rule Impact
1. Cryosleep areas may need to be ruled similarly to arrivals and evac, where intentional destruction is discouraged.
2. EORG would potentially no longer be a consideration on the evac shuttle itself, as it no longer exists and instead
   would only be a concern during the round-end timer (when the round end screen has popped up).

## Technical Considerations
1. Cryopods may need a refactor to accommodate the animation of exiting and entering a cryopod.
2. Requires the implementation of service events.
3. Requires the removal of the end-of-round evac shuttle.