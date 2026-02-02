# Security Redux

| Designers | Implemented | GitHub Links |
|---|---|---|
| pirakaplant | :x: No | TBD |

## Overview

This is a proposal to remove all nonlethal options from security's arsenal. They will have (nerfed) truncheons as a "less-lethal" weapon instead of stun batons.

## Background

Unlike most other *Space Station 14* communities, Funky Station is being redesigned to incorporate **class conflict** as a major component of the narrative. This means that Command (and Central Command) are supposed to be **explicitly exploitative**, and the Security department serves as a means to enforce that status quo **through force**. Several features, such as [scrip](/scrip.md), [corporate secrets](/corporate-secrets.md), and [unions](/unions.md) have been designed and/or implemented based off of this direction.

One of the major issues with following this direction is that there is a **ludonarrative dissonance** in how Security players engage with criminal activity on-station. When every threat onboard the station can be dealt with *the Magic Gun That Harmlessly and Automatically Knocks People Over*, being a Security Officer feels less like being a corporate enforcer and more like being Steven Universe in a ballistic vest.

## Features to be added

- The stun baton, the disabler, and the disabler plus will be removed from the game.
- Security personnel will start with a truncheon in place of a stun baton.
- The truncheon will do less damage (probably about half or so). Its stamina damage will be unchanged.
- Truncheons will be able to be made roundstart, and will no longer be unlocked by the Riot Control (buff the knuckledusters or something to make it still worth it).
- HOP will get a different self-defence weapon, in the form of a cane that can launch people (specifics are outside the scope of this document).
- Characters with the Pacifism trait will not be able to roll Security jobs.

## Game Design Rationale

### Maintaing (Thematic) Authenticity

Security as it currently stands feels incredibly inauthentic as both part of the game's world and (corporate) police in general. (See "Background" above for more details.) With Funky, we're intentionally drawing parallels to real-life class conflict rather than shying away from it. Part of this involves reflecting how it feels to run counter to law enforcement. Even "less-lethal" methods that have been employed IRL against those deemed criminals (especially strikers and other protestors) not only hurt and maim, but kill with alarming frequency. By making Security draw blood to stop people fleeing arrests, we can emphasise the lengths that Nanotrasen, as a captialist organisation, is willing to go to enforce order.

### Maximizing Roleplay Potential

One thing that [corporate secrets](/corporate-secrets.md) achieved was that it makes crew suspicious of Security and Command during changeling rounds. ("Why are they going around and blood testing random people? Is that an extrajudicial execution? What the hell is going on?") It's a dynamic that's very good at encouraging authentic IC conflict. This change would emphasise that dynamic regardless of the gamemode, as it makes Security less of a "good guy" in a way that's both more common and more blatant.

### The Stunmeta

Getting rid of disablers would also pretty much kill the stunmeta. While truncheons can still stun, security officers will have to get in close to use them, and being truncheoned feels more authentic than being stunbatoned.

## Roundflow & Player interaction

These changes should encourage players to play Security more brutally than the department is typically played at the moment. Refusing arrest *hurts*, and running away can get you shot. This can lead to more escalation, which leads to more interesting and authentic roleplay. Crew might be side-eyeing Security over how their coworkers are treated, and even refuse to assist Security on other matters because of that. Not every round is going to have a revolution, but crew should see firsthand that Security are fair-weather friends at best.

## Administrative & Server Rule Impact (if applicable)

Security should neither be expected nor encouraged to be "good guys". They're corporate enforcers, and it should be emphasised to players that playing them as pacifistic Officer Friendlies is akin to playing a Nuclear Operative as a dude who just wants to hang out and play chess. Admins should be more lenient on Security concerning escalation in the context of arrests, since their "arrest toolkit" is a lot more harmful than it was previously. As alluded to in "Roundflow & Player interaction", shooting at people fleeing arrest would be an IC issue with this change.

That being said, the admins will have to draw a line on what is "too far" for a security officer. Security has a lot of power as a department, and an eye should be kept open towards players who abuse this power in a way that disrupts roleplay instead of aiding it.

# Technical Considerations

I'll have to add a system for locking off jobs based on selected traits, which shouldn't be too hard.
