# Stage Based Treatment


| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

This design doc provides an over-view of what stage based healing in medical would look like. 
It does not seek to provide a true "status med" with limb damage, wound types, infections, ect. 
Instead it is designed to work within the existing mechanical framework to provide a more cohesive system that can be used in the shorter term with more depth.

## Background

Cyber-Med is lost, and there still is no true status-med document, so this document will not take them into account.

This Document will also not be considering the addition of "diseases".

This document is designed taking into account the push to lean into species having more negative unique points around them.

This document is also designed around the push for a more intensive and slower healing process.

## Features to be added

### "Treated" and passive healing (all roads lead to RMC)

Passive healing is entirely removed, replaced with the type of damage being "treated".
"Treated" wounds heal very slowly till the person is entirely cured.

As Vox-Boxes have become standard to be mapped in, even the vox's poison healing will be removed.

Only Bloodloss and Airloss will heal passively as they do now, being healed when the need is satisfied, they do however have a decreased base rate of healing.

### Applying "treated"

Topicals are the primary way of applying "treated" to a patient's wounds.
Ointment provides "treated" to heat and shock burns.
Gauze provides "treated" piercing and slashing.
Bruise packs are removed.
Showers provide "Treated" to radiation.

Healed through "Treated":
1. Heat
2. Shock
3. Piercing
4. Slashing
5. Radiation

Not healed through "Treated":
1. Bruise
2. Cold
3. Caustic
4. Poison
5. Genetic
6. Bloodloss
7. Aspyxiation

### Bedrest

Laying in a bed ("bedrest") provides passive healing to certain damage types that cannot be "treated".
The healing of "bedrest" healing is the same speed as being "treated".

Bloodloss and Airloss healing are increased by bedrest, including hastening blood regeneration.

Healed through "Bedrest":
1. Bruise
2. Cold
3. Poison
4. Blood levels
5. Bloodloss
6. Asphyxiation

Not healed through "Bedrest":
1. Heat
2. Shock
3. Piercing
4. Slashing
5. Caustic
6. Radiation
7. Genetic

### Pill chems

Pill chems are a sub-set of chemicals that have sub-1 OD limits, often closer to .5, and ingest slowly. 
They do, however, last an extended amount of time and alow the patient to continue to do their job and heal with 2-3 prescribed doses.
Given their light nature, they are also much more efficient on chem cost than standard chemical treatments.
They lose efficiency on patients above 25 in the given category.

In addition to these changes, pills will be capped at 1u per pill.

Chronic prescriptions (such as psicodone) are in this category.

It should be noted that moths cannot interact with Pill chems as they cannot ingest pills. They will have to add it to water or finish being treated within medical.

Healed through "Pill Chems":
1. Heat
2. Cold
3. Shock
4. Caustic
5. Bruise
6. Poison
7. Radiation

Not healed through "Pill Chems":
1. Piercing
2. Slashing
3. Genetic
4. Bloodloss
5. Asphyxiation

### IV chems

IV chems are similar to pill-chems, but with faster ingestion times, have the downside of severely increasing thirst and work best in the 150-25 damage range.
This encourages them to be mixed with Saline solutions in IV drips to counteract the loss of water.
They are approximately as efficient

Healed through "IV chems":
1. Heat
2. Cold
3. Shock
4. Caustic
5. Bruise
6. Piercing
7. Slashing
8. Poison
9. Radiation
10. Bloodloss
11. Asphyxiation

Not healed through "IV chems":
1. Genetic

#### Saline and Blood

Blood is no longer replenished by saline, though IVs can still be used to directly inject blood.
Medical will instead be encouraged to set up blood drives to replenish it's blood reserves as incidents happen, and use chems to keep the patient stable until their blood is replenished.

### Emergency Chems

"Emergancy Chems" are chems intended to work with syringe or single use injector based delivery systems.
They have higher ODs around 15, staying in the patient's system for an extended period of time, and will work best around 200-150 damage.
These chemicals are built to mostly stabilise patients, rapidly bringing their damage within acceptable ranges, and having airloss stabilisation.
These are also vastly more expensive as a chemical, requiring extensive work in chem to make.

Healed through "Emergancy Chems":
1. Heat
2. Cold
3. Shock
4. Caustic
5. Bruise
6. Piercing
7. Slashing
8. Poison
9. Radiation

Not healed through "Emergancy Chems":
1. Genetic

### Cryogenic Chems

Cryogenic chemicals heal a category of damage on the living or dead. 
The tube prevents rot while working, similar to stasis beds.
The chemicals are relatively expensive, being intended for use on "important" people (See your insurance provider to see if you are covered).
This is also where blood regenerating chems are, further speeding up treatment times.

Healed through "Cryogenic Chems":
1. Heat
2. Cold
3. Shock
4. Caustic
5. Bruise
6. Peircing
7. Slashing
8. Poison (Living)
9. Radiation (Living)
10. Bloodloss
11. Asphyxiation
12. Blood levels (Living)

Not healed through "Cryogenic Chems":
1. Genetic

### Pyrogenic Chems

Pyrogenics chemicals rapidly heal damage on living or dead patients.
Every chemical used in pyrogenics is vastly more expensive than other chemical treatments aside from Exotic chemicals, and tend to have side effects to their use.
This is also the only way to heal genetic damage, and the chem to heal it is comparatively cheaper than other pyrogenics as a result.
Pyrogenics are also generally a 2 stage process, as the heat of the fluids severely burns the patient inside.
After initial treatment, a secondary treatment of burn healing compounds is required that reacts negatively with other pyrogenic fluids if mixed.

Healed through "Pyrogenic Chems":

Every form of damage can be healed through "Pyrogenic Chems"

### Botanical Chemicals

Botanical chemicals are precursors to powerful chemicals such as Cryogenics, Pyrogenics, and Exotic chemicals.
On their own they have moderate-light healing effects that almost always come with side effects, and as such must be refined through chemical processing to become stronger.
Balanced varies depending on what type they are, but without refinement are stated to below the "pure chem" equivalent.

### Exotic chemicals

Exotic chemicals are vastly more expensive than any other chemical.
Generally requiring a level of pre-planning that extends past the shift itself, AKA chemsheets.
Requires a strictly limited chemical (EG 10u in the CMO's locker, or found by salvage/telescience).
Requires tie-in chems brought in from Botany and Atmospherics.

### Genetic damage

Genetic damage is to be altered slightly, to better fulfil the way its intended as a "meta punishment".
As such every minute genetic damage will increase by 10% of its current value until cured.
The only way to cure genetic damage is through the use of pyrogenics, which are costly and require after care.

### Antagonists

Most antagonists have a way of getting healing already, but chems may have to be made to specifically assist certain antagonists with longer term sustain such as nukies getting "interdyne chems" that upgrade from a standard chem type.

## Game Design Rationale

This is designed around keeping the flow of patients in medical at a slower pace than what it is currently, leaning more towards realism in time spent especially as we have multi hour rounds.
Through the use of different stages people are encouraged to come in when they are injured, rather than let fester and require stronger treatments.
Additionally the use of stages keeps the treatment process more interesting to medical personnel who now have to ensure the patient is receiving the correct treatment for their given damage type and health.

## Roundflow & Player interaction

This will mean patients are often in medical care for longer for more severe damages, but for lesser damages it may lead to shorter medical times through the application of "Pill Chems".
People will however have to more frequently visit medical for injuries with the removal of natural regeneration.

## Administrative & Server Rule Impact (if applicable)

This has very little impact on the rules, though it may require a higher level of competency/teaching from the CMO.

# Technical Considerations

The only things that would need to explicitly be programmed outside of YAML is "treated" versus "untreated".


