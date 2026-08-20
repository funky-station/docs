# Blood Cult Redesign

| Designers | Implemented | GitHub Links |
|---|---|---|
| Terkala | :Partial: | [TBD](https://github.com/Terkala/Fern-Station/tree/Bloodcult_rework) |

## Overview

Redesign Blood Cult so it's more about the blood, and so less round-removals happen as a result.

One of the guiding principles about this is to have the Blood Cult follow a sort of "narrative flow" during the round. At first the cult is weak, and not able to do as much, but also able to be stealthy. As the cult progresses through the stages, they get more powerful (able to break mindshields), but it makes them more obvious.

Balance wise it's intended for Chaplains and holy water to shut the cult down and for this to be something the crew knows about. So this antagonist isn't designed around any form of metashield protecting who/what they are. As a tradeoff the cult is much more powerful in this incarnation (more able to convert people, better able to convert even security and command). So both sides of the conflict have buffs.

It's also intended that this antagonist type is not meant to target command members. Unlike most team antagonists, a blood cult doesn't care if they convert a captain or a tider, it's all blood to be spilled either way.

## Background

Blood Cult currently has great themeing as a unique antagonist. But it has some large flaws when it comes to how it handles mindshielded people (gibbing them and making them mute soulstones).
And it doesn't splash blood everywhere. Sure, people are drawing runes and bleeding, but when I think of a hideout for a blood cult, there should be oceans of blood on the ground.


# Features Kept Intact

Rather than talk about what features were added/changed, I'll start with what features are the same.

## Spells
Spells work the same as current bloodcult spells.
Except for the Twisted Construction spell.

## Runes
Offering behavior is significantly different under the hood, but still works as the general "convert people to your side" rune.
Revive Rune allows you to revive anything that's dead, at the cost of removing all the blood from them and reviving them directly to a critical state (and likely to die if not offered to Nar'Sie, due to the lack of blood).
Also the Revive rune costs significant health from the user, to pay for this reviving, in the form of bleeding.

## Pylons
Cult Pylons (that heal people) now get 25% stronger at phase 2, and 50% stronger at phase 3. To encourage the cult to use them more.

## Soulstones
Soul stones still exist. But are reserved for IPCs (who make no sense as blood cultists), Borg Brains (giving a way for the cult to interact and convert borgs), and actual brains (giving them a way to revive gibbed people, sorta). This is coded as "anything that can't bleed is sacrificed", so it should handle all future cases of species being implemented that don't have the capacity to bleed. 
The soulstone system is different now, it hurts the user of the soulstone when they activate it, but it releases the soul as a shade to help the cult fight, with no distance limit. And when the shade dies they return to the stone.
Stones are inert, can't move or interact, but can talk. And they are still used to make Juggernauts, so an IPC/Borg can be crit, sacrificed, have their respective brain types turn into a soulshard, and be placed into a Juggernaut.

# Feature removed 

No more targeting of one player for the cult to sacrifice. Nar'Sie doesn't care about specific sacrifices, only about spilling blood.

# Features added

## Juggernauts

Juggernauts are more durable, and able to drag, and able to repeat Nar'Sie related phrases. Their speech is replaced with set lines, to keep it thematic and stop them from breaking character.
They go crit at slightly above normal health, to make up for the slow speed. But most importantly, they can be healed by being splashed with blood. Similar to skeletons with milk.
I still need to test if it's overpowered that unholy blood works for this purpose, since there will be quite a lot of it around. 
The idea is that a player could scoop up a lot of blood, toss it on the juggernaut over and over to heal it. Time-to-repair wise it should be about 1/3rd the speed of welding a borg (so they have to splash it a lot), so I'll have to tweak and experiment here.

## New Cult Objective

Nar'Sie should be about blood, first and foremost. Sacrifice of people, sure, but that's more of a means to an end.
So to get there, I removed the objective making you track down a specific person. This had a whole host of issues (how to find this person, how to isolate them, what to do if they just run away), and this sidesteps that issue by removing it.
So instead the cultists have to collect and offer a certain amount of blood. But the game needs a way to track the offered blood, and make sure people can't offer the same blood twice.

### Unholy Blood
Unholy Blood is a new reagent. Offering blood to Nar'Sie corrupts it and turns it into unholy blood, and spills it on the ground. Also all cultists bleed unholy blood.
The reason cultists bleed unholy blood is so they can't offer "their own blood" to Nar'Sie. They'll have to offer someone else's.
Unholy Blood also reacts with Holy Water. Because it really should. And I was thinking about what should the blood turn into. It should be something negative for the cult, because I want the RP of "priest throws bucket of holy water at the cult" to be a really effective strategy.
So I made it react with holy water to form Zauker. Zauker really has next-to-no lore in game, and is a deadly airborn poison. So having it created ontop of them is going to be quite bad for the cult. 

## Blood Cult Progression

Ramping up the threat is part of the theme. For this I decided it should be a certain amount of blood offered for each stage. I'll have to test how well this works in practice.
Each person offered to Nar'Sie gives a certain amount of Blood sacrifice, in addition to actual containers filled with blood or blood spilled on the offering rune space itself. This counter also increments when blood cultists drink blood. Which heals them, and induces vomiting. They vomit up Unholy Blood when they do, so it's impossible to get double value out of it.

## Holy Water Interactions

Holy water now reacts with Unholy Blood to create a smoke cloud that damages only cultists. So throwing holy water at a cultist (who is likely to be in an area with a lot of spilled blood, due to all of the cult mechanics around bleeding) is incredibly effective.

## Machines

### Features that might be designed later



### Suggestions

## Game Design Rationale


### Seriously Silly
Making borgs into soulgems, comically large amounts of blood

### Maintaining Authenticity
Building objects takes resources, they have to actually gather everything from the world. Everything they do is either created "from their blood" or directly from materials.
Nothing pops into existance unrealistically.

### Dynamic Environment + There is no Winning or Losing

## Roundflow & Player interaction

### Roundflow


### Player interaction

## Administrative & Server Rule Impact

## Technical Considerations

If do my job correctly I don't expect any performance impact, there could be issues with entity spam but I'm planning on profiling the code and improving the current performance. There's been plenty of arguments on improving the botany code and switching to more of an ECS design pattern but I'm planning on working on content first and foremost rather then getting bogged down in making a perfect system and the code is workable for the most part, I'll look into it further down the development pipeline.

I'll develop a mockup for this UI if the proposal is received well and I'd require help spriting for this project since I'm horrific at drawing.
