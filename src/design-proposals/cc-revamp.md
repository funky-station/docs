# Central Command Revamp

| Designers | Implemented | GitHub Links |
|---|---|---|
| TheHolyAegis | :x: | https://github.com/funky-station/funky-station/pull/2733 |

## Overview

This proposal is about the idea to make Central Command like the ghost bar, or at least make it a space for dead people (or observers) to chat around and do something while they wait for the round to end.

## Background

Currently, there is a ghostbar. But that gets rarely used by anyone I have noticed.
And I have seen people talk about a Central Command revamp in [this PR](https://github.com/funky-station/funky-station/pull/2714).

I wanted to make a doc proposal out of it to summarize it and for people to talk in a space where it's about it, instead of a PR that is already merged.

## Features to be added

First off, the Central Command Intern. There are some minor tweaks it needs to get:

- They need to get their own stamp.
- They also need to get some OOC rules, due to it being able to overrule the NTR and Magistrate
- And they need to require playtime from both the NTR and the Magistrate. Around 30h each I was thinking, but could be tweaked. The reason being the same as the previous point.

When the Central Command Intern changes are made, there will be two of those roles available roundstart.

Roles that will be at Central Command, like some medics at the medical wing, and some engineers in the engineering wing.
Those will be ghost roles for players to pick from the ghost role menu, in the description of the ghost role it will clearly state it is on Central Command.

Or, it could be a separate menu that replaces the ghost bar button.

## Game Design Rationale

The current ghost bar gets rarely used. This proposal would put the idea of the ghost bar in a new light, that being the players who do not play (anymore) have something to do if their player body isn't recoverable or when observers want to do something.

For some people it can be infuriating to die from something stupid, and the already existing ghost bar isn't exactly popular. This would give people a place where they can RP without an antagonist interrupting the fun moment.

## Roundflow & Player interaction

After a player permanently dies, they might quit because of it. This would give players a place to RP while the actual round is still going on.

This wouldn't influence the round per se, except for the Central Command Intern roles that will be available. Or, an admin could decide to make them all visit the station as a minor ERT squad, if necessary. Just to give an idea of what could be possible.

## Administrative & Server Rule Impact

This might give admins a bit more workload, due to Central Command being a separate map.
Maybe small changes for the EORG rule need to be made, we wouldn't want players to destroy Central Command before the end of round.

Additionally, the Central Command Intern needs to get some ground rules, currently they kind of are a Central Command Official, but not an admin.

Every role available at Central Command then, will all have randomized characters. So people wouldn't know who is what unless they say something OOC to one another. (Unless it's okay if it can pick a player's character, this isn't final)

## Technical Considerations

This proposal uses mostly already existing systems and UI elements.
The ghost bar button might get removed, or that it will open a new UI that looks like the ghostroles menu, but displays roles available for at Central Command instead.

For performance, it might improve it a bit. If this feature gets added, the ghost bar would be unnecessary and that would be one less map to have active.