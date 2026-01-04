# Atmospheric Technician & Station Gas Economy Overhaul

## Status
**Draft** / **Proposal**

## Overview

This proposal introduces a dedicated **Atmospheric Technician** role under the Engineering department (a role that was recently removed due to lacking a clear distinction from Engineering gameplay). It fundamentally reworks the station's gas economy by making **all gases** a purchasable resource with associated costs, and clearly separates responsibilities between standard Engineers (power-focused) and Atmos Techs (air/gas mixture-focused).

The core goals are:
- Reintroduce Atmospheric Technician as a properly unique, meaningful role with distinct responsibilities
- Create clear role specialization and healthy inter-departmental cooperation/tension
- Turn gas management into a core economic, logistical, and gameplay pillar
- Prevent infinite gas utilization/waste and free resources while rewarding thoughtful production & waste management
- Tie exotic gas production to the broader station economy (requiring Cargo cooperation)

Alternative name: Gas accountant

## Motivation

Atmospherics was removed because its gameplay was not unique enough - it often devolved into Engineering Plus with little consequence for waste, blurred responsibilities, and powergaming. Examples include atmos players forcing their way into power generation or providing all of Cargo's funds. 
Stations run infinite gas setups with almost no maintenance.  
Power generation frequently exploits free or looped atmos gases without real cost.

By reintroducing the role with a **dedicated gas economy** and clear boundaries, we aim to make **station air supply a scarce, valuable, and truly specialized responsibility** - giving Atmos Techs a distinct identity separate from (but still collaborative with) Engineering. Unlike before, unless otherwise directed by the Chief Engineer, their primary role and concern IS station gas reserves and management and nothing else. Mechanics will be balanced around making this a full time, dedicated station role that is justified in having it's own department. 

## Proposed Changes

### 1. New Role: Atmospheric Technician
- Belongs to **Engineering department**
- Answers to **Chief Engineer**
- Primary responsibility: **Production, mixing, buying, managing, and distribution of the station's entire air supply**
- **Not** primarily responsible for station power (unless collaborating on specific systems like TEG's burn chamber)

**Reasoning**:  
The role needs a clear, exclusive identity that cannot be easily subsumed by Engineers, nor is seen as a senior Engineering role as it currently is. By making the entire station's breathable atmosphere their core duty (with economic weight behind every mole), and making them answer to Engineers on matters within the Engineering department, enforced by SOP, we create gameplay that feels meaningfully different from that of standard Engineering. 

### 2. Gas Economy System
- **Every mole of gas now costs money**
- Price tiers (examples):
  - Extremely cheap: Water Vapor, CO₂, Nitrogen
  - Moderately priced: Oxygen, N₂O
  - Expensive: Plasma
- Station starts with a modest budget for initial distro/reserves priming
- Overfilling distro early drains starting funds rapidly

**Reasoning**:  
By attaching real economic cost to every mol (even if tiny for basics), every decision matters - overpressurizing, wasting, or mismanaging quickly becomes a budget issue. Early reserves and cheap basic gases keep survival feasible even with an underperforming Cargo department. Mismanagement, however, can quickly drain funds and leave you unable to supply fuel for burn chambers, mix any exotic gases, or even refill spaced areas, needing to wait until funds become available before being able to do so. 

### 3. Departmental Jurisdiction & Access Changes
- **Engineers**:
  - Primary focus remains power generation & distribution
  - Use **canned gases** for power generators requiring gases(SM, nuclear reactor) with strong emphasis on waste reduction
  - No direct/privileged access to atmos pipe networks
  - Connecting pipes to atmos now requires **explicit discussion/cooperation** with Atmos Tech
  - Jurisdiction over power producers (SM, Nuclear Reactor, etc.)
- **Atmos Techs**:
  - Full control over atmos department area & gas production facilities
  - Responsible for station-wide breathable air mixture
  - Can assist with engineering tasks when directed by Chief Engineer
  - **Cannot** unilaterally interfere with powergen systems under SOP. Engineers outrank them on such matters.

**Reasoning**:  
Blurred lines caused conflict and role dilution before. Strict access boundaries and chain-of-command clarity prevent "atmos bullying" while still allowing cooperation. Engineers keep power as their domain; Atmos gets exclusive ownership of the station's atmospheric system. 

### 4. Power Generation Adjustments
- **Systems heavily dependent on steady atmos gas flow**:
  - Removed at round-start or converted to canister/closed-loop systems
- **TEG (Thermo-Electric Generator)**:
  - Remains a joint responsibility system
  - Burn chamber supply & maintenance remains an **Atmos Tech primary responsibility** (mapped connection encouraged)
  - Loop setup can be done by either role
  - Running round start on plasma rather than on hydrogen wastes money needlessly
  - Oversupplying power burns money causing a natural economic limiter
- **HFR**:
  - Rebalance to cost a bit less power while still remaining fairly high
  - Fuel cost becomes the primary limiter (plasma/tritium/hydrogen)
- **Electrolyzer**:
  - Remove "magic gas vanishing" balancing mechanic
  - Rework to function like a generator:
    - Requires **plasma** or **uranium** to operate (refueling needed)
    - Uranium provides significantly longer runtime

**Reasoning**:  
Many issues can be traced to free atmos gas feeding powergen. TEG stays as a deliberate bridge between roles (Atmos owns the burn room, Engineers can help with gas loops), creating natural collaboration without Atmos dominating power. One thing to note is that the use of gas does not necessitate an Atmos tech. Atmos techs are there to manage **station atmospherics**, not every single pipe or gas can. If a power source requires the use of gas, Engineers will be required to learn how to manage it's gas loop. Electrolyzer changes are simply needed for balance. There is no feasible way for them to follow the laws of thermodynamics, so as a drawback they will require maintenance in the form of refueling. 

### 5. New Tools & Quality-of-Life
- **Pipe analyzers**:
  - Show gas mixture inside pipe (gas analyzer window)
  - Color-coded pressure indication (green < 4500, orange > 4500, red > 9000)
  - Help Engineers monitor and debug gas loops without needing to carry a gas analyzer
- **Temperature gates**:
  - Special valves that only open within a configurable temperature range
  - Helps maintain safe return temperatures in loops

**Reasoning**:  
Pipe analyzers will allow engineers and atmos techs alike to immediately visually identify clogged pipe networks, making it far easier for even inexperienced technicians to indentify and address issues quickly. Temperature gates will be neccessary for safely recycling distro gases.

### 6. Typical Atmos Tech Gameplay Loop (Intended Shift)
1. Setup basic distro (conservatively - avoid overpressurizing)
2. Establish oxygen independence:
   - Pipe water vapor to burn chamber with electrolyzer (with plasma/uranium fuel)
   - Split into oxygen and hydrogen
   - Burn hydrogen to produce heat for gas recycler and recycle CO₂ into O₂
3. Carefully mix & produce gases:
   - Shut down your gas factories when not needed to avoid wasting funds
   - Prioritize station air needs first
   - Produce valuable gases (e.g. Frezon) only when funds allow
4. Sell excess gases via Cargo to finance more production
5. Collaborate with Engineers on TEG setups when requested, but only after establishing cheap oxygen and fuel sources
6. Play with gases in the SM, HFR or cystallizer

**Reasoning**:  
This loop emphasizes proactive management, economic awareness, and prioritization. No longer will Atmos techs be able to speedrun infinite amounts of all gases. Without a steady flow of income through cargo, they cannot simply mix gases endlessly. Although the station as a whole may profit by Atmos mixing gases, at 10% of the station budget, even gases they sell through cargo are not likely to make back their production cost for the AIR budget unless very careful steps are taken to prevent any waste. Atmos would rely on cargo producing a flow of cash to fund their own Atmos projects and gas production. Their priorities will consist primarily of finding ways of saving money while supplying a steady supply of air and any other gas needs the station may have. Mixing gases will be a secondary endeavor, still important to the Atmos tech, but done so carefully and at a small scale so as to not drain funds. 

### 7. Economic & Progression Implications
- Early: Focus on cheap gases + basic oxygen/hydrogen production.
- Mid-game: Start on making exotic gases. Quickly run out of department funds. 
- Late-game: Cargo must actively work to provide station funds enabling further exotic gas production.
- If Cargo is inactive, station risks oxygen shortages and inability to produce interesting gases
- Future tie-in: Exotic gases could provide **research value** to Science department tying into this suggestion:
 https://github.com/funky-station/docs/pull/24/files?short_path=362209f#diff-362209f400135f73e1629d3831f35fa7f2e601cb41dec8504df42a46583f6d8a

**Reasoning**:  
Tying gas production to Cargo performance creates station-wide economic interdependence. Without cashflow from Cargo, Atmos just won't have the means to mix gases, including air. The Science tie-in (researching exotic gases and their reactions) offers future expansion potential, giving atmos tech's a reason to produce and keep some exotic gases on hand.

### 8. Atmospheric Reserves Computer & Atmospheric Integrity Reserve (AIR) Budget
- **Atmospheric Reserves Computer**:
  - A unique cargo-request-style computer located in the Atmos department
  - Dedicated tab/interface for purchasing **gas credits** using the AIR budget
  - Controls the flow rate / activation of connected gas miners
  - Allows fine-tuned management of mined gas input to prevent wasteful overproduction
- **Atmospheric Integrity Reserve (AIR) Budget**:
  - Separate, dedicated budget exclusively for the Atmospheric department
  - Used for all gas purchases, miner operations, and credit top-ups via the Reserves Computer
  - Completely independent from the standard Engineering/Maintenance budget
  - Atmos Techs **cannot** access or draw from the Engineering budget (to be enforced mechanically)

**Reasoning**:  
This system reinforces the Atmos technicians independence from Engineering. The dedicated computer makes gas sourcing feel like it's own logistics mini-game. A separate AIR budget prevents overlap/conflict with Engineering funds, ensures atmos mistakes only impact air supply and atmos funds, and makes the role's budget feel owned and distinct - further emphasizing the role's unique place on the station and the need to manage and account for every mol that is leaving atmos.

## Balance Considerations
- Prevents infinite oxygen/TEG loops without fuel cost
- Forces meaningful limitations to exotic gas production
- Creates natural cooperation and tension between Cargo, Atmos and Engineering
- Keeps TEG viable but economically limited (Should still be far more rarely mapped)
- Makes early-round atmos mistakes **expensive** (teachable moment)

## Drawbacks & Risks
- Increased complexity for new players
- Potential for toxic atmos-engineering conflict if roles aren't clearly communicated
- Cargo dependence might feel punishing on low-pop or dead Cargo rounds
- Requires careful tuning of gas prices, budget allocation and starting budget

## Implementation Notes
- New role job definition + access levels
- Gas credit economy backend
- Electrolyzer & HFR reworks
- Temperature gate pipes
- Pipe analyzer sprites & functionality
- Map updates

## Feedback Requested

This is a proposal to bring back **Atmospheric Technician** as a properly unique role with a dedicated identity that it lacked before its removal.

Particularly looking for feedback on:
- Does this give Atmos Tech a strong, unique gameplay identity separate from Engineering?
- Are the proposed boundaries and economic systems likely to create fun tension/cooperation rather than frustration?
- Pricing philosophy - how aggressive should the pricing of basic gases be?
- Any other ways to further emphasize the role's uniqueness without overlapping too much with other jobs?

All input appreciated
