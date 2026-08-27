# Court and Trials

| Designers | Implemented | GitHub Links |
|---|---|---|
| Ferynn + Dev Chat | :x: No | PR Links or TBD |


See this discord conversation for relevant parties, and the root discussion.

https://discord.com/channels/1276640157511979008/1276653734767755294/1460819328650706956

## Overview

This is a formalization of a large brainstorming session we had on improving the legal system, trials, and the magistrate and lawyer system.

The goal of this is to move the action of sentencing and criminal punishment away from the purview of the warden, and shifting it towards the courtroom. Short and speedy trials will be the basis of sentencing.

## Background

Currently, the legal system and trials are in a strange position. The trial system, and the roles surrounding it, sit largely unused. Trials often last longer than any sentence, barring perma cases. They are rarely called upon, and instead almost all sentencing happens and concludes through the warden. This process largely negates the usage of the lawyer and the magistrate, and leaves trials as an exotic and often loathed experience in the wider ecosystem.

This isn't ideal, as these roles have great potential to enhance the roleplay of the process. We don't need to settle for a stressed and overworked warden handling it all, and those courtrooms mapped on stations should be actually used. So, changes need to be made about how we approach and handle criminal sentencing.

## Features to be added

### Increasing Sentence Timers

Our laws and sentencing guidelines were inherited from the Wizden/Goob sphere, where they target much faster rounds than Funkystation does. These sentence times, accelerated compared to the tempo of the rest of the round, cause a very tight squeeze on any legal roleplay or deliberation. Our criminal punishment system should be expanded to fit our timelines, and so all recommended sentence timers should be doubled. This also leads to perma being recommended at a 40 minute sentence timer, instead of 20. These changes will allow for more meaningful legal system interaction, as it becomes more important to argue cases and work for diminished or eliminated charges. Now, spending a few minutes in a trial seems potentially attractive, instead of a waste.

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

- Risks of trial times ballooning and both wasting the times of those directly involved, and those awaiting trial after. 

- Critical need for Judges to keep trials moving. Most trials will ideally be resolved within a handful of minutes, the guilt or innocence often clearly apparent. Outliers are the risk.

- Plea deals are an option to speed through backlogs of cases. A chance to waive trial to keep the queue moving, and keep things on time.

## Administrative & Server Rule Impact (if applicable)

- **Workload:** Well, hopefully it will help in one way, which is restraining the somewhat chaotic nature of current sentencing, where the process is often haphazard and disorganized. This will centralize and order the process, giving clear spaces for them to watch and check in if needed.

- **Player Disputes:** There is the risk for an increase in animosity amongst involved players. Trials can at times get heated, especially for more major crimes. The open nature of a trial could lead to angry "performances" to either get their desired outcome, or to abuse or harass those they feel responsible for their negative outcome.  

- **Enforcement:** This is less of a mechanical change, and more an in character procedural change. Enforcement of the system and its outcomes will ideally be handled with Security and the CC VIPs working in tandem.

# Technical Considerations

- **Performance Impact:** Not applicable

- **New Systems/Refactors:** Requires some form of communication/ping system amongst involved parties. Likely a PDA app, similar to the SOS app, for an initial implementation.
