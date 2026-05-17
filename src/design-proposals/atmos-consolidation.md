# [FORKY] Atmospheric Consolidation

| Designers | Implemented | GitHub Links |
|---|---|---|
| pirakaplant, yaraaray | :x: No | TBD |

## Overview

This document outlines the implementation and justification for removing the Atmospheric Technician job from [the Forky codebase](https://github.com/funky-station/forky-station), as well as several auxiliary changes intended to complement this removal.

## Background

In early January, 2026, funky-station/funky-station#2500 was merged. As the name implies, it removed the Atmospheric Technician job wholly from the game, and consolidated its titles, responsibilities, and equipment into the Station Engineer job. While this change was initially met with concern from various angles, it has provided various benefits to engineering gameplay from multiple angles with very few drawbacks (addressed in "Game Design Rationale" below).

Tay has requested that a complete design document to be made to outline how this change would be enacted on Forky. This is that document.

## Features to be added/changed/removed

### Atmospheric Technician

The Atmospheric Technician job will be removed in its entirety. Its job titles (including "Atmospheric Technician"), responsibilities, and most of its equipment are added to the Station Engineer job instead. Atmospheric job positions and spawns on maps will be replaced with Station Engineer equivalents. SOP, the guidebook, loading screen tips, and most flavour text will be removed and/or amended to account for this.

Chief Engineer will now require 25 hours in the Engineering department to unlock instead of its prior requirements.

### Atmospheric Equipment

Most atmospheric equipment formerly restricted to Atmospheric Technicians will be renamed and/or moved around to make them more general engineering items (for example, atmospheric gas masks will just become engineering gas masks, and will be found in engineer lockers instead of atmospheric lockers). Atmospheric technician lockers will be replaced with "atmospheric equipment lockers", which feature equipment specific to atmospheric work (such as holofans and firesuits).

Atmospheric-unique clothes can simply be removed, as they are merely palette swaps of existing Engineering clothing. The same goes for AtmosDrobes and Atmospheric Wardrobes. "Fluff" items like plushies and figurines of atmospheric technicians will also be removed and/or renamed on a case-by-case basis. Atmospheric hardsuits will be removed in favour of the Montag XACU (see below).

### Montag XACU

The Montag XACU (eXtreme Atmospheric Conditions Unit) is a mech created for extreme atmospheric conditions and is, visually, to a firetruck what the Ripley APLU is to a forklift (except more of an engineering orange). Each atmospherics bay starts with one mapped in.

The Montag is extremely resistant to both pressure and extreme temperatures. It can have compressed matter and air grenades inserted into it for use with its modules (see below). It also has a big toggleable siren that flashes and makes a cool firetruck noise.

It has two modules, both of which are installed in the mapped-in Montag:
- **RXD Construction System:** Features both an RCD and an RPD.
- **Atmospheric Hazard Equipment:** Features a high-capacity fire extinguisher, an air grenade launcher, and a unique jaws of life that can pry hull tiles.

The "Ripley APLU" R&D technology will be renamed to "Industrial Exosuits", and unlock the parts for constructing both more Montags and their modules in addition to its current unlocks.

### Infrastructure Access

Atmospherics access will be removed and replaced with Infrastructure access. Infrastructure is required to access the atmospherics bay, engines, and similar secure areas vital for the station's ability to operate. Distrustful Chief Engineers who want to quietly keep comfirmed moles or grossly incompetent personnel away from these aspects of the station, while still giving them access to the equipment to make repairs, can simply take away the engineer's Infrastructure access. This additionally leaves room for jobs relating to station maintenence but *not* the upkeep of engines or air distribution to be created for the Engineering department (such as a separate Mechanic job focused on keeping computers and other machines in good condition).

Any job (that currently exists) that has access to Engineering will have access to Infrastructure.

### Mapping Conventions

Ideally, maps would also be amended to account for these changes. In addition to unmapping deprecated items and features:
- Atmospherics as a subdepartment should be de-emphasised visually. "Atmospheric cyan" trimming, as well as separate front desks, locker areas, etc. should be reduced and/or remapped as appropriate, at least from an external perspective. Cyan trimming is still suitable for internal organisation regarding the atmos bay proper.
- The atmospherics bay should be extended where appropriate to account for a larger amount of engineers working there.

## Game Design Rationale

Unlike most other features that necessitate a design document, we have an existing environment where the bulk of these proposed changes have already been enacted. This allows us to analyse the merits of removing Atmospheric Technician objectively.

### Engineering Design

Prior to the changes enacted on the Funky codebase, there were several issues that made Atmospheric Technician a particularly problematic job.

First of all, most of Station Engineer's domain *required* Atmospheric Technicians to participate in some capacity. For example:
- Station Engineer is expected to set up engines, but half of the engines in the game require atmospherics mechanics of some kind (nuclear, supermatter, TEG, although the last one is becoming deprecated for the most part).
- Station Engineer is expected to fix structural damage to the station, but most structural damage to the station also spaces the station, and only Atmospheric Technicians have the access (air alarms) and equipment (holofans) to fix spacing.

This lead to Atmospheric Technicians just doing what's supposed to the Station Engineers' job most of the time, which reduced the latter's job to setting up the AME, setting up the singulo, and just waiting around on the off chance there was structural damage that somehow didn't space any rooms.

Second of all, Atmospheric Technician being its own job with its own access made atmospheric mechanics incredibly difficult to teach. The game essentially treated it as a step above Station Engineers, requiring Station Engineer playtime to play, but no part of playing a Station Engineer at the time prepared players for working with gases and pipes. To a new engineering player, Atmospheric Technician is a job that's entirely closed off from the rest of the department until you unlock it, at which point you are implicitly expected to know all its previously gatekept mechanics in order to set up distro and the Supermatter in a timely manner.

These issues lead to the job not only being Station Engineer+, but also being the only job that could do Station Engineer's job reliably. Removing Atmospheric Technician fixed all those problems on the Funky codebase, and it will fix them on the Forky codebase too.

### Artistic / Thematic Cohesion

Forky Station gives us the opportunity of a (relatively) blank slate to shape the game into a more cohesive, polished version of our ideas without prior baggage in terms of bloat features and content. If we remove Atmospheric Technician like we did on our original codebase, keeping a bunch of content in the game that represents and compliments a job that no longer exists feels sloppy, like it's an oversight. Some people might argue that since Atmospheric Technician is still a Station Engineer job title, it still merits the recognition it currently has in the game. However, almost none of this recognition is afforded to the other titles, and even if we were to represent these titles through bespoke outfits, figures, and plushies, then the amount of hyperspecific engineering fluff would be disproportionate to the other departments in the game. Of course, we could account for all other departments then, but then we're faced with the choice between adding a million different weh plushies or just removing one.

It's also worth mentioning that unlike some other job specifications, such as Courier and Shuttle Pilot for Cargo Technician, Atmospheric Technician has zero distinct visual identity to its name (except maybe the firefighter aspect, but firefighters still wear plain jumpsuits under their nomex tunics). If you look at their unique jumpsuits and bags, they are literally just palette-swapped versions of existing Engineering clothing.

### Maximizing Roleplay Potential (Avoid QOL slop)

Atmospheric Technician was a job that, when not going out and doing Station Engineer work that was mechanically shoehorned into their design, stayed in the atmospherics bay for the whole round and barely interacted with anyone else outside of Atmospherics, let alone outside of their department. While there are a few other "stay in your office" jobs (namely Warden and Chemist), those jobs have a much greater degree of interaction with their department than Atmospheric Technician did with Engineering. Even outside of their department, the Warden has to process prisoners and suspects from across the station, and the Chemists, at the very least, have to interact with the Botanists regularly.

The Montag exists as a replacement to atmospheric hardsuits because atmos hardsuits just being "engineering hardsuits but better in almost every relevant aspect" feels kind of like QOL slop. With radiation, your best option in most cases is to wear a highly specialised suit that doesn't work that well against other conditions like spacing, high pressure, and such. In the same vein, having a big mech that's really good at firefighting or working with highly pressurised gas, but is inconvenient in most other use cases (given that mechs are bulky and slow) is a more interesting way of dealing with those conditions than just the Better Engineering Hardsuit.

## Roundflow & Player interaction

These changes would make atmospheric mechanics part of engineering's "curriculum". The basics of pipes, gases, and air systems would be taught to Technical Assistants alongside engine setup and construction.

Optional atmospheric work (such as mixing gasses for selling, setting up the HFR, setting up superfluous atmospheric engines for PTP money, etc.) would serve as passive gameplay for all engineers between engine upkeep and structural maintenence, not just a subset of them.

The removal of atmospheric hardsuits and the addition of the Montag XACU would result in extreme pressure hazards being something that has to be actively planned around rather than just being ignored by wearing the Better Engineering Hardsuit that the person dealing with it was probably already wearing. If there's a particularly large hazard area that requires multiple engineers working on it, one of them will have to use the Montag's equipment to make the area safe for engineering hardsuit use first, and then further assist as needed.

## Administrative & Server Rule Impact

When this feature was implemented on the Funky codebase, there were concerns that these changes would drastically increase the collateral damage caused by both intentional griefing and mistakes on the part of Technical Assistants. However, these possible issues have not actually revealed themselves in practice.

# Technical Considerations

The only thing that would need new code is inserting compressed matter and air grenades into the Montag XACU. Everything else would just need changes to YAML, XML, and FTL.