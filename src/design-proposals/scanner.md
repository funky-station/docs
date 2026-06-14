# Medical CT Scanner

| Designers | Implemented | GitHub Links |
|---|---|---|
| vivry | :x: No | TBD |

## Overview

This proposal aims to introduce more depth, complexity and RP potential to the medical department by adding a new machine that loosely replicates a CT scanner from real life. This machine would replace the functionality of the health analyzer, providing an exhaustive outline of a patient's status.

## Background

The medical department had been subject of many design proposals, many think that med gameplay is boring and underwhelming. In many cases, the process of treating someone is very rigid and straightforward - scan the player with the health analyzer, then left-click them with an appropriate treatment type until the damage goes back to zero. A [recent PR](https://github.com/funky-station/funky-station/pull/2868) wanted to deal with the problem by just deleting the health analyzers outright and providing no alternatives. This proposal instead replaces the health analyzers with something different and more fun to try and split the medical department into diagnostics and treatment, requiring many steps and cooperation between different player to solve a complicated case.

## Features to be added

### CT Scanner
- A 2x2 or 3x3 buildable machine that resembles a real-life CT scanner.
- The scanner has a bed that a patient can be placed on.
- While working, the scanner will emit a low level of radiation. The emission should be small enough not to cause any harm to the patient, but sufficient to force medical staff to use the scanner and shielding appropriately to not irradiate themselves throughout the shift.
- It will only work if the patient is not wearing anything, or is wearing a medical gown. A gown provides some shielding from radiation.
- The patient must have some contrast solution in their bloodstream for the scanner to work. Some contrast is provided at round start in the map and more can be made by Chem with a simple recipe (exact recipe and solution type TBD).
- The scanner bed slows down or prevents further deterioration of the patient, like a stasis bed. Radiation damage isn't prevented.
- Scans take some time, but aren't too slow.
- The scanner needs a lot of damage to be destroyed, but once it's gone, building a replacement is a long process. A crate containing everything required to build a CT scanner would be added as an orderable item from cargo.
- The scanner requires a direct connection to an HV or MV wire (TBD).
- Depending on the size of the map, it may be useful to have multiple scanners in the department, subject to further testing and balancing. To make them less bulky than they'll already be, multiple scanners could be placed in a shared scanning room.

### CT Scanner Console
- The console is a simple computer that is linked to a single scanner and is used to run scans and view results.
- It displays the status of the patient and the scanner.
- If the scanner can't start, the console will indicate the issue (insufficient contrast, clothing blocking the scan, no power, etc).
- The scan can be interrupted midway through the process, yielding no results.
- Once a scan is finished, an extensive medical report is provided in the UI. The report includes vitals, all types of damage and any other necessary medical information.
- The last scan results persist in the UI, being overwritten when a new scan is complete. A Print button will make a printing noise and spawn a piece of paper with the scan results on top of the console.

### Other Systems
- To encourage use of the scanner, health analyzers will not be accessible to regular medical staff. An analyzer will be available to the CMO for emergency uses only (like if the CT scanner is destroyed), having a debilitating downside that makes it unviable for long-term use (limited charges, much slower scanning, or dealing damage upon use).
- The UIs of the cryo pod and the body scanner computer (usually connected to an operating table) will be simplified to only provide the patient's vitals and overall damage, but no specific damage types.

### Mapping
- The scanner room should include at least the following: CT scanner (one or multiple), medical locker with a gown and some contrast, power cable to the scanner. The outside walls should have ionizing radiation warning signs.
- The scanner console room should include the following: CT scanner console (one per scanner), medical locker with some spare essentials. It should be completely separate from the scanner room and shielded from radiation. Ideally, these two rooms should be placed together, with a window to observe the procedure.

## Game Design Rationale

Here is why I think the scanner would fit in with the design philosophy.

- **RP potential:** this proposal *drastically* increases the number of interactions within the department and between doctors and crew. Instead of a simple checklist (health analyzer -> heal damage -> free up space for someone else), the doctors will need to compete for time at the CT scanner. This would encourage actual triage, where simple issues are treated on the spot based on patient complaints, the shift-click health menu and their overall status as reported by the medical HUD. More complex cases would need to be assessed in order of urgency and severity. In times of crisis, optimal performance would require a dedicated doctor that just runs scans, and great coordination to ensure that treating doctors have accurate reports for each patient.
- **Authenticity:** a multi-step diagnosis process like this is fun and authentic. It interacts with many game mechanics that are already in SS14 - chemicals, computers, radiation, paperwork. A CT scanner fits into the retro-futuristic style that Funky is pursuing, especially if an older, bulkier model is used as a reference.
- **Chaos:** adding so many interaction points adds more potential for silly disfunction. Arguments between doctors about whose patient is more important, careless operators irradiating strangers in the CT room, an antag tampering with scan reports to sabotage a patient's treatment, room damage forcing medical to either stop scanning while they're being repaired or accept leaking some rads into the department, paperwork getting misplaced. Ideally, it would be chaotic, but in a good, SS14 way.

## Roundflow & Player interaction

- This mostly affects only the medical department and involves only doctors and their patients. Two major exceptions are antags and groups that have health analyzers of their own (like salvage), because it could decrease their capacity to diagnose and treat people on their own. This is realistic, and players should be expected to come to medical to solve major medical issues, but it needs to not choke out those playstyles too much. Perhaps, a lesser health analyzer alternative could be added if this proves to be an issue.
- This addition would majorly affect the efficiency of the medical department. While most cases should be treatable without using the scanner, stationwide crises could gum up the entire system. Lines to the ER are realistic, but it shouldn't be so bad that entire shifts constantly spiral out of control solely due to a slowed-down medical department. Fallbacks and emergency options should be provided, like the CMO's health analyzer that was proposed earlier.

# Technical Considerations

- Despite being a complex addition, this shouldn't add any new systems that should be taken into account. All listed mechanics already exist in separate machines on the station.

- The only UI changes are the added scanner console UI and nerfed cryo pod and body scanner UIs, both are described in the features section.