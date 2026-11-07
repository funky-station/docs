# The Distress Beacon, and Beacon Responders

| Designers          | Implemented | GitHub Links |
|--------------------|-------------|--------------|
| cattyowo/jackel234 | :x: No      | TBD          |

## Overview

This document will outline a proposal for an alternative to ERT, which I believe has the potential to cause interesting scenarios and RP. The idea here isn’t to entirely replace ERT, but to give the crew an option to have some chance of assistance when they need it, without hopefully disrupting round flow too much. This idea is in part inspired by CMSS13/RMC14’s Response Teams feature, which I believe is a genuinely interesting idea.

## Background

Currently, ERT is only used when antags are round stalling, in admemes, or other extreme situations. While I do not disagree with this policy, as ERT in its current state can easily counter valid antag victories, I do think there is some room for improvement. I believe that the crew should be able to potentially get some assistance in dire situations, however this assistance should be either weak, unreliable, downright unhelpful in the worst case scenario, or in the best case scenario, actually helpful, but not enough to turn the tide of what would be a legitimate antag victory.

## Features to be added

### The Distress Beacon, and the Emergency Distress Protocol

Inside the Bridge of the station, there will be two small locked cabinets, with large red buttons behind glass. These cabinets will require Captain or HoP access to unlock and open, and will require synchronized activation (with some small delay of a couple seconds, just to account for internet issues and whatnot) to trigger their intended effect. When both buttons are activated, the Emergency Distress Protocol will initiate, and a new button on the Communications Console UI will unlock. This button, when pressed, will activate the Distress Beacon and put the Emergency Distress Protocol into effect, sending the station into Alert level Gamma. This will send a station wide announcement stating that the Emergency Distress Protocol has been activated, and that the Distress Beacon is now active.

### Beacon Responders

Now that the Distress Beacon is active, it will send an automated message into deep space, one that anyone can answer. Mechanically, this means that one of a list of Beacon Responders will spawn on the map nearby, spawning in several ghost roles with it, not unlike the Unknown Shuttle midround event. These Beacon Responders can be from one of many factions - some may be NT or NT-aligned, some may be neutral to NT and may need convincing to assist the crew, and some may be outright hostile to NT. In general, these responders should be weighted so that neutral responders are the most common, with NT-aligned responders being less common, and hostile responders being the least common, however with good chances for any of the three categories, as activating the Distress Beacon should be a gamble as to whether or not the responders are actually helpful.

The Beacon Responder ghost roles will all be given a small brief as to who they are in the ghost role menu, with a more in depth brief given when they choose to join the raffle. These briefs should generally be in-depth enough to give the player a good idea of what their character is, without being too restrictive on how they should play them. If possible, the Responders should receive the distress beacon signal as a message/announcement when they take over the role, and it should inform them of the name of the station, along with generic info about it. The signal should not tell them about why the beacon was activated, only that it had been, and the station that activated it.

### Example NT-aligned Beacon Responder: NT-X 012 “Trifecta” Expedition Ship

#### Background
NT-X 012 “Trifecta” would be a Nanotrasen ship sent out on an preliminary expedition to survey and research an anomalous Xenoarcheological site on a planet in a nearby solar system. Interrupted in their mission by the distress beacon, they have come to the station to assist, but ultimately want to return to their mission as quickly as possible. The crew of this ship would be NT military research team, only lightly armed as the initial survey of the planet that discovered the site determined that heavy resistance was not to be expected.

The ship itself should have an armory, a small medical bay, and a research lab. The armory should have 4 armor vests, a Lecter safe, and a N1984 safe.

#### Ghost roles

**Captain**


- This is the Captain of the ship, and the Commander of the operation. Pretty self-explanatory.
- The ghost role description would say something along the lines of:
  + *“You are the Captain of the NT-X 012 “Trifecta” expedition ship, sent on a research expedition to a nearby planet, interrupted by a distress signal coming from an NT station.”*
- The ghost role information would read:
  + *“You are an NT military Captain, and your ship has been sent on a mission to survey and research a Xenoarcheological in a nearby solar system. After hearing the distress signal, you have come to assist the NT station in need. **You don’t know why the signal was called, and you have no idea of the threats you will face.** You should seek to aid the crew however you can, although the life of your crew comes first, and you ultimately still have a mission to return to after this. NT isn’t paying you to save a station, after all. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- They should have standard Captain equipment, albeit with an N1984 in place of the laser pistol.

**Chief Research Officer**

- This is the second in command of the ship, and is the one actually heading the research done on the expedition.
- The ghost role description would read:
  + *”You are the Chief Research Officer aboard the NT-X 012 “Trifecta” expedition ship, sent on a research expedition to a nearby planet, interrupted by a distress signal coming from an NT station.”*
- The ghost role information would read:
  + *”You are the Chief Research Officer working aboard the ship, sent out to head the surveyal and research of a Xenoarcheological site in a nearby solar system. Your work was disrupted when the Captain decided to answer the distress signal coming from a nearby NT station. **You don’t know why the signal was called, and you have no idea of the threats you will face.** You should seek to aid the crew however you can, although your life comes first. You want to get back and finish your research, after all. NT can’t pay you if you’re dead. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- They should have the equipment of a normal Research Director, however with a PDA that designates them as a Chief Research Officer.

**Research Officer**

- This is the scientist working with the Chief Research Officer, and debatably the one doing most of the work.
- The ghost role description would read:
  + *”You are the Research Officer aboard the NT-X 012 “Trifecta” expedition ship, sent on a research expedition to a nearby planet, interrupted by a distress signal coming from an NT station.”*
- The ghost role information would read:
  + *”You are the Research Officer working aboard the ship, sent out to head the surveyal and research of a Xenoarcheological site in a nearby solar system. Your work was disrupted when the Captain decided to answer the distress signal coming from a nearby NT station. **You don’t know why the signal was called, and you have no idea of the threats you will face.** You should seek to aid the crew however you can, although your life comes first. You want to get back and finish your research, after all. NT can’t pay you if you’re dead. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- They should have the equipment of a normal scientist, however with a PDA that designates them as a Research Officer.

**Rifleman**
- These are the two Riflemen staffed aboard the ship, there to keep the rest of the crew safe from any threats they may face
- The ghost role description would read:
  + *”You are a Rifleman aboard the NT-X 012 “Trifecta” expedition ship, sent on a research expedition to a nearby planet, interrupted by a distress signal coming from an NT station.”*
- The ghost information would read:
  + *”You are a NT military Rifleman, staffed aboard the ship. Your ship was sent out to survey and research a Xenoarcheological site in a nearby solar system. However, the mission was disrupted by a distress signal coming from a nearby NT station, which the Captain chose to investigate. **You don’t know why the signal was called, and you have no idea of the threats you will face.** You should seek to aid the crew however you can, although your life and that of the rest of the crew’s comes first. You still have a mission to complete, and NT isn’t paying you overtime for this. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- This role would be the most unique of the ones here, as they would likely have custom equipment and clothing, but would still have standard body armor. However, for simplicity they would reuse an already existing role icon, if possible.

### Example Neutral Beacon Responder: “Waves of Gold” Luxury Yacht

#### Background

The “Waves of Gold” would be a luxury yacht owned by a wealthy space baron, unaffiliated with NT or any other major faction. The baron, upon intercepting the distress signal, was on a leisure trip through the sector. On a whim, and against the better judgement of their bodyguards, the baron decided to see what all the fuss was about, and investigate the signal. How they got their wealth is up to the player, but the main point is that the baron is extremely wealthy, enough that their wealth alone could turn the tide for either side.

#### Ghost roles

**The Baron**
- This is the wealthy baron that owns the ship, and should be a generally fickle person. It should be an effort for any side to convince them to help their side.
- The ghost role information would read:
  *“You are a wealthy space baron, unaffiliated with any major faction, who has decided to check out the distress signal on a whim.”*
- The ghost role description would read:
  *”You are a wealthy space baron, unaffiliated with NT or any other major faction. During a cruise through the sector, you intercepted a distress signal from a local NT station. You have decided to investigate the distress signal, against the better judgement of your bodyguards. How you approach this signal is up to you, and you may side with either side, or none, leaving the station to fend for itself. You don’t know why the signal was called, and you have no idea of the threats you will face. You are a Free Agent, but you are not an antagonist: you should help the side that either makes the most compelling argument, or that would benefit you the most. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- They’d be dressed in a fine suit, with a briefcase full of money and other valuables, and a PDA with a proper ID.

**The Bodyguards**
- These are the two full-time bodyguards the Baron has on staff, and their entire goal should be protecting the Baron from threats, advising them, and following their orders, in that order.
- The ghost role information would read:
  *”You are the full-time bodyguard for a wealthy space baron, hired to protect the baron, and to do their bidding.”*
- The ghost role description would read:
  *”You are a full-time bodyguard for a wealthy space baron. Your job is to protect, advise, and follow their orders as they investigate the distress beacon on a nearby NT station, against your better judgement. You don’t know why the signal was called, and you have no idea of the threats you will face. You are a Free Agent, but you are bound by the orders of your employer. After all, it’d be a dumb idea to go against their interests. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*
- Their equipment would be pretty simple, being a Mk 58, an armor vest, a white dress shirt and slacks, with some sunglasses and a PDA with a proper ID.

### Example Hostile Beacon Responder: “Trader’s Bane” Pirate Sloop

#### Background
The Trader’s Bane would be a small sloop owned by a group of pirates, looking for any goods they can steal. Upon hearing the distress signal, they came straight for it, knowing they could capitalize on the chaos to make more than a few spesos. If they can’t get any money from extortion, they’ll raid the ship for whatever it’s worth. While this is somewhat resemblant of the Pirates gamemode, these pirates wouldn’t actually be pirates in that sense, more just antags with the goal of making money from the chaos however they can. The ship is going to be fully stocked with pirate goods, with chests and barrels full of stolen goodies, grog, and rum.

#### Ghost Roles

**Pirate Captain**
- This is the Captain of the ship, and the leader of this group of pirates. It’s rather self-explanatory. They’d use the standard Pirate Captain gear, nothing more complex.
- The ghost role information would read:
  *”You are the Captain of a small pirate sloop, here to take advantage of a distress beacon coming from a NT station.”
- The ghost role description would read:
  *”You are the Captain of the Trader’s Bane, and have come to take advantage of the distress beacon coming from a nearby NT station to make as much money as you can. Whether you extort the crew for spesos or just ransack everything valuable is up to you. While you are an Antagonist, you are not to cause massive amounts of death or destruction. You don’t know why the signal was called, and you have no idea of the threats you will face. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*

**Pirate First Mate**
- This is the First Mate aboard the ship. Their goal is to oversee the safe transfer and security of any cargo the pirates may acquire, along with performing negotiations between the crew of the station and the pirates. While the Captain is the head and face of the ship, the First Mate is the one who manages the logistics. They’d have the standard First Mate gear, along with an appraisal tool in their quarters.
- The ghost role information would read:
  *”You are the First Mate of a small pirate sloop, here to manage the logistics of this piracy operation relating to the distress beacon.”*
- The ghost role description would read:
  *”You are the First Mate aboard the Trader’s Bane, and your goal is to oversee the logistics of this piracy operation relating to the distress beacon. Your goal is to make sure this operation flows smoothly, by securing any cargo, and negotiating with the crew of the station as necessary. While you are an Antagonist, you are not to cause massive amounts of death or destruction. You don’t know why the signal was called, and you have no idea of the threats you will face. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*

**Pirate**
- These are the three pirate crew aboard the ship. Their goal is to follow the Captain’s orders, and do as they say. They would have standard pirate gear.
- The ghost role information would read:
  *”You are a Pirate, a scallywag, here to take advantage of a distress beacon coming from an NT station.”*
- The ghost role description would read:
  *”You are a Pirate aboard the Trader’s Bane, here to respond and take advantage of a distress beacon to make as much money as you can. You are to follow your Captain’s orders, whatever they may be. While you are an Antagonist, you are not to cause massive amounts of death or destruction. You don’t know why the signal was called, and you have no idea of the threats you will face. You are absolutely NOT allowed to remember, say, the name, appearance, etc. of your previous character.”*

### Bonus Feature: Syndicate Objective - Summon the Syndicate Battleship

This will be a special objective only available to round-start traitors. If possible, when the objective is handed out to one traitor, a second will be chosen to have the objective as well. It’s additionally possible that this could be its own entire gamemode, as it would disrupt roundflow rather heavily. The objective will involve either stealing the proper access, or breaking into the bridge with an Access Breaker and opening the buttons to activate the beacon. Before the beacon is activated, however, the Communications Console must be emagged. Emagging the Communications Console corrupts the Distress Beacon, making it send out a signal which only the Syndicate Battleship can intercept. Once the Beacon is activated in the emagged state, the Syndicate Battleship will be summoned, however, the Beacon still activates the Emergency Distress Protocol, sending the station into Gamma Alert. This means that the traitors who summoned the battleship still have to survive until the reinforcements arrive.

#### The Syndicate Battleship

The Syndicate Battleship will be a unique ship designed specifically for war. The operatives on this ship will be similar to Nuclear Operatives, albeit with one key difference in their objectives: their goal is not to destroy the station, but take it over and claim it for the Syndicate. They will be given plenty of tools to accomplish their objectives, and in order to accomplish them, they must either mind-control, capture, or kill all of the Command personnel on the station.

The Battleship will have five ghost roles on it, which are identical to their Nuclear Operative counterparts outside of their objectives. These being: Gorlex Marauder Commander, Gorlex Marauder Agent, and three Gorlex Marauder Operatives.


## Game Design Rationale

### Seriously Silly

The Distress Beacon adds a lot of new possible scenarios, some of which could result in some very silly scenarios. Imagine, in their time of need, the station activates the Distress Beacon, and they get a ship full of clowns. Or another possible scenario, where the crew has a rich baron come to help, only for them to help the other side because the Captain was a little too mean to them. Of course, there’s also plenty of more serious scenarios, like with NX-012 Trifecta, or the Syndicate Battleship, but there’s a lot of room for silliness with this idea.

### There is no Winning or Losing

The Distress Beacon is a gamble when you activate it. Sometimes, the Responders may be helpful, but most times, they’ll be mostly unhelpful, or possibly make the situation worse. It’s meant to be a last ditch effort for when all else has failed, and I hope that players will engage with it with that mindset, especially since activating it is a gamble. It should hopefully maintain the flow of the round, and if not, will certainly add to the story as the many unique encounters create the possibility for wholly unique stories.

### Maintaining Authenticity

Currently, when the station is in a truly desperate situation, the best they can hope for is to contact Central Command or pray for some help, which they likely won’t receive. The Distress Beacon adds a new vector for requesting help, and is something a space station would reasonably have. The way it’s activated is authentic as well, as it needs multiple steps and coordination between the two highest ranking officials on the station to activate. The Responders being random and inconsistent adds authenticity as well, as the people who respond to a Distress Beacon are likely going to be the nearest Joe Schmo to the station.

### Maximizing Roleplay Potential

This feature ultimately only adds more potential for roleplay, and generally doesn’t take away in my opinion. The only situation where this could potentially take away roleplay is in faxing Central Command, but I expect that Captains would be more likely to fax Central Command to see if they could get assistance from the more helpful ERT before they try to activate the much riskier Distress Beacon.

### Roundflow & Player Interaction

The point in which the Distress Beacon will come into play will likely be in the latter third of a round, if at all. Most rounds do not get chaotic enough to warrant a Distress Beacon, and in the rounds that do, the Distress Beacon would not likely disrupt much, as the round would likely already be thrown into chaos. This could affect the pace of some rounds by resolving stalemates, or making rounds last a bit longer just by virtue of having some extra hands. Of course, the Responders have the potential to not really affect the pace of the round at all, as most would be neutral responders.

My hope is that players only activate the Beacon when things are desperate, and by making most of the Responders neutral, this should reinforce that. By making the helpfulness of the Responders a gamble, it should mechanically reinforce and prevent players from just calling the Distress Beacon the moment they need a tiny bit of help. Additionally, the need for the Captain and HoP to both activate it should help prevent it from being activated willy-nilly, as it would need consensus to even be considered for activation.

### Administrative & Server Rule Impact

As with adding any ghost roles, this will increase the potential for rule-breaking and griefing, However, my hope is by adding the in-depth descriptions and limiting the number/power of the Responders, this will hopefully reduce administrative workload. It shouldn’t introduce any new challenges, as all the ghost roles added will be similar to the already existing unknown shuttles. There’s also some potential for abuse with the Gamma Alert called when the Distress Beacon is activated, but my hope is that by requiring both the HoP and the Captain to activate it, that potential will be limited. I anticipate that the Syndicate Battleship objective won’t bring about any new challenges or issues, since the idea is similar to the already existing Revs and Nukies.


## Technical Considerations


I don’t expect any server impact from this feature, as the Beacon Responders are similar to the Unknown Shuttle event, just not random in when they spawn. This will require some new systems, but the only new systems are for the Beacon and the activation of the Emergency Protocol itself, and I expect those to be similar to systems we already have. There’ll need to be a new UI element for the beacon activation, but again, that’ll likely just be a copy of pre-existing elements. All in all, I don’t see much technical issues arising from this idea, but I’m not an expert, so there’s possibly something I’m missing.
