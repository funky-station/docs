# HUD Removal

| Designers | Implemented | GitHub Links |
|---|---|---|
| pirakaplant | :x: No | TBD |

## Overview

This is a proposal to remove all HUD eyewear from the game in favour of existing, non-HUD eyewear as appropriate.

## Background

Lately, there has been a lot of discussion concerning the direction we want to go in, both aesthetically and mechanically. Security glasses have been brought up in tech-level discussions in #lore as both something that does not fit our aesthetic and an example of QOL slop that actively prevents interestin situations from occuring.

When writing this document, I took a look at the other HUDs, and realised that none of them actually justify their own existence either (see Game Design Rationale).

## Features to be added (well, mostly removed)

- The security glasses and its variants will be removed from the game.
- The medical HUD and its variants will be removed from the game.
- The diagnostic HUD and its variants will be removed from the game
- The administrative glasses and its variants will be removed from the game.
- The beer goggles will be removed from the game.

Instead:

- Jobs that had security or administative glasses instead get sun glasses (except HOP since their version didn't have flash protection to begin with).
- The "table sliding" ability of the beer goggles would instead be relegated to "bartender gloves" or something similar.
- Sunjar glasses will be an option to aesthetically replace the security jamjar glasses (and also provide more options to the captain and other jobs which had admin glasses).

## Game Design Rationale

### Aesthetic Consistency

The art and lore teams are trying to establish a more consistent tech level (1980s cassette futurism) across the board, and I believe our design should take that into consideration. When it comes to digital interfaces in the game, they should either be attached to a large, immobile mainframe (such as consoles) or relatively simple in function and implementation.

While heads-up-displays *as a technology* definitely existed in the time period we are drawing from, it was mostly limited to aircraft cockpits, with head-mounted HUDs being cumbersome and experimental. Of course, this is a science fiction setting where artistic liberties are taken with future technology, but Google-Glass-style eyewear does not fit in with the style of tech we envision the crew using.

### Maximizing Roleplay Potential (Avoid QOL slop)

Almost all HUD eyewear is inherently QOL slop.

Security HUDs exist to save a security officer from spending a single second checking someone's ID. This stifles any opportunity for subterfuge that doesn't involve either taking someone else's ID or using an agent ID. If we removed them, anyone with a reason to be deceptive about their job or position has the chance to sneak past inattentive officers, instead of being busted by a superfluous UI element. Security officers can ask to see someone's ID if they're out of range, which is a more interesting interaction than  instantly knowing.

Medical HUDs show a literal video game health bar as we design a medical system divorced from hit points and damage numbers. Even in terms of Forky's current medical system, the medical HUD has zero reason to exist. Every job that has a medical HUD also has a health analyser, so you can just scan someone to get the exact numbers.

Administrative HUDs have the same problem as security HUDs, and diagnostic HUDs have the same problem as medical HUDs.

## Roundflow & Player interaction

I anticipate that the removal of the security and administrator HUDs will give room to "hiding in plain sight" tactics when evading Security, such as entering a crowd or dressing up as someone meant to be there. It'll also necessitate authentic interaction between Security and other characters when it comes to ID. ("Stop so I can see your card.")

I anticipate that the removal of the medical and diagnostic HUDs will lead to Medical personnel (and the Roboticist with borgs) doing a quick shift-click and getting a more flavourful description of the damage to comment on in-character than just a health bar.

## Administrative & Server Rule Impact (if applicable)

Not applicable.

# Technical Considerations

This PR would only require YAML changes.