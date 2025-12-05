# IPC Rework Document - Draconic Edition

| Designers | Implemented | GitHub Links |
|---|---|---|
| SigmaTheDragon (Discord: Sigma Draconis) | :x: No | N/A |

## Overview
IPCs, being so different to other species, are hard to balance. They must remain both unique and balanced, which can be hard to achieve. With this doc I aim to rebuild the IPCs ground up to bring them up to the standard they should be in.
For this rework IPCs would have to be remade. Most of the code that IPCs currently have would have to be removed and standardized to be the same as other species as to remove much of the technical woes they cause.

## Base Modifications
Base IPCs will not need air but will still be affected by pressure, taking increased amounts of blunt damage when compared to other species as their components break down, but these can change depending on the ‘engine’ which will be explained later.
IPCs will be immune to poison and asphyxiation, but take ion damage and 20% more shock damage, alongside 10% more piercing damage (things piercing through your components hurt!) and 20% more blunt damage.
They will have 90 normal health and 90 critical health (for a total of 180). Much like other species, IPCs will slowly die once crit, but instead of asphyxiation damage they would slowly take shock damage. Instead of gasping, they would do a ‘[CHARACTER]’s wires fizzle as they short circuit!’ emote.
Defibbing an IPC shocks everyone around and drains their battery, so to revive an IPC a new item is required: The IPC Reboot Key. These keys would be medium items that use batteries, and can be used on IPCs to reboot them. These keys would be available in robotics round start and be printable in both the protolathe and medical lathe.
Finally, IPCs will not be able to rot due to their mechanical nature.

## Metabolism, Engines and Power

### Metabolism
IPCs will have a unique metabolism that can change depending on the ‘Stomach’ installed - aka the Engine. An IPC’s engine will modify how and if they metabolize certain drinks, foods and chemicals, but some chemicals will still have effects regardless of the engine installed.
Always-effective chemicals:
* Space Lube: Saline equivalent, great at restoring the oil of IPCs.
* Space Glue: Greatly slows down the IPC, causes jitter.
* Razorium, Ellectric chems, etc: Would still affect the IPCs by dealing their respective damage types.
* Fresium: Cools down the IPC and deals cold damage, but greatly speeds up the IPC in exchange (machines work best in the cold, but too much cold damages them!)
* [NEW] Nanite Soup: Omnizine Equivalent, heals all damage. Could be made using iron, exotium, uranium and other chems.
* [NEW] Unstable Nanites: A strong ‘poison’ that quickly kills IPCs via dealing large amounts of blunt damage. Made using unstable mutagen, Nanite soup and other chems.
* [NEW] Disruptor Nanites: Nocturine equivalent for IPCs, made with unstable nanites, electric chems and liquid exotium.

### Engines
Engines would replace stomachs on IPCs. Most would be available at round start via traits, but some would also be researchable, and others not obtainable via normal means. When an IPC runs out of power, be it via EMP or through running out of fuel sources, they enter an ‘energy crit’ state where they become super slowed and they become unable to use their hands, but do not die. IPCs will also no longer be able to recharge from APCs.

Round Start Engines:
* Electric Engine: The standard IPC engines, electric engines use power cells to keep running. The IPC can swap these cells any time, but it is slow and cannot be done on the fly. Not only that but it is extremely vulnerable to EMPs as it'll make the IPC unable to recharge unless someone else switches their battery or they reach a cyborg recharger.
* Fuel Engine: This engine uses liquid fuel to replenish its power. This fuel can come in the form of welding fuel (less efficient) or alcoholic drinks, which tend to be more efficient. Liquids such as water and juice do not replenish fuel, and as such are quickly discarded from the IPCs system. The IPC can store up to 120u ( of fuel inside them from drinks and liquids they drank (lasting 15-30 minutes). This fuel tank is consumed to keep the IPC powered, and when they run out they enter the energy crit state.
* Biofuel Engine: Similar to the Fuel Engine, this engine makes the IPC require fuel to have power. In this one however the fuel comes in the form of food. Any organic food type can be eaten to fuel this engine, and as long as the IPC’s biofuel tank (which similarly to the fuel engine should last 15-30 minutes when full) has nutrients in it.
* Turbine Engine: This generator makes use of the natural air current to generate enough power to keep IPCs running. IPCs running this engine will no longer be immune to spaced areas, as being in an area without any gasses for more than 10 seconds will cause them to go into the energy crit state.

Researchable Engines:
* Nuclear Engine: Lasts longer and produces more power than other engines, giving the IPCs a 5% speed boost, but requires the handling of uranium, which will cause the IPCs to receive unwanted damage.
* Infinite power and a 10% speed boost, but deals passive radiation damage while the IPC is alive, requiring constant repairs if they are to be kept alive.

Other Engines:
* Syndicate Engine: A nuclear operative only engine, essentially works like the RTG engine without the speed boost and irradiation but is immune to EMPs.

## Oil and Blood
IPCs will use oil as their blood. In machines, oil is used in lubrication, cleaning and cooling. All this to say that, the lower the oil, the slower they get. They cannot regenerate their oil either due to being inorganic, so they have to keep an eye on it!
Certain chems will regenerate their oil, such as:
* Oil: The thing they bleed. If it's leaking, scooping some up and reinjecting into it will help a little, but it's only a stopgap solution.
* Space Lube: Saline equivalent, great at restoring the oil of IPCs.
* Ice: Not very good at restoring oil and it cools down the user, potentially causing damage, but it may be useful in a pinch.

## Organs and Body

IPC body parts and organs are mechanical, and as such are not craftable through the bio generator. Instead, the roboticist is able to craft them through their exo fab and medbay is able to do so via their lathes.
IPCs lack some organs other species have, but still have a decent collection. 

* Brain: The IPC possesses an advanced positronic brain called Advanced Central Processing Unit (or ACPU for short). These unique positronic brains are significantly more advanced than standard Borg brains and as such cannot fit in Borg chassis and are unable to speak unless connected to an MMI. (Works the same as a normal brain and is located in the head)
* Eyes: IPCs have robotic eyes. (These eyes function the same mechanically as normal eyes.)
* Heart: The IPC heart is in reality a powerful oil pump that keeps the shiny black liquid running through their body. (Functions the same as a normal heart)
* Lungs: IPCs do not have real lungs, instead they have a fuse box. If it is removed the IPC will start short circuiting. (Similar to a normal lung, but doesn't allow them to breathe, rather just stopping them from short circuiting (asphyxiating) directly.)
* Stomach: IPCs have their engines in the place of their stomach. These engines define how the IPC powers itself. (An unique organ that will change how IPCs power themselves.)

## Healing Damage
### Brute Damage:
Brute damage can be healed with two items: Steel and Plasteel. Steel would heal 3 brute damage per steel, taking a total of 60 steel to heal an IPC from dead to full. Plasteel however is significantly more effective, healing 6 per Plasteel. Of course, they are more expensive and much harder to come by.

### Non-Shock Burns:
Burn damage, such as heat, cold and caustic, can be fixed via Plastic and Durathread. Plastic heals only 3 burn damage per plastic, but Durathread being the more advanced option will heal 6 per plastic.

### Shock Burns and Ion:
These types of damage often affect the circuitry of IPCs, requiring cables to fix. The amount healed per cable depends on the quality of the cable, being 2/4/6 for LV/MV/HV respectively.

### Radiation:
Radiation damages the more delicate and advanced internals of the IPC. To repair radiation damage, they require plasma, which would heal 5 rad per plasma (requiring 36 to heal from dead to full.)

### Blindness:
The advanced eyes used by IPCs require high grade materials to heal. These come in the form of plasma glass, requiring at least 5 of it to heal an IPC that had welded without a mask.

### Surgery:
Surgery can be done to repair damage on IPCs, similar to how it is currently done, however it would also be possible to repair radiation damage with surgery on top of burn and brute damages. (IPCs won't be essentially RRed if they go ssd near some uranium!)

## Other
### EMPs:
EMPs should have a ‘lingering’ effect, which should keep the IPC disabled for at least 10 to 20 seconds regardless of the engine installed. Electric engines would be especially affected by this as they'd have to have someone else swap their cell after the lingering effect passed or have to slowly walk to a cyborg recharger.

## Antagonist Interactions:
### Traitors & Thieves:
With new options for poisons and a nocturine-equivalent to use against IPCs (that should be added to both the sleeper kit and the uplink) and the lingering effect EMPs will have when disabling an IPC, both thieves and traitors should be better equipped to handle them both quietly and loudly.

### Nukies:
With pressure damage and a unique syndicate Engine that is emp immune, having IPCs in your nukies team should no longer be a liability.

### Changelings:
Changelings, with the addition of the lingering EMP effect, should be able to deal with IPCs much more efficiently rather than the EMP being a mere inconvenience.

### Blob:
The blob should remain largely the same towards IPCs, with the exception that it's EMPs would become significantly more effective.

### Zombie:
Zombies should also affect IPCs, growing a tumor that slowly infects them. This way they don't become either a hindrance or a counter to zombie rounds.

### Other Antags:
Other antagonists such as wizards, ninjas, dragons, cults, etc do not have as many deep rooted issues with IPCs that need to be addressed.

## Addressing Current Issues:
Many issues with IPCs have been brought up, and I hope to address them all:

### “IPCs are not threatened very much”:
With these changes IPCs should have ways to be dealt with by all antagonists that previously had struggles against them. Traitors, changelings, even nukies will have better interactions against them. Not only that, with the addition of barotrauma damage and the modification to their health pool and critical state they should be significantly weaker in combat, making them no longer the optimal species to fight all antagonists.

### “Security being the department with the most IPCs is concerning”:
Now significantly weaker in combat, IPCs will no longer be the go-to security species. Oftentimes having IPCs as security may be an issue especially when dealing with enemies equipped with EMPs. This should hopefully deal with the issue of power gaming via choosing the best species to deal with station threats. IPCs will no longer be able to simply waltz into space with some winter clothes either, they'll require proper space protection and, depending on the engine they use, even an air supply.

### “IPCs are inconsistent with cyborgs”
Hopefully by making so that medbay can also print their limbs and that their brain does not work like a positronic brain, we can increase the gap between cyborgs and IPCs enough that they will be shown as their own unique species. Much like medbay can print limbs but not rebuild a person from scratch, robotics shouldn't be able to do it either, as the resources required for such advanced manufacturing wouldn't be available in a fringe research station.
With the modification of the brain it should also show that the IPCs aren't cyborgs, but rather quite different and significantly more advanced, and because of that they cannot be built, only repaired. Hopefully this should be enough to show new players that IPCs cannot be built like cyborgs.

## Final Considerations:
IPCs are a species that many love in Funky. Several IPC characters are seen every day, some becoming iconic or even a staple of everyday funky rounds. Hopefully with this rework of IPCs, most if not all of the current issues plaguing the species can be resolved, and we can return to hugging the stupid little robots we love.
