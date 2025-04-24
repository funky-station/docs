# Revolutionary Gear

| Designers | Implemented | GitHub Links |
|---|---|---|
| mxghast | :x: No | TBD |
## Overview

Revolutionaries need some pizzazz in their strategies. What if they could unlock the true potential of the station's productive forces?

## Background

Revolutionaries is in a somewhat tenuous position as of writing this proposal. There is concern about it's speed as a game-mode, and while I think the Open Revolt feature is soon-to-be implemented will significantly improve this, it could also bring back what I think is the root issue of why the game-mode is so quick and extreme violence compared to even similar game-modes: There isn't really any way to acquire any weapons that isn't by killing and stealing from command or security, and if you can pull that off, you win anyways! This implies that by far the best strategy is to just rush command while they aren't paying attention. This proposal seeks to change that.

Revolutionaries are also... rather one-note and linear to play. Yes, you can decide who and where to convert first, but ultimately the goal is to just snowball to critical mass regardless. There isn't much room for different gameplay strategies unless you count the choice to kill or not kill heads of command, and even then the choice is usually VERY clear depending on the situation - And we want people to be leaning towards converting more anyways, honestly, so it shouldn't be a primary gameplay decision. Revolutionaries needs a way to have other strategies, that are based around their core mechanics, and explicitly discourage random murder.

## Features to be added

Revolutionaries will have a new, core feature they start with: the Nanite Pattern Disk. This disk is provided by their mysterious Benefactors, who are the same as the ones who provided their revolutionary uplink. The Nanite Pattern Disk, however, is clearly far more the specialty of whoever these benefactors are. The greatest advancement in the development of productive forces, the Nanite Pattern Disk is capable of:
- Automatically **refactoring and reorganizing factory technology**, such as autolathes and protolathes, to produce suspiciously USSP reminiscient NT-illegal technology and objects. 
	+ The long-defunct original, but cheap and surprisingly effective AK-47 (*not* the futuristic AK-MS version) is once more deployed to combat. How will it stack up against futuristic rifles and sci-fi equipment? Time to find out.
	+ Strangely familiar barricades and manually operated doors, all foldable and portable, can just be printed directly from the modified lathes. I wonder where these are from?
	+ Redsteel equipment:
		* IMPROVED ROLLERBEDS! They keep bodies in stasis!
		* Redsteel shields, with a decent reflect chance versus all laser rounds, and giving solid resistance to bullets. The communist's top choice of protection.
	+ Long-banned internationally for debated reasons, smart bullets do normal lethal damage *without* causing any bleeding whatsoever through advanced cauterization, and simply harmlessly disintegrate when impacting against targets in critical condition. Strangely, whoever loaded the disk with designs *did not include normal bullets*. Maybe they are not so malicious after all?
- Turning condiment machines and snack vendors into full on replicators capable of converting energy into **consumable matter meals and ingredients**, another forbidden and long-destroyed USSP technology.
- Turning clothing vendors into versatile autolooms, that can produce **revolutionary uniforms** and even some **cheaper body armor and useful tactical kit**, such as webbing. 
- Enabling ore processors to turn ore and materials into **redsteel**, a specialized material with paradoxical bluespace properties used in **advanced USSP designs**.
	+ Redsteel may or may not be able to be combined with metallic hydrogen to create something truly special.
	+ Redsteel takes a small amount of *bluespace crystal* to fabricate, so is not cheap, and requires *actual mining and infrastructure!*
- Medical fabricators and security fabricators are modified into **unique lathes** instead of the usual modified one.
	+ Medical
		+ Anesthesized sutures and bruise packs are much worse than advanced topicals due to the limitations when it comes to medical technology that lathes can use, but are used faster due to being more comfortable to be treated with.  
		+ Redsteel sutures are not anesthesized due to incompatibilities with their unique composition, but are absurdly effective at binding grievous wounds. Their lack of use in modern times is a topic of much debate.
	- Security
		+ Neuralblockers, pens designed for anesthesia but quickly shifted towards nonlethal containment due to their ability to disable the movement of anyone in melee range extremely quickly. Costs redsteel and is one time use each! Use wisely against top targets.
		+ Revolutionary nanobombs, implants which cause the user to automatically disintegrate on death. Designed to prevent forced borgification or interrogation, as well as stealing of weapons or resources. USE AND DISTRIBUTE SPARINGLY. Sometimes used as an execution method against known war criminals. Using it on an innocent person against their will is a breach of international law and all of the revolution's ideals, so don't!
* Modified faxes will be able to print decorative revolutionary posters at will. Viva la revolution!

**All of these ideas can be moved, altered, removed, or nerfed or buffed as needed.** The **core concept** is the **hackable and modifiable station infrastructure**.

**Nanites need a solid, anchored station to function properly as a reference point, and go very very wrong if used on a moving ship or shuttle. Possibly making lots of grey slimes that kill people.**

## Game Design Rationale

Allowing and encouraging revolutionaries to build actual infrastructure does a few things: 

- It slows down rounds organically in a way that isn't frustrating, as built infrastructure is ASSAULTABLE infrastructure. This should create actual organic conflicts over territory instead of just a complete clusterfuck as is usually complained about. 
- It's fucking COOL, like holy shit imagine PRINTING AN AK-47, FUCK YEA
- It allows us to give them tools and objects that discourage random killing, while also encouraging new and interesting playstyles and strategies. While not nearly as dynamic as Traitor, it can hopefully begin pushing it somewhere that direction, which also gives Revolutionaries a unique identity.

## Roundflow & Player interaction

The nature of the lathes and production mechanics should create a middle ground between complete stealth and open revolt, encouraging 'shadow factories' or hidden revolutionary bases to form, requiring systems and methods to hide and restrict entry to these bases while still keeping them accessible. The hope is that his is an interesting dynamic by itself, but it should also reduce the stalling/quick end feast or famine effect of rounds, by encouraging revolutionaries to build and defend infrastructure and than go all out once they're ready. This creates a proper gameplay loop and flow which lots of the game sorely needs, revolutionaries and most antagonists included.

## Administrative & Server Rule Impact (if applicable)

- The goal is to *reduce* admin load through tools such as smart bullets, which should *mostly* nullify the advantage of truly-lethal equipment for revolutionaries, which is often a moderation 'clusterfuck' due to the constant round removals and killings. 
- The ability to make unique uniforms aids with an encourages proper command structures, possibly allowing systems such as revolutionary 'lieutenants' to relay and give orders in lieu of the head revolutionary themselves. This should also cut down on random killings before Open Revolt.
- Random deaths coming out of nowhere is MUCH less likely if revolutionaries have cool stuff they have to somewhat out themselves, or at least take huge risks, to make. 

# Technical Considerations

- This should be relatively easy to implement due to the already existing lathes, protolathes, and printers. It would be very cool to give them a unique, possibly red-colored UI, but such a thing is not required for the features to work.