# ID & Contracts

| Designers | Implemented | GitHub Links |
| ----- | :---: | ----- |
| Moxie\_is\_Moxie | ❌ No | TBD |

## Overview

This document alters how ID’s function and how crew members are tracked. Every crew member will have a tracking number, which is used for paychecks, storing contract info, and disciplinary action. 

## Background

This is a document meant to support the less-defined features and consequences from both the Scirp and Unions game design docs. By fleshing out the fine details before anywork is done, the hope is to smooth out the development process while adding features to support the themes and ideas of funky moving forward.  

## Features to be added

###  ID & Tracking Numbers

All employees will have an NT Tracking number. They consist of two parts, the prefix and the number. The prefix is what a person is to Nanotrasen. 

| Prefix |  |
| :---- | :---- |
| NT | Has a valid NT contract and is crew (this is the only one considered crew by borgs) |
| TM | Has a terminated contract with NT |
| IS | Is the currently in imprisoned servitude to NT |
| UR | Non-NT people who use NT systems for vacationing or trade |
| XX | Legally marked as dead and all accounts are frozen(this is what crew are marked as during epsilon) |
| NA | The tracking number has been voided, and a new one issued  |

The prefix of the tracking number can be changed by the hop or the captain freely, but has no bearing on the system that uses the number. The number is what is used for systems like banking, managing contracts, and using other NT systems. 

Example: NT-123456, an assistant who holds a valid NT contract. When the assistant is fired, it becomes TM-123456

Tracking numbers are used in a number of systems instead of the crew's name and should become the primary way to look someone up and add them to the system. When a crew member is added to a manifest and given a contract, they will use the tracking number and not the name. If you ever lose your ID, your roundstart tracking number will be in the character menu. 

#### ID Cards

ID cards can not be vended in blank PDAs. Instead, they have to be printed on a special machine first with the unchangeable tracking number, card base, and the physical job icon. Once it is printed, it can then be set up with a name and access on the id computer.  If a new id with the used tracking number is printed, the older one will be voided 5 minutes after printing the new one (agent IDs being the exception). The Base of the ID is what gives them the privileges on the station. 

Card Bases

| Base | Normal Cards |
| :---- | :---- |
| Standard  | Basic id card for accessing public NT properties  |
| Silver | Can access employee contract records, and submit contract changes. These are the IDs that Heads of staff use. |
| Gold | All the perks of Silver. It needs to approve contracts, termination, and other systems that need safe guards. These are for HOP and the captain.  |
|  | CC Restricted Cards |
| Sapphire  | Like the standard, but can not be changed nor fined. For IAA and other Lower CC roles |
| Diamond | Like the Silver, but can not be changed nor fined. For NTR, and ERT |
| Emerald | Like the Gold, but can not be changed nor fined. For magistrate and ERT Leaders |
| Opal | All the perks or gold, and all the special stuff for admemes (unprintable) |
|  | Special Cards |
| Platinum  | Like standard, but vendors can give special gifts for NT loyalty. Aren’t you special\! |

### NT Banking & Pay Checks

As mentioned in the scrip doc, the crew will be paid out every 10 minutes. This will be transferred into an NT bank account that uses the crew member's Tracking ID. By inserting their ID card into an ATM or manually inputting their tracking number. From there, the scrip can be physically withdrawn or loaded into the ID Card for BankApp.

#### Contracts

Your paycheck will be determined by the contract you currently hold with NT, but be increased up to 200% or decreased to 0% via the Hop’s payportal console. At round start, there is a chance for your pay to be between 75 to 125% of the normal pay.  Additionally, the crew will start with 1-3 deposits already in their account. 

| Contract | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Civilian | 10 | 15 | 20 | 25 | 30 |
| Service | 15 | 20 | 25 | 35 | 45 |
| Engineers | 20 | 30 | 40 | 50 | 60 |
| Security | 20 | 30 | 45 | 60 | 80 |
| Medical | 25 | 35 | 45 | 55 | 65 |
| Science | 25 | 35 | 45 | 60 | 75 |
| Command | 35 | 45 | 60 | 75 | 90 |

Assistants have their own unique contracts with them, starting with a class 0 contract. Instead, they must get Head of Staff stamps on their work card for a bonus. 

#### Tickets

Sec and command can now give out fines or tickets using their Id scanner (elaborated on later). If approved, the amount of the ticket will be deducted from the crew member's account. This is the only way a bank balance can become negative. 

### Head of Personal and Contracts

The Head of Personnel will be the person who will interact the most with IDs and contracts. They are responsible for making sure the crew gets paid, and sometimes do not get paid. There is a limit on how much NT is willing to pay staff. Only payments made in the last 15 minutes will count towards employee cost (with money from ticket lowering it). If employee costs get high and stay high, NT might have to step in. Making sure the employee costs stay reasonable will prevent them from approving every bonus. To survive, the crew from tearing them limb from limb, they must weaponize bureaucracy. Additionally, this may require HoP to be split off from service and be a second in command to cap. 

####  New HoP Consoles

**Payment portal** \-this is a console that lets the HoP manage the paycheck. This includes an increase of up to 200% or a decrease to 0%, halting payments, and forcing manual review (applies them as a bonus). Bonus can also be manually sent through this console. This console requires a gold ID to be inserted to make adjustments. 

**Staff manager** \- This console is used to approve or deny bonuses, pay adjustments, and contract change requests that are submitted via command. CC can also send in the bonus or bonus events (like a pizza party).

**Contract terminal** \- Allows for manual change and termination of NT contracts, and to mark if a crew member has a Mindsheild.

**Tickets console** \- Allow for the approval of denial of tickets and arrests (this is mainly for magists but being a CC role, HoP should be a backup)

### Security and IDs

Gone will be the day of being able to look into a crowd of people and pick out a wanted suspect. In its place, a golden age of checkpoints and stop-and-identify procedures

#### Security Scanner

The Security Scanner is used to pull up all relevant information related to the ID by scanning it (the id can not be in a device when scanning). This will open a UI containing all the relevant info pertaining to the ID, including name, tracking number, warrants, minddsheild status, and criminal history. A standard ID or better is to be inserted to function.

If the security officer deems it fitting to give a ticket or need one for an arrest, they can do so in the scanner. The officer must give both a reason and the amount of the ticket (either scrip or the sentence time). Once submitted, they will go to the ticket console to be approved by the Magistrate if one is available or the HoP if not. The name of both the ticket submitter, the ticketie, the amount, and the reason will all be available to see. The Magistrate is encouraged to hear a person's case before a ticket is submitted. If the ticket is to serve time, a quick trial must be had. 

#### ID detectors 

Similar to contraband detectors, these will scan the ID of those who pass them. The detector looks for two things. The first is checking if the ID has the programmed accesses (none by default, security ones can be mapped), and the second is the NT prefix on the tracking ID. If one or the other is missing this an alarm will go off for 5 seconds. 

#### Security Headset 

Security glasses and the hud concept will be removed from the base security load. Instead, they will be a research option for Sci. Even still, they will be made into full headsets that block both the head and mask slots and reduce vision like a welding mask. This can only be unlocked via research. 

### Command and ID

Like the sec glasses, the command glasses will be killed. In its place, command will be given the ability to monetarily punish employees and even have an express way to fire them. 

#### Command Scanner

Functions like a security scanner, but with the ability to submit pay adjustments, contract changes, and bonus requests. It requires a silver ID or better to function. If the ID is silver, submissions will go to the staff management console for HoP approval. If a gold ID is instearted the request will be changed automatically. CC restricted id will also have the ability to send the change up to CC instead for automatic approval with a long delay (or being rejected by the admins). 

## Game Design Rationale

### Maintaining Authenticity

This system makes the ID systems more authentic and in-depth. This is especially for security and command, who will no longer be able to check IDs by looking at them. Instead, they must ask employees to hand over their IDs to be scanned. It also give a way for heads to fire or punish employees in a way that feels more tactical. This is especially true for the Magistrate and HoP, who get the final say on fines and bonuses respectively. 

### Maximizing Roleplay Potential

This will allow for more drama about contracts and pay raises between employees and Heads of Staff and Heads of Staff and HoP. Not only can drama be created from the bonuses and tickets, but also from those who refuse to hand over their ID to avoid tickets requiring out-of-department action. 

## Roundflow & Player interaction

As mentioned in Maximizing Roleplay Potential, this will make Heads of Staff more reliant on the HoP to process paperwork and get mad at them when it is denied. It also adds more interactions in the judiciary department, as sentences and fines will need to be approved, and means lawyers are more relevant. 

Additionally, this would significantly slow down Sec’s ability to track someone down and be able to find out if someone has a stolen ID. Lucky, the difference in ID value has never been more apparent than ever, so Standard ID is no longer as valuable alone. 

## Administrative & Server Rule Impact (if applicable)

These systems can be abused like most systems that can affect the rounds and consideration about what is considered round sabatash. This may be especially for HoPs and being too liberal with their payraises and bonuses. This will hopefully be fixed in time, but watching out for abuses will be necessary. 

## Technical Considerations

Several new UIs and mechanics will need to be made:

* ID scanners  
* All HoP-related consoles   
* Contract database

Additionally, this would require multiple changes to have players spawned in and how the crew manifest works.  
