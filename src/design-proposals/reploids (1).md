# Replacing IPCs Completely; Reploid Addition

| Designers | Implemented | GitHub Links |
|---|---|---|
| ParasiteSaintLeech | :x: No | TBD |

## Overview

Completely replaces the niche IPCs occupy; that being a highly customizeable synthetic speices. Reduces the gameplay differences to ones more in line with the milder changes that other races have; such as Slimes, Vox, Thaven, and the like. This avoids both lore and mechanical pitfalls associated with IPCs. Long has this issue plagued many-a-server. Now, ideally, it will plague one less. But the hole there should be patched up, and that's what this aims to address. Scifi 'synthetic' species are always cool to explore, and, ideally, this will expand the options farther past 'just a robot' without letting the existing ones die in the cold. Also, this has a few options: The easy way, and the not easy way.

## Background

This PR has most of the issues that need to be/will be addressed:
https://github.com/funky-station/funky-station/pull/2200

As we can see, the biggest points are as follows:
- Mechanical consideration. IPCs need to be regarded EVERY time a new antagonist or feature is even thought of. They are too strong to ignore, whilst still managing to have glaring weaknesses that ensure that if the opposition to the IPC is well prepared, someone is losing out on a good interaction. Either they shut down your gimmick completely, or they get shut down completely.
> - Changeling is a victim of this.
> - Zombie is a victim of this.
> - Anything potentially involing space is a victim of this.
> - Cult has issues with them.
> - Any attempt to deal with them that does not kill them outright or maim them means they can find a way to repair in an EXCEEDINGLY quick manner. This is strong enough that there are servers in the past that completely removed the ability for IPCs to self-repair. This way, at least the person doing it would need a welding mask to avoid going blind, or something similar.
> - Attempts to balance IPCs or to tailor them have been made, as Taydeo has kindly pointed out to me; the interest in just 'reworking them' or 'changing them' is functionally gone.
- Lore considerations. This one I don't care as much about, but there are questions that are raised at the existence of IPCs on the station. I myself have answers for them; but I don't care to go over them. Here instead are the questions:
> - If NT is employing IPCs, why are cyborgs around?
> - If NT is using cyborgs, why are IPCs around?
> - Can IPCs exist in a gameplay sense without lore as baggage in the first place?
> - Why doesn't NT just hire exclusively IPCs if they have an army of funtionally deathless machines who's posibrains they can just rehome in a pinch?
> - If the only difference between an IPC and a cyborg is laws, what's the point?
> - If they can't be rebuilt, why are players able to build parts for them? (This one I am actually unsure of, I didn't even know that was a limitation in ss14)

## Features to be added

Assume these changes are made with a basic human as the template. Every organ a 'basic' species has will be here. Heart, brain, lungs, stomach, kidneys, liver, eyes. All present and accounted for.
| The Way With Some Effort |
|----|
| Existing IPC markings, sounds, and emotes will be ported to the class, but additional markings will be presented instead of also porting more from other species. The visual aesthetic and the fact that they are “artificial” are the most important parts to preserve, so future marking additions would want to lean into that and _not_ into lifting assets from other races. In this theoretical version, the main templates for Reploids are solely humans, and they are altered in order to fit the environment they are in. There would probably be some redesigning on part of the players to salvage their previous character concepts. ||

| The Easy Way |
|----|
| In oder to maintain/preserve existing characters, the main and **most important** thing that needs to be done is...the porting of most/all markings, sounds, or hair options to this new species (except maybe "robotic wings;" those look rediculous). All those unique looking IPCs are thereby salvaged as Reploids. I'm uncertain on adding anything from vox, slimes, thaven, or diona. |


The basic color pallet should allow from a high degree of choice; not limited to human skin tones. I'm assuming people can be trusted with this.

- The ‘meat’ that is gained from them should be called `“Synthflesh”`, as well should the organs be flavortexted as `"Synthetic [Organ"]`.I will suggest copper-based, horseshoe-crab-esque blue blood for them, as it further visually differentiates them from the baseline and makes it apparent upon damage what they are by default.

- The main feature, of course, would be Reploids themselves. The lore entry when selecting species would be something like the following:

| Artificial beings grown in vats to help stabilize colony workforce numbers on planets with poor supply chains or excessively harsh conditions, from batches upon batches of donor imprints from species of all sorts. They have since become a welcome presence amongst many locations, albeit with scrutiny from those who view them as wholly unnatural. |
|---|
| Because of intentionally weakened immune systems and suppressed reception to pain, Reploids seamlessly integrate technology and flesh into one another; often, it can be hard, if not impossible, to tell where one begins and the other ends. |

Considerations for why they are on sation could be easily rationalized:
- An overabundance on colonies leaves them wanting for work. Especially common amongst those who are younger and less established in their colony's routines and processes.
- Degrading capability to cope with the conditions of certain planets naturally phases them out of participation, so they go to work elsewhere.
- Perhaps, paradoxically, going to work at a megacorp is more “freedom” than whatever is happening on whatever colony they came from.

Naming convention: Common with variable numbering identifier (ex. John Doe 19), Custom variable numbering identifier (ex. M3G4N, B1ll-9), Simple defining adjectives with variable numbering identifier (ex. Picky-13, Calm-82, 53-Dull)

For the damage modifiers, I propose the following, to reflec the 'harsh environments, weak immune system' idea:
  
  `Cold: -50%`
  
  `Heat: -50%`
  
  `Shock: +100%`
  
  `Cellular: +75%`
  
  `Poison: +50%`
  
  `Radiation: +50%`

`Native' Traits: These are **potential** mechanics that might be added to them in order to give them some flavor.
- Damage Assesment

Using an action, accurately deduce the state of one's internal, if they are sick, what is hurt. Basically, personal vitals sensors. This leans into them being artificial, and additionally being fully aware of their own artificial nature.
- Coordination Comms

Using one of the unused letters or a number (say, :b or :0 whatever), Reploids can speak to eachother via the radio. This of course requires active telecomms or close range (able to view one-another) to work. This is heavily influenced by the capabilities of "Vaurca" on the Aurorastation SS13 HRP server. However, there, this is telepathic. In Funky, this will operate no different than using your headset.
- Emag interaction

Becoming Emagged causes reploids to experience auditory and visual hallucinations, and induces the 'drugged/drunk' filter on ocassional intervals. They would begin to twitch, visually. Potentially fun things might additionally be cuasing the combat mode to toggle at random. The "total" time that this occurs should be limited, somewhere between five and fifteen minutes. The idea to is impair them, not to completely debilitate them for the rest of a given round.

- Ion Storm interaction

During an Ion storm, there is a percentage chance to apply the Emagged status. Alternatively, induces hunger/thirst.
- Chemical/Food Interaction (WIP)

Consuming oil, space lube, or 'normal' liquids (Milk, water, soda, etc) will sate hunger and thirst simultaneously.

Consuming solid foods (basically, any interaction that triggers the 'chew' sfx) will also sate both, but provide a reduction to speed and/or stamina for a while.

Although radiation does a decent amount of damage to them, a small amount of uranium could serve to stave off hunger or slightly increase stamina/speed. Alternatively, welder fuel could work here, additionally acting as an intoxicant in the same vein as alcohol (which would still effect them as normal).

- Unique antagonist interaction: Personality Reformat (MALF-AI)

At a certain point in a Malfunctioning AI's capability, something like a virus, transmitted through an electrified item, will enslace the nervous system and mind of Reploids to the AI itself. They will be prompted to follow the AI's instructions; be that to blend in, or to do specific tasks. They will be encouraged NOT to announce what has happened to them. This should require a flag that marks the object as 'infected', and a text string that informs the Reploid of what is going on; this is most similar to the mechanics of a heretic's ghoul.
## Game Design Rationale

This kind of thing seems as if it'd be a no-brainer for the kind of sandbox stuff Funky seems to want to provide. Not only that, there ends up room for quite a bit _more_ than what was bargained for initially, as it's no longer 'just a robot' and etends into bio-organic territory, too. I'm unsure of what more one would want to add mechanically; but that can be fleshed out in the future. Making the basic concept exist is the most important part; all the mechanical stuff can be fleshed out later, if that is more beneficial. 

## Roundflow & Player interaction

- If the native traits make it in, they can now interact with all the basic mechanics that everyone else does. Now with funky robo-flavor.
- People seem to like playing robots, and (rp-wise, at least), people like to interact with them. Here's something similar, so that they can keep making good impressions on others.
- The main point of player interaction is player expression itself. Making cool things is cool.
- Most importantly, though, the player is now exposed to all of the mechanics that one is expected to deal with in a typical SS13 round. They are no longer a `blatant obstacle` for lings or zombies, no longer something that people outright need to deal with. The ion is now for things like rogue borgs, mechs, or other 'purely' mechanical threats, whilst still doing _something_ to Reploids that flavors them as having an underlying mechanical nature.


## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?

Theyre shouldn't be. If there are any potential issues, I'm sure someone will say something about it.
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?

No, but it might make telecomms a bit more of a target in the case that Coordination Comms is added as-is.
- How are the rules enforced mechanically by way the feature will be implemented?

Ideally, they don't need to be. Players messing around with this probably know what they have in mind, and someone making a 'default' Reploid would be just as welcome.

# Technical Considerations

- Are there any anticipated performance impacts?

I have no idea. Probably not.
- Does the feature require new systems, UI elements, or refactors of existing ones?

The only thing that might be needed is the UI element for "Damage Assesment."
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)

I would assume that the "Damage Assesment" UI element will require only a basic interface; something identical to the information displayed in the sensor overlay.
