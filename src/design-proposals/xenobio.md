# Xenobio

| Designers | Implemented | GitHub Links |
|---|---|---|
| taydeooo | :x: | TBD |

## Overview

Xenobiology is a new branch in science that deals with treating organisms with gasses, funny chemicals, and other anomalous materials. Scientists can now specialize in three branches, anomalies, xenoarcheology, and xenobiology.

## Background

Xenobiology is a feature beloved in Space Station 13. Science is severely lacking in content, especially in regards to interacting with live critters.

## Features to be added

Science needs a lot of changes to deal with Xenos, but heres the gist of everything that should go into it.

### Xenos and Xeno specific stuff

#### Xenos

Xenos are in round start in their testing chambers, these critters have a higher chance to split earlier and have a better chance of getting more insane combinations. These are your bread and butter, and you want to keep them alive for as long as you can. Cargo may order more of these, but they are expensive as hell. They also have a chance of spawning naturally in maintenence tunnels.

Salvage can also bring these to you, if they're nice enough. Salvage can capture these critters in pet carriers, or in xeno carriers.

Xenos, after eating a certain amount of biomass, lay an egg. Eggs naturally create a single larva, which also needs biomass to survive.

Xenos, can produce as many eggs as needed, although the quality of the eggs deteriorates the longer they are alive.

#### Xeno Carriers

Xeno carriers are specialized containers that can hold very hostile organisms. They do not break, and lock just like artifact containers.

#### Larva

Larva are xenos that haven't matured yet. They are worth nothing, but can be influenced. Limbs can be removed, chemicals can be injected, gasses can be pumped in, and more. These influence how Larva grow up. Larva also need a considerable amount of biomass to mature. After reaching a certain threshold, they grow into a Xeno. Specifically what Xeno depends on their mother, as well as the environmental effects during their infancy.

Larva are also very weak, and die easily. They need ideal temperatures and plenty of food. You may also provide a television which will enrich their learning experience.

#### Xeno Eggs

A xeno egg is an egg that takes 15 minutes to hatch, in standard station atmosphere. A single egg will create a single larva. Xeno eggs can also be used in various recipes, so excess eggs can be given to the chef if need be. A xeno can produce a single egg at a time, due to the heavy biomass loss they take when producing an egg.

A xeno egg is also given a quality, which is passed onto the larva as modifiers for certain types of mutations. Fresher eggs from a healthy xenonid will have better chances to mutate into something.

#### Xenonid Types

Xenos all have the basics.

* Lungs that can either breathe pure oxygen, nitrogen, or a mix of the two. No, players cannot use these.
* A base resistance to blunt damage, with weakness to fire and piercing.
* A healthy appetite.

Specifics of each xenonid type are enumerated:

- Drone: A simple xenonid that doesn't do much of anything, except lay eggs. They can be either neutral, but can turn aggressive when attacked. In a word, they are "meh." Good cannon fodder.

- Stinger: Relatively complex, has a stinger that it can sting players with. Injects a random reagent(s), where the glands can be extracted to extract an amount of a reagent. Can be kept alive as reagent farms, or squished into spesos or research points.

- Bull: Dimwitted, but very strong. Aggressive as hell, will attack scientists at will. Lays very aggressive eggs, and is worth a lot more research points than other types of xenonids.

- Queen: Real. Turns other xenonids into guranteed ghost roles, and can command xenonids at will. Can eat through walls and doors. Does a ton of damage. Worth the most, and has organs that might be worth keeping around.

More to be added, pending maintainer discussion.

### Science Tools

#### Xeno Value Tool

The critter point gun, is a tool just like the appraisal tool for cargo, that tells researchers how much scientific value is contained within a xeno.

Science can produce these in their protolathe, with a new Xenobio tier 1 research.

#### DNA Processor

This is the machine that squishes and squashes critters until they are strung out in a very long DNA ribbon (which kills them), and converts that DNA into research points. Xenos are essentially "cashed in" in exchange for research points. This ends a lineage of critters, so this should be done sparringly.

Science can produce these in their machine board lathe, with a new Xenobio tier 1 research.

#### Incubator

The incubator allows scientists to hatch critters more efficiently, speeding up the time an egg takes to hatch, from 15 minutes all the way down to 5 minutes. The incubator is prone to break easily, and does take a lot of power to operate. The incubator can hold a total of 3 eggs at a time.

Science can produce these in their machine board lathe, with a new Xenobio tier 1 research.

#### Changes to existing maps

* New Xenobio rooms with at least 2 chambers to conduct experiments in
* Incubators mapped in
* DNA Processors mapped in

## Game Design Rationale

### Seriously Silly

The things we encourage by adding this feature are experimentation with potentially dangerous beings that feed off of biomass. The idea of scientists having to take care of larva on the station then grinding them up later adds a certain type of morbid flavor to the game that, in my opinion, serves well to act as a catalyst for insane stories to play out. Players getting fed up with science over how they treat these larvae, then they themselves get mauled to death by the very same former larvae they swore to protect. This increases the chances of something going wrong in science 10 fold, without it being a mediocre explosion.

### There is no Winning or Losing

Let's make it clear, scientists are going to get hurt. They are going to get hurt by things that are not antagonists, and that's okay. Xenos aren't exactly antagonists on their own, but science can make them antagonists. This contributes to the open sandbox feel of the game while still maintaining proper in-character motivations for players to either mess with Xenos or not. The possibility of round removal is also non-zero, further blurring the line between winning or losing.

### Maintaining Authenticity

NanoTrasen is an evil corporation, and them doing live experiments on animals seems par for the course. People are free to not engage with this feature at all, which is a perfectly rational way to play. Science also having no way to experiment on live animals except just all roleplay "experiments" is also very lame, and not very authentic when put into the context of the base games features. While its true, eggs don't hatch in 15 minutes in real life, this is a fair compromise for gameplay, as them just needed to be tended to for a short period of time is more than enough to have players immerse themselves in the role of a xenobiologist.

### Dynamic Environment

Players are encouraged to find new stimuli (gasses, surgeries, food, etc.) to get their xenonids the best they can possibly make them. The aftermath of xenonids becoming potentially uncontainable adds to that dynamic environment, causing all departments in the station to engage with xenonids somehow, even if individual players choose not to.

## Roundflow & Player interaction

Science becomes a stronger contender for being the department that causes the story of a round to move forward. Science is a resource dump for the station, and while they use a lot of resources, a lot of that becomes obfuscated away from the rest of the station. This allows players to see the resources they create, such as chemicals, gasses, whatever the like, be used in a way that influences another "living being," which is infinitely more interesting than the current way science does things. 

## Administrative & Server Rule Impact (if applicable)

I do not see any additional workload for administrators, other than just enforcing already existing no griefing rules. Sometimes a xenonid becomes uncontainable, and that's okay. That's part of the round. Xenonids can't be made into zombies either, so the worry of II or other antagonists becoming overpowered is not warranted.

# Technical Considerations

This will require a new Xenonid System, along with new UI for the DNA Analyzer. The Xenonid system may not need to change any existing science code, but that is to be seen.