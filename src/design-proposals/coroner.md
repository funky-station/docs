# Coroner

| Designers  | Implemented | GitHub Links |
| ---------- | ----------- | ------------ |
| correspond | :x:         | TBD          |

## Overview

The *coroner* is a job from Space Station 13, tasked with anything in relation to the morgue. Their primary concern is preventing corpses from rotting and are properly revived, however, they are also in charge of performing autopsies and ensuring cloning properly works. This role is present on both [Paradise](https://www.paradisestation.org/wiki/index.php/Coroner) and [/tg/](https://wiki.tgstation13.org/Coroner). This implementation would likely not stray very much from Paradise's implementation, barring the actual differences in 13 and 14's medical systems. 

With the coming addition of [woundmed](https://github.com/Goob-Station/Goob-Station/pull/1859), primarily the addition of organ rot, medical is close to getting the complexity to allow for the coroner. Along with this, rotting bodies not properly being taken care of is a common problem in rounds. Having dedicated staff to make sure that corpses are, at least, properly placed into the morgue or body bags will help ensure less players are round removed due to medical incompetence. 

By adding a role with an emphasis on post-mortem investigation, stealth-based antagonists are also given a way to have more interaction with the crew. Even if an antagonist round removes or near-round removes a corpse, the coroner can still perform autopsies in order to try and guess who and what the antagonist is. For example, a coroner would be able to accurately tell the difference between a death caused by a changeling, traitor, or heretic sacrifice, regardless of if said antagonist has a direct way for the crew to know what they are (ex. if a changeling's hollowing text was removed). With more development, this may offer a way for the maintainers to further move away from the metashield.

With this, a need has risen for a dedicated position to handling cadavers; the coroner being an obvious answer to this niche. Even outside of the mechanical need for this position, the coroner offers the potential for more roleplay. Both funeral services and court cases could benefit from the additions the coroner adds, ranging from embalming services to forensics.

## Background

The coroner is a role originally from SS13, featured in both Paradise and /tg/. Its implementation in SS14 will likely not change very much from SS13, its main differences stemming from the two different medical systems. As SS14's medical system grows, the coroner's mechanics will have more parity with SS13. 

## Features to be added

The coroner relies on the addition of woundmed, as one of their key roles is handling organs of corpses. While they are able to be able to added without woundmed, some of their key gameplay mechanics (embalming and formaldehyde) require some sort of organ rot system in order to work properly. 

Autopsy reports are also reliant on a better system for describing wounds and their possible causes. While the current medical system can somewhat achieve this, it does not have the same complexity that woundmed offers. Ideally, with woundmed, coroners and detectives would be able to compare the type of wounds on a cadaver (ex. gunshot wounds versus bone fractures and internal bleeding) in order to guess the cause of death, rather than having to simply guess from the type of damage (ex. lots of pierce damage means a gun was likely used). 

### Autopsies

Autopsies are thorough examinations of any corpses in order to determine the cause of death. Autopsies would follow a simple gameplay loop: scan the cadaver with a medical scanner, determine if they are revivable, scan the cadaver with an autopsy scanner, and then document the information. Medical doctors would still be tasked with revival, coroners instead focusing on the actual notetaking and forensics. 

The autopsy scanner would give coroners the following information about the cadaver:
- The time of death
- Injuries and their likely causes
- A toxicology report (any reagents in the corpse at the time of death)

Mechanically, this loop largely relies on the player filling out forms and trying to uncover the truth of a murder OOC, rather than the game concretely telling them. For example, autopsies would tell the time of death of a corpse. With this information, detectives and coroners should be able to cross compare the location if a death in order to figure out who the murderer likely was. 

The purpose of these in SS14 is to give forensics something more to do. By encouraging players to pay more attention to someone's cause of death, antagonists are encouraged to be more subtle with their kill methods. This overall encourages a gameplay loop similar to other traitor games, rather than the current gameplay encouraging antagonists to 'go loud.'

### Medical Records

Since coroners focus so heavily on forms and notetaking, a proper system in order to catalogue and organize this information is necessary. The medical records computer would be given functionality in order to fulfill this need, becoming similar to the criminal records computer.

### Embalming

Embalming is largely a stretch goal for coroners, not offering very much mechanical gameplay. Embalming would be the exact same as surgery, its only difference being that it would require the usage of an embalming chemical. 

Instead, embalming is meant to be a task only necessary in roleplay-driven scenarios. If a corpse is unable to be revived or cloned, yet a player deems that they want to perform a funeral service, then the coroner could embalm the corpse in order to prepare the cadaver for a funeral service. 

## Game Design Rationale

### Seriously Silly

This design doc makes the coroner a more serious role, generally encouraging a more MRP playstyle. Its emphasis on forensics and real medical processes generally places the coroner in a more realistic setting. However, despite this, the nature of the game still allows the coroner to be silly, as players would be encouraged to treat otherwise ridiculous settings as serious. 
### There is no Winning or Losing

The coroner helps solve many current issues with gameplay. Players are often round removed because they rot in medical, and the coroner is specifically tasked with making sure that corpses do not rot. In the case that new medical staff do not know how to address specific causes of death or how to clone people, the coroner is specifically tasked with making sure that players are properly revived. 

### Maintaining Authenticity

While autopsies are a real-life procedure, this is ultimately a very simplified version of them. They are meant to be authentic the end goal of an autopsy, determining the cause of death. Details of an actual autopsy or embalming will be skipped in order to be more aware of players who may feel uncomfortable with medical procedures. In this case, maintaining authenticity is an important aspect to consider with the implementation of the coroner because of its heavy implications to real life procedures. The coroner, and its associated mechanics, should be simplified and silly. They should feel authentic, but not be too realistic. 

### Dynamic Environment

The coroner is, by technicality, an optional role. It should range from 0-2 slots, low pop stations forgoing the role entirely. Ultimately, the coroner is meant to be an optional role to dynamically interact with the station's events. If the game mode focuses on stealthy antagonists (lings, traitors, thieves), then the coroner is meant to work with the detective to try and figure out who the antagonists are. If the game mode focuses on high impact, loud antagonists (nukies, late game cults), then the coroner should focus on managing corpses and ensuring that players are properly revived. Their role should change with the station. 

## Roundflow & Player Interaction

The coroner is a role best suited for mid to late shift times. They, by definition, do not have very much to do during the first few minutes of the shift. However, the coroner is a role that encourages roleplay with some mechanical backing. The coroner offers an interesting background to characters, since it is such a specific role. For example, why would a character choose to be a coroner, surrounded by death, rather than a medical doctor? 

## Technical Considerations

Most of the technical details have been outlined prior. This, of course, requires woundmed. The coroner will also will also need multiple new devices and their corresponding UIs: the autopsy scanner and medical records. There will also likely need to be some refactoring of how corpse information is stored, as the autopsy scanner will need to report detailed information of the time of death and reagents in the cadaver. 

I'll make Figma prototypes for the UIs at some point... 
