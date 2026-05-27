# Galph Species

| Designers | Implemented | GitHub Links |
|---|---|---|
| dusty-plant, battlecruiser12, moxie, scrambleking | :x: No | TBD |

## Overview
Galphzzzeb (singular is Galph) are a new species who can be described as trunked bug-eyed floaty sea slug-skinned seals whose main feature is a semi-autonomous trunk slot.

## Background
Funky is in need of more quirky species that add to the depth of the game in more than aesthetics. Galphzzzeb are a new species that does not follow conventional design and attempts to feel closer to the "truly alien",
 adding a lot of mechanics that make playing them a truly unique experience.
Galphzzzeb come from a gas planet with a heavy atmosphere. They originated from a species of flower-eating grazers known as proto-Galph that would jump between floating moss islands using their gassy stomachs as buoyancy.
Proto-Galph would graze on moss flowers for days on end, using the large degree of vision afforded by their large bulging eyes to avoid predators.
Proto-Galph were a highly social species that would communicate using toots and snores in order to warn each other or advertise good grazing grounds. 
Their fins for high dexterity manipulation, needed to balance from floating island to floating island without falling too low and eventually leading to the use of tools.

## Features to be added
Galphzzzeb would be a round start species people can create characters from and customize using markings.

### Trunk slot
Galphzzzeb have a trunk on their face in lieu of a mouth, which they use to speak (along with their breathing flap) but also hold items and eat.
the trunk slot is added between the two hand slots but does not function as a hand (cannot be swapped to)
The trunk functions as a third pocket which will use any item it holds every twenty seconds (think of it as having a mind of its own). 
This behaviour cannot be interrupted by moving but can be interrupted by being harmed.
To eat, Galphzzzeb need to pick up a food item in their trunk, upon which they passively begin eating it. 
The trunk hand will slowly dissovle and eat the food, which functionally makes Galphzzzeb take a bite out of food they are holding in their trunk once every twenty seconds.
Drinking also requires this action.
The use of pills likewise relies on the trunk slot, and feeding a Galph a pill, drink or meal will require putting it in their trunk slot.
The trunk can carry anything a pocket can.
Some space suits account for Galph morphology and allow for putting things in and out of the trunk slot, such as the paramedic, engineer, and security hardsuits. (heavy resprites required to add a trunk tube)
Other space suits like emergency, EVA, NTSRA or prisoner EVA suits do not allow players to put things in and out of that slot, so proper forethought will be needed before going into space sporting these.
Galphzzzeb DO NOT USE THEIR TRUNK TO BREATHE. They have a small breathing flap under the trunk which they use to absorb oxygen, as such they can wear medical or emergency masks.
Wearing a breating or medical mask allows for the use of the trunk as it is not the breathing organ.

### Gas stomachs
Galphzzzeb are slow eaters and digest slowly, sporting three stomachs (this can be seen on the sprite but functionally it is one stomach) that generate buoyant gas from digestion.
This makes Galphzzzeb always float as though they were in zero G, which can be counteracted by wearing magboots.
Being shot in the body area while not wearing armor (or by piercing rounds) has a chance (perhaps five percent) to burst the gassy stomachs (if we ever get status med, a 'leaky' status effect could be implemented instead or as an addition), dealing huge damage to the Galph and opening a large wound causing dramatic blood loss, as well as removing the organ and releasing hydrogen into the air.
What's more, burning Galph bodies will see their stomachs explode after a certain threshold of burn damage, leading to the aforementioned effects.
Galphzzzeb stop floating if they do not have their Galph stomachs organ.
Galphzzzeb can only digest plants or plant-derived foods (this includes cotton foods) and do not tolerate animal proteins such as from meat or eggs, which make them vomit.
Any species who gets a Galph stomachs organ implant will share the Galph diet as well as their floatiness (effectively like wearing moon boots) and will also require magboots to stay on the ground.

### Bug Eyes
Galphzzzeb have large, fly-like eyes which allow for 320 degree vision but lower detail perception at close range; as such they need glasses to read and write on paper documents.

### Spacing weakness
Due to their morphology, Galphzzzeb are particularly weak to barotrauma, taking double the blunt damage humans do when exposed to spacing.

### Sounds, naming conventions and accents
Galphzzzeb use long, rolling 'rrr's, snoring 'zzz's and flatulent 'phh's and 'thh's as well as dooting and tooting sounds. They also have a tendency to soften consonants (turning t into d, k into g, p into b etc).
Their naming convention is simple, Galph use three names, all an amalgamation of Galph-like sounds.
Examples of names: "Buthrrr Zzzem Qapw'", "Glrrrrph Shzzzittt Oughhh", "Doozzzh Vffa Loozzza".
Galphzzzeb have multiple unique emotes, such as 'toot', 'snore' and 'buzz'.

### Breathing
As stated in the trunk section, Galphzzzeb have a breathing flap under their trunks. 
Galphzzzeb can use breathing masks and gas tanks as normal, and breathe water vapor, exhaling oxygen.
Since they breathe an unorthodox gas, Galphzzzeb are provided emergency water vapor tanks in their survival box, and spawn with one in their pocket, connected to a gas mask they are wearing.
Galphzzzeb also breathe extremely slowly, being slow-paced grazers that do not require constant exertion to move.

### Appearance
Galphzzzeb look like large seals with fin-like hands and feet, a little bulbous tail and rotund belly and head.
Galphzzzeb wear specialized Galph bags (they have a little ball at the bottom to enable friction-free dragging accross the ground) attached close to their legs. These cannot be worn (but can still be carried) by other species.
The ressemblances stop there, as they have large bug-like eyes, a trunk instead of a mouth and flashy-coloured skin in the manner of sea slugs.
Players have the ability to add sea slug-themed markings that apply to the skin, as well as different trunk shapes, belly flaps and protuberances and optionally antennae.


## Game Design Rationale

### Seriously Silly
Galphzzzeb are silly creatures but exist in a serious environment. They can suffer gruesome injuries during gun fights due to their morphology and are generally implemented in a realistic way.

### Maintaining Authenticity
As said in Seriously Silly, Galphzzzeb are implemented realistically and impose a sense of realism despite the appearance of a goofy sci-fi alien.

### Dynamic Environment
The inclusion of changes such as the trunk slot, floatiness or slow eating allows for interesting new gameplay or roleplay scenarios to develop as players learn to integrate the new features and traits into their playstyle.
What's more, the species has a strong identity, both functionally and visually, which creates a sense of variety and richness.

## Roundflow & Player interaction
This new species focuses on making meaningful changes that heavily impact gameplay, leading players to change their playstyle and learn a new way to play the game.
Players will grow to recognise the strengths and weaknesses of Galphzzzeb and account for them in multiple types of scenarios.

## Administrative & Server Rule Impact (if applicable)
There is no reason to expect an impact on server rules or their enforcement.

## Technical Considerations
There are many features to be added, some new items needed are the survival water vapor tanks and galph bags.
There will be a need for clothing resprites or displacement mapping since Galphzzzeb are rotund, and some hardsuits have a trunk pipe.
Ensuring the trunks function as described might be tricky.
The stomach explosion mechanic may be difficult or possibly impossible to implement.
The stomach floating mechanic may also be difficult to implement.
The 320 vision feature will only come into effect if vision cones are ever implemented and may lead to balance concerns.
The emote and talking sounds will require finding proper royalty-free sounds. 