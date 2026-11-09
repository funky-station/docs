# Resource Overview Console

| Designers | Implemented | GitHub Links |
|---|---|---|
| TropicalOwl | :x: No | TBD |

## Overview

The removal of the global ore silo from the game was an inevitable change- While massively helpful to solve resource management issues regarding the existence of several lathes and fabricators, it created another massive issue: It completely trivialized and hyper-optimized the supply of materials accross the station.

Now that it is removed it is up to the cargo technicians to keep the station's localized ore silos well-stocked, which does come with a price; with every lathe and silo essentially being thrown to one of the four corners of the station, resource management proves itself very difficult, and it's not uncommon for cargo techs to eventually become weary of resource distribution, causing at times for them to become stingy towards any departments that are not science, leading to resource denial accross the board.

## Background

I recently returned to Funkystation after suffering from a health issue, I needed a SS14 server to play that wasn't as fast-paced, and so this became my home. However I was a bit bummed to notice the techfab of the department I was playing at wasn't stocked at all 2 hours into the shift!

I've mentioned the issues this could create; Those being the lack of player authority over resource management and difficult resource management in general. While this doesn't solve player authority as an issue it does optimize resource management *enough* for that to likely not be an issue at all to begin with.


# The new stuff

## The Resource Overview Console

Think of it as the energy distribution console of the cargo man: it's a simple concept, it gives you an overview of the lathes and ore silos on the station, with the ore silos being your "SMES'es" and the lathes/fabs being your "APC's" or "Substations".

The idea behind this is to allow cargo technicians to peek at which departments are in more need of X or Y material and blare an alert if a department is currently not stocked with the three essential resources (Steel, Glass and Plastic). If it does include listings for the department techfabs it would be wise to also include a way to change the essential resources threshold, science has a lot of use for plasma, while glass is debatably not that useful for security as well.

A simple, but elegant solution to the daunting task that currently is resource management that does not completely trivialize roleplay.

What the console looks like is actually not that important. Its task is so simple that even a list specifying how supplied each department silo is could already do the trick. Ideally, however, it should probably look similar to some of the existing engineering consoles.

It should come pre-mapped into the cargo bay, so it can work in tandem with the department silos from the start.

## Why is this good for the game

The console optimizes resource management without trivializing roleplay, as mentioned earlier. Having a numerical display of how well each department is doing in terms of materials is an attempt at *game-ifying* the process without throwing away the roleplay value of such interactions. Players on MRP servers may sometimes be more gameplay-oriented than roleplay-oriented; this system incentivizes both groups. Gameplay-focused players would have a metric to push maximum efficiency in distribution, while roleplay-focused players still get to interact with other departments. In short, there’s something in it for everyone.

## Game Design Rationale

#### Maintaining authenticity
While an integral part of life on a space station, manual resource management—down to personally checking what each lathe has is not authentic. As the design principles point out, it’s downright **infuriating** at times. Cargo may deny materials erroneously, and some techfabs may remain unstocked for entire shifts.

If cargo can see which departments actually need materials from the start, they can not only preemptively deliver them but also exercise fair judgment over requests. For example, if a cargo tech can confirm that Medical truly lacks plastic, it makes much more sense to approve that request.

#### Maximizing Roleplay Potential (Avoid QOL slop)
Much like global silos, the resource management console is **objectively** an optimization of the cargo technician’s duties. What it is *not*, however, is a trivialization of them.

Cargo technicians would still need to interact with each department to stock them. The difference is that they would know which departments to prioritize, how much to allocate, and when to do it.

## Technical considerations
I’m not coding this. I am a **terrible** programmer when it comes to C# and ECS—there’s a reason I gave up on Shitmed after designing it and just let Mocho take over. I’m a game designer; when it comes to coding, I’m mediocre at best.

