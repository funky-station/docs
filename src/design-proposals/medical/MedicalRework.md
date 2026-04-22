# Reworked Medical System

| Designers | Implemented | GitHub Links |
|DocToast|:x:|TBD|

## Overview

Chemicals now have a much faster metabolism rate, to the point that using just 10-30u will only heal for few seconds before the chem dissapears. This forces Medical to use IV Drips to administer medicines that do not work via bolus, this making the healing require more effort. I am also proposing that we add various medical equipment that replaces some of the more abstract and "gamey" mechanics to make it more RP friendly and "realistic"
Currently, Medical is underdeveloped to the point that people come in there, get injected with 1-2 chems then just leave because they finished everything. Medical could be reduced to 2 rooms, one for patients to come in and one to make the chems. People getting injured should matter a lot more than it does now, including death. What I propose is mostly simple changes to what is about 80-90% of Medical's various systems, mostly YAML changes and some basic systems changes.

## Background

-Medical right now is very basic, it needs more complex systems to make it interesting for both the crew and the Medical staff.
-Healing is extremely simple, needing some form of chemical and maybe topicals to heal someone completely.
-Medical has little else to do if the round doesn't have that much activity going on.

## Features to be added

- A much faster metabolism rate to make "bolus" chemicals basically useless, except for combat meds and such. Combat meds should be a lot more difficult to make to compensate. Basic healing meds needs a consistent transfusion to make it effective, requiring more setup than a syringe and jugs.
- IV Drips, IV Cannulas, disposable one-time use syringes, disposable gloves, masks, etc. More disposable items that can't be reused, making Medical a trash-heavy and resource-heavy department that it actually is.
- Make making chemicals more involved then mixing and heating. More catalyzed reactions, cooling, distilling, multiple chemicals that heal the same damage but with different doses, metabolism rates and toxic doses, adverse drug reactions for some people (selectable as a trait) to emulate alternative drug selection.
- Making medical records a lot more important for healing minor, more RP focused medical conditions.

## Game Design Rationale

- Makes Medical a more intensive process, requiring the cooperation of multiple Medical personnel to heal people efficiently, or one person can handle it at a slower rate. No more "Brute / Burn mixes", no more jugs in bags, usage of patches, IV drips, etc. is a lot more important.
- Adding more chemicals that do the same job allows Medical doctors to specialize in particular fields if they so wish. One doctor could focus on "Bolus" only treatment, ignoring IV drips. They will be much slower than others, but can heal more people. Or they can go fully into IV drips, creating custom mixes that will heal the most efficiently for one particular mix of damage types.

## Roundflow & Player interaction

- Healing without any medical expertise or medical equipment becomes a lot harder. You can't just grab some gauze and brute packs and basically heal yourself with a time investment as good as proper medical care.
- More interactions with Medical is encouraged, especially when a round is combat or injury heavy.


## Administrative & Server Rule Impact (if applicable)

- It shouldn't create anymore admin or server impact than regular Medical does, but it will make healing in-combat more dangerous as the chemicals used will be much more valuable. Patches will be vital, maybe even field surgery if it ever becomes implemented to deal with more grevious injuries.

# Technical Considerations

- It will require recoding almost all the Medical chemicals to work with the "lower healing potential, faster metabolism, and lower OD dose", mainly the basic chems. Also more chems will need to be added to do the same damage type healing,with different doses, OD doses, healing rates, etc. Side effects can be expanded upon, making the chems more interesting.
- It might requite adding more types of damage other than Slash, Puncture, and Blunt. We could add organ damage as a damage type to reflect various organ injuries, thus requiring more specialized medications to heal.