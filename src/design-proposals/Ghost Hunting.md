# Ghost Hunting

| Designers | Implemented | GitHub Links |
|---|---|---|
| SophiaImpetus | :x: No | TBD |

## Overview

Revernant will be removed and replaced with three ghost role minor antagonists, the Poltergeist, Phantom and Nightmare, who are themed around causing disaster, possessing crew members and spreading madness and fear respectively. 
These occult threats will require occult methods to overcome, so the Chaplain and Librarian will be enhanced to be the ones capable of overcoming them using magical rituals and implements. 

## Background

Nanotrasen is a miserable corporation to work for in funky's canon. Workplace accidents, murders by corporate climbers and other tragedies are going to be common. In a setting with many occult influences, these conditions are bound to lead to stations being haunted by the tormented souls of their former employees. Why else would Nanotrasen bother to keep a dedicated and armed chaplain on payroll, one not even guaranteed to share faith with any other crew member, except to use their expertise to exorcise these threats and ensure deceased crew members pass on to the next without returning to haunt a station (and thus lower profits).
Unfortunately, this isn't fully realized right now.

The current revernant implementation is boring, full of bugs and exploits, and worst of all, fails in all aspects to simulate the experience of ghost haunting. The ghost experience currently is, wait for a ghost to appear, then punch it in the face with your fist until it dies. 
The chaplain currently has under implemented ghost hunting features like the holy damage null rod weaponry and the spectral locator, but the practicality and likelihood of ever hunting a revernant with them is so low that their inclusion in the chaplain's toolkit is constantly questioned. In order to justify their inclusion and give chaplain more reasons to interact with the crew the chaplain has been given occasional interactions with cultist type antagonists, but this effectively just makes the Chaplain a special security officer on certain rounds and doesn't contribute anything to others. 
Additionally the librarian is in a sore place. The Librarian is a role who is tasked with running a section of the station that crew will never want to frequent, due to the total absence of things to do there. Attracting people to the library as a librarian takes great effort and commitment, such as planning a game of carps and crypts, and while doing things like this can be fun it is also an insular experience. 
These issues can be resolved together by creating new replacement ghost antagonists that much better fit the role of being an occult, incorporeal threat, and placing the Chaplain and Librarian as the ones equipped to resolve the threats, in order to give more shape to their position on the station, encourage interactions with them over the course of a round and engage them in the story of the round without requiring them to act out of character.

The chaplain also stands in stark contrast to the array of occult antagonists in the game who have to go out of their way to perform their magic, or at the very least make more of a spectacle of the magic they do perform. If the chaplain is using faith-granted magic on the station, the systems the chaplain uses should feel authentically occult too. The goal of the ritual books system in this design document is to add more of the ceremony expected in the performing of miraculous acts. 

## Features to be added

### Ritual Books

Ritual books are the method through which lesser beings can access spellcraft. A ritual book that has been opened and is held in one hand and a drawing implement held in the other lets you draw a ritual circle. With this ritual circle you can perform rituals by clicking on it with an open ritual book in your other hand, selecting a ritual from a list menu, placing the required items inside the circle, then clicking the circle with the Ritual Book to say the words to perform the ritual. A ritual circle can be erased as any graffiti would be. Ritual circles should not overlap with each other or any graffiti or any puddle as that would make them invalid. 
Clicking on a ritual circle without the appropriate ritual book open displays the message "You have nothing with which to decipher the purpose of these runes". The Chaplain and Librarian instead receive the message "This looks like a ritual circle drawn with X, configured to perform Y." where X is the ritual book used and Y is the selected ritual.
Some rituals have immediate effects, while others prepare spells. By default, anything used to perform rituals are consumed by the spell.

### Spellcasting

Spellcasting is a general system for casting spells from ritual books.
The average crewmember can prepare one spell, and spells cast are removed on use. 
The Librarian and Chaplain are able to prepare a greater number of spells, both being able to prepare three in total. 
Heretics and Wizards could also operate under this system, with their own sources of power from the mansus and years and years experience waiving the cost of prepared spells being removed after casting. Instead, they would be able to manually dismiss prepared spells through a ability they have.
By default all spells require the use of a Focus to cast even after being prepared, with most Ritual Books serving as a valid focus while open. The Chaplain's null rod items also double as a focus for their spells, and the Librarian will have a magic staff focus that doubles as a cane.

### Chaplain Curse Immunity

The chaplain is immune to any effects designated as a curse, and can handle cursed items without issue.

### Librarian's Staff

A unique magical staff with an Alexandrite gemstone. When wielded, acts as a focus for spells. Acts as a cane at all times. The Alexandrite Gemstone gives the staff the ability to do spirit damage.

### Gemstones

A variety of gemstones are added, which are common components for spells and rituals. These gemstones are Diamond, Ruby, Sapphire, Emerald, Alexandrite, Angelite, Tourmaline, Citrine, Amethyst, Malachite and Cinnabar.
Gemstones can be obtained from mining sparking spots in rocks, having engineering use the crystalizer to produce gemstones, or ordering them individually via scrip (or in bulk via spesos). Due to their usage in primarily harmful spells and rituals, Malachite and Cinnabar cannot be ordered by scrip or spesos. (Traitors may be able to bypass such restrictions on purchasing them with Scrip).

### Chaplain's Ritual Books. 

Chaplain can pick one of a selection of ritual books, though the difference is just cosmetic. The covers of the ritual books are based on the altars on the station, and books can be used with an altar to either transform the altar to match the book, or the book to match the altar.

All Chaplain Books contain the following Rituals, which directly combat ghosts and allow the chaplain to perform occult miracles.

* Transmute Holy Water - Ritual that transmutes any water in the circle into holy water. 
* Prepare Rebuke Spirits - Ritual requiring Angelite, Salt and 30u of Holy Water. Prepares Rebuke Spirits, a spell which stuns and reveals any ghosts in a fairly large radius.
* Prepare Destroy Undead - Ritual requiring a bluespace crystal, Angelite and Silver. Prepares Destroy Undead, a spell which deals heavy Spirit and Brute damage to magical undead.
* Prepare Lay on Hands - Ritual requiring A Diamond, Gold, Silver and Holy Water. Prepares Lay on Hands, a spell which heals 60 of each damage type from a living person.
* Remove Curse Ritual - Ritual requiring Holy Water and Gold, and paper with the name of the curse or cursed item written on it. One person standing in the ritual circle will have the curse written on the paper removed from them, or the cursed item equipped will be unequipped and dropped. 
* Make Familiar Ritual - Ritual requiring a Diamond and an animal placed in the ritual circle. Any animal placed in the circle will be transformed into the familiar of the caster, if not already player controlled becomes available for ghosts, and gains damage resistance and spirit damage added to their attacks, and gains the Familiar alignment. Familiars lose their magic if they die, returning to normal. You can only have one familiar. 
* Prepare Recall Familiar - Ritual with no requirements to use. Prepares Recall Familliar, a spell which, after a telegraphed do-after, teleports your Familiar to your position over any distance at the cost of briefly stunning your familiar during the casting and after the cast ends.

### Introduction to Spectral Parascience

Librarian's ghost battling book. Contains the following rituals, building a less direct method of defeating ghosts.

* Spectral Prison Ritual - Ritual requiring Tourmaline, Citrine and Amethyst alongside 50u of salt. Transforms the ritual circle itself into a Spectral Prison which will trap any ghosts traveling over it inside, causing them to be revealed, lose a portion of their essence over time, and be unable to leave. This is not a full stun, ghosts inside a Spectral Prison can still talk. or even use abilities if their essence regeneration is high enough, or they have only just been caught and not drained of essence. The Spectral Prison will break after absorbing enough essence, making it dangerous to keep a ghost for too long, especially stronger ghosts. Spectral Prisons are invisible to ghosts not trapped inside one, but still function as a ritual circle for this spellbook to the librarian. A spectral prison will also trap anyone possessed by a ghost inside.
* Metaphys Goggles Ritual - Ritual requiring Sapphire and a pair of glasses. Metaphys Goggles, when worn, grant information about ghosts when examining them such as the items required to banish them with the Banishment ritual, and their true names. 
* Call Spirits Ritual - Using a piece of paper with a ghost's true name on it, Alexandrite, Angelite and Tourmaline, summons the ghost specified to the location of the ritual. This method fails against a Phantom that is currently possessing a body. Using this without creating a Spectral Prison is probably a bad idea.
* Banish Spirit Ritual - Using a ghost and all of the items listed in their banishment ritual requirement, banish a ghost from the station, permanently.
* Prepare Nightmare Passage - Ritual requiring Emerald and Tourmaline. Prepares Nightmare Passage, a spell which lets you touch someone trapped in the Nightmare Realm and breach into the dream. Unlike those who have been cursed, you are able to attack and do damage to entities in the realm, providing you bring a source of spirit damage with you. Using this spell forces the Nightmare to return to their realm and locks them inside so long as you remain there. Defeating the Nightmare or any of the Greater Figments inside the realm will kill it as normal. Leaving the realm is a action you can take freely (with a interruptible doafter). However, dying in the nightmare realm does extreme backlash to you killing you permanently as your head explodes from the psychic feedback. 

### Necronomicon

Ritual Book exclusive to the uplink. Not exclusive to the chaplain, but the chaplain and librarian will be able to use it at maximum effectiveness. Due to the wide range of utility the item grants (summoning possibly unlimited minions, persisting after death, dealing damage magically, and having leverage to cooperate with spirits or heretics), this item should be extremely committal and cost over 100 TC, requiring traitors to buy it with shared TC, be DAGD or find it on sale in order to buy it.

Contains the following rituals.

* Summon Cerberus - Ritual requiring the corpse of a dog and an active reagent fire. Summons Cerberus.
* Prepare Inflict Wounds - Ritual requiring any rotting animal corpse. Prepares Inflict Wounds, which does heavy brute and genetic damage over a few seconds when cast on someone. 
* Prepare Curse of Decay - Ritual requiring any rotting animal corpse, Malachite, Alexandrite and Emerald. Prepares Curse of Decay, a spell which subtly curses a target to periodically experience agonizing pain and have one of their organs rot away at random, replacing it with a non-functional rotten version.
* Prepare Elegy of Malice - Ritual requiring a bluespace crystal, one of your own severed body parts, Tourmaline and Malachite and Alexandrite. Prepares Elegy of Malice, a spell not requiring a focus which casts automatically on death (you can cast it early, but it kills you) and transforms the caster into a Phantom that retains your current alignment and goals.
* Transmute Unholy Water - Ritual requiring a container with water and malachite and cinnabar. Does not consume the gemstones. Converts the water in the container into Unholy Water, which can be used to heal magical undead (including ghosts, cerberus, and ghouls). Harmful when consumed by the living.

### Ghost Minor Antagonists

Three ghost minor antagonists are to be added. These minor antagonists can spawn as ghost roles in a round. As they are designed in a way which makes them difficult for anyone but a chaplain and librarian to combat, there should be a cap on how many can spawn in at any one time, probably one of each type maximum. 
Other midround antagonists spawning should not stop the ghosts from spawning. The current midround antagonist spawns are all problems solved with gunfire, often all hands on deck situations. Ghosts don't have the same impact as an antagonist, nor do they increase up the workload of the same department, so it should be safe for these to exist alongside each other and raise the overall number of ghost roles available in the round.
The ghost minor antagonists existence are not metashielded nor corporate secrets. However, the average crew member probably shouldn't act like a ghost expert, nor should security or command. That's the chaplain and librarian's job. Knowing basic things like "salt can reveal and slow ghosts down" or grabbing something that is effective at damaging ghosts, if you experience activity that is obviously ghost related, is probably fine. How much you can know as a average crew member is intentionally left vague. 
These antagonists each share the following traits. 

The ghosts are immune to all damage types with the exception of Spirit damage. 
The ghosts can pass through solid walls and are invisible unless an effect explicitly reveals them, at which point they are beholden to collision and visible to the living. 
Ghosts don't have omniscient vision, they can't see through walls. 
Ghosts do not move very quickly while invisible to crew. Crew members should be able to easily outrun or chase ghosts.
Ghosts are slowed and forcibly revealed by pools of salt.
Ghosts are stunned and forcibly revealed by pools of holy water.
Ghosts are destroyed when reaching 0 Spirit.
Ghosts regenerate essence over time, up to a cap, and spend their essence to use the various abilities they have unlocked.

### Poltergeist Minor Antagonist

Poltergeists are one of the three Ghost Minor Antagonists. 
Poltergeists feed off of the pain others around them experience. When a being with a soul takes damage near a Poltergeist, the Poltergeist gains Consumed Pain to spend on abilities. 
Poltergeists have no intrinsic goal other than to gain as Consumed Pain as possible. The consumed pain mechanic and goal discourages the Poltergeist from trying to use their abilities for mass station destruction, dead crew can't feel pain, and damage that occurs away from the poltergeist provides no benefits.

Poltergeists start with 50 Spirit and 50 Essence. 

Poltergeists start with the following abilities:
* Spend 2 essence to draw in crayon.
* Spend 20 essence to temporarily be able to pick up and throw objects for five seconds.

Poltergeists unlock the following abilities through Consumed Pain.

* Defile, which gradually damages random nearby windows, spreads dirt and stains on floors and walls, causes food and drinks to become rotten (filling it or partially replacing it with mold reagent), plants wither, and tiny animals may spontaneously explode into damaging gore. The effects take place over a duration during which the poltergeist is fully revealed, and the poltergeist can move around while this ability is in use, moving the area of effect about as well. Any lights around the Poltergeist will flicker independent of the random rolls and targeting for Defile's main effects. The Poltergeist WILL aurafarm.
* Overload Lights, which is rebalanced to actually shatter lights, flinging out glass shards which can embed into people as well as shocking and stunning and burning.
* Ignis Fatuus, which, after a telegraphed delay, creates a flame which can light fires on reagents, gasses and anyone standing on it. The flame floats towards the closest living creature in line of sight, but does not attack.
* Tamper, a expensive ability which has various effects depending on the target, including the following. Loose wearables will become cursed to be impossible to unequip, fluid and gas storage will spill some of their contents if not locked, machines like the lathes, anomaly generator, microwaves, artifact crusher, AME (not other power engines), even syndicate bombs, will all activate with random settings. Doors will become shocked and have their accesses wiped so nobody has valid access. Devices like APCs, Substations, other binary on and off devices will be switched to their other state. Bots will shock crew they touch until fixed with a screwdriver. 
* Desecrate, a more powerful and more expensive defile that inherits the effects of defile and additionally does increased window damage and has a chance to rip out wires, obliterate disposal chutes, destroy tables, unanchor objects, and fling loose objects into any living creatures in the radius. Lasts for a much longer duration.
* Expand Spirit increases spirit by 30. This is the only way to recover spirit. Each use increases the cost of the purchase.
* Expand Essence increases essence by 20 and increases essence regeneration by 50%. Each use increases the cost of the purchase.

### Phantom Minor Antagonist

Phantoms are one of the three Ghost Minor Antagonists.
Phantoms spawn with a goal, typically to kill one or more targets, and achieve their goals by possessing the body of a crew member not targeted by their goals, who's mind is not shielded by technology or magic, nor too powerful or alien to manipulate (can't possess mindshielded crew, cultists, chaplain, changelings, wizards or heretics). Once they pick a crew member to possess, they enter that crew member's body, but can't immediately puppet the crew member. Leaving someone's body after integrating with it is a damaging act that inflicts 100 spirit damage. In addition, any spirit damage taken by bodies you inhabit is dealt to you. Puppeted crew members that are not in critical condition or dead can talk, and should be able to struggle in other ways such as having an ability with a cooldown to drop items or regain movement control briefly.
Phantom's gain power by draining the body and mind of the person they are posessing, as well as every time they take control. They can spend this Drained Power on additional abilities to use when posessing a crew member.

Phantoms start with 50 Spirit and 10 Essence.

Phantoms start with the following abilties: 
* Spend 10 essence to possess a person, entering their body.
* Spend 10 essence to Drain Sustinance, taking away your victim's hunger and thirst, granting drained power.

Phantoms can unlock the following abilities with Drained Power.
* Drain Vitality, inflicting major airloss and bloodloss to your victim causing gasping and dizzyness, granting drained power. 
* Nudge, an ability which lets you very briefly force your victim to do something such as walk in a direction, trip, use their held item.
* Drain Substance lets you feed on your victim's physical substances and starts to convert your victim's "unnessecary" matter into a viscous, sticky and flammable tar. For the duration your victim takes minor poison and genetic damage, drips tar occasionally, and has a chance to vomit tar. Provides a substantial amount of Drained Power.
* Deathly Grasp lets you grab and pull someone while preventing them from escaping for a duration. They are not restrained and can still take other actions against you.
* Float lets you spend essence per second to ominously levitate your victim while taking control of them, making them unable to be slipped and making them move faster, ignoring hunger, thirst, pain or stun.
* Spew Tar lets you spend essence to force your victim to spew fourth sticky, flammable tar towards a target. Targets hit by the tar will be knocked down briefly and take blunt damage. Your victim takes poison damage from the tar in their body as it metabolizes.
* Unearthly Smash lets you spend essence to cause your victim to attack a target with extreme force, doing high blunt and knockback as well as and extreme structural damage at the cost of completely breaking the limb that was used to attack. 
* Puppet lets you take control of your victim for 1 minute. 15 min cooldown after control is given back to your victim.
* Corpse Puppet, a passive ability that lets you continue to control your victim even after their death, at the cost of any further damage dealt to them being dealt to you as spirit damage. Once you have this ability, if your victim dies, you take over control automatically.
* Increase Control permanently increases your time controlling a victim with your take control ability by 1 minute on each use. Each use increases the cost of the purchase.
* Expand Spirit increases spirit by 30. This is the only way to recover spirit. Each use increases the cost of the purchase.
* Expand Essence increases essence by 10 and increases essence regeneration by 100%. Each use increases the cost of the purchase.

Letting a player possess and thus greatly impact someone's else round requires a lot of trust in players who become Phantoms. While this power can definitely be used for good, there is also a risk of power gaming in unfun ways by only possessing players you know to be a traitor or thief or otherwise have powers you believe useful. These issues could be mitigated by some or all of the following options.
* Have a trait which makes Phantoms unable to possess you, selectable in the trait menu.
* Extend possession immunity to all antagonists, even if there is no in-character explanation for this.
* Randomly select a handful of crew you are able to possess upon becoming a phantom, forcing you to select one crew member from those options instead of select from the entire crew on the station.


### Nightmare Minor Antagonist

Nightmares are one of the three Ghost Minor Antagonists.
Nightmares feed off of fear, and wish to frighten crew and eventually kidnap them into a nightmare world wherein the crew members are captive audiences to their antics. Unlike Poltergeists and Phantoms, they don't interact at all with the physical plane and are only powerful insofar as they can warp and disturb the minds of the crew on the station.
Nightmares gain Consumed Fear when taking actions that are witnessed by crew and spend it on abilities. 

Nightmares start with 30 Spirit and 100 Essence.
Nightmares start with the following abilities:
* Spend 2 essence to draw in crayon.
* Spend 20 essence to pick a new, scary disguise to appear as when appearing corporeally. 
* Spend 0 essence to become visible to crew, in your horrifying form. Being witnessed generates consumed fear, attacking crew in your illusory form generates more, but does no damage.
* Spend 0 essence to transport between your current location and your nightmare realm.
* Spend 20 essence to shape your realm by creating a new object inside. Or removing an object.
* Spendf 0 essence to politely break a crew member's Curse of Somnia, releasing them from your realm if they were inside it.

Nightmares can unlock the following abilities with Consumed Fear. 
* Figmentary Enemy summons an illusory creature of your choice which attacks anyone nearby (though these attacks do no damage). The creature lasts 2 minutes but are vulnerable to spirit damage.
* Curse of Somnia subtly curses someone. The target periodically falls asleep, during which time they are transported to your nightmare realm. These episodes last for around a minute if nobody else is there to wake them from their sleep. The starting number of people you can have cursed at once is three, and trying to curse more than the maximum will always fail.
* Curse of Abberance subtly curses someone. After a random duration, the subject begins to mutate and transform into a monstrosity, at least visually. They appear to others as a space monster of some kind, but this is purely a visual illusion. However, the curse also takes away the person's ability to talk or emote. Only death will reveal the illusion for what it is. Anyone who sees someone transformed by the curse grants you fear.
* Greater Figmentary Enemy summons a illusory creature of your choice which is controlled as a ghost role. It can travel between the station and the Nightmare Cage at will, talk, toggle its visibility to others, and may have additional abilities beyond that of a regular figmentary enemy would have. This could have some funny unique options of creatures to spawn that work better through roleplay, like a demonic clown, or a scary IAA who chases you through walls to present SoP violation paperwork.
* Nightmare Cage forces a target whom is already inflicted with Curse of Somnia to go to sleep, with an additional visual indicator showing this nightmare is of the more permanent kind. Without a remove curse spell, they are trapped permanently in the nightmare realm.
* Expand Spirit increases spirit by 20. This is the only way to recover spirit. Each use increases the cost of the purchase.
* Expand Essence increases essence by 50 and increases essence regeneration by 75%. Each use increases the cost of the purchase.
* Expand Somnia increases the number of people who can be afflicted by the curse of Somnia by 1. Each use increases the cost of the purchase.

### Nightmare Realm

A small Z level not unlike the cosmic cult area you are sent to when slept. Should be scary. Unsure if there should just be one type, or if a Nightmare should be able to pick a theming to their realm. I.E. Xeno Hive, Nanotrasen Blacksite, shadow anomaly type forest.
Damage in the nightmare realm FEELS real, but dying inside it will instantly wake the person up, unharmed in the real world. 
The dream bodies of crew in the nightmare realm are however unable to damage to themselves or anything else in the nightmare realm, preventing them from waking themselves up by hitting themselves... But not by deliberately waking into a death trap of some kind, so there is still a chance of escape if left unattended inside the realm.
People inside the nightmare realm create more consumed fear when interacted with than people in the station proper, so its worth harassing them and not just leaving them alone in there or something.
If the Nightmare dies, the realm is destroyed and anyone stuck inside awakens with the curse of Somnia broken.
 
### Tier 2 Civilian Research: Ghost Hunting

Science can research this package of tools in order to supplement the chaplain and librarian's ghost hunting, or fill in for them in their absence from the station.

The package includes.
* Ultraviolet Lantern, a lantern which reveals ghosts in a radius around itself when turned on. 
* Ultraviolet Bulbs, lightbulbs that can be installed into light sockets that reveal ghosts in their radius. 
* Spectral Ray Magnifier, a clunky ray gun that fires spectral rays that have spirit damage. Recharges at weapon charging stations.

### Tier 3 Civilian Research: Ghost Busting

Science can research this package of very powerful tools in order to deal with a very serious ghost problem. These tools greatly eclipse the chaplain in effectiveness, but may prove the only way to destroy a powerful poltergeist.

The package includes.
* Hyperviolet Flashbang, a flashbang which reveals and stuns ghosts in the radius.
* Hyperviolet Portable Flash, a Portable Flash which repeats the Hyperviolet Flashbang effect, to secure areas from ghosts.
* Hyperviolet Sunglasses, sunglasses which protect crew working in the area from hyperviolet flashes.
* Spectral Beam Gun Pack, a weapon which fires a beam dealing heavy spirit damage to anything it strikes. Requires a power backpack with a power cage to power and shoot the weapon.

### Ghost Killer Cargo Crate

A very expensive cargo crate that contains tools for when you just need to KILL a ghost.

This crate contains the following items.
* Silvered Sword, a blade with heavy Spirit attack power. 
* Silvered Mace, a mace with heavy Spirit attack power.
* Silvered Spear, a spear with heavy Spirit attack power.
* Spectral Pinpointer, a unique pinpointer combined with spectral locator which points the way to the nearest (antagonist) ghost.
* Holy Water Foam Grenade Box, a box of grenades that release a huge spread of holy water foam, enough to stun and reveal any ghost for a long time.

### Remilia

As chaplains can now bind any animal as a familiar, Remilia will be a roundstart chapel pet instead of being summoned from the bible. 

### Holy Damage

Holy damage is renamed Spirit damage for clarity. Spirit damage is still only effective against spirits.

### Adjust Chaplain Null Rod Items

All Null Rod weapons are consecrated and enchanted to only harm ghosts. Non-Spirit damage components (with the exception of stun or structure type damage) should be removed from the weapons and the holy ammunition. 
All Null Rod items, weapon or not, count as a spellcasting focus when held.

### Adjust Chaplain Altars

Chaplain Altars emanate radiation that does spirit damage to any ghosts in its aura, fortifying the chapel against ghostly threats by dissuading their exposure. Ghosts being irradiated with spirit damage via altars should be notified with a noise.

### Adjust Chaplain ERT

The Chaplain ERT should be equipped to excel in hunting and destroying ghosts, which is expected to be the primary reason chaplain ERT is called. ERT Chaplains should arrrive in a shuttle that is stocked with a holy water tank, several salt buckets, plenty of materials for rituals, a ghost pinpointer and several boxes of holy water foam grenades, Every squad member should have copies of both the chaplain and librarian ghost hunting ritual books and Metaphys Goggles, along with backup Silvered weapons to supplement their choices of null rod item in case a non damaging option is picked.

### Adjust Chaplain SoP

Chapalain SoP is rewritten to reflect the new gameplay for chaplain.

1. The chaplain must investigate any hauntings that crew have reported.
2. The chaplain is free to conduct rituals anywhere on the station as necessary. 
3. The chaplain must not distribute their ritual book or weaponry to any other member of the station under any circumstances.
4. The chaplain is free to practice any religious beliefs that are not subversive or dangerous to nanotrasen and do not require harm or discrimination against nanotrasen station employees.
5. The chaplain may preach their faith to attempt to convert others, provided it is not in an excessive manner and that faith does not breach SoP point 4.
6. The chaplain may not withhold performance of any service or duty based on another crewmember's faith, and may not personally attempt to determine or enforce that another faith or doctrine of that faith is subversive, dangerous, false, and otherwise undesirable as this is the purview of Nanotrasen officials.
7. The chaplain should ensure the postmortem instructions of all unrevivable personnel are followed. In absence of postmortem instructions, a funeral should be held on station. All funerals should be concluded with the use of the crematorium. Funerals with special requests for the disposal of the body's remains, before being conducted by the chaplain, must first be authorized by the Head of Personnel. Failure to put to rest the spirit of non-revivable personnel in a reasonable timeframe is considered a breach of SoP. 

### Librarian SoP

Librarian now has SoP.

1. Ritual Books that are stored in the library must not leave the library without HoP permission.
2. If a Ritual Book is removed from the library with permission, it is the Librarian's duty to ensure the book is kept track of and the conditions of its removal are adhered to.
3. The Librarian is permitted to facilitate the use of rituals and casting of spells from Ritual books in their collection by other crew members, provided this takes place within the library.
4. Only the librarian is permitted to cast spells from their ritual books outside of the library. 
4. The Librarian is to secure and prevent the distribution of any Ritual Books or Literature which may be subversive or harmful to Nanotrasen. If the Librarian deems such literature too dangerous for the Library, it must be moved to the Vault at the soonest time possible.

### Code Magenta

Threats from ghosts shouldn't warrant calling any alert (even blue) in most cases as it's not security's role to deal with them, the threat isn't "on-board the station" in a physical sense, and the tightened security measures under blue would not be effective in combating ghosts at all. 
However, in cases where there are a number of ghosts which are overwhelming the abilities of the chaplain and librarian to deal with, or a ghost has become so powerful it is threatening to cause extreme station disruption (Perhaps a Nightmare is able to sleep half of the crew population at once), then Code Magenta should be called.
In most cases where there is a Chaplain or Librarian on board, code magenta should be requested by them in communication with the HoP, rather than command calling it the moment they see a ghost do something to them. It should be treated like Code Cyan as a special alert level for when things have gotten far out of hand - you wouldn't call code cyan just because one borg was emagged or a derelict borg with dangerous laws drifted into the station.

Under Code Magenta, crew should listen to the directions of the Chaplain, or the Librarian if a chaplain is not present. All non-essential work should cease and essential work should be supervised by crew able to defend from ghost activity, ideally areas in which essential work needs to be done should be secured against supernatural threats. Crew who had been doing non-essential work are expected to congregate at secure locations, such as areas with alters or areas with hyperviolet portable flashes, and security is allowed to arrest crew for endangerment if they fail to move to the declared locations. The Chaplain and Librarian are allowed to temporarily grant ghost hunting equipment and prepare ghost hunting spells for any crew members who they deem competent and trust. This equipment is to be returned after Magenta Alert is dismissed.

### Wizard and Heretic focii

Any item that counts as a focus for the heretic or the wizard, I.E. Robes, Codex Ciratrix, also counts as a focus for casting all other spells prepared from ritual books.

### Adjust Changelings

Changelings are not magical. They have limited magical potential, being able to use magical items, but not perform magic.
Changelings can't prepare spells, or perform rituals. Changelings both harvest and can morph into Quylons, but don't experience attenuation and can't create ritual circles. 



### Removals

* The Bible is replaced by the expanded chaplain ritual book system.
* Revernant is replaced by directly by Poltergeist, indirectly by Phantom and Nightmare.


## Game Design Rationale

The features added are intended to address the points mentioned in the background and create opportunities for types of roleplay that don't exist in funky currently. 
The Nightmare's magical kidnapping, the Phantom's ability to "take over" someone without actually being a conversion antagonist, as well as the ghost hunting mechanics in general are all things that touch on storylines currently unrealized or rarely realized. 
Adjustments to chaplain's SoP will better reflect their role on board the station, their relationship to Nanotrasen, and add a lot more opportunities for conflict with the IAAs and Nanotrasen who may choose to more closely scrutinize the beliefs and activities of the chaplain in the same way they would for any other job that can disseminate ideas, such as the reporter. 
While the chaplain and librarian being the main ones tasked with defeating ghosts is a break from the standard of security being the ones to deal with antagonists, this isn't an issue any more than salvage being asked to help kill a space dragon. The Librarian and Chaplain do not have to investigate crimes, uphold space law or be trusted with lethal weaponry. Ghosts are not crew members or employees, certainly not anymore, and don't need to be treated with any kind of due process as their malevolence is unambiguous. Moreover, having non-security personnel combat this ghost role makes it possible to have more interesting ghost role spawns without completely overwhelming a department, and moves the game away from the idea that the main gameplay of each round is "security vs the bad guys". 
The gemstones are a new valuable that can be sold or utilized to reward salvagers mining and engineers using the crystalizer, providing another small way in which they might interact with others and others might need to interact with them.
These features also lay the groundwork for future features that may be conceptualized. The Ritual Books system could be integrated into heretic or wizard reworks, new ritual books can be created for other purposes as well. 

### Seriously Silly

The abilities of the ghost antagonists have a huge potential for both drama and comedy. A poltergeist can spill a container of welding fluid to slip someone unsuspecting running by with a lit cigarette. Phantoms can force someone to, against their will, kill the crew member they had been bonding with throughout the round while they scream and protest. The ghosts should be able to be creative, threatening and silly with their hauntings. 

### There is no Winning or Losing

 For Poltergeist and Nightmare, there is no objective other than contribute to the story by roleplaying your hauntings. Your reward for roleplaying these hauntings is being able to continue to roleplay the hauntings in ways which have greater impact, and to survive for longer to continue the roleplay. Consumed Pain and Consumed Fear are designed in such a way that there shouldn't really be a "best" way to go about it, and creativity will certainly be a lot more fun than treating it as a number goes up game. The Phantom has specific goals, but is designed around the push and pull of trying to wrest control from the person you are possessing, being an affliction on them, and having them resist you as much as they can. The goal is the incentive to create this roleplay scenario, and the crew member you have possessed using a loophole to avoid following your command or successfully resisting you and helping your target flee the scene at a critical point is just as interesting of a story as successfully using them to complete your goals. 

### Maintaining Authenticity

Nearly everything to be added or changed here is done with maintaining authenticity guiding it. Hauntings by ghosts will be more authentic, the ghosts will be actual incorporeal entities who you can't simply shoot to death with a gun and who's impact is designed around causing situations that should be inexplicable, spooky, immersive and not simply waiting around dead bodies until you can slurp the soul out when nobody is looking. There will be a much larger number of ways in which you will interact with the ghost antagonists in order to make sure they are not just a generic threat for the dedicated threat shooter to shoot. 

## Roundflow and Player Interaction

As the ghosts are minor antagonists that will only show up as a midround ghost role, ghosts will begin to come into play after some time has passed in the round. Some rounds might not spawn any, but they should be a fairly common sight, at least as common as seeing heretics. If ghost activities are suspected to be the cause of some accident, reports of monsters or an affliction a crew member has, service should be informed for the Chaplain and potentially Librarian to investigate and seek more answers. A clever ghost player doesn't have to be stealthy (but can work to hide their presence or make it ambiguous), but will likely move ther haunt from location to location to be a step ahead of attempts to hunt them down. The ghost hunters may choose to lay traps using salt, utilize ghost hunting tools like the Ultraviolet Lantern to patrol areas and reveal ghosts, and will have to give their aid to crew members who have been cursed or possessed. 

Ghosts will not be metashielded to crew. Due to this however, other crew, especially command and security, have to be willing to let the chaplain and librarian deal with these threats when they occur, rather than demanding science unlock ghost hunting or cargo buy the ghost killing crate in order to arm security against ghosts and bypass the intended ways of interacting with ghosts. Players feeling as if the point of the game is winning against the antagonists and doing anything they can to win is not an attitude that can be counteracted fully, and the worst case is that this only works when neither science nor cargo have any of the ghost hunting tools available and the only option for a crew lacking a chaplain is to call centcomm for a chaplain ERT. However players will be incentivized to engage with the antagonist in the spirit it is designed because that is a more fun and immersive experience than "winning". The intangibility and invisibility of this threat should contribute to guiding this type of interaction, crew members can no longer see a ghost and instinctively know the correct thing to do is punch the ghost over and over. Inexplicable things will happen, crew might have an suspicion that this is caused by ghosts, but they will have to seek out shelter and aid from the chaplain or librarian to begin tracking this ghost down and getting to the bottom of the mystery. In general the crew should not be reaching for the ghost hunting tools science and cargo can procure from the station unless Magenta Alert is active, which is an alert level that the Chaplain and Librarian are supposed to advise when to call.
In a similar vein, the chaplain and librarian should not be over-preparing for a potential midround threat by pre-emptiviely stockpiling materials and distributing ghost hunting items before a ghost has appeared. The other duties they have and roleplay aspects of their job should come first until a haunting is reported somewhere. Its okay for a chaplain to have already prepared some spells, or a librarian to have already made emerald goggles, but this would be the limit of due preparedness. The fact that the items all have associated costs and delays to obtaining them will make clear that overpreparedness is a waste of company money and time to engage in.

## Administrative & Server Rule Impact 

Poltergeist can use Tamper and Desecrate to perform acts that may cause large levels of station damage, such as large explosions, reagent fires, spacing and even being able to damage critical cabling infrastructure. Poltergeists are intended to be capable of harm through sabotage, and are harbingers of even great disasters, but are not intended to actively seek to end a round. Ensuring poltergeists gain no benefit from dead crew is supposed to nudge players towards the idea that causing too many mass casualty events, especially ones where the poltergeist is not close enough to benefit from, has no value and is detrimental to the long term feeding of the ghost. Some players however might need a nudge to not use their powers to arbitrarily cause damage for no purpose or to use it in a way which could, on its own, lead to significant round-ending problems. Phantoms have some potential to be used to metagrudge by possessing someone you don't like, or power game by using spectator info to pick your possession target. Some possible remedies are suggested with it if it becomes an issue. 

# Technical Considerations

The ritual books system, while similar to heretic rituals, should be treated as an entirely new system and be built from the ground up.
Based on the current buggyness of revernant, the new ghost antagonists should be built from the ground up on a fresh base. Since my understanding of the revernant bugs is that many of them stem from it being partially a spectator, I anticipate new code would treat the antagonists the same as any other creature, except with full invisibility and movement that can ignore all obstacles. 
The capabilities phantom has of spawning AI controlled creatures could have some impact on performance in extreme scenarios with huge numbers of spawned entities from the Phantoms and other events.

More input will be required to fully scope out the technical details of the design doc.


