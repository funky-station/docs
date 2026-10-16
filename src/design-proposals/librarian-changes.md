# Software Library

| Designers | Implemented | GitHub Links |
|---|---|---|
| taydeo | :x: No | TBD |

## Overview

The Librarian is an overlooked role, and with machines being able to be built with no skill or consequence to anyone, it's time to re-evaluate the roleplay value in constructing a machine. It's also rather strange that machines don't require any software or whatever. This inclusion should allow more creative ways to upgrade machines as well as more involvement from the service department in everyday station life.

## Background

Currently, it is trivial to construct a machine. If you have the materials and the circuit board, you can consider it done. This is fine for faster paced servers, but for Funky Station this presents a gap in logic. Why can machines run with no software (even if its implied the circuit board has it embeded), do machines always need new parts to be remade? What exactly goes into sabotaging a machine? Why is everyone else uninvolved in the construction of new machines, and should the librarian be responsible for only books?

This design document seeks to expand the role of the Librarian and related service roles. There should be much more at stake on the station in a lore sense.

The librarian will now be in charge of cataloguing and sorting software, and determining which would be best for a department to have. 

## Features to be added

To support the software library, bookshelves would need to be filled with a new item, master disks.

### Master Disk

A master disk contains software content for a specific machine and can be copied from. Master disks are round start or can be created by Science. The librarian can create copies of the master disk, which cannot be read from outside of the machine it is intended fork.

The master disk can be emagged. Specific interactions for single master disks can vary.

Master disks must be protected by the librarian. Original master disks cannot be ordered from the ATS. If they are gone, the station might lose out on a specific piece of machinery.

Master disks can only be read from a certain number of times. Research must be done with them in order to make sure there are enough for the station.

### Floppy Disk

A floppy disk is an empty or filled disk that contains the software for a particular machine. For example, the flatpak is just a hunk of metal without a disk inserted. These disks can change the efficiency of machines, either making machines cost more in materials, produce things faster, or other unintended side effects.

Every machine in the game will now have a floppy disk slot, that can only be access by engineering or science. Every machine needs a floppy disk to operate, including computers. Emagging a computer or machine only affects the floppy disk, so the emagged state of a machine is now saved on a physical piece of media. Using the disk of an emagged machine in another machine of the same type will cause the machine to operate like its emagged counter part.

### Disk Cloner

The disk cloner is a machine that takes two slots, one for the master disk, and another for the recipient. This machine is at the libarians desk. Due to the intensive reading process, the durability of master disks goes down. It takes approximately 10-20 seconds for a clone to be complete. After the clone is complete, it will beep and the disk will auto eject. Ejecting a disk during the copy process may destroy the master disk, so patience is a virtue.

### General Purpose Software Optimizer (GPSO-1-M)

The GPSO-1 is a massive assortment of machines that read entropy from the station (think burn chambers, the bar, medical, etc.) and feeds it through an AI model that must be kept cold. The AI model is called the GPSO-1, and GPSO-1-M is the name of the machine that hosts it. This must be cooled, as allowing the GPSO-1-M to reach over 250C will cause it to explode, requiring several hundreds of thousands of spesos worth of materials to be imported as well as a form being sent to Central Command.

### GPSO-1 Output Node

The GPSO-1 Output Node is where new disks are printed when research into a specific machine is complete. Each research cycle lasts around a minute, and produces a new master disk. These master disks only last 5 uses. The master disks can be recycled back into materials if they really are that garbage. 

### GPSO-1 Input Node

The GPSO-1 Input Node is a node that can take a master disk. In this way, the AI model learns what optimizations to use by referencing old disks, and the more of a statistic you stack the better chances it will have of affecting that statistic. These nodes may also take in books. Books are infinite use and their effects are unique per machine. The librarian must research what each book does to the machine. Each GPSO-1-M megamachine may take up to 6 of these Input Nodes. This does use one durability on each disk.

### GPSO-1 Gasseous Entropy Node

The GPSO-1 Gassous Entropy Node may read data from a gas being pumped through it. These gasses, the more exotic and volatile they are, produce more entropy, allowing for more variation in changes, and may include special side effects for software. 

### GPSO-1 Entropy Node

A GPSO-1 Entropy Node collects data that feeds the AI model data. These can be placed discreetly around the station, being hidden in plants, containers, bottles, etc. These collect information about the crew and this information is used to develop optimizations for software. Just like the Gasseous Entropy Node, regular entropy nodes allow for variation in changes during a printing run.

### Master Disk Recorder

The Master Disk Recorder is another machine that the librarian posseses. Any new master disks must be reported to NanoTrasen, and the station is given an additional stipend to its budget by CentComm. This machine reports the disk made to NanoTrasen, as well as displaying any new stat changes to a machine that has this disk. This does not use up read durability on a master disk, as it is a much lighter read capacity. Failing to report new disks produced may be met with a theft charge, or much worse.

### Master Disk Cooler

The master disk cooler is another machine that the library may access. This keeps disks cold. That's it.

## Game Design Rationale

### Seriously Silly
The space game uses floppy disks for software. Quite funny. Plus, the variations of what these floppy disks can do to machines is really where the sauce is. This may potentially turn all mops into grenades, or each security lathe now prints double ammo for the same cost. The more organic variance between rounds the better.

### There is no Winning or Losing
Sure, there are some winning and losing combinations, but the point is to give players more freedom to explore different ways to help the station. Combos may fill specific niches, even with some draw backs.

### Maintaining Authenticity
This is very important. More often than not, breakthroughs in technology do not come in the form of more raw power. Instead, they come from optimizations and new ways to think about software. Two identical machines can exist, but perform wildly, depending on the software they use for a specific operation. We seek to emulate something similar, and seeing how this is a *research* station, this is a worthwhile emulation for simulating this aspect of real life.

### Take Things Slow
Machines are no longer things you don't think about. They now demand care and attention be put toward them, creating a worthwhile story for each machine made.

### Maximizing Roleplay Potential (Avoid QOL slop)
nothing about this is qol

### Dynamic Environment
custom machines that do different stuff depending on whats in them? come on, thats sandbox heaven.

## Roundflow & Player interaction

This lengthens roundflow in a positive way, forcing science to interact with more departments than it does now in a tangible way. Science now has more of a direct impact in rounds because of their say and capability in producing disks en-masse. Not only that, but the Librarian is given a job that is incredibly important, and must be the one to catalogue so much data. We elevate the librarian from being a purely RP role with no impact to the station, to a role which has similar status to the Chaplain, a role that may potentially shape rounds depending on what they find and do.

## Administrative & Server Rule Impact (if applicable)

- none really

# Technical Considerations

- new yaml for supporting these slots
- new protos for floppy and master disks