# Regional Command, Corporate Liesan & Isolation

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |

## Overview

This Design doc seeks to outline admin interaction, the role of the Corporate Liesan in connection with Central Command, and what alternate approaches admins can explore to maintain isolation themes during intervention.

## Background

One of the larger themes focused on in funky is the idea of "isolation" for the station.
Currently the station is only a hop-skip-and-a-walk away from "Central Command" which is far from the ideal.
[Other Docs](https://github.com/funky-station/docs/pull/104) are seeking to improve that feeling from a transportation standpoint.
This Doc is looking at it from an admin intervention and communication perspective.

Additionaly the [Cargo Rework](https://github.com/funky-station/docs/pull/65/changes) document provides additional measures of interaction with the station outside of CC itself.
This includes altering the way that mail is delivered to the station from bluespacing in.

## Features to be added

### Regional Command (RC)

Regional Command is the "evacuation" point, and where communication between CC and the station happens.
This in particular is more of a re-name for the current CC outpost and enhances the idea of it being no more than a minor logistical center.
Any communications with CC (where real decisions happen) are relayed through RC where they get filtered through the bureaucracy for a response.

### Faxing and Bluespace

Bluespace is a technology that is badly understood, thus why the station is actively researching it and associated phenomena.
It is incredibly expensive and would be unlikely to be used as a simple means of "faxing a report" when "nothing happens on the stations".
Additionally, given there are at least 18 other stations in the sector (Via in game descriptions) and likely more in other sectors, they would not put experimental, and expensive, technology on all of them.
Additionally instantaneous communication like this is a violation of the isolation theme, given the station is mostly expected to be an autonomous entity with a trusted command crew/captain.
The RC itself may accordingly hold a bluespace fax, but would only use it in the most extreme of scenarios (god summoning or blob as examples).
This means that the station itself would still have to wait for standard fax times accordingly.

Any communication with RC alone should be expected to take 20 minutes or more for communication, and further communication taking approximately an hour outside of severely important situations (skipping bureaucracy).
This should not be expected as a normal method of communication however, to the point that casually sending a fax to RC outside of an emergency is frowned upon as a waste of resources.
In world this would be justified as a Pre-Bluespace method of FTL communication, less expensive, but not cheap.

### Corporate Liesan (CL)

Part of the RC personnel, the Corporate Liesan visits the stations via their shuttle to gather paperwork, check on the situations, and perform their other duties.

In round the CL starts on the shuttle "mid transit" to the station on one of a variety of shuttles, similar to how nukies start off-station.
This shuttle may be damaged in some way (EG meteor impacts, or a pirate attack) or be otherwise forced to delay their movement to the station, and are likely to require additional repairs/restock upon docking.
This would delay their start upon the station, highlighting the unusual and out of place-ness of them upon an NT station while also providing additional methods for them to start their interactions.
Additionally it would provide a reason why they do not have an entourage (killed in the incident, or a small shuttle).
Lastly they should also not be a guaranteed roll, having a close to 50% chance of spawning as a form of NT-aligned antagonist to further push their unusuality in rounds.

### ERT

A limited Emergency Response Force is stationed at RC, though they are ill-equipped for much of the threats the station will face on our own shifts.
They are primarily a medical/engineering team, though they do also have limited biological threat capabilities (CBURN).
These would only be deployed to the station in times of *significant* distress, as the cost of sending a shuttle alone across such vast distances would be extraordinary.

### Mercenaries and Other Combat Forces

In the rare situations where a heavy hand is needed, instead of combat ERT, a passing mercenary force can be used to lend a hand.
These forces may be contacted by RC to intervene, or may generally be picking up a distress signal/announcement from the station that they respond to.
These fit into existing lore with the existence of Merc gear, and the trading shuttles more than likely needing guard forces to make it to and from the station.
Some of these forces may even be subsidiaries of NT akin to security, or have previous/ongoing contracts with them given they inhabit the space.

Some particularly troublesome characters on station may additionally have contracts on their life that bounty hunters have come to collect.

### Central Command Event "Warnings"

Many of our random events currently have warnings given by central command, such as vending machines gaining sentience, vent critters, and meteors.
These announcements should instead be casted as if from the station AI, given it exists on station and would be monitoring such things.

## Game Design Rationale

### Maintaining Authenticity

Given the coming introduction of trader ships from the [cargo rework](https://github.com/funky-station/docs/pull/65) we already have local non-NT forces in the area.
This existence should be leveraged further in-rounds for admin interactions rather than always using the "far away" CC with instant communications to influence rounds on occasion.
The continued use of instantaneous communications, especially combined with short shuttle travel times, feels more like CC is just next door, but that it is normally either empty, or otherwise ignoring us.
This creates a massive contrast when "we are under attack by nuclear operatives" or "there is a cult summoning a god" go unanswered, but "Billy needs a new machine" or "the botanist made a mess" gets answered in seconds.

### Maximizing Roleplay Potential

Currently the Magi/NTR/IAA power feels both real and imminent due to communication and response times and styles.
While in the new role situation the CL should feel like they have some level of power, the power should feel weeks to months away from manifesting which instant communication does not provide.
By providing other avenues of admin interaction aside from CC, and delaying CC communication significantly, admins still get to interact with rounds as needed, but without shattering the isolationism.
This consistent isolationism then produces a better space for the CL and anti-corperation sentiments to exist without the expectation of it being squashed by an elite hit squad teleporting in within seconds to wipe everyone out.

## Roundflow & Player interaction

These changes are meant to influence the perception of the CL and the way they interact with the station early, and throughout their stay.

Additionally they are meant to effect admin intervention and the overall role of CC, turning them from an entity standing behind everyone, to a more distant entity even if their power is not reduced.
With these changes in interaction I hope that there is more of a rebellion mindset offered than with a constant and immediate threat of CC "correction".

## Administrative & Server Rule Impact (if applicable)

This is meant to have minimal/no impact on server rules, though it may lead to direct admin intervention being more difficult to notice or control compared to ERT and fax response.
This is however in line with the wish to provide players with more trust for their actions.

# Technical Considerations

Additional shuttle types for the CL and interacting forces will need to be made.

Possible new uniforms and gear for the given forces may need to be sprited/designed.


