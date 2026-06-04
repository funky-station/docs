# HUD Removal (& the Panopticon Helmet)

| Designers | Implemented | GitHub Links |
|---|---|---|
| pirakaplant | :x: No | TBD |

## Overview

This is a proposal to remove all HUD eyewear from the game in favour of existing, non-HUD eyewear as appropriate. Warden will get a helmet that helps them surveil the brig instead, for gameplay and aesthetic reasons.

## Background

Lately, there has been a lot of discussion concerning the direction we want to go in, both aesthetically and mechanically. Security glasses have been brought up in tech-level discussions in #lore as both something that does not fit our aesthetic and an example of QOL slop that negatively impacts roleplay.

When writing this document, I took a look at the other HUDs, and realised that none of them actually justify their own existence either (see Game Design Rationale).

## Features to be added (well, mostly removed)

- The security glasses and its variants will be removed from the game.
- The medical HUD and its variants will be removed from the game.
- The diagnostic HUD and its variants will be removed from the game
- The administrative glasses and its variants will be removed from the game.
- The beer goggles will be removed from the game.
- The fake mindshield implant will be removed from the game (as it's no longer really needed, nobody will be able to see mindshields anymore).

Instead:

- Jobs that had security or administative glasses instead get sun glasses (except HOP since their version didn't have flash protection to begin with).
- The Warden will recieve a panopticon helmet (see below).
- The "table sliding" ability of the beer goggles would instead be relegated to "bartender gloves" or something similar.
- Sunjar glasses will be an option to aesthetically replace the security jamjar glasses (and also provide more options to the captain and other jobs which had admin glasses).

### Panopticon Helm

A bulky, white helmet with an opaque, adjustable visor that covers the eyes. A lopsided radio antenna sticks out the top. An icon of an eye is stencilled onto the front.

The panopticon helm can be found in the Warden's locker. It can be worn in the helmet slot. It slows the wearer down slightly and provide mild protection from brute damage.

As long as the eyewear slot is free, the wearer can lower a viewport over their eyes to tap into the Security department's cameras (either through the context menu or the action bar, like a hardsuit's helmet). This provides flash protection and security HUD vision (minus mindshield status). It also removes line-of-sight, but only renders tiles viewable by Security's cameranet, showing everything else in static (like the Station AI's view). Getting EMP'd will also cover the visor's vision in static for a short while.

## Game Design Rationale

### Aesthetic Consistency

The art and lore teams are trying to establish a more consistent tech level (1980s cassette futurism) across the board, and I believe our design should take that into consideration. When it comes to digital interfaces in the game, they should either be attached to a large, immobile mainframe (such as consoles) or relatively simple in function and implementation.

While heads-up-displays *as a technology* definitely existed in the time period we are drawing from, it was mostly limited to aircraft cockpits, with head-mounted HUDs being cumbersome and experimental (hence the design of the panopticon helm). Of course, this is a science fiction setting where artistic liberties are taken with future technology, but Google-Glass-style eyewear does not fit in with the style of tech we envision the crew using.

### Maximizing Roleplay Potential (Avoid QOL slop)

Almost all HUD eyewear is inherently QOL slop.

Security HUDs exist to save a security officer from spending a single second checking someone's ID. This stifles any opportunity for subterfuge that doesn't involve either taking someone else's ID or using an agent ID. If we removed them, anyone with a reason to be deceptive about their job or position has the chance to sneak past inattentive officers, instead of being busted by a superfluous UI element. Security officers can ask to see someone's ID if they're out of range, which is more interesting roleplay than just instantly knowing.

Medical HUDs show a literal video game health bar as we design a medical system divorced from hit points and damage numbers. Even in terms of Shitmed (our current medical system), the medical HUD has zero reason to exist. Every job that has a medical HUD also has a health analyser and/or MedTek installed on their PDA, so you can just scan someone to get the exact numbers.

Although Nuclear Operative Agents rely on their medical HUD heavily, they really don't need to. The three main damage types they're dealing with (burn, piercing, bloodloss) are easily observable through shift-clicking.

Administrative HUDs have the same problem as security HUDs, and diagnostic HUDs have the same problem as medical HUDs.

### Why the Warden Gets a HUD

My initial concept that I had as I started writing this did not give the Warden anything special. However, discussion touched on the fact that the Warden was more reliant on the security HUD than other members of security, as it indicates which characters are prisoners. It would have been possible to just given the warden security or admin glasses, but I felt like this would not fit the aesthetic style we are curating for the game (see "Aesthetic Consistency" above).

The panopticon helm is a reimagining of the kind of equipment the Warden would get to maintain a prison, keeping big and bulky retrotech in mind. It provides the HUD functionality needed to keep the Warden's duties at an acceptable difficulty, but also ties them further into the archetype of being a dystopian sci-fi prison warden by literally making them a part of the digital surveillance system.

## Roundflow & Player interaction

I anticipate that the removal of the security and administrator HUDs will give room to "hiding in plain sight" tactics when evading Security, such as entering a crowd or dressing up as someone meant to be there. It'll also necessitate authentic interaction between Security and other characters when it comes to ID. ("Stop so I can see your card.")

I anticipate that the removal of the medical and diagnostic HUDs will lead to Medical personnel (and the Roboticist with borgs) doing a quick shift-click and getting a more flavourful description of the damage to comment on in-character than just a health bar.

I anticipate that the addition of the panopticon helm will make leaving the brig a more conscious choice for the Warden. It wouldn't bar them from leaving entirely (which is something we don't want to encourage anyway), but them actively having to take their helmet off to go have a drink is going to cut down on unnecessary Wardloosing.

## Administrative & Server Rule Impact (if applicable)

Not applicable.

# Technical Considerations

The panopticon helmet would require changes to the `StationAiOverlaySystem` to provide an option for rendering its "camera-watching" effect.

Besides that, this PR would only require YAML changes.