# Reagent Pipes

| Designers | Implemented | GitHub Links |
|---|---|---|
| zergologist | :x: No | TBD |

## Overview

A reagent pipe system quite similar to the existing atmos pipe system, utilizing the same pipe layers and allowing for reagents to be pumped throughout the station.

## Background

Given that, on a space station in the middle of the void, there being an infinite and free source of water through the sinks seems very gamey. Drains just removing a set amount of liquid reagents permanently doesn't help with this feeling. The fact that the only variety of plumbing is for gas pipes is also strange. Given that atmos pipes were recently updated to allow for three layers of piping or a total of up to six individual pipe networks crossing one tile, adding in a new system that utilizes the same pipe layers to make actual plumbing work wouldn't interfere with the station's atmos to a severe degree.

Making atmos pipes look less like actual pipes and more like ductwork in order to differentiate the two nets would likely be needed.

## Features to be added

### Reagents in Pipes

Give the ability for reagents to sit in pipes and interacted with much like atmos gases using plumbing devices. Would work more like atmos but with only units of reagent to worry about, not pressure or volume per se. The entire network should act as one entity in regards for calculations. Reactions would be handled across the entire net, being silent and choosing a random segment/machine in the net to spawn entities/gases that a reaction may create. 

#### Base Reagent Pipes

Basic pipes that hold a given amount of reagent and connect to other pipes on the same layer as them. Conflicts with atmos ducts but doesn't interface with them.

Glass pipes that let you see the contents of a pipenet directly and let you hear if any reactions are going on within should also be included, but only to be used sparingly. Generally targeted for any tile-specific reactions that occur.

#### Pipe Clogging

Random events, interactions, and reactions that create items can clog a reagent given pipe, preventing reagents from passing through it. Should require attention in order to unclog the pipe. Drains and basins can also clog if too many units of reagents are emptied into them at once. If an item is to be responsible for the clog, unclogging a pipe should release that item.

#### Reagent Pipe Breaking

If a given reaction either severely overfills the reagent pipenet or causes a reaction that creates an explosion or gas, some part of the pipenet should break. Wherever a reaction is chosen to occur, the pipe at that location should break, performing the reaction, spilling some of the net, and leaving an open pipe that continues to spill out the reagents in the network until either the level in the net reaches below a certain percentage threshold or the puddle that the pipe is sitting in reaches above some reagent threshold. Broken pipes and puddles should interact if the puddle has more reagents in it than a given threshold, allowing for puddles to partially drain into broken pipes.

#### Reagent Pumps

A pair of pumps that move reagents through pipes. Set pumps move a set amount of reagent per second into a pipenet. Fill pumps move reagents to a set fill percentage of a pipenet. Both pumps stall as they fill the pipe network they're pumping into.

#### Reagent Pipe I/O

Reworks the existing drains and sinks to work with the reagent pipe network while adding in taps and vents. 

Drains still pull reagents from puddles, but only if the pipenet they're emptying into has enough space. 

Reagent vents interact with puddles in a region around them, either letting reagents enter or leave depending on the pipenet's fill level and size of the surrounding puddle. 

Sinks are broken up into faucets and basins, with faucets letting you pull reagent from one pipenet and basins letting you empty a container into another one. Faucets can be turned on and allowed to make puddles if either they have no basin or the basin beneath them becomes clogged.

Specialized fixtures like shower heads should also exist, but they can be implemented in their own PRs experimenting with this system.

#### Reagent Tanks

Lets you store a greater amount of reagent in a given space than can be stored in puddles or moderately sized pipenets. Has a fill percentage different from its connected pipenet, letting them fill up a pipe without being full themselves. Can be filled with set pumps when their network is "full" or have fill pumps connected directly to them.

Allow for interactions with the mobile reagent tanks, allowing them to be wrenched on top of an interface and either filled or emptied.

#### Open Reagent Pipes

Acts like broken pipes but with higher thresholds to spill over and offers an entry into the pipenet. May or may not mean that uncapped reagent pipes release out the contents of their net.

#### Reagent Filters and Mixers

Effectively the same as atmos filters and mixers but for reagent pipes, mix two pipe nets at a set percentage and filter off a given set of reagents from one pipe net. Filters use a UI, much like the debug "edit solutions" add menu, letting you search through the list of reagents for the ones that you want to isolate. Filters work like set pumps, mixers work like fill pumps.

#### Reagent Sensors and Alarms

Allows you to read the contents/temperature of a reagent pipenet or section of a puddle, as well as alarms that can be linked to other devices much in the same way that air alarms can. 

#### Reagent Valves

Lets you section off parts of a pipenet with either manual or signal-activated valves.

#### Reagent Radiators

Allows for the temperature of a pipenet to interact with atmos, either heating up or cooling down depending on the ambient temperatures.

#### Reagent Thermal Devices

Either gives a set of or allows for existing atmos thermal devices to interface with reagent pipes. Lets you automatically heat up or cool down the contents of a pipenet as such with heaters or coolers.

### Integrate Existing Systems with Reagent Pipes (Phase Two)

#### Chemmaster 4000

Makes the discard function of the chemmaster purge into a connected pipenet. Maybe gives you the ability to fill it from a pipenet on a separate layer?

#### Industrial Reagent Grinder

Lets the Reagent Grinder empty into a pipenet.

#### Reagent Dispensers

Makes the clear function of reagent dispensers flush the reagent into a pipenet.

#### Piped Lube?

Gives machines with containers the ability to pull from a pipenet, automating filling them with space lube. Gives one hell of a mess to clean up when the clown inevitably unwrenches/breaks a lube pipe in the middle of the hallway.

### Plumber Duties and Mapped-in Pipenets

#### Centralized Water Main

The station should start off with a dedicated water line that must be filled with water throughout the shift. Lets departments have access to water without needing to drag in a tank from maints, and lets station-wide sabotage of the water main occur. 

#### Reagent Waste Line

Acts like the atmos waste line, either being something that runs alongside the water main or being department specific. If a main waste line exists, then filters can be placed at the end of it to help reclaim specific reagents that may be discarded over the course of a shift.

#### Plumber Role

A role dedicated to maintaining the water main and other pipenets. Helps build new ones. Likely an engi role if actually distinct, otherwise has responsibilites are to be rolled into station engi and janitor.

## Game Design Rationale

### Seriously Silly

By having the ability to much more easily move reagents through the station automatically, this offers the ability for both localized and mass sabotage alongside some interesting interactions. Say someone spikes the water main with a bit of space mirage, and now everyone who gets their drinks from the faucets starts to see things. The clown, in their infinite jest, decides to lay down network of pipes and vents to flood the station with lube at their command. Engi makes a welding fuel pipeline throughout the station, thinking it'll save them so much time, as someone opens a faucet and realizes that they accidentally flooded the water main with welding fuel. Say you unclog the chef's waste line and pull out an entire wheel of cheese... What was that doing in there?

### There is no Winning or Losing

Reagent pipenets, much like atmos pipenets, are merely tools to be utilized. They let you devise more interesting strategies, whether it be through their creation, tampering, or destruction.

### Maintaining Authenticity

Why is it that a space station in the middle of the void would have pipes for atmos but not pipes for liquids? Plumbing shouldn't have been forgotten over the course of a millenium, and having the ability to both overflow and eventually run sinks dry is an yet authentic action. Unclogging pipes should be something that you need to get your hands dirty for, either digging up the pipe directly or worming a drain snake down to retrieve whatever it is that was causing it.

### Take Things Slow

Building and interfacing with reagent pipenets should be fairly slow - one pipe at a time through the entire system. The set pump allows for somewhat slow filling of tanks and such, while the fill pump allows for a pipenet to be somewhat quickly filled without instantly causing the entire station's pipenet to burst. Manually adding reagents to the system should be somewhat slow, giving time for things to slosh around without just letting a chemist dump three jugs down the wastenet and retrive all of the medicine they just made wherever waste is filtered off.

### Maximising Roleplay Potential

This removes forever free water out of the sinks, and could even act as a way to get engi to do more things around the station. If the waste line gets clogged and the janitors can't empty their buckets anymore, either engi has to go and find the clog or give them "temporary" tanks to drain all of the blood they mopped up into. The bartenders may petition the station to see if they can't replace the free water with free drinks, filling the water main with a whole slurry of alcohols and pissing the chemists off who still needed that water. While this does potentially allow for chem to hide in the chemlab if the appropriate lines are setup, maps with mailing units in chem do kind of already pose that problem.

### Dynamic Environment

Ever wanted to make a cheese production floor? Perform tiderchem without the need for a portable chemmaster? Turn the station into a water park because the plumbers pissed you off? Reagent pipes seem to be more versatile than atmos pipes, partially because reagents interact with far more systems than atmos at the moment. By giving people at least two pipenets for people to dig through (water main and the waste line), people get to understand that yes, you can have pipenets dedicated to one reagent and yes, you can have more generalized pipenets that may do some unexpected things.

## Roundflow & Player interaction

Ideally someone should wrench in a couple of water tanks and turn on the water main and set up the filters on the waste line close to the start of the round, letting for water to be distributed throughout the station and for people to be able to dispose of reagents appropriately. As the round progresses, maybe something clogs the pipenet and needs to be removed. If someone breaks a hole into the water main, it might be up for engi to make sure that it doesn't dry up the entire station. Giving the ability for ice to be mined, melted into fresh water, and emptied into the water main wouldn't be a bad idea if it's otherwise been emptied.

Forgetting to set up the water main isn't going to be as bad as forgetting to set up distro - bartenders still serve drinks and you can still find water tanks in maints, you just can't depend upon the sinks for water until someone sets that up.

As for player interactions, I ideally don't want shitters to break open every pipe just to feel something and cause a mass disturbance as a result. I am uncertain on how mappers should implement the pipe networks - this shouldn't be just another atmos that needs to be managed, but at the same time having a couple of reagent pipe networks would be useful for people to use even if they aren't familiar with the system. Having a dedicated water main feels right, while waste doesn't necessarily need to be handled in any specifc way. If you want to just empty out the wastenet by venting it onto a piece of lattice, go for it. Open faucet instead of vent? Also works. Store everything that was discarded on the off-chance that it's still useful? Why the hell not? If someone wants to create a burn chamber by continually dumping in gaseous oxygen and liquid welding fuel into a room, that's an ingenious use of the system and I don't think that should be shut down.

Tampering with the water main shouldn't be something that happens before say the first fifteen or so minutes of the round, just to make sure that people can do roundstart stuff with the sinks safely.

## Administrative & Server Rule Impact (if applicable)

Ideally the reagent pipenets shouldn't let you do dumb and exploity things like subframing, as the hard limit of how many units of reagent can exist in a pipenet should prevent stuff like that from happening. Having logs on who dumps what reagents into which pipenet would probably be a good idea for tracking extremely early mass poisonings and horribly irresponsible chemical dumping.

# Technical Considerations

- The entirety of the reagent pipenet system would need to be implemented in a way that doesn't generate too much lag for having a series of pipes running from one end of the station to the next, ideally the "one net, one volume" design should help with this problem.
- Engis need to have a way to look into the pipenets, maybe by turning the gas analyzer more generic pipe analyzer.
- Documentation both in-game and out of game needs to exist on how to interface with and utilize reagent pipes.
- Spriting everything for the reagent pipes and respriting atmos pipes (again) will take some time to complete.
- Current maps will need to be edited and new maps designed with the water mains in mind.
- Specific numbers will need to be settled on for practically everything here to make certain that everything feels appropriately fast.