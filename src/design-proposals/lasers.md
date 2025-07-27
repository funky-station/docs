# Lasers and Armory Overhaul

| Designers | Implemented | GitHub Links |
|---|---|---|
| Miiish | :x: No | TBD |

## Overview

This design doc outlines the removal of current ballistic weapons in the armory in favor of safer, more retro, family-friendly weaponry designed to melt station-ending threats.

## Background

Ballistic weaponry from an in-universe common-sense/immersion perspective is not ideal whatsoever when bullets can break windows and space (very dangerous!!!) sections of the station, potentially killing crew if no protections are in place.

This design doc is made from the perspective of both allowing melee weapons to be more viable and to unify NanoTrasen standard weaponry in a way that makes more sense.

They are additionally the primary killing tools of the Syndicate (bad guys!!), and this works to differentiate NanoTrasen brand killing tools (good) and Syndicate brand evil killing tools (bad), as well as allow unique balancing around factional weaponry. Found bullet casings in maintenance? You probably can't blame that on a trigger-happy cadet anymore.

## Why this is Good for the Game

These changes all aim to serve a few purposes:

Aesthetics: Energy weapons are cool and retro sci-fi-y, and very distinguishable as opposed to having 5 generic Gun sprites.

Melee, especially unique antagonist melee such as the energy sword and armblade, should be more viable as a method of killing, as a high risk-reward profile. The overall increase of Time-To-Kill on ranged weaponry should aim to incentivize the use of more 'up close and personal' killings and encourage antagonists to take on Security more.

The splitting up of Sec lethals should also encourage Security to use their other tools, like truncheons, more for better damage profiles instead of using their gun as a metaphorical hammer for everything.

This also aims to bring Sec more 'back to Earth', so to speak. By lowering the amount of pure weaponry they have access to roundstart, we curb the constant Sec - Antag cat-and-mouse balancing game that leads to intense powercreep, and makes crew cooperation and interdepartmental play somewhat more useful in ending station-wide threats, such as the Blob. In short, this helps allow for antagonist abilities to be imposing without having to be overwhelmingly powerful or durable.

Ranged weapons, due to their inherent safety and power over using melee, should require a bit more tactical use and forethought than just pointing in a direction and killing whatever's there. Lasers allow for more of this planning through the use of, for example, constructing windows to prepare for a threat. The lowered amount of charges and damage-per-charge/magazine also requires more forethought when bringing them out. Why use a gun when I can relatively safely use melee here?

## Additions

### Temperature Gun
See https://github.com/space-wizards/space-station-14/pull/35447 for implementation. Main difference: this will be an Armory weapon and not researchable.

### Ion Rifle
A powerful three-shot rifle that deals 50 ion damage on a direct hit as well as a 3x3 tile weak EMP where it lands. Very powerful against cybernetic threats, such as borgs, IPCs, or mechs, but only tactically useful against other energy-weapon users.

### Energy Gun
A battery-powered carbine (can fit in the backpack) which can fire either disabling or laser bolts, with less charge than the base Laser Rifle. It has 15 charges.

### Miniature Energy Gun
The replacement for both the Officer's disabler and pistol, this is simply a smaller version of the Energy Gun. It can fit in your pocket and has 12 charges, which can be used to disable or laser.

Cadets will also start with this, but it will be locked on Disable until the childproof plastic lock is broken using a screwdriver.

## Changes to current Features / Gamestate

### Armory (Mapping)

The removal of all ballistic weaponry from the Armory, in favor of the new laser-based weaponry.

Kammerers should stay as they are explicitly very CQB weapons, as opposed to the longer-range, more reliable lasers.

The addition of a disabler safe to all armories for emergency Command-arming reasons.

The removal of the WT-550 from the Head of Security office.

The removal of disablers from Sec officer lockers.

Overall, Armory would now contain:
- 1 disabler safe (containing 5 disablers)
- 3 energy guns
- 3 laser rifles
- 3 Kammerers
- 1 ion rifle
- 1 temperature gun

**Note: Although the weekly rollouts can simply migrate weapon safes in the armory through migrations.yml, it would be best to have them also mapped out by their respective map's maintainers where possible.**

### Cargo

- The removal of the WT-550 SMG crate from Cargo.
- Replacing the Enforcer crate with the Kammerer crate.
- Replacing the smg and pistols crates with the Energy Gun and Miniature Energy Guns crates.

### Technical / Misc. Tweaks

- One unified Laser Projectile and one unified Disabler Projectile defined in Funkystation files.
- An overall increase in laser damage.
- The removal of self-recharging from the HoS' multiphase gun (why is it a better captain's laser?)
- The removal of self-recharging from the EG-4 energy revolver (Blueshield)
- Reduce the Warden's energy shotgun to 6 shots.
- The removal of the mk58 pistol and disabler from the Security Officer loadout for the miniature energy pistol.
- Changing all laser-based weaponry from hitscan to projectile, except for the retro laser blaster because it is funny.
- Remove ion damage from disabling bolts.
- Reduction of the total amount of disabler shots-per-charge.
- Reduce the reflective vest's deflect chance from 100% to 66%

### Possible (Future) Tweaks and Concerns

New Arsenal research paths for better energy / ballistic weaponry, printable by Sec to make up for the reduction in overall roundstart firepower.

Certain antag's heat resistances, most probably Nukeops and Dragons, will likely need to be tweaked down a significant margin.

Blob health might need tweaking as a result of the now mainly-heat-based armory.

## Game Design Rationale

### Seriously Silly

Laser guns are as dangerous as they are silly-looking and sounding and a staple of retro sci-fi. In short: they're flavorful and iconic, much more so than generic ballistic assault rifles.

### Maintaining Authenticity

In the future corporate hellscape that is Space Station 14, anachronistic current-day technology exists with futuristic-but-not-really tech. Fax machines exist in the same station as alien artifacts and extradimensional anomalies. Dinky laser guns just fit the environment of a space station much better than a gun that would fit in the hands of a Vietnam War-era soldier.

### Roundflow & Player Interaction

This should ideally encourage players in combat to fight in more up-and-personal ways, using more game mechanics while in combat. Slips, stuns, shoves, and antagonist abilities will have a chance to thrive when not every fight is a shootout.

# Technical Considerations

This is all possible to do with purely .yml and mapping changes. Coordination will be required from mapping maintainers for armory changes.

More input will be required from the maintainers, particularly concerning the specifics of numbers.
