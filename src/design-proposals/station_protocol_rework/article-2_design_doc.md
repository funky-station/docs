# Nanotrasen Colonial Law and Procedure: Corporate Law

| Designers | Implemented | GitHub Links |
|---|---|---|
| SOP Workgroup, Design Doc written by Joaco545 | :x: No | TBD |

## Overview

This proposal aims to revamp Space Law completely, while keeping the new theme direction in mind.

Space law has been revised to conform to the style of a legal document.
The crime list has been expanded, and sentencing guidelines have been simplified.
Contraband has been vaguelawed.


## Background

Funky Station has been changed to have a Corporation vs Crew, Class Conflict theme. This requires updating Space Law as it no longer fits the theme.
Currently, space law feels like something an external entity that is not Nanotrasen has set in place, and is forcing NT to comply with it; We aim to change that feeling completely.
We also took this opportunity to add some things to increase the RP potential, coupled with the [sentencing changes](article-5_design_doc.md).


## Features to be added

To see all the new proposed changes to Corporate Law, please check out the [supporting doc](Article%202%20-%20Corporate%20law.md) with the draft (Still not up at the time of commiting this, for now, the things can be found on the [Google doc under the Article 2 tab](https://docs.google.com/document/d/1HhQ9L_5KLPLiYH3W9_V8gIqyjH2lBxOt-W90n76cLtY/edit?tab=t.ushwxj8tclf6#heading=h.x3qf6opli0z2). Yes Tay, this link is temporary)

### Space Law rename
While it may not seem like much, Space Law has been renamed to Corporate Law to better fit the theme of NT owning you, the station, and all surrounding space. You are in their house, you play under their rules.

### Corporate Law: Searches
The way searches are conducted has been reworded with a bit more legalese, and in the case of departmental searches, they have been made clearer as to what is included, and especially what's NOT included (personnel).

### Corporate Law: Detainment and Arrests
There is now a difference between being detained and being arrested:
Detained means the person is not free to go. It is here mostly for the investigation part, not letting suspects go free until you have the evidence you need.
Arested means that the person will be guided to security for search and a subsequent trial.
In both cases, the detainees or arrestees should not be cuffed if they are complying.

### Corporate Law: Chain of Custody
This specifies how Security is expected to play out each of the steps from arrest to the brig. This is mostly a supporting change for [Sentencing, Trials, and Hearings](article-5_design_doc.md).
This ups the standards Security personnel are held toin-character, while giving good lawyers more tools to finagle their clients out of a sentence, or at least enter a reduced one.

### Corporate Law: Treatment of Arrestees and Prisoners
This section is kept mostly the same as the old treatment of prisoners.

### Corporate Law: Implantation
This section is kept mostly the same as before, with a bit more legalese.

### Corporate Law: List of Crimes
This area has been majorly reworked and expanded. NT now has more ways to get employees who are not behaving.

#### Crime Categories
The tier system has been revamped into 4 named crime tiers:
- Infraction: They cover minor offenses, which do not lead to brig time.
- Misdomenor: They cover more serious offenses, which can lead to brig time.
- Felony: They cover serious crimes, can lead to more brig time.
- Capital Offenses: They deal with the most serious crimes against NT, can lead to permanent confinement, contract termination, or execution.

Note: Execution requires Captain and XO (HOP) approval

Big times have been standardized so that sentencing gets easier. They now directly depend on their category, instead of the individual crime.

The crime list has also been expanded to give NT more power over how people and unions behave. The line between a strike and a riot is a thin one.
We expect security vs crew to increase the friction between Command and the Crew, giving more opportunities for escalation should the players choose to do so.

#### Infraction enforment
Infractions are not meant to be something everyone needs to go to a judge for; They will be handed out by Security.
Fines can be disputed, but that requires the player to say they want to do that (See [Technical Considerations](#technical-considerations)).
As a perverse incentive, fines made by Security will go to the Security department’s budget, and the Head of Security will be able to use those funds to buy things for the team or increase the pay of Security employees.

### Corporate Law: Contraband Classifications
Old Contraband has been replaced by Vaguelawed Contraband. To support this change, contraband markers will need to be removed from the game.
These changes were made to increase the RP potential, as now, confiscating something is a choice to be made by players, and not by a marker.
This also makes meteshielded components harder to identify, unlike the old system which made confiscation a must (Syndicate pajamas, anyone?)
It is also another way for escalation to happen is Sec confiscates too much or too little with the crew and command, respectively 

### Corporate Law: Legal Exemptions
Certain jobs may be except of certain laws under certain conditions, this includes security's monopoly on violence, or more mundane things like engi breaking into places to fix a fire.

#### Clown Exception
The clown crime exception has been re-added for some Seriously Silly points.
It has a couple more caveats to reduce the scope of what the clown can do, while also requiring the judge to find it funny for the exemption to apply.


## Game Design Rationale

A lot of these changes have been done with two pillars in mind:

- New Theming / Authenticity
  Working on an NT Space Station will now feel more oppressive for the normal workers, while unions act as a small reprieve, NT still has a lot of power inside and outside the station. It makes the story being told more coherent.

- Escalation / Maximising roleplay potential
  The features mentioned in this doc all aim to keep the same level of RP or increase it.


## Roundflow & Player interaction

Corporate Law is something that will permeate each round from roundstart till evac docs on CC, and all players will have to engage with it.
Common sense will keep most players outside of Securities radar, but it will still be something present.

Example of Non-Antag Escalation Oportunities:
As an example an assitant could get fined by security for Loitering, the assistant, not able to get the Scrip to pay the fine, gets charged with Failure to Pay a Fine. This builds up resentment, and once they are out of the brig, the look for other people wronged by sec and start a strike.
As the strike was not approved, Security tries to split up the strike. First peacefully, then by using Tear Gas. Then the thing turns violent and now there is a partial riot on the station.

Example of Antag Shielded Contra:
A wizard appears on the station, a security officer stops them for a random search. They see some clothing and an orb, think nothing of it, and let them go. Half an hour later the wizard has killed 3 people and is captured, this time command gets involved and recognizes that the orb and clothes are used for casting the dangerous spells the wizard has been using per the CTMs info. They decide to confiscate the items saying that their combined use is like that of a major weapon


## Administrative & Server Rule Impact (if applicable)

As mentioned on the main doc, with so many changes we think players will AHelp more to ask for clarification on said changes.

## Techincal Considerations

For infraction enfocement, two new things will need to be implemented:
- Sec will need to get a new device capable of printing fines, and;
- An ATM-like device near the courtroom that allows players to pay the fine, or give the option to page the judge for it to be disputed.
