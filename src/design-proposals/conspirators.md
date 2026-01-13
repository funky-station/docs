# Conspirators

| Designers | Implemented | GitHub Links |
|---|---|---|
| zergologist | :x: no | TBD |

## Overview

Adds in [Conspirators](https://wiki.ss13.co/Conspirator) to Funky, roleplay focused team antagonists ported from Goonstation 13. They are intended to bring a more RP-focused conflict into the shifts that they're present, either by infiltrating specific departments, attempting to convince the station of one inane thing, or by otherwise impacting the overall flow of the round in a silly yet disruptful way.

## Background

As Funkystation currently is, there is a significant lack of RP antagonists to tie into the roleplay that MRP implies. With the addition of pinktext, there are definitely more incentives for existing antagonists to RP and be creative with their objectives - thieves are especially subject to this - but there is a lack of antags where the focus is RP. Especially so for team antagonists.

Adding conspirators and a gamemode focused around them intends to adress this issue. While criticisms of Goon's conspirators seem to pin down a lack of tools, direction, and end reward for them, chances are that these issues may be reduced with the different server culture of Funky and SS14 as a whole.

## Features to be added

### Encoded Names and Identity Encryption

Maybe less of a conspirator specific thing but antags can get special encoded names that they can be called by/referred to, automatically highlighted. Used when a user's identity is encrypted, effectively masking their voice by replacing it with their encoded name.

#### Encryption on Non-Wncoded Entities

If an entity without the encoded name component speaks over an encrypted key, their message gets chopped up and their identity is hidden.

#### Encrypted Radios and Keys

Radios and headset keys can have a component added to them which makes it so that the people who speak over said radio have their identities anonymized/replaced with their encoded name.

#### Encrypted Headsets

Headsets can have a voice-encrypting component, making the wearer speak with their encoded name independent of where they speak. Does nothing to remove accents/voice affecting conditions.

#### Spawn-in Encoded Names

The system that actually assigns encoded names to a given entity, would need to work in several different ways - adding in an encoded name to an entity that doesn't have one, randomizes an entity's encoded name if they do, automatically adding the name and parts of it to the highlighted words. Also need to add in a way to compile a list of entities and their encoded names for conspirators to know what names their fellow conspirators are using. 

### Conspirators Themselves

Base conspirators would be a team antagonist with a shared objective per round, several tools to assist them in planning, and key vulnerabilities that ideally shouldn't be metagamed to make their lives a living hell.

#### Conspirators Gamemode

A dedicated conspirators game mode that places somewhere from four to seven conspirators on the station alongside various side antagonists. Spawns traitors alongside conspirators.

#### Conspirators as a Side Antagonist

Gives the station anywhere from three to five conspirators to perform their conspiracy alongside other antagonists.

#### Conspiracy Radio Channel

Conspirators start off with a special, hidden and encrypted key in their headset that can only be removed with wirecutters. This key occupies a special slot and doesn't contribute to their headset's normal key limits. Broadcasts over the same frequency as handheld radios.

#### Voice Encrypter

A device that can be worn in place of a normal headset, generally not an NT-sanctioned device and should be confiscated if possible. Has the voice encrypting component and can have keys inserted into it.

#### Objectives

Generally the objectives of any given conspirator group are moreso guides than anything else. They give a suggestion of what conspirators should strive to achieve, not requirements that should be met - the objectives don't have any tracking but which ones they were prompted with will be shown at the end of the round.

Initial list of objectives that conspirators will be given at random and allowed to choose from

 - Host an insane life-or-death quiz show and kidnap non-conspirators to serve as contestants.
 - Liberate all animal life on the station and ensure that they can live peaceful lives.
 - Turn command against each other for petty reasons.
 - Establish the station's first ever wresting championship.
 - Form a crime family within the station.
 - Dismantle the surveillance state.
 - Implement excessive bureaucratic measures within the station.
 - Fold in as much of the station as possible into the conspiracy.
 - Engage in a de-mindshielding campaign across the station.
 - Remove the distinction between individual departments.
 - Test the limits of NT's station-side prison systems.
 - Remind the crew of their own mortality by stockpiling as many of their organs as you can.
 - Pose as a team of undercover Nanotrasen inspectors and make an example out of anyone you deem incompetent or too competent at their job.
 - Make sure as many messages as possible sent across the station go through secure channels.
 - Establish a super cool and exclusive drug ring.
 - Convince or coerce the crew to abandon their duties and be lazy and/or strike.
 - Try to get as much of the conspiracy as possible into positions of command.
 - Completely remodel the entire station.
 - Enforce dietary restrictions upon the crew where they can only eat foods made with [ingredient].
 - Run a "vaccination" campaign where you try to inject as many crew members as possible with [reagent] to vaccinate them against a made-up disease.
 - Convince the crew to engage in self-destructive behaviors
 - Convince the crew to truly ground themselves.
 - Ensure that the station remains as quiet as possible.
 - Test the limits of the station's announcement systems.
 - Engage in a public smear campaign against the [department] department.
 - Repeatedly inconvenience the station's crew through minor ways.
 - Explore the "practical" applications of atmospherics.
 - Convince crew members to go to great lengths "for the greater good."
 - Convince the crew to join a made-up religion.
 - Splinter the crew into disjointed factions.
 - Convince the crew to leave their immediate future to random chance.
 - Become the personal advisors of command members.
 - Petition for increased silicon rights across the station.
 - Treat the station as a tourist destination and walk people through tours of the entire station.
 - Convince the crew that Central Command has forsaken them.
 - Press charges on crew members for crimes they may or may not have committed.
 - Deliberatly spread misinformation about a topic across the station.
 - Throw a large feast for the crew under commands' nose.
 - Appoint a random member of the crew as the leader of your conspiracy and do as they plan.
 - Extract a signature from as many members of the crew as possible.
 - Stow less-than-legal items across the station.
 - Entertain the crew with a grand performance.
 - Ensure efficiency across the station by imposing strict requirements and regulations upon the crew.

Plots may be broken up into several categories that will be selected from, giving the conspiracy a healthy selection of plots to choose from if they don't feel comfortable carrying out one or two of the options provided.

## Game Design Rationale

### Seriously Silly

Conspirators will act to perform inane yet sincere plots across the station, creating friction and distrust within the crew as they make the lives of the crew progressively more interesting.

### There is no Winning or Losing

The point of a conspiracy's plot being untracked means that the conspiracy can't exactly be told whether they win or lose. So long as they spice up a round, they're doing the role they are meant to play.

### Maintaining Authenticity

It makes little sense that there wouldn't be internal plots against Nanotrasen brewing especially considering the prevalence of other antagonists. Conspirators should ideally bring out some of that turmoil and distrust while muddying up the works of NT's operations.

### Take Things Slow

Conspirators should be working over the course of an entire round to carry out their plots, either slowly enveloping the station in their actions or building up to a breaking point where all hell breaks loose. Some conspiracies may decide to do things "legally" while others work in the shadows to exert their will.

### Maximising Roleplay Potential

As a roleplay focused antagonist, their actions are intended to create IC friction and tension across the station that, ideally, should involve more and more people as the round progresses. Conspirators are given a fairly open-ended approach to their objectives where, so long as they stay within the spirit of the conspiracy and properly escalate through their plots, they are allowed to pursue their plots through many means.

### Dynamic Environment

If implemented as side antagonists, conspirators have the ability to add a lot of dynanism to the round without necessarily needing to fully complete their plots. Conspirators could conspire with other antagonists, members of the crew, or even command to realize their plots. 

## Roundflow & Player interaction

Conspirators should develop their plots over the course of a shift, ideally not being able to fully realize it well before the shift is over.

With the escalation rules, crew members are allowed to play into the plots of a conspiracy without being hammered for "self-antagging" or anything like that. Conspirators are meant to a catalyst for further conflict in the shift, similar to unions.

In order to prevent metagaming the conspiracy, crew shouldn't be seeking out handheld radios early in the shift to either find and arrest conspirators before they do anything or try to intentionally join the conspiracy without knowledge of them existing.

## Administrative & Server Rule Impact (if applicable)

By being a new antagonist, conspirators will need to be moderated and explained for people to properly understand both how to play them and how to interact with them. Conspirators should be allowed to ahelp for more interesting conspiracies to follow if they decide that they want a harder challenge or want to officiate their silly yet unofficial conspiracy plan.

# Technical Considerations

- The encoded names and encrypted keys will need to be created and ideally implemented across more antagonists than just conspirators.
- The objectives of the conspiracy should be able to be viewed and altered by admins.