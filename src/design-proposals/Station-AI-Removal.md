# Station AI removal

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |


## Overview

This PR advocates for AI removal, and challanges those who wish to keep it to argue as if it wasnt already in the game, nor in space station 13.

## Background

The AI is the thing you ask to open doors, and occasionaly shocks you to death for not having an ID

https://discord.com/channels/1276640157511979008/1277475061909159969/1488848862184476695

## Features to be removed

Station AI

## Game Design Rationale

1. Station AI in its current iteration does not satisfy funky's design philosophy, and would not be added were it not inherited already. (The atmos-tech argument)
It was only made on wiz because it was in space station 13, and we inherited it because it was the cool new thing

2. Station station AI is a glorified tool to open/close/bolt/AA doors, along with doing various menial tasks such as editing air alarms. 
This bypasses the existing job system we have implimented in the game, reducing RP for the sake of conveniance.

3. Station AI gameplay loop is neither interesting, nor does it promote funky's design principles. 
You are to stare at the station through cameras/monitors until such a time that you get bored and do something, or someone orders you to do something. 
Sometimes you repair things, or order things to be reparied, which is engineering's job
Sometimes you hunt people for commiting crimes which is security's job
Sometimes you call out injured/dead crew which is medical's job
Sometimes you replace lights which is the janitor's job
Sometimes you help antagonists and have to find the fine line to tread from rulebreaking

4. Station AI has been buggy since its initial implimentation on wizden, including the ability to access things in fog of war, other grids, or things you shouldnt have access to.
After investigation on funky, it was found that these bugs are innate to the way the AI is coded to work and would require an indepth rework to fix.

5. Station AI creates a frequent conflict in the metashield.
The station AI has to determine every round if what it is seeing is something that would concern it enough to inform others, which it more often than not does due to it not having much else to do.
The Station AI frequently causes CTM material to be "leaked" with no reprocusions on either end due to the frequency it happens on command coms, lessening the impact of command coms being stolen, and what CTM leaks mean.

## Roundflow & Player interaction

Consider addressing:
This will slow down round pacing

## Administrative & Server Rule Impact (if applicable)

It will reduce admin load and rule complexity
