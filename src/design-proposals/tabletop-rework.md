# Tabletop Snapping Rework

| Designers    | Implemented | GitHub Links |
|--------------|---|---|
| RedaREDACTED |  :x: No |  TBD |

## Overview

I think Chess, and by extension other Tabletop games need the ability to "snap" pieces into "boardgame spaces". This is a peeve of mine of misaligned pieces.

## Background

In the current state of the game. you can pick up pieces and place them anywhere. not only can you make "illegal" moves, you can completely misalign pieces.

## Features to be added

I would like to add, at minimum, a change to the system to allow the definition of "snapping" to a grid, or allowed "area" (the captured pieces zone in chess)

## Game Design Rationale

Consider addressing:
- How does the feature align with our [Core Design Principles](../design/design-principles.md) and game philosphy?

It expands on the current system, allowing for easier use of tabletop games, hopefully increasing their use

## Roundflow & Player interaction

Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?

Self explanitory, it expands the ability to use these interactions

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?

N/A

# Technical Considerations

- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)

This requires the consideration of;
different tabletop games
"out of board" areas (such as the chess "capture" zone)
piece capture