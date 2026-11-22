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
4. Give the Dragon more interesting behavior and identity as a piece of space fauna.

### OK, so... you've got dragons in your spesstation

**Stage 1: Establishment - Localized**

The Dragon identifies a suitable location and begins establishing a nest.

Rather than seeking an empty, cold, and spaced environment, the Dragon seeks somewhere it can establish and maintain a suitable atmosphere. A functioning station provides something an asteroid, ruin, or derelict cannot: infrastructure that can eventually stabilize and sustain its nest.

The Dragon begins modifying its surroundings, potentially damaging walls, doors, and other structures in the process. Security and crew can discover and interrupt this process.

**Stage 2: Incubation - Escalating**

The Dragon begins harvesting nesting material, consuming structures and other available resources for biomaterial.

Consuming nearby structures, items, or crew can reduce the time required to complete nesting. This should be an optional accelerator, not a mandatory requirement.

Ichor could provide additional utility during this stage. For example, the Dragon might use it to seal breaches, repair portions of its nesting area, or otherwise modify its surroundings.

As the nest develops, it begins producing significant amounts of heat. This creates an increasingly dangerous localized environmental hazard.

**Stage 3: Territorial Establishment - Escalating**

The nest becomes established and begins producing enough heat to affect its surroundings.

Heat can spread into nearby rooms and maintenance corridors, creating hazards for crew who may not even know a Dragon is present.

The Dragon remains near its nest and defends its territory. Carp-related activity could increase as the nest develops, potentially through eggs or other forms of propagation.

The primary threat is no longer a Dragon actively hunting down crew across the station. It is a growing territorial hazard that becomes increasingly difficult to ignore.

**Stage 4: Territorial Defense - Established**

The Dragon defends its nest and the surrounding area.

The crew must destroy the Dragon and/or its nest to end the threat. The Dragon's priorities are to protect its territory and maintain its nesting environment, rather than actively hunt crew members across the station.

## Implications

The existing Dragon arrives on the station with the objective of evading Security and establishing three portals. Its five-minute timers force confrontation of an offensive nature, without necessarily producing emergent gameplay from the crew.

Redirecting its objectives toward nesting creates a different kind of threat.

The Dragon is no longer trying to invade the station. It is trying to establish a suitable habitat. The station just happens to provide the resources and infrastructure needed to do so.

This gives the Dragon a reason to choose an inhabited station over an asteroid or derelict. It can exploit existing infrastructure, consume materials, and modify its surroundings to create a suitable nesting environment.

It also gives the crew an opportunity to discover, report, investigate, and respond to a localized threat before it becomes a larger emergency.

The environmental consequences should be gradual and recognizable. A maintenance tunnel becoming unusually hot, damaged walls, strange biological material, or unexplained Carp activity can all serve as indicators that something is happening.

The Dragon should add to the round rather than become the entire focus of it. It can be a thorn in one department's side, an infestation in maintenance, or a growing problem that Security eventually has to address.

## Features to be added

1. Reorganization of Dragon priorities and objectives.
2. Nesting mechanics, including environmental requirements and biomaterial collection.
3. Nest entity and associated heating mechanics.
4. Atmospheric interaction and potential breach-sealing functionality.
5. Territorial behavior and nest defense.
6. Additional Dragon-specific behavioral instincts, potentially as a later feature.

### Nesting Requirements

A suitable nesting location should meet several environmental requirements:

- Enclosed or sufficiently sheltered.
- An atmosphere suitable for sustaining the nest.
- Enough surrounding structure and material for the Dragon to establish itself.

The Dragon must remain in the area while performing a nesting DoAfter. This should take approximately two minutes, with the ability to reduce the duration by consuming nearby structures, items, or crew.

If the requirements are not met, the Dragon should receive feedback indicating that the location is unsuitable for nesting.

The Dragon should be able to interact with its environment to make a location suitable. This could include consuming materials and using ichor to seal breaches or repair portions of the nesting area.

Successful nesting begins the next stage of the encounter.

### Nest and Heat

Once nesting is established, the nest begins generating significant heat.

This heat should be a meaningful environmental hazard, but not necessarily an immediate station-wide emergency. Nearby rooms and maintenance corridors should become increasingly dangerous as the nest develops.

Heat escaping through maintenance tunnels could provide an observable warning to the crew. An unusually hot maintenance corridor should be something players can investigate, rather than an arbitrary environmental event.

Engineering has a natural role in responding to the resulting atmospheric and thermal problems, while Security and other departments can investigate the source.

The nest should be a recognizable source of the heat, rather than simply another fire or random atmospheric malfunction.

### Carp Activity

Carp activity should be tied to the Dragon's nesting behavior.

One possibility is that the Dragon lays Carp eggs as part of establishing its nest. These eggs could require a sufficiently warm atmosphere to hatch.

This could replace or supplement the existing Carp Rift mechanics, depending on how much of the existing functionality is worth retaining.

I would prefer gradual propagation over immediately opening three portals and flooding the station with Carp. A small number of Carps can create a localized problem, while a neglected nest can eventually become a much larger one.

The exact number of Carps and rate of propagation would need to be balanced around the intended scale of the encounter.

## Game Design Rationale

Five questions:

- **Would the mechanic make sense if NPC-controlled?** Yes. Animal AI could seek out suitable locations, gather nearby resources, establish a nest, modify its surroundings, and attack when provoked.
- **Does it create gameplay for others?** Yes. Interdepartmental reporting, Security response, Engineering intervention, atmospheric troubleshooting, and general crew coordination.
- **Does it create consequences without requiring murder?** Yes. Nesting, gathering and hoarding materials, breach repair, thermal hazards, and Carp propagation can all exist without the Dragon needing to actively hunt crew.
- **Does it have believable character motivations?** Nobody wants a Dragon on their station. It is dangerous and causes problems, but the Dragon simply sees a suitable nesting location.
- **Is it worthwhile if the Dragon accomplishes nothing?** Yes. It can be killed before nesting, interrupted during establishment, or successfully build a nest that creates a localized environmental and biological hazard.

## Roundflow & Player Interaction

The Dragon's gameplay should revolve around finding a suitable location, establishing its nest, and defending it.

Security has an opportunity to discover and interrupt the Dragon before nesting is complete. If the nest is discovered, Security has a clear objective: eliminate the Dragon before it can establish itself and become a larger problem.

Engineering has reasons to respond to the environmental consequences of nesting. Atmospheric damage, unusual heat, and breaches provide practical reasons for intervention.

Other departments can become involved through reporting, assisting with containment, or dealing with Carp activity if nesting succeeds.

The encounter should create multiple opportunities for interaction rather than immediately forcing a fight between the Dragon and Security.

A small team of crew should be able to hold its own against the Dragon with sufficient coordination and equipment. The Dragon should be dangerous, but not so durable or overwhelming that dealing with it becomes the sole focus of the round.

Likewise, the Dragon should not be so weak that it can be casually removed by one person without meaningful interaction.

## Administrative & Server Rule Impact

This rework should not require fundamental changes to existing server rules.

The Dragon remains an antagonist, but its objectives and behavior are redirected toward territorial establishment rather than actively seeking out and killing crew.

The intent is to create a threat that can be interacted with and responded to organically, without requiring the Dragon to force conflict through direct aggression.

## Technical Considerations

This rework may be able to reuse several existing systems:

- Existing Dragon entity and behavior.
- Existing Carp Rift and portal functionality, if retained.
- Devour and ichor mechanics.
- DoAfter functionality.
- Atmospheric temperature and environmental systems.
- Existing entity destruction and interaction systems.

The largest technical considerations are likely to be the nest entity, its environmental requirements, biomaterial collection, atmospheric interaction, and heating behavior.

Ichor may provide an opportunity to reuse existing Dragon mechanics for additional utility. For example, it could be used to seal breaches or modify the nesting area, rather than serving exclusively as a healing resource.

Carp propagation will also need consideration. Whether this uses existing portal functionality, eggs, or another system should be decided based on what best supports the intended gameplay.

## Future Considerations

There may be an opportunity to expand Dragon behavior through additional Dragon-specific instincts or moods.

These could be optional behavioral objectives selected from a short list, rather than additional mandatory antagonist objectives.

Examples:

- Gather objects of a particular color.
- Hoard shiny or valuable objects.
- Protect a lesser creature.
- Eat its fill before nesting.

These instincts could give individual Dragons different personalities and motivations without changing the central nesting objective.

There may also be an opportunity to explore the relationship between Dragons and Thaven through these mechanics. Thaven have an established connection to Space Carp through their lore, and Dragon-specific instincts could provide an interesting avenue for expanding that relationship.

However, I do not think Dragon-specific Thaven moods should be a dependency of this rework. Any additional Thaven moods should be considered separately through a future Thaven mood PR, with their own design rationale and player interaction considerations.

## Conclusion

Dragons are my Autistic passion. I implore my proposal to help them move forward as Funky moves to Forky!

I think there's a lot of potential in taking an existing antagonist and giving it a more interesting identity, one that creates gameplay through its existence and behavior rather than relying exclusively on direct confrontation.

I want Dragons to feel like Dragons. Not just another antagonist with a timer, three objectives, and a station full of people to kill.