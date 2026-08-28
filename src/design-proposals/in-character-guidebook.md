# In Character Guidebook

| Designers | Implemented | GitHub Links |
|-----------|---|---|
| Mkanke    | x  | TBD |

## Overview

The main goal of this is to break job guidebook sections into actual IC books that can be used and referenced and of which has a narrow scope written IC that pertains just to that job or topic.

## Background

Currently the guidebook both overwhelming and a mix of both IC and OOC wording. This is not really conducive to talking about ingame topics outside of the use of Help chat which is inherently immersion breaking. After a bunch of discussion in the development chat and guidebook chat the conslusion we came to is that it needs broken up and converted to something that makes sense IC so people can properly reference topics without resorting to OOC speech styles.

## Overall style guide

Guidebook entries should read as if they are written by Centcom training departments by an expert in that particular field. Spice can be added with writing style based off of this such an engi stuff being very exacting while cooking directions might sound like an eccentric cook. The bit should only be so strong as to leave the overall message understandable. Like it makes sense for a clown guide book to be silly and whimsical with colors and styling but at the end of the day Centcom had to approve the document as a readable, usable manual.

## Breakdown of the books

### Old guidebook

This will still exist and be accessed the same way as the current guidebook but will only have topics that are fully OOC, this includes the sections on server rules, Metashield, character creation, antags, survival, glossery and controls. In particular it was agreed the controls section needs expanded to include all of the "word of mouth" shortcuts such as quick retriving items, pinning items in a container and lots of other small things that exist but are mostly unknown to the masses. If any other topic that is fully OOC or meta (such as meta info in general.)

### Service

Currently there are only entries (besides SOP) for the Jani, bartender, botonist and chef. This will need expanded to include the Chaplain, Clown, Mime, Musician and Librarian. Each job book will include a page that is a general overview of their job and expectations as well as a page for their SOP. A few have special considerations though, the Bartender will have a tab featuring drink mixing directions while the chef will have a cookbook for each skill type in the vein of the currently in game Guide to Pies using more IC styles of units (Pinch, cup, etc)

### Cargo

This is a very simple department to break up needing only two books. One for cargo and one for salv. In the same way as above where each job has a main page with a general explaination of their duties and how to carry them out as well as a page with just their SOP.

### Medical

The medical doctors book will be very similar to what they currently have just tweaked to be more IC. The Chemist wont get a book persay but instead their duties will be on a handbook that spawns attached to a chemmaster but is removable, much closer in visual style of the command manual. This will have their specific duties as well as the reference charts for mixing chemicals.

### Science

This department needs the least work of any and mostly just needs a pass over to bring it to feel like an IC training manual.

### Engineering

Oh boy this will be one of the biggest and hardest to do. It is currently very filled with OOC language and will require some heavy reworks to remove OOC terms and introduce more IC version that characters can use in game without sounding out of place. There will only be one part split out of this and that is the gasses tables. Those will be turned into a poster ther when interacted with brings up a book just for it with an individual tab for each gas for quick and easy reference.

## Game Design Rationale

This feature is all about authenticity of the experience. The IC guidebooks are meant to establish a vocabulary that players can use to discuss the topics of their job without having to resort to means such as Help chat or other OOC methods such as discord. It also slows down gameplay in and of the fact that if you want to reference something that is not related to your round start job you must travel to the library or ask someone from that job for their instruction manual.

## Roundflow & Player interaction

This is a round start feature that persists the whole round. Instead of pressing the guidebook function players will have the option to start with one (learner roles start with one). If someone does not start with one they will also be able to found in the library. Some of the more reference materials ones (atmos gasses, chems, recipies) will also be in places around the station that make sense for them to be at such as the stations they are used at.

## Administrative & Server Rule Impact (if applicable)

These changes would not cause any major changes to admin workflow. It only gives players tools to stay more within the rules and immersion.

# Technical Considerations

These changes should all be rather simple yaml work and will not have any performance impacts.