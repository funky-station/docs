# Mage of Ascension

| Designers | Implemented | GitHub Links |
|---|---|---|
| Terkala | :x: No | |

## Overview

This proposal adds a new Mage of Ascension antagonist built around a Ley Line system and spell schools. Mages of Ascension start weak and grow into a nearly station-ending threat by opening confluences (ley-line confluences) to places of power. Spells are organized into schools (Necromancy, Elementalism, Honkamancy, Hemomancy, Dimensionalism, Chaosmancy), and progression is tied to confluence-opening and a mana system. This variant exists alongside the existing Wizard as a midround/event antagonist.

**Player goals:** The Mage's goal is to ascend to ultimate power. Once ascended, their goal is to show the station their power.

## Background

**Relevant code:** `Resources/Prototypes/Catalog/spellbook_catalog.yml`, `Content.Shared/Magic/SpellbookSystem.cs`, `Resources/Prototypes/Entities/Objects/Magic/books.yml` (WizardsGrimoire), `Content.Server/BloodCult/EntitySystems/BloodCultRiftSetupSystem.cs` (3x3 confluence reference), electrical anomaly spark behavior for mote travel.

## Features to be added

### 1. Ley Line & Confluence System

Confluences are ley-line confluences—points where ley lines converge, opening rifts to places of power.

**Spawn rules:**
- One confluence exists at round start.
- One new confluence spawns each time a confluence is pried open.
- Only one "new" (unopened) confluence exists at a time.
- Confluences spawn indoors, in areas with safe atmosphere (normal temperature, normal pressure).

**Visibility:**
- Unopened confluences are visible only to the mage.
- When a confluence is pried open, its sprite changes and it becomes visible to all players.

**Finding confluences:**
- Each confluence fires a mote of mana on its own timer (25–35 seconds, randomized to prevent syncing).
- **With only one open confluence:** The mote shoots from the unopened confluence toward the mage. The mage can trace the vague direction to find it.
- **With two or more open confluences:** Each confluence randomly shoots its mote toward either the mage or another confluence. The mage must either stay near a confluence to observe which direction the mote travels, or hope to get lucky. Mana motes travel through walls (similar to electrical anomaly sparks).

**Opening confluences:**
- The mage must have the spellbook out and open in one hand.
- The mage clicks the confluence with the open spellbook.
- Once pried open, the confluence's sprite updates and it becomes visible to everyone.

**Final confluence:**
- Special, more visible confluence.
- Occupies a 3x3 area (similar to blood cult final rune rift).
- Grants the capstone spell when opened.

### 2. Spell Schools

Six schools: Necromancy, Elementalism, Honkamancy, Hemomancy, Dimensionalism, Chaosmancy.

**Selection:**
- The mage chooses a school at round start via the Grimoire.
- This locks their spell path.
- After choosing, the path store transfers to the mage (similar to uplink implant).
- The Grimoire is then used to interact with confluences to drain them.

**Progression:**
- Each confluence opened: choose between two spells for that school.
- Spells improve by tier as more confluences are opened.
- Capstone spell: earned after opening the final confluence.

**School themes (high level):**
- **Necromancy:** Undead, death, resurrection. Capstone: transform into an immortal lich that reforms their body minutes after death.
- **Elementalism:** Ice/fire. Capstone: constant ice effect around the mage, replacing floors/walls with ice and freezing nearby players.
- **Honkamancy:** Clown/silly. Capstone: transform into a Clown Behemoth roughly as strong as a dragon.
- **Hemomancy:** Blood/vampiric.
- **Dimensionalism:** Teleportation, confluence manipulation.
- **Chaosmancy:** Customizable: random Effect + Delivery + Type per spell (e.g. Lightning + Bee + Verbal Long Chant; Verbal Long Chant reduces mana cost). At least 10 options per pool. Effects = damage types/themes (drain blood, heal, electric, fire, etc.). Delivery = touch, short range, long range, name (pick from list), etc.

### 3. Universal Blink

- All Mages of Ascension start with Blink.
- Instant long-range teleport.
- 30 second cooldown.
- Purpose: early escape when spotted.

### 4. Mana System

- **Max mana:** 100 base, +10 per confluence opened.
- **Regen:** 1/second base, +0.1/second per confluence opened.
- All spells use mana; no charge-based spells.
- Some spells are "maintained" and drain mana continuously while active.

**Balance:** Early mana limits sustained combat; late-game mana supports more sustained casting. Maintained spells need clear cost and duration.

## Game Design Rationale

- **Seriously Silly:** Honkamancy and Chaosmancy support absurd situations; other schools can still create memorable moments.
- **No Winning or Losing:** Progression is about power growth and spectacle, not strict win/loss.
- **Take Things Slow:** Confluence-opening and school choice create a 2–2.5 hour progression arc.
- **Maximizing Roleplay Potential:** School choice and confluence locations create distinct mage identities and stories.

## Roundflow & Player interaction

- **When it matters:** One confluence exists at round start; a new one spawns each time a confluence is pried open.
- **Finding confluences:** The mage uses mana mote pulses to trace direction. With one open confluence, motes point toward the unopened one; with two or more, motes randomly travel between confluences and the mage—the mage may need to stay near a confluence to observe direction or get lucky.
- **Opening confluences:** The mage holds open spellbook, clicks confluence to drain it.
- **Visibility:** Unopened confluences are mage-only; opened confluences are visible to all.
- **Enforcement:** Confluence visibility is enforced by the confluence system; spellbook-in-hand and open-spellbook checks gate confluence interaction.

## Administrative & Server Rule Impact

- Capstone spells (lich, ice aura, Clown Behemoth) are very strong; admins may need tools to monitor or intervene.
- Chaosmancy's randomness could produce unexpected outcomes; consider logging and admin visibility.
- Grief potential depends on capstone and school design; balance and rules should be reviewed.

## Technical Considerations

- **Performance:** Confluence visibility (mage-only vs. global) may need PVS or similar handling. Mana mote projectiles need to travel through walls.
- **Systems:** Ley line system, confluence spawning (indoor + safe atmosphere), mana system, school-locked store, Chaosmancy Effect/Delivery/Type composition, maintained-spell mana drain.
- **Reference:** Electrical anomaly spark behavior for mote travel through walls.
- **UI:** Store UI for school choice and spell selection; mana bar; confluence markers on navmap or HUD for the mage; open-spellbook state for confluence interaction.
- **Refactors:** Spellbook/Grimoire store logic, spell action structure (mana instead of charges), store transfer to mind (uplink implant pattern).
