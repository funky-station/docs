# Resource Overview Console

| Designers | Implemented | GitHub Links |
|---|---|---|
| TropicalOwl | :x: No | TBD |

## Overview

The removal of the global ore silo from the game was an inevitable change- While massively helpful to solve resource management issues regarding the existence of several lathes and fabricators, it created another massive issue: It completely trivialized and hyper-optimized what's essentially a core duty of the cargo technician: To supply.

Now that it is removed it is up to the cargo technicians to keep the station's localized ore silos well-stocked, that does come with a price however, with every lathe and silo essentially being thrown to one of the four corners of the station resource management proves itself very difficult, and it's not uncommon for cargo techs to eventually become weary of resource distribution, causing at times for them to become stingy towards any departments that are not science- And in turn- Denying essential resources.

## Background

I recently returned to Funkystation after suffering from a health issue, I needed a SS14 server to play that wasn't as fast-paced, and so this became my home. However I was a bit bummed to notice the techfab of the department I was playing at wasn't stocked at all 2 hours into the shift!

I've mentioned the issues this could create- Those being the lack of player authority over resource management and simply, difficult resource management in general. While this doesn't solve player authority as an issue it does optimize resource management *enough* for that to likely not be an issue at all to begin with.


# The new stuff

## The Resource Overview Console

Think of it as the energy distribution console of the cargo man: It's a simple concept, it gives you an overview of the lathes and ore silos on the station, with the ore silos being your "SMES'es" and the lathes/fabs being your "APC's" or "Substations".

The idea behind this is to allow cargo technicians to peek at which departments are in more need of X or Y material- And blare an alert if a department is currently not stocked with the three essential resources (Steel, Glass and Plastic)

A simple, but elegant solution to the daunting task that currently is resource management that does not completely trivialize roleplay.

What the console could look like is actually not that important- It's task is so simple a list specifying how supplied each department silo is could already do the trick, but ideally it should probably look akin to some of the engineering ones.

It should come mapped into the cargo bay on the maps already, that way it could work in tandem with the department silos from the get-go.

## Why is this good for the game

The console optimizes resource management without trivializing roleplay as mentioned previously- Having something display in numbers how well each department is doing in materials is also an attempt at game-ifying it without throwing the roleplay value of such interactions out of the window. Players in MRP servers may at times be more gameplay-oriented than roleplay-oriented, this attempts to incentivize both groups to do the task, with such a metric gameplay-oriented players could feel inclined to draw out the max performance out of their distribution, and the roleplay-oriented players get to interact with the other departments, it has a bit of meat for everybody.

## Game Design Rationale

#### Maintaining authenticity
While an integral part of living in a space station, manual resource management down to having to see what each lathe has in person like we have now doesn't feel authentic- It's much like the design principles put it, it's downright **infuriating** at times. Cargo may erroneously deny materials, and some techfabs can end up un-stocked for entire shifts.

If cargo can tell which departments actually needs those materials from the get-go they can not only preemptively deliver those materials, they can also assess fair judgement over resource requests. If a cargo tech can see that medical in fact, does not have plastic for example, it would make a lot more sense to accept the request.

#### Maximizing Roleplay Potential (Avoid QOL slop)
Much like the global silos, the resource management console is **objectively** an optimization of the cargo technician's duty, what it isn't however is a trivialization of it.
Cargo technicians would still need to interact with each department to stock them, they'd just be able to know which ones to prioritize, how much to give and when to do it.

## Technical considerations
I'm not coding this. I am A TERRIBLE programmer when it comes to C# and ECS, there's a reason I gave up on shitmed post designing it and just let Mocho take over it. I am a game designer, when it comes to coding I am mediocre at best.

