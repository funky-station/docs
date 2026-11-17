# Dragon Rework Proposal

| Designers | Implemented | GitHub Links |
|---|---|---|
| RedaREDACTED | :x: No | TBD |

## Overview

The Dragon is an underdeveloped piece of game content whose existing mechanics restrict its potential.

I propose some design changes that I believe will:

1. Change the goals, objectives, and repercussions of having a fire-breathing space fish on a space station.
2. Align better with the "antagonist-optional" design philosophy.
3. Fix some user experience and technical issues I had with my first playing of said Dragon.

### OK, so... you've got dragons in your spesstation

**Stage 1: Establishment - Localized**

The Dragon identifies a suitable location and begins establishing a nest. The location must meet certain environmental requirements. Security and crew can discover and interrupt this process.

**Stage 2: Incubation - Escalating**

The Dragon begins harvesting nesting material, breaking walls, doors, and other objects for biomaterial.

Consuming nearby structures, items, or crew can reduce the time required to complete nesting. This should be an optional accelerator, not a mandatory requirement.

Once established, the nest begins warming up and producing Carp-related activity.

**Stage 3: Infestation - Station-wide**

The nest becomes extremely hot. Three Carp portals open at randomized locations across the station, creating a station-wide emergency.

These portals begin introducing Space Carps to the station, potentially flooding it with 20-30 Carps. Engineering now has an additional environmental problem to contend with, while the crew has to deal with the infestation.

**Stage 4: Territorial Defense - Established**

The Dragon remains near its nest and defends its territory.

The crew must destroy the Dragon and/or its nest to end the threat. The Dragon's priorities are to protect its territory and defend its nest, rather than actively hunt down crew members across the station.

## Implications

The existing Dragon arrives on the station with the objective of evading Security and establishing three portals. Its five-minute timers force confrontation of an offensive nature, without necessarily producing emergent gameplay from the crew.

Redirecting its objectives toward nesting creates a different kind of threat.

The Dragon is no longer trying to invade the station. It is trying to establish a suitable habitat. The station just happens to be an unsuitable place for that habitat to exist without consequences.

This creates an opportunity for crew to discover, report, investigate, and respond to a localized threat before it becomes a station-wide emergency.

It also gives the Dragon a reason to remain in one place and defend something, rather than constantly moving between objectives and attacking crew to achieve them.

## Features to be added

1. Reorganization of Dragon priorities and objectives.
2. Nesting mechanics, including environmental requirements and biomaterial collection.
3. Nest entity and associated heating mechanics.
4. Carp portal generation following successful nesting.
5. Territorial behavior and nest defense.

### Nesting Requirements

A suitable nesting location should meet several environmental requirements:

- Spaced.
- Cold.
- No oxygen.

The Dragon must remain in the area while performing a nesting DoAfter. This should take approximately two minutes, with the ability to reduce the duration by consuming nearby structures, items, or crew.

If the requirements are not met, the Dragon should receive feedback indicating that the location is unsuitable for nesting.

Successful nesting begins the next stage of the encounter.

### Nest and Infestation

Once nesting is complete, the nest begins generating significant heat and opens three Carp portals at randomized locations around the station.

The portals introduce a larger Carp infestation, turning what began as a localized threat into a station-wide problem.

The nest and Dragon become the center of the encounter. Destroying them should be the primary means of ending the threat.

## Game Design Rationale

Five questions:

- **Would the mechanic make sense if NPC-controlled?** Yes. Animal AI could seek out suitable locations, gather nearby resources, establish a nest, and attack when provoked.
- **Does it create gameplay for others?** Yes. Interdepartmental reporting, Security response, Engineering intervention, and general crew coordination.
- **Does it create consequences without requiring murder?** Yes. Nesting, gathering and hoarding materials, thermal hazards, and the eventual Carp infestation can all exist without the Dragon needing to actively hunt crew.
- **Does it have believable character motivations?** Nobody wants a Dragon on their station. It is dangerous and causes problems, but the Dragon simply sees a suitable nesting location.
- **Is it worthwhile if the Dragon accomplishes nothing?** Yes. It can be killed before nesting, interrupted during establishment, or successfully build a nest and create a station-wide Carp infestation.

## Roundflow & Player Interaction

The Dragon's gameplay should revolve around finding a suitable location, establishing its nest, and defending it.

Security has an opportunity to discover and interrupt the Dragon before nesting is complete. If the nest is discovered, Security has a clear objective: eliminate the Dragon before it can establish itself and trigger a Carp infestation.

Engineering has reasons to respond to the environmental consequences of nesting. Other departments can become involved through reporting, assisting with containment, or dealing with the Carp infestation if nesting succeeds.

The encounter should create multiple opportunities for interaction rather than immediately forcing a fight between the Dragon and Security.

## Administrative & Server Rule Impact

This rework should not require fundamental changes to existing server rules.

The Dragon remains an antagonist, but its objectives and behavior are redirected toward territorial establishment rather than actively seeking out and killing crew.

The intent is to create a threat that can be interacted with and responded to organically, without requiring the Dragon to force conflict through direct aggression.

## Technical Considerations

This rework may be able to reuse several existing systems:

- Existing Dragon entity and behavior.
- Existing Carp Rift and portal functionality.
- Devour and ichor mechanics.
- DoAfter functionality.
- Atmospheric temperature and environmental systems.
- Existing entity destruction and interaction systems.

The largest technical considerations are likely to be the nest entity, its environmental requirements, biomaterial collection, and the transition from successful nesting to portal generation.

The existing portal system may be reusable, but cleanup behavior will need to be considered if the Dragon or nest is destroyed during or after infestation.

## Future Considerations

There may be an opportunity to explore the relationship between Dragons and Thaven in a separate proposal.

Thaven have an established connection to Space Carp through their lore, and Dragons could provide an interesting avenue for expanding that relationship.

However, I do not think Dragon-specific Thaven moods should be a expansion of this rework.
Any additional moods should be considered separately through a future Thaven mood proposal, with their own design rationale and player interaction considerations. (as well, as not tied directly to the "Dragon antagonist event")
## Conclusion

Dragons are my Autistic passion. I implore my proposal to help them move forward as Funky moves to Forky!

I think there's a lot of potential in taking an existing antagonist and giving it a more interesting identity, one that creates gameplay through its existence and behavior rather than relying exclusively on direct confrontation.

I want Dragons to feel like Dragons. Not just another antagonist with a timer, three objectives, and a station full of people to kill.