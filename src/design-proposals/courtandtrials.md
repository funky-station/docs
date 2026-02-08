# Short, Properly Capitalized Title

Reworking the Legal System

| Designers | Implemented | GitHub Links |
|---|---|---|
| Ferynn + Dev Chat | :white_check_mark: Yes or :warning: Partially or :information_source: Open PR or :x: No | PR Links or TBD |

`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.

## Overview

This is a formalization of a large brainstorming session we had on improving the legal system, trials, and the magistrate and lawyer system.

The goal of this is to move the action of sentencing and criminal punishment away from the purview of the warden, and shifting it towards the courtroom.

## Background

Currently, the legal system and trials at large are in a strange position. The trial system, and the legal apparatus at large, sits largely unused. Trials often last longer than any sentence, barring perma cases. They are rarely called upon, and almost all sentencing happens and concludes through the warden. This process largely negates the usage of the lawyer and the magistrate, and leaves trials as an exotic and often loathed experience in the wider ecosystem.

To change this, several things need to be shifted. Criminal sentencing guidelines have been inherited from Wizden and similar servers, which aim for a faster paced game, and shorter rounds. This leads to trial related actions going to the wayside, as most sentences finish before a trial could conclude. The fact that trials are such a rare occurrence further seperates them from common thought and practice. 

Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.

## Features to be added

### Increasing Sentence Timers

All sentence timers will be doubled. Perma is at 40 minutes instead of 20. Our rounds are targeted for two hours is which is about double of the Wizden/Goob sphere. Our criminal punishment system should be expanded to fit our timelines. This allows for meaningful legal system interaction, as it becomes more important to argue cases and get diminished or eliminated charges.

### Reworking Trials

Trials will be reworked in a broad sense, streamlined, and made central to the criminal enforcement system. Instead of the warden sentencing prisoners, all prisoners will be brought to the court for trial. All trials should be resolved within several minutes, and ten minutes at max. Trials should be commenced soon after the arrest and initial processing of a prisoner. Trials can be delayed at the accused's discretion, for their legal representation to gather evidence or relevant witnesses. If such an extension occurs, the accused will spend this time in the brig.

The prosecution is filled by an IAA. As part of this change in legal systems, IAAs are shifted to cover both SOP and Space Law, acting in either sphere as the NTR and Magistrate require. If an IAA is not available to serve as prosecution, a court appointed prosecutor can serve.

Defense is handled by Lawyers, or by a judge approved alternative. A trial can proceed if no defense is available. When scrip is added, this will provide the opportunity for legal fees and other pressures to be added to crew.

The Magistrate serves as the Judge, overseeing trials and assigning sentences. If there is not a Magistrate available, the NTR judges. If the NTR is not available, the Captain judges.

When a prisoner is arrested and in need of a trial, all relevant staff are required to attend within one minute. Extensions can be given for extenuating circumstances. The accused will be transferred to the courtroom by a member of the security department, serving as a Baliff. This role can be appointed through collaboration between the presiding Judge and the Head of Security.

The prosecution begins by giving their case, presenting evidence and witness testimony, and recommending charges to the presiding judge.  The defense then counters arguments and potentially provides their own witness testimony. Throughout this, limited cross-examination can be provided. The goal is for most trials to go quickly, and the presiding judge will work to ensure this happens.

While charges are recommended by the prosecution, and they build their case to support them, all final decisions on charges are given by the presiding judge. If guilty of any crimes, the accused is sent to the brig for their sentence. If not, they are let go.

A prisoner can waive their right to a trial and enter a guilty plea, to expedite the court process. While this does not always lead to reduced sentencing, the presiding judge should take cooperation into account. This allows for the creation of plea deals between the defense and judge, as well.

### Required Dev Work

To support this system, at minimum, a PDA app would need to be created, allowing for relevant parties to be pinged when a trial is imminent. A sample default set of PDAs including this would be the Warden, CC VIPs, Lawyers, and the HOS. Usage of a software cartridge would allow for this system to be included for a chosen Baliff. 

This could be potentially expanded with further work into a more advanced system, so information could be transferred on the impending trial to relevant parties, and allowing for information to be sent back to the warden on sentences. 


## Game Design Rationale

- **Taking Things Slow**: This extends our legal system to the longer time frame of a Funkystation round. It allows the crime and punishment system to be extended and deepened beyond a the 15 second deliberation of an overworked and stressed Warden.

- **Maximizing Roleplay Potential**: Having trials for all crimes allows for the legal roles to finally have a use on the station. No longer will they all have to sit in sec aimlessly hoping for something to happen. The legal system will become a core part of the sec and crime experience, allowing for courtroom drama to happen on a regular basis.

- **Maintaining Authenticity**: It makes *sense* to use the courtroom for crimes. It makes *sense* to have lawyers arguing, judges deliberating. All of these things are  thematic and ingrained in cultural media, and right now they're missing in the Funky experience. This is a step to bring that resonance back.

- **Seriously Silly**: This change doesn't inherently tie into this principle, but the increase in roleplay could passively result in more of this. Whacky lawyer speeches, courtroom bombings, and more. The more reasons there are to group large amounts of players in a room and have them talk, the more chances there are for strange and fun situations to arise.



## Roundflow & Player interaction

With this change, the legal system and trials will happen regularly, and often intersect with player experience. While this does have positives, as listed above, there are dangers as well.

Time control by the Judge is perhaps the most critical part of this. Trials have a reputation for running long, and even with streamlining the process, the risk remains. Ideally trials will be speedy and a decent enough experience for all involved. Most crimes are fairly open and shut, one way or another. The outliers though could lead to ballooning trial times if not carefully monitored.


## Administrative & Server Rule Impact (if applicable)

- **Workload:** Well, hopefully it will help in one way, which is restraining the somewhat chaotic nature of current sentencing, where the process is often haphazard and disorganized. This will centralize and order the process, giving clear spaces for them to watch and check in if needed.

- **Player Disputes:** There is the risk for an increase in animosity amongst involved players. Trials can at times get heated, especially for more major crimes. The open nature of a trial could lead to angry "performances" to either get their desired outcome, or to abuse or harass those they feel responsible for their negative outcome.  

- **Enforcement:** This is less of a mechanical change, and more an in character procedural change. Enforcement of the system and its outcomes will ideally be handled with Security and the CC VIPs working in tandem.

# Technical Considerations

- **Performance Impact:** Not applicable
_ **New Systems/Refactors:** Requires some form of communication/ping system amongst involved parties. Likely a PDA app, similar to the SOS app, for an initial implementation.
