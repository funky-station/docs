# Corporate Spy
| Designers | Implemented | GitHub Links |
|-----------|---|--------------|
| mkanke    | :x: No | TBD          |

## Overview

Corporate spy is a new low threat antag to fulfill a similar niche as the thief but with more focus and more antagonistic goals.

## Background

Currently withing our lower intensity antags there is a pretty harsh line between the thief that is fully freeform and non-violent and the traitor which nearly always has some form of kill goal. This antag is meant to fill the gap between those by being mostly non-violent in a direct way but still causing issues for the crew as a whole.
There is also a strong tendency to metagame what antags a round is by if certain sets of goals are being completed that only that specific antag has. The corpo spy will be designed in such a way as to mimic some of the goals of other antags to throw off sec as to what kind of threat they are dealing with.
Corpo spy will also be testing the waters on a dynamic goal system not super unlike cargo bounties in having different goals they can hope to achieve to earn more TC to do bigger harder goals.

## Features to be added

### Dynamic Mission List
A major aspect of this antag will be a shop screen the player can pull up with a list of tasks that once completed will award the spy with a set amount of TC. They will start with very little TC and only low tier easy goals and have to work their way up adding a round progression system and oncentives to not delay working on goals until the end of round if they want any chance of getting the better goodies.

### Examples of goals

Low tier goals aka mostly indirect goals that do not involve face to face or very noticeable outward signs:

Plant a listening bug in a specific area, drain and APC of power with a special device, gain certain comms channels or certain accesses on their ID card

Medium tier goals: These begin to be much more direct and have a higher rick but higher reward for completion:

Plant a tracking device on a player. Scramble the medial records consoles data, scramble the wanted list database, plant an item on another player, setup a bug to slowly drain money from cargo, hack another players script account, steal a high value item like the corp secrets book or nuke disc, gain a promotion to the rank of a member of command.

High tier goals: 

Steal an organ from another player, murder another player, plant bombs in objects such as an APC (APC destroyed, mission accomplished all right!), break a perma'd prisoner out of the brig, destroy other important crew items like the camera monitors.

## Game Design Rationale

It makes great sense from a lore perspective that the syndicate has cloak and dagger agents on a NT station that operate much more secretively than their traitor counterparts and operate on their own terms because of it. There is also no definitive win condition there is always room to complete new goals and provide a continuous stream of interaction with the station. The goals need not be all serious, there is a lot of room to play with especially if there are special goals for different starting jobs. I could see the clown and mimes going wild with goofy things (looking at you pIED) if that route is followed. The goals are self paced though. Someone who is more of a novice can stick to simple low tier goals while a more experienced player can go for the bigger plays giving a wide range for both skill and dynamics on what scenarios a spy can bring to the table.

## Roundflow & Player interaction

This is a round start antag with a slow buildup to how heavily the affect the round. The goals built for this antag should directly interact and\or benefit other antags when possible and/or mask their goals from clear sight. Examples are listening bugs give traitors more info to work with, breaking people out of perma, activities that look outwardly like other antags with their most obvious tells, steps that directly hamper security and command such as comms/cams sabotage. It might be better to think of this as an antag designed to amplify other antags.

The player of the spy should do everything in their power to lurk in the background and be seen as little as possible, far more than a traitor their deeds staying hidden are key to their survival and thematic focus. A general lack of weapons from their uplink will help enforce this as they will have little more than what an average crew member has to fight back if pursued.

## Administrative & Server Rule Impact (if applicable)

I see two main admin concerns with this antag. First is that some of their bigger actions will need logs built in for easy searching and possibly better logging for when someone is say voice masking or disguised so its more clear who the original player is.
There also exists the possibility for someone to power game the role in order to treat is like traitor+. If this were to become an issue time gates could be added for certain goals so that the more violent ones cannot appear until deep into the round. That said a way to easily see the completed and offered tasks, similar to lsobjectives will need to be in place so admins can verify that a player isnt lying about their tasks as an excuess to murder randoms.

# Technical Considerations

- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should

- A special "task shop" possibly on the character screen will need to be implemented for the spy to see what jobs are available at the time. It could also be themed as a second tab on the uplink that only a spy can see.
- Some tasks will require additional checks for vicinity and wether a object or player has an item on their person
- Antag weights will have to be balanced to make room for this in the roundstart antag pools