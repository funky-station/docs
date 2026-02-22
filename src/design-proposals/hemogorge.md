# Round-Start Antag: The Hemogorge


| Designers | Implemented | GitHub Links |
|---|---|---|
| frostwight | :information_source: Open PR | TBD |

## Overview

This design proposal adds a new, stealth-focused, round-start antagonist called the Hemogorge. This antagonist is based on the classical vampire.

## Background

As the Changeling is set to be removed (perhaps pending a rework) [https://discord.com/channels/1276640157511979008/1276641732557013154/1469151886916452603],  I would like to propose an alternative to it, in the form of something less deadly, less powerful, and more dependent on stealth and deception. I personally have a great love for vampires and their contemporaries, and would love for them to be represented in some form within Funky Station. These points were the crux of my thought process when designing this doc.

## Features to be added

### Hemogorge Overview and Objectives
The Hemogorge is a round-start, solo antagonist, focused on feeding upon the blood of crew members. It is opt-in via the Antags menu, and you will spawn in as your chosen character in a non-mindshielded role on-station. 
Your first objective will be to drink a specific amount of blood, which must be done directly from its source using the "Bite" action. Only crew members can be fed on, which deems animals and other similar entities off-limits. Slime, Sap, Sugar-water(?), and Insect Blood, from each respective playable species, are all considered valid for this objective, so long as it's obtained with the "Bite" action. 
Your second objective will be to completely drain every drop of blood from 2 specific, randomly-chosen crew members, and ensure their blood is not returned to them. This objective will not be marked as Completed unless the cause of death was the "Bite" action. 
Your third objective is simple: Survive. This will be marked as failed if you are Dead at the time of round-end.

### Hemogorge Abilities and Resources
The Hemogorge will have abilities purchased from a shop menu (detailed below) that are added to the action hotbar when purchased (or in the case of the "Bite" action, is there by default). Each of these abilities (save for "Bite") will cost a varying amount of your Blood Gauge (working name, detailed further below). 

The "Bite" action must be used on a living target, unless the entity in question is one of your drain objectives, in which case they can be fed on with any status. This action has a brief, 2-second doafter, and when it is completed, the target will instantly lose 15% of their maximum blood and take 10 fixed puncture damage, as well as notify the target with "You feel your essence being drained." This action will also leave an additional descriptor on the entity's Health Examine window ("There are two small puncture wounds on their neck"). This action does NOT leave DNA on the victim. Similarly to eating and drinking normally, you must not have a mask or hardsuit helmet blocking your mouth to use this ability.

The Hemogorge will have a shop menu, similar to the Changeling, where they can purchase a limited amount of abilities. Let's call this the Hemostore for now. The Hemogorge will start the round with a fixed, limited amount of shop points, and cannot gain more, so the player must choose their tools wisely. Within the store are the following:
- Rat Form: Transform into a rat. Uses the same sprites as the Rat-King's servants. This form can be used for quick escapes or sneaking into rooms, as it has a relatively high movement speed and can slip under airlocks. You cannot communicate (all messages will be translated to squeaks), and taking any damage will revert this transformation. This ability can also be used to escape restraints such as handcuffs and bolas.
- Mist Form: Transform into a barely-visible mass of water vapor. This is mainly a B&E tool, and has a limited time-of-use (working: 20 seconds). Movement is slowed immensely, but you are able to slip through windows, grilles, wall frames, and other obstructions (not including airlocks and firelocks). You cannot take damage in this form, and you cannot attack, but if you are exposed to a spaced tile, this transformation will be reverted. This ability can also be used to escape restraints such as handcuffs and bolas.
- Claws: Sprout claw-like nails from the tips of your fingers, turning all of your unarmed attacks into claw-swipes, with damage comparable to the Captain's Sabre. This can be used to defend yourself, should you find that combat is your only way out of a sticky situation. Reuse ability to retract your claws.
- Charm: Mind control a target within Hug range. This ability is removed when used, and will cost your entire Blood Gauge. This ability sends a telepathic message into your target's brain that compels them to follow every order you give them. This ability is cast instantly, and has no visual indicator, so it can be done in the presence of others without alerting anybody. This ability does not work on mindshielded entities or cyborgs, but will still consume it when used on one, so it is important to choose your target wisely if you don't wish to waste your only charge of this ability. This effect will last until the affected entity's status changes to Dead, or they are injected with a mindshield, after which they may remember any action they took while charmed, but *NOT* who charmed them.
- Hemal Sense: This ability is a vision toggle, similar to Thermal or NV goggles. It will make your entire screen go black-and-white, highlighting living entities with a bright crimson aura. You can see these highlight auras through walls. If an entity is in critical condition or sleeping, their aura will gently pulse, indicating their vulnerability. This ability will passively drain the Blood Gauge at a low rate.
- Soporific Breath: Let out a gentle breath, forcing a high dosage of nitrous oxide into the lungs of a target in Hug range, putting them to sleep. When this ability is used, your character will automatically perform the "sigh" emote. This ability will have no effect on targets with breath masks, hardsuits/eva helmets, or gas masks.

The Hemogorge's abilities will all consume a varying amount of Blood Gauge points. The Blood Gauge will be visualized on the right side of the screen, under your Health indicator, and can be hovered over with the mouse to see the exact amount of points you currently have. 
This gauge does not passively refill, and must be refilled by using the "Bite" action, refilling the same percentage as was drained from the victim (15%). Any blood drank while at 100% Blood Gauge will not overfill the gauge. 
Additionally, the Hemogorge has ***very slow*** passive healing. Drinking blood with the "Bite" action will also heal.

### Other Changes
- The Changeling gamerule should be less common (if it were to remain), while the Hemogorge gamerule can be slightly more common than the current Changeling rate.
- A wooden stake will need to be created, then be added to the Chaplain's vending machine.
- An addendum to Space Law and Chaplain SOP, that prohibits the forced imbibing of Holy Water without clear and valid reason.

## Game Design Rationale

### Seriously Silly
The mere prospect of a space-vampire is already goofy in-and-of itself, and can open the door for some very silly roleplay. Perhaps a player would decide to put on the traditional "vampiric" (poor Romanion) accent when speaking to their charmed comrades, or drain targets. They're doing evil, heinous things to their crewmates, but are spiritually complete dorks. 
Imagine a situation in which a Hemogorge is discovered by security, and has to make an escape. They shapeshift into a rat to scurry away through maints, but make the mistake of stepping on one of the chef's mousetraps. Now they've exposed themself in front of the chef, who is *incredibly* confused, with security beating on the door on the other side. The Hemogorge knows they're screwed, but the situation is too silly to be bothered by.

### Maintaining Authenticity
Considering all of the other horrors and straight-up *magical* entities that exist in the SS14 universe, a space-vampire would fit right in. As I see it at the moment, Hemogorges are normal people that have been cursed by some kind of space magic, compelling them to feast on blood and granting them abilities to assist with the task. And as every playable species has some kind of blood running in their veins, it isn't at all farfetched to believe that something out there exists to *take* it.

### Roundflow & Player interaction
The Hemogorge is a round-start solo antagonist, starting the round in a similar vein to a thief, traitor, or changeling. This antagonist is metashielded by Corporate Secrets, meaning normal crew members do not know of its existence, though when witnessed, it would be reasonable to call them a "Vampire." Its revealing factor for Command is the puncture wounds left on the necks of the Hemogorge's victims. Command personnel can choose to brief Security on their existence at their reasonable discretion.

The proper course of action when dealing with a confirmed Hemogorge threat is to first identify who it is. If security detains a violent criminal after a Hemogorge is confirmed on-station, they can force-feed them holy water. If a Hemogorge drinks holy water, they will take minor burn damage and vomit blood. 

***Note: Holy Water force-feeds should be treated the exact same as forced Mindshield implants, and must not be given without very clear reason. A possible SOP and Space Law addendum may be required for clarity.***

The next step is to deal with the Hemogorge. This is when Security properly employs the help of the Chaplain. The Chaplain must dispense a Wooden Stake (will be added with this antagonist) from their clothing/accessories vendor and use it on the Hemogorge. After a medium-length doafter, the stake is driven into their body, the Hemogorge component is removed, and the Hemogorge is killed. 

The ex-Hemogorge MUST be revived afterwards (unless they become catatonic), as they are no longer a blood-drinking ghoul. If acquisition of the Chaplain's wooden stake is impossible by some means, Command may elect to engage in DNR methods regarding the ex-Hemogorge.


## Administrative & Server Rule Impact (if applicable)

- **Does this feature introduce any new rule enforcement challenges or additional workload for admins?**

This should be no more of a workload than current Traitor rule enforcement. The only singular complication is ensuring the Hemogorge players aren't needlessly killing people on the station who aren't their targets. This is not a murderbone antag (and I suspect the player would have a really hard time doing so anyways).
 
- **Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?**

Less so than Traitors, and doubly less so than Changelings. The Hemogorge is significantly underpowered and underequipped compared to the other two, so I doubt there would be much complaint, if any. 

- **How are the rules enforced mechanically by way the feature will be implemented?**

As iterated in the two points above, I feel the players in this role would find themselves to not be powerful enough to murderbone. 


## Technical Considerations
As this is an entirely new antagonist gamerule, coding, as well as minor spritework must be done for the UI and some abilities. 

Here is a mockup of how the UI will possibly look.

![Hemogorge UI Elements Mockup Image](https://raw.githubusercontent.com/funky-station/docs/c55c53806b290c4181fbb341853340debb3b0ded/src/assets/UI%20assets.png)