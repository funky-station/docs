# Respiration Overhaul

| Designers | Implemented | GitHub Links |
|-----------|---|--------------|
| mkanke    | No | None    |

## Overview

This is intended to be a general gameplan for taking the respiration system of the game and make it much more extensible and immersive for both the general player and those in the medical department. 

## Background

The current implementation of airloss damage is currently very game-y. Just a number goes up or down shove medication in person and make sure they have air. Thats where the dynamics of it stop. This leaves the only way to interact with the system to "deal damage" or shove meds and air into someone, which is fine for a baseline just so the game can function but we can do better. 


#### Implementation

The system will get split up into 3 parts "Respiration","Saturation change","Saturation", all given in a range from 0-1, that all interact with each other as well as outside effects such as chems and damage. Respiration and Saturation Change are the systems players can directly interact with while Saturation is the closest this system will come to the current airloss damage system and is what will dictate the changes of overall health from Good, to Crit to at a saturation of zero, dead since the brain cannot get o2 (or whatever gas they breathe) and the organs begin to die. This overall system will also introduce a more granular soft crit system based off of Respiration and Saturation. The formulas that will follow are mearly rough drafts for whoever implements the system so they have a jumping off point.

#### Respiration

This is the fastest moving category and where most external systems will interact with the entire system. My current working formula for calculating this is,
1-(damage/400)-(|80-heartrate|\100)+(External Sources)    Lets break this down

(damage/400)
This takes the overall damage a body has and divides it so that 200 damage will reduce respiration by 0.5 aka half 

(|80-heartrate|\100)
This section takes the heart rate and figures out its deviation from the standard heart rate of 80 and once it goes 50 in either direction it reduces the total respiration by 0.5

(External Sources)
This is where most outside factors do their business such as Dex increasing respiration or drugs that cause suffocation reducing it. CPR also falls into this catagory since it forces the body to breath as well as future effects that might be added such as choking someone out or other such systems.

#### Saturation Change

This adjusts the actual saturation of breathable gasses in the person and its a much more simple and slow moving system. This current formula lacks a final rational multiplication such as * 0.1 so that saturation has a maximum change per in game tick.
Blood Level * (Respiration * Moles) * Tick rate Change

Blood level
This will be the current blood level from 0-1 with 1 being no bloodloss

(Respiration * Moles)
This section Takes the already calculated respiration and multiplies it by how many moles of breathable atmosphere are available. The reason for this is so that there can be variability in air quality and needs some sort of extra constant multiplication so normal air mix makes it slightly better than 1 but a pure mix leads to a better change so a patient recovers quicker when on internals. 

Tick Rate Change. This exists to pace the rate of change per tick this imparts on the Saturation 

#### Saturation

This is the overall health of a person simulating how much breathable gas is reaching their organs such as their brain. Its formula is very simple SaturationChange + Saturation. On a medical scanner this would be the stat that people see in place of airloss damage. Nothing should directly affect this stat and instead to manipulate it a player will have to treat the symptoms that reduce Respiration and Bloodloss so that the other systems feed into this. Player facing it would look like a % from 0 to 100 but under the hood it would be a simple 0-1 range so that is can be easily clamped or checks for cases such as over saturation causing hyperoxia can be implemented. 

---

### How does all this look to the player

#### Respiration
This is where the classic gasping will kick in but be expanded on. The first sign of not being able to breath would be the loss of the ability to shout. Further respiration loss would cause gasping, then whispering only with zero respiration fully muting the player from talking. This slow trickle down of symptoms will give the player plenty of time to have a "oh shit" moment and seak to fix whatever is causing this or to seek help from someone who can such as the medical team. 

#### Saturation

This is what will control the soft crit system. As your Saturation goes down your body has less fuel to keep going so the player will suffer a gradual slowdown to start with. As it starts to get really bad the normal crit state overlays will kick in and not super long before passing out will be forced to crawl similar to our current soft crit system. Once it hits zero death will happen and if someone decides to implment it, things such as organ death could occur such as brain death but that is outside the scope of the initial implementation.

---

## Game Design Rationale

### Seriously Silly

The current system is rather limited in how a dev can interact with it making it just a simple numbers game. Specifically it all being one big damage group. Lets look at just respiration, splitting this up opens us up to a range of possibilities to how items interact with the simple act of breathing. Lets say a clown gets a pneumatic launcher, why SHOULDNT they be able to load a horn into it, target someones mouth and get it lodged in their throat like that one scene from spongebob. Let it lower respiration and force them to honk instead of talk. It has a tangible effect on their ability to live but without being immediately life threatening.

### Maintaining Authenticity

This new system will provide a stronger base in reality so a player can assume off their own personal experience why things are happening and the steps they should take to fix it and allow more interesting and realistic ways to interact with the system as a whole. 

### Take Things Slow

As the system exists now for a medical player, breathing is almost a non-issue that can be solved very quickly. Even if a room is fully spaced you just shove some airloss chems in them and they can keep going without too much issue. Breathing is an important part of life and doesnt just resolve in an instant. By having statuation change tied to tick rate after stabilization a player will still need time to rest and regain their saturation.

### Maximizing Roleplay Potential (Avoid QOL slop)

I would expect to see a lot more talking between docs to diagnose extactly whats going on and if possible actually talking to the patient to ask them what happened as this communication could lead to faster results so its incentivised.

## Roundflow & Player interaction

Not being able to breath or bloodloss will be felt much stronger by both the normal player as well as the medical department. More effort will be required to diagnose and treat the symptoms of Saturation loss leading to a more dynamic period of diagnosis and stabilization of a patient being admitted into medical.  

## Administrative & Server Rule Impact (if applicable)

There should not be much rule impacts besides reaffirming that until you are dead you remember things.

# Technical Considerations

Basically anything touching the respiration system that is ported will require reworking to interact with this system as its basically a full overhaul of how airloss works. This should not be the most difficult thing as most instances that would cause airloss with the current system would just cause respiration loss which would trickle into the other parts of the system.  