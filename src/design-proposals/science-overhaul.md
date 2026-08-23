# Research Point Types (Science Overhaul)

| Designers | Implemented | GitHub Links |
|---|---|---|
| JoulesBerg | :x: No | TBD |

## Overview

Currently there is not an extremely coherent interplay of mechanics within the science department. You can do either arti or anom research and both amount to the same thing. You can even do both if there are enough scientists. This proposal aims to increase departmental interplay with science and enhance overall science gameplay by adding categories of points that are spent differently when performing research. 

## Background

The desire for these changes come from the viewpoint of a player who hasn't played much science because I think their gameplay loop is tedious and kind of dumb. You do the same two things, and then the RD spends the points you earned on whatever they want. 
You only talk to other departments to ask if you can get into their area with an APE or when they come to your front desk and ask for speed boots. When I play other departments I don't even go ask science for things at this point. I learned early on that its just fully hit or miss if science is even bothering to research something you need until very late in the round when research is completed. Its not clear to other departments what researches have been completed or what tools are available until you look at a lathe, or see the roboticist running at mach 34 with speed boots, speed legs, and two speed arti's. 
One of the major goals of this proposal is to increase science content in a way that also requires interdepartmental mechanics.

## Features to be added

- Research point *types*
    - Explosive (work with atmospherics and/or security)
    - Enigmatic (xeno-archeology as it currently exists - advanced technology thats possible to understand, but might as well be magic)
    - Physics (study the tesla, the sm, HFR, or the singularity with the help of engineering)
    - Biology (work with medical, chemistry, and virology)
    - Aberrant (anomalies, work with security to capture heretics, cultists, or other users of "magic" - maybe kidnap the mime :godo:)
    - Material (scan rare elements, goliath shells, bone shards from changlings, hydrogen metal, goliath bones, etc. - work mostly with salvage)

- Remove the tech "categories" as they currently are. Techs will be defined by *specific* tech pre-requisits, like X-Ray cannons require advanced laser tech or something before the specific tech can be researched. The paths will still be branched, but the limitation will be the types of points you can get in masse instead of just unilaterally saying "We only get T3 armament this round"
    - Specific points costs for different techs
        - lasers take lots of physics and materials points
        - hardsuit tech takes biology and materials points
        - certain medical techs require lots of biology points
            - an example could be a stabalizer chemical that takes a mix of biology points, physics points, and abberent or enigmatic points that lets you mix advanced brutes without forming razorium or something
        - explosives protections and tools take lots of explosives points
            - an example could be an explosives dome that you can place and anchor over an active bomb threat that you don't have time to diffuse
            - better personal bomb protections
            - pathways for the station to get certain ballistics weapons
            - blast mining functionality for salv
        - as the project gets further along this will be more fleshed out, but thats the general idea.

- Initial idea for means of getting "explosives" points:
    - explosives testing chamber: a premapped but constructible (expensive) room thats basically indestructible, and contains a device that can detect the power of explosives - probably by grabbing the value of the radius of the explosion, and its damage amount. larger explosions will generate a greater amount of points. The room will require slight repairs between each explosion, depending on damage. technically a large enough explosion should be able to destroy the room, but this should be difficult.

- Initial ideas for means of getting physics:
    - add a new console that will be mapped into the engine areas, IN SPACE because doing science in a hardsuit sounds cool as hell.
    - Console will automatically connect to the Tesla or singulo (within 10 tiles or something)
    - Console can "Pulse" the singulo or tesla, which will cause something to happen, like generate ball lightning for example. 
        - An engineer or two will want to be PHYSICALLY present and assisting, as sometimes they will need to take actions to stabalize the engine, like re-weld teslas, or double pulse emitters to increase the field strength. Stuff like that.
        - the scientist will need to log some detail of the reaction, like how many ball lightnings were formed, or what stage the pulse dropped the singularity to in order to get results.

- Initial ideas for means of getting biology points:
    - Disect dead bodies on a research table
    - Put a special monitor on a patient and inject them with interesting chemicals :godo:
    - Perform live surgery on a research table - there will be some level of increased danger to the patient for doing this, but you will get science points :)
    - Expose a patient with a monitor to interesting atmospheric gases

- Initial ideas for getting materials points:
    - Create a special type of ore that can spawn, that spawns with random properties that science can research, similar to how arti works now, but less "could destroy the entire station" pilled. 
    - create a special type of analyzer that you can put materials like goliath shells in, or other special stuff, and an interactive system for that like the above idea. actually, both of these are just the same idea, just one uses a special randomized ore and the other uses shit salv kills or gathers from like, expeds.

- Aberrant:
    - kidnap the mime and make them build an invisible wall on top of a scanner on cooldown. Because thats funny as fuck.
    - Anomalies as they currently exist will produce this type of point.

- enigmatic:
    - xeno archeology as it currently exists will produce this type of point.
    - if xeno-biology ever gets implemented that will be like a hybrid point maker.

- hybrid point makers:
    - Materials and biology hybrid could use changeling blood or flesh or something. An IC reason to keep lings alive.
    - The possibilities are endless.


## Game Design Rationale

Consider addressing:
- Seriously Silly: kidnapping the mime. Need I say more? I am sure more silly ideas like that one will ALSO be implemented as part of this.
- There is no Winning or Losing: The different means of generating the different researches will have the potential to drastically alter round flow depending on who else is playing and what they are actually capable of helping you with. If the atmos tech or CE knows how to make maxcaps that could drastically increase the speed that you can research explosives points with, but theres a risk reward there too, because maxcaps = dangerous. But with all these science ideas, I cannot really picture people approaching all of it with win/ lose in mind. if you blow up 10 maxcaps odds are you are going to fuck one up and kill all of science because you forgot to repair the room between explosions. The intent is for all of the features to be a proper balance of point reward and risk. Kidnapping the mime won't give you a ton of points, but the mime will probably have fun helping science and being important.
- Maintaining Authenticity: I actually think this IMPROVES authenticity a lot. It feels incredibly NOT authentic that I will never have access to a hellfire freezer because security demanded they get some gun or something that round. It will make other departments want to interact with science because the way that their department interacts with science/research DIRECTLY benefits THEIR gameplay loop. (materials science can give salv access to better mining tools and hardsuits, biology can give medical access to better diagnostic and treatment tools, physics can give engineering access to better means of power production, among other things). This system will also make it more realistic for people to add things to the game, as if you lock it behind enough research requirements theres not really anything you could add that would be imbalanced, and the point types are self explanatory enough that it should be pretty obvious which ones to lock a tech behind.
- Take Things Slow: I actually think this will make it almost impossible to "finish" research? it will definitely ADD content and gameplay time, and also round variance. 
- Maximizing Roleplay Potential: I think the changes and other comments I have made speak for themselves here? This is going to make it harder to do science without involving other departments. It will also make it so the RD isn't just making point spending decisions, but is forced to coordinate with other departments and do actual organization of the science team in order to efficiently research technologies. Instead of just speed running punching rocks until blood comes out. It will diversify their duties and make them an actual leader instead of them just being the special scientist that just gets to decide how the points are spent / when to deactivate borgs / when to card the AI in time for evac.

## Roundflow & Player interaction

- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
    - Every round. all round.
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
    - DO: Kidnap the mime.
    - DONT: singuloose.

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
    - Maybe? I don't think so though, other than probably needing to rewrite science SOP, but thats kinda a given with an overhaul this big.
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
    - Maybe? When you increase player interactions you will probably also increase disputes. But I think our player base is good enough that this can really only be a good thing.
- How are the rules enforced mechanically by way the feature will be implemented?
    - The way you buy technologies will be a hardcoded change. I might make it so you can spend 2 of one point type as a substitute for 1 point of a different type, but otherwise, the system is just going to be self enforced.

# Technical Considerations

- Are there any anticipated performance impacts?
    - I don't think so? aside from explosions happening more often I can't really think of anything big this is going to change, it will add a couple events, and some more consoles for the system to keep track of, but nothing heavy like adding a new gas that has to be managed on every tile in the game at once.
- Does the feature require new systems, UI elements, or refactors of existing ones?
    - yes. absolutely.
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
    - I am not sure yet. My intention is to do everything in the following order:
        - The ability to kidnap the mime and get a couple points every time they spawn an invisible wall on a sensor. because thats just funny as hell, and it will be a good way to familiarize myself with the basic science code as it currently lives.
            - new scanner thing that can be hooked up to an anom scanner, and generates points whenever an anom is on top of it. Mime wall will count as a very weak anom for this purpose
        - Explosives research (this will just provide normal research points at first)
            - A couple new structure types
            - some kind of scanner to detect the damage the bomb did, and its radius
            - a console to make it seem official.
        - physics research: 
            - a console that attaches itself to the tesla or singulo, or maybe a method for the scientist to do the attaching manually.
            - Pulses from this cause phenomena with the tesla or singulo, and then ask the scientist for an input
            - engineers may need to repair things or up the PA power to bring a weakend singulo back up to full power
        - more content. You get the idea. These are big changes, and for now I am not going to enumerate every single new console etc when at this time I am not even certain this is an idea that is wanted on funky.