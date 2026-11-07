| Designers | Coders   | Implemented | GitHub Links |
|-----------|----------|-------------|--------------|
| PopUpPup  | PopUpPup | :x: No      | TBD          |

## I. Summary

A rework of engineering's station maintenance role that increases the complexity of the job. Reworks welding and many other repair jobs and overall slows repairs and construction while adding new equipment.

## II. Problem

The job of the engineering department can be summarized as maintaining station habitability. Currently this manifests in engineering setting up atmospherics at the start of the round, setting up power, and repairing damage as it happens. The amount of time, skill, and equipment required to do all of this is minimal. Atmospherics can be set up in minutes, power in barely more, and repairs are often trivial and can be done by one person. While changes such as the removal of the RPD and RCD have helped to alleviate this problem they haven't gone far enough. As it stands now most engineers will either spend most of the shift like a passenger with a better ID or will hunker down in engineering optimizing power and/or atmospherics systems to create as much power and/or money as possible. This effectively segregates a part of the crew to an RP-light mechanically dense subset of the game.

## III. Intent

 This rework aims to make station repairs a slower, more impactful, and immersive part of the game in a way that brings engineers out of their department to interact with crew. These changes would also make station damage a much more impactful part of the round, giving, for example, a bomb going off the impact it deserves on roundflow. Locking station repairs behind considerable equipment would also give engineering more leverage in union negotiations, bringing tension to the round. A large number of these changes also increase engineering's usage of materials, leading to more dependance on (and interaction with) supply (and prisoner salvage). All of this would give engineers more to do and integrate the department better with the rest of the game. Bringing engineers out of their department such that the station is constantly undergoing repairs would also fit themetically with the idea of an uncaring coporation placing you on the cheapest viable station for your job.

## IV. Solution

### Less Portable Materials
Stack sizes should be decreased, item sizes should be increased, or both.

### The Material Cart
The material cart would have slots for materials. It should carry more materials than a duffle bag. It allows materials to be input into it similar to a silo until a certain limit on total materials is reached. Materials are retrieved similar to a silo with a different UI. Keep in mind that in-universe this is a cart on which materials are put in stacks. It is basically a fancy wheelbarrow- the ui should not be a computer. Take inspiration from the new vending machine UI. Whether it can store more than a crate being pulled along the ground is irrelevant because it can move much quicker because it has wheels.

### Limited Welding
Welding can no longer magically repair windows, walls, and other things.

### Hoses and Cables
Hoses and cables will be a connection between a cart and something else. Hoses can carry reagents and gasses while cables carry electricity. Hoses and cables can only extend a certain distance, beyond which they snap. Hoses should spill some amount of their contents before a valve on the cart automatically shuts requiring manual intervention to re-open, while cables should be hazardous to touch or walk past for anyone without sufficient insulation for their voltage. They should also electricute water and grates in the same way a wire under them does. Electrocuting something should drain power from the cart with the batteries and heat the gas around it.

### Sealant Foam (and Cart)
Sealant Foam is a new reagent that can be applied via certain items to damaged windows, doors, and other structures to restore some amount of health. It cannot completely repair anything. Once permeability is added (TODO: IS THIS A WIP OR SOMETHING I SHOULD ADD TO THIS DOC) sealant will not be able to completely restore impermeability to a damaged structure. Sealant foam will come in small cartridges that can be inserted into nozzles and in a cart that can be connected to a nozzle via hose.

### Reworked Welding
Welding fuel will be removed from the game. Welders will be removed and replaced by welding torches. Welding torches will require a hose to a welding cart to operate. Welding torches will require a certain mixture of oxygen and plasmic phoron in their hose to light. If they fail to light they will release gas into the air. Welding carts will carry two or three things: a gas canister containing pressurized plasmic phoron, a gas canister containing pressurized oxygen, and optionally accordion curtains (see below). Once a torch is lit it can only weld if it is held in one hand with a welding rod or stack of welding rods in the other. In the same way that the duration of a welding doafter determines fuel use it should determine welding rod use. A lit welding torch will blind anyone at a rate determined by their distance from it if they are not wearing adequate eye protection and the welder is in their viewcone. Welding carts should be mapped how welding tanks are now to allow for access to explosives. They should explode upon being hit enough times with a source of fire like a lit welding torch, lighter, or match.

### Accordion Curtains
Accordion curtains should initially function as a normal inert pullable object. Once activated in a way similar to medical curtains they should anchor to the floor. Once anchored they can still be pulled. They expand to follow the person pulling them up to a certain length. They snap such that each vertex as at the center of the edge of a tile. To retract they must be pulled in reverse and locked once they are fully retracted. Accordion curtains should block vision. They are intended to be set up around welding sites in trafficked areas like hallways that cannot be shut down. They would prevent eye damage to those outside of the cordoned off area. They would also function to guide traffic around, say, gaping hole in the side of the bridge until a new wall can be built.

### Gas Carts
Gas carts are gas canister carts. They come in oxygen, nitrogen, and storage varieties.

### Water Cart
Water carts can be connected via hose to firefighting nozzles. Water can also be taken out of them to fill any container, including decapoid gas tanks. Water tanks cannot be refilled. The cart itself will have a slot for a large watercooler style water takm to fit. The water tank can be removed with a doafter and stamina cost proportional to how full it is. Movement speed when holding a water tank will also scale with fullness. Water tanks will have to be held with both hands. Slipping or crawling while holding a water tank will cause it to fall and rarely shatter and spill, otherwise it'll bounce and roll away with fun sounds. Maps should have a few spare water tanks in engineering. New water tanks can be bought.

### Pull Cart and Caravans
Sometimes a single repair might require multiple carts. Two carts next to each other can be connected via a context menu action such that one is "pulling" the other at their sprited coupling. Multiple carts can be connected like this in a caravan. Eventually a caravan might be too heavy to pull. The pull cart is a small vehicle that can be attached to a caravan to pull it. The pull cart runs off of an internal battery and can be connected via a cable to other carts or equipment.

### Battery Cart
The battery cart is a battery. It can be connected via cable to other carts or equipment. If its output is connected to the motor cart's input it would charge it.

### Electrical Equipment
With the duration of repairs it might be nice to set up lighting for particularly large jobs (eg: the aftermath of a supermatter delamination). Lights can be battery powered or connected to a power source like a battery cart, the pull cart, or a power jack.

### Power Infrastructure
Maintenance should be mapped to have power jacks at entrances and somewhat throughout. These can be used to power equipment like lights and charge the battery cart and power cart. Engineering should also have some to charge those carts while not in use. Maintainance jacks should be connected to MV cables. The power jack should come loose if the wire is pulled past max length causing small arks, it should electrify puddles over it, and generally be "shit."

### Construction Changes
Some construction processes should become more complex and involve steps like welding, especially things like basic walls.

## Degrading machines
Machines like computers, medical cryopods, doors, and vending machines will slowly break down and require repairs. The repairs required will depend on the machine. Most repairs would be a simple swap of the board (eg: doors, computers) while others would require other things (eg: sealent applied to cryopods). Machine degredation should be tuned alongside meteor spawns and other sources of station destruction such that they provide a small amount of tedium in down-time between larger repairs like those neccesitated by meteors to fit the theme of being a cog in the machine without making the game boring.

## Emergency generators
With the removal of welding fuel P.A.C.M.A.N. generators become pretty much usless. P.A.C.M.A.N. and S.U.P.E.R.P.A.C.M.A.N. generators should be removed and replaced by the emergency generator, which runs off of a welding cart via a hose. They should output M.V. power and connect via a maintainance jack.

## V. Considerations
### Technical
* A component for caravan-able carts would have to be implemented
* A component for reagent and gas hoses would have to be implemented
* Electrical cables would have to be implemented
To make these changes come into play more often gamerules might have to be changed, such as by increasing the likelihood of meteor strikes.
* Some chemistry recipes will have to be updated to not rely on welding fuel

### Admin
People could use welders to mass blind people. Admins would have to decide how to deal with this, if at all.

### Player
Some people might hate these changes initially as they remove QOL similar to green-comms removal.