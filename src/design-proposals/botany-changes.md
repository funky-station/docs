# Hydroponics Changes

| Designers | Implemented | GitHub Links |
|---|---|---|
| ReconPangolin | :x: No | TBD |

## Overview

Expands the role of botany by opening the design space through the rebalancing of existing features, a new mutation system, and the addition of new plants, machinery and mutations.

## Background

I initially set out to incentivize shadowlands exploration by adding plants as interesting loot, however, the more I tested certain features the more potential problems I found. I discussed some of these problems with Terkala/The Fern of Functionality and they agreed that the current state of botany wouldn't support some of the more powerful plants I planned to add. As a result, the scope of this proposal has grown far beyond my initial expectations.


# Features to be added

## Unique plant crossbreeding

### Feature Description

 Different seeds can be crossbred together into new species. This would be achieved through a new roundstart machine that would consume seeds and potentially a catalyst to output a new species of plant.
 
 One path could relate to steel-caps, for example:
- Combine papercane and steel-caps to create plastic-caps
- Combine plastic-caps and golden apples to create aurum-caps which could produce small amounts of gold

This feature would allow botany to grow plants that would have been too strong or would invalidate other departments if they existed purely in the current system. The process of mutating three unique plants, combining them together, and finally trying for self-harvesting mutations should be long and difficult enough to make salvage the much preferred route to gold, however, it allows botany to fill gaps in the manifest and provides a longer term goal. It's also easy to balance. If we wanted gold to be locked behind salvage we could make a requirement be salvage loot.


### Motivation

Currently players need to apply unstable mutagen and hope for the best to mutate plants. In isolation this system if fine, although it has a heavy reliance on chemistry, there's limited skill expression and - provided you've got access to exotic seeds - you can grow everything almost immediately from round start. If I added new varieties of mutations they'd all be easy to achieve purely by dumping buckets of mutagen and then dylo/multiver/vitamins onto certain plants. I've also seen a common trend in botany of cryoing earlier after growing certain plants. Usually these plants consist of everything the chef could need or some combination of omni, cognizine, deathnettle and gatfruits. This new feature should encourage greater variety in the number of plants grown, add to the progression throughout a round and allow botany to grow plants that are useful to a variety of departments.

## Machines

### Plant Sequencer
Swabbing is completely random and fairly obtuse for new botanists, so I propose adding a new machine to aid the learning process and partially remove the randomness. It would be available as a tier 3 civilian services research. 

The plant sequencer would consume two seeds to displays what traits could be spliced between them. The player would then manually choose some mutations and traits, limited by a new mechanic called 'genetic stability', and then the remaining traits would be spliced randomly, identical similar to the current system. More powerful traits would cost more genetic stability and this would only be recovered as plants grow. This machine requires a competent botanist and civ t3 to make full use of so I'll probably tune it higher to start and if it's problematic we can tune it down late.

### Plant Analyzer
I'd like to make adjustments to the plant analyzer to give it different tiers so it can be available from roundstart as well as more powerful versions through research. At T1 the plant analyzer would be available at round start but it would only display less useful info such as potency, yield and potentially growth rates and use more power. At T2 it'd be the current plant analyzer with - potentially slightly faster with less information? - which would add information such as chemicals, gas and mutations. At T3 it'd be available from the T3 civ services research. It would be fairly fast and show details such as potency divisor, weed growth and threshold, and mutations.


#### Seed Splicer
A new machine for crossbreeding plant species. This would take two unique seeds in varying quantities and combine them into a new species. Certain plants may require more then one packet of seeds or catalyst (vestine, exotium, artifact shards) as a balancing measure.

## Botany rebalance

### Motivation
As mentioned earlier, the best method to achieve anything in botany right now is to throw a cocktail of chemicals on a plant. Whilst most of these chemicals aren't a huge concern there are a couple that I believe are problematic, notably diethylamine. 

Diethyl can be used to speed up a plant's growth by increasing it's age. This bypasses anything that could affect the plants health so it can be abused to instantly grow any plant regardless of its requirements. I've managed to grow 9 gatfruits in under three minutes from round start using a single seed and 35 gatfruits in about five minutes with a bucket of diethyl, despite the fact that it's bugged to be less effective then intended. Diethyl greatly limits the botany design space as any plant with longer growth times, complex requirements, or unique conditions can be instantly grown.

Another issue is that multiver/dylo/vitamins can restore plant health and phalanx can remove an invalid gene so a plant can always be kept alive at no cost.


I'm proposing that we link plant health to growth rate and instead have diethyl speed up growth rate. A healthy plant with this change could grow even faster than in stable but plants with worse conditions or botanists with thousands of units of diethyl would have a harder time. As part of this change I'd be modifying mutations to remove some conditions that I've never once seen satisfied (Requires zauker/trit/bz) and adding some new ones - including intended features that were never finished.

### Changes
- PlantGrowth now increases the rate a plant grows instead of instantly increasing a plant's age
- A plant's growth rate and health is increased or decreased based upon a formula rather than the current all or nothing system. 
- Implemented missing features or features marked as TODO (such as improper light doing nothing, potentially pests if the playtests go well)
- Modified gas mutations to be safer (I'll talk to Terkala/Fern for this one)
- Removed a number of the health modifying mutations that will never be satisfied. (I don't think an atmosian has ever been or should ever be asked to trit flood botany and it's not an interesting way to punish excessive mutation)
- Colored the third hydroponics light to differentiate between what's impacting a plant's health
- Robust harvest has a 5-10? unit threshold so it won't punish botanists for being one or two units over
- Modified the mutation weights to be more enjoyable

#### <ins>The following are a few potential tentative and controversial changes to botany, most won't be implemented.</ins>

 These are potential balancing levers for if more variety and content leads to powercreep, to potentially reduce entity spam, and to reduce the gap between standard plants and perfect plants to help newer botanists. If given the choice I'd rather have power in the variety, experimentation and content of botany rather than a few very strong plants.

- Specific plant species have a max yield 
- Plants have a maximum chemical storage based on potency
- Chemicals are decreased the more that exist in a plant
- The potency divisor of certain chemicals is increased
- High yield plants take longer to grow, chemicals in a plant are potentially increased to compensate (Might require kitchen changes)
- Plants take slightly longer to grow if they're multi-harvest, increased for self-harvesting or these traits reduce yield
- Plants will always be able to be clipped exactly two times. Maybe can limit to 1 or 0 for extremely powerful plants so you need a lot of effort to grow one.
- Clipping will reduce the stats of the parent plant, clippings might be unaffected. Could use genetic stability so plants recover over time


## New plants


### Shadowlands Loot

I'll work with an artist and maintainer on the naming and theming of these. 

The majority of these plants will be poisonous and grow better in low light conditions. This gives the option for engineering to help build a space but these plants could also be grown in the botany locker room (on most maps), grown in maints, or spliced to remove this trait. I'll also add some standard plants too, I'm just listing the ones that should be in a design document.


#### <ins>Ebonberry</ins>

<em>Peer into the shadows</em>

A berry obtained by crossbreeding a shadowlands plant and blue pumpkins. It grants nightvision to aid in exploration but it can also be beneficial for hiding or exploring maints.

#### <ins>Duskpalm</ins>

<em>Obscure the world</em>

A rare plant found responsible for creating the shadows found near shadow portals. It can be mutated into dawnpalm which has an intense glow that banishes away any nearby shadows. If science is using a shadow anomaly as a portal an expedition team can retrieve this and a botanist can mutate it to help deal the anomaly and it may be useful for exploring the shadowlands. I'll need to look into performance impacts for this one.

#### <ins>Spectra</ins>

<em>Fade into darkness</em>

A crossbreed of a chilly, glasstle and a rare shadowlands plant. Anyone who consumes this plant will become temporarily invisible.

Uses the upstream regent Spectra-Fade pull request.

#### <ins>Wormhole</ins>

<em>Warp yourself into genpop</em>

A crossbreed between an extra-dimensional orange, spaceman's trumpet and a rare shadowlands plant. Any player who consumes this regent will be teleported a short distance randomly, suffer heavy toxin damage and empty their stomach from the transition. It's a great escape from antags or for antags with a heavy risk attached. It should be difficult to use as a poison since it's extremely obvious, you don't want your target to teleport to safety, and it's consumed after one teleport.

### Salvage Loot

#### <ins>Radium and Phosphorus plants</ins>

<em>For when you've pestered chemistry too much</em>

Currently there's only one component of mutagen available in plants without random mutation, chlorine. A plant would be available from salvage that could be crossbred with a few standard seeds to produce radium and/or phosphorus so botany could better mutate without a chemist. 


#### <ins>Gaia</ins>

<em>The only plant anyone ever suggests</em>

With the introduction of rare plants and crossbreeding we can finally add Gaia back without breaking the game. Gaia would be the pinnacle of difficulty to obtain and require advanced mutations, salvage and potentially even an expedition to the shadowlands. Once it's been achieved plants will no longer need weeding, water or compost.


#### <ins>Catmint</ins>

<em>Have any ahelp instantly answered!</em>

A plant that contains drugs that only affect felinids and cats. Can be crossbred with blueberries into a plant that contains a regent similar to wehjuice that makes players meow. This regent can be used for a chem that can temporary polymorphs players into a cat. When scurrets/slugcats get merged upstream (**VERY IMPORTANT**) it'll also be used for scurret polymorphs. 

### Features that might be designed later

This is already long enough but here's a list of plants I'm looking into and some other features I might include

- Expanding the cap series of trees to include most resources the station could need - provided the right seeds are found and the right plants are mutated
- An expansion to syndicate botany that requires growing, mutating and crossbreeding gatfruit among other plants and vestine. It rewards more powerful guns at much greater risk of sec discovery and a big investment in time and resources
- A low capacity battery that can be grown that slowly recharges over time
- A plant that grows improved fibres to make slightly larger backpacks.
- A more consistent way to obtain anomaly berries
- More mutations 

### Suggestions
- Stunbaton equiv of nettle, might be fine if it uses the same salvage plant containing licoxide to crossbreed with difficult enough requirements


## Game Design Rationale


Botany was the first department I started with in SS13 (and SS14) and I believe that it's unique in its position as beginner friendly job that's never required for the station to run whilst simultaneously having a high skill ceiling and potentially patch almost any issue in a station. If medical is understaffed you can produce omnizine, if materials are an issue you can supply the station with steelcap and random chemicals help keep the department fresh. Despite all it's very common to see reworks suggested and I agree there are improvements that could be made. I've reviewed proposals and pull requests across different repositories and the common threads are the following:

- Botany lacks interdepartmental interactions outside of providing ingredients to the chef and requiring chemicals from the chemist
- There is limited progression throughout a round
- Traits are obtuse and mutation is random 

I disagree that botany only interacts with one, maybe two, departments since I've had botany specific interactions with almost every role, however, there's plenty of room for improvement and the new plants should aid in this. Additionally, the addition of crossbreeding should add long term goals and the loot can open up exciting possibilities for a botanist late into a round. New machinery alongside our previous addition of and improvements to the plant analyzer ashould aid players in learning how to mutate and splice traits from plants together.

### Seriously Silly
The new plants should open up some very silly possibilities. I love the idea of bluespacing only to end in the worst location, invisibility timing out at the worst time, new fun chems to mess around with and overall just an improvement to the amount of people I roleplay with in a botany round. Also the image of a syndicate agent gearing up with plants instead of a hardsuit and high tech weapons is hilarious to me.

### Maintaining Authenticity
Crossbreeding plants and genetically modifying them is a common part of modern agriculture. Kale, cauliflower, broccoli, cabbage and Brussels sprouts all were developed from the same plant and there's thousands of chilli varieties. Improving this feature should feel authentic and add to the idea that this station was primarily setup for research and development. I concede that some of the sillier plants aren't realistic although I think it's fine to sacrifice some realism for entertainment.

### Dynamic Environment + There is no Winning or Losing
For this proposal these principles are intricately linked so to avoid repeating the same thing: At the moment botany can feel somewhat solved; while random chems in plants are great at creating roleplaying experiences and dynamic rounds they aren't consistent. Your best bet right now is to grow omnizine, deathnettle, gatfruit or killer tomatoes. I'm hoping these changes open up new strategies, unique options and expand on what makes botany dynamic rather than player's focusing on a small set of meta plants.

## Roundflow & Player interaction

### Roundflow
Most of these plants will be difficult to come by and require a competent botanist, chemist and salvage team working together and some features require T3 service research. In longer rounds you could see botany become a force to be reckoned with, however, plenty of other jobs (salvage, atmos, science, cargo) also scale well so I'm not expecting anything major to change we could always rein it in if it does and apply some nergs. If Verna or Fern become DAGD agents then I'm sure they could abuse these changes but that would be peak SS14.


### Player interaction
Players would have many new options open to them and it these changes encourage other departments - notably salvage - talking to botany so this should be great for player interaction. I could see veterans being annoyed after going from an extremely skilled botanist to a new player so that could be a problem but I'd like to hope our playerbase is above flaming newbies for not being Verna. Some botanists might ignore the chef at the risk of breaking SOP and getting fired?

## Administrative & Server Rule Impact
Everything added would just expand existing features so the admin load should be similar. There's the potential it would make it easier to self-antag or powergame as botanist but given the current system allows for botany to produce lethal amounts of BZ or trit I'd expect it to reduce workload if anything.  There is also the potential for OOC mald at new players (which already exists in other departments) in a role that's well suited for new players.

## Technical Considerations

If do my job correctly I don't expect any performance impact, there could be issues with entity spam but I'm planning on profiling the code and improving the current performance. There's been plenty of arguments on improving the botany code and switching to more of an ECS design pattern but I'm planning on working on content first and foremost rather then getting bogged down in making a perfect system and the code is workable for the most part, I'll look into it further down the development pipeline.

I'll develop a mockup for this UI if the proposal is received well and I'd require help spriting for this project since I'm horrific at drawing.