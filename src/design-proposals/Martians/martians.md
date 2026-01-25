# Martians/Eggheads

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers     | Implemented | GitHub Links |
|---------------|---|---|
| Teasq | :x: No | TBD |

## Overview

![martian preview.png](martian%20preview.png)

Martians, or colloquially known as eggheads, are the classic and quintessential alien. They're short, have big heads, 
and big, black eyes. Everyone knows them, so instead I'm going to drop some lore.

## Background

Martians come from the planet Mart (Mars? Who knows).

For many years, companies have tried and failed to add Martians to their workforce due to the Martians' unique
neurological disposition. Initially, NanoTrasen social workers believed it to be a simple language barrier, but when
usual methods to establish an effective and common language failed it was realized that the Martians' brains did not
work like any other species they had made contact with before.


Many initially believed it to be a neurological disorder similar to aphasia: what Martians mean to say and what they say
*never* align. Early neurologists coined the term "Martaphasia" but that was quickly dispelled due to PR concerns and
for the simple fact that it was not a disorder. This is the norm for Martians. While Martians can understand the

common language (idk what the common language is called? Simlish type shit), any attempts to reciprocate results in
the Martians' uniquely encoded language: glumphish. Many attempts have been made by non-Martians to translate the
language, but all attempts have failed. There are no grammar markers and no correlation between the words they mean to
say and the glumphish that is produced. This seemingly insurmountable language barrier has made every attempt at integrating
Martians a failure, until...


A group of musical Martians took the music industry by storm: the beloved Alien Kids! This group of Martians possess
a unique neurological disorder: their language is not automatically encoded. This not only created a metaphorical
bridge between Martians and the rest of the universe, it also resulted in a massive wave of tourism to Mart
due to the Alien Kids's indefatigable hunger for concerts.

Finally, when asked in an interview how the divide between Martians and the rest of the universe could be bridged even
further, the super-genius superstars made a revelation never before thought of: "Just use AAC tablets." This was
later renamed to the "Speech Pro™" as the brand became synonymous with the product.

## Features to be added

- They are adapted to high pressure environments and have to wear special inner clothing suits and bubble helmets 
or they blobify
- Blobification does not necessarily kill them, just makes them incredibly slow and requires them to be repressurized to
fit back into their suits. (Current idea is a long do-after to "squeeze" them back in.)
- They have language barriers and need Speech Pro's™ to communicate with other species.
- They are particularly weak to piercing damage, because it makes holes in their suits and that is a no-no.
- They have a slightly higher heat resistance, thanks to their adaption to the heat of their planet and the insulative
nature of their suit.
- A selection blues, greens and gray skin tones or at the very least a limited hue selection.

- Most importantly, unique uniform sprites for each department so Martians can still be identified easily.
- A variety of bubble helmets to allow for greater individual expression.

## Game Design Rationale

### Maintaining Authenticity

Martians are as authentically sci-fi as it gets. Their unique appearance,speech and pressurized suits,
while hardly realistic, creates a more authentically alien and strange species that is immediately identifiable.

### Seriously Silly

I mean, just look at them. Other than that, I think their unique encoded language is an entirely new possibility for 
funny scenarios (see the "I am using a Speech Pro™" bit or having a translator that is just translating absolute bogus),
while the AAC tablet still allows them to engage with the rest of the station in a uniquely limiting way similar to mimes
or mute characters.

## Roundflow & Player interaction

Between blobification, the encoded language and the Speech Pro™ I expect player interactions to be largely comedic, while
still allowing for deeper emergent roleplay the same as any other character or role with speech limitations. 

## Administrative & Server Rule Impact (if applicable)

The one, and I imagine most prevalent administrative concern I can think of for Martians are the formation of 
cliques/metafriending. When one's speech is limited, some naturally gravitate towards those they can communicate with
more easily: that being other Martians. 

However, I do not expect a greater degree of meta-friending other than what is already present. Players may gravitate 
towards Martians to form friend-groups or cliques, but I firmly believe that is something they would already have done 
had they intended to and not something the mechanics inherently promote.

# Technical Considerations

- There is a need to port over language systems from other forks specifically for the glumphish, or otherwise a system
that scrambles your speech for those who do not have a specific component.
- Infrastructure is needed to change the Martians' sprites conditionally. This is already being worked on, but the 
mechanic of blobifying is impossible without it.
- VERY IMPORTANT: the AAC tablet needs to be renamed to "Speech Pro™"