# Atmospheric Technician & Station Gas Economy Overhaul

## Status
**Draft** / **Proposal**

## Overview

This proposal introduces a new job: the **Atmospheric Technician** (commonly called Atmos Tech), placed under the Engineering department.

Atmos Techs are completely responsible for the station's air supply and overall atmosphere. That means producing gases, mixing breathable air, distributing it through the pipe networks, maintaining reserves, pressure and temperature, handling all gas-related emergencies, and - importantly - owning **firefighting** across the entire station.

They report to the **Chief Engineer** in the department hierarchy, but their day-to-day duties are entirely separate from standard Engineers. The two roles run in parallel with almost no overlap:

- **Engineers** focus on power generation, electrical distribution, station construction, and structural repairs.  
- **Atmos Techs** focus on **everything** related to gases, air quality, atmospheric integrity, and firefighting.

To support this clear division, a new shared **Engineering access** level gives both jobs entry to common areas (main Engineering, tool storage, lathe room, shared maintenance corridors, etc.). Beyond those shared spaces:

- Power generation facilities (Supermatter chamber, Nuclear Reactor area, major SMES rooms, etc.) remain **Engineer-only** access.  
- The Atmos department, gas production facilities, major pipe distribution hubs, and canister storage remain **Atmos Tech-only** access.

Equipment is split accordingly to reinforce the specialization:

- Atmos Tech lockers will **not** include RCDs (their work isn't construction-focused) or insulated gloves (they can grab them from shared Engineering storage when needed).  
- Engineers will **not** start with Rapid Pipe Dispensers (RPDs) in their lockers, but RPDs will still be available in Engineering areas where piping is generally required and will be printable at the protolathe.

**Firefighting** is explicitly owned by Atmospherics. Only Atmos Techs will spawn with the specialized firefighting backpacks round-start. This makes it very clear who is accountable when a fire breaks out or an atmospheric incident occurs, establishing a clear sense of responsibility and the urgency it holds.

Atmospheric alerts will be significantly improved for better visibility and accountability. The alert console will trigger consistent alarms, room-wide announcements, and flashing lights throughout the entire Atmos department. These alerts **cannot** be passively ignored - an Atmos Tech must actively acknowledge and clear them to end the alarms. Warnings will be detailed and specific: exact location, type of issue (dangerous gas leak, extreme heat, low temperature, overpressure, underpressure, etc.), so there's no ambiguity about the problem. Per SOP, Atmos Techs are **required** to respond to every fire and every atmospheric alert - no exceptions. Failure to clear Atmos warnings will result in fund penalties extracted from the Atmospheric budget. Marking legitimate emergencies for ignore without first addressing them will be a violation of SOP and a massive failure of duties, likely resulting in IC firings, and possibly even role bans if egregious enough.

An app will also be added to the Atmos PDA that will ping the Atmospheric Technician with the above information any time there is a fire or other atmos emergency. The app will show any warnings and danger alerts in the atmospheric alert console. This will prevent there being any excuses for Atmos Techs failing to respond to atmospheric emergencies. In an emergency, all techs are required to respond with whatever relevant equipment they can reasonably grab. These changes establish the sense of urgency that atmospheric disasters on a small space station are worthy of.

In the event of major station damage (meteor strikes, bombings, hull breaches, etc.), Atmos Techs are expected to assist with rebuilding the atmospheric distribution and emergency networks. They will focus on restoring pipe networks, fire alarms, and firelocks. They are not expected to carry bulk construction materials or handle the majority of structural reconstruction - that remains Engineering's domain - but they must be present to monitor atmosphere loss, minimize venting, and ensure the station doesn't bleed air while repairs are underway.

The core gameplay loop for Atmos Techs revolves around carefully managing the station's limited resources while keeping everyone breathing. Refilling spaced or vented areas can get expensive (roughly **$3 per tile** as a baseline, primarily oxygen), so careless spacings, overpressurization, or waste can drain the department budget very quickly. This incentivizes smart, efficient production: setting up and maintaining the gas recycler, running the electrolyzer to produce oxygen and hydrogen on-site, burning hydrogen to reclaim CO2 into usable oxygen, and other cost-saving measures. These systems become expected priorities rather than optional side projects.

The new gas economy fundamentally changes several long-standing problems. Gases will no longer be a source of infinite free value. Because Atmos only receives **10%** of the credits from any gases they sell through Cargo, mixing and selling exotics will typically not be profitable enough to sustain the Atmos budget on its own. While the station as a whole may earn money (spending less on raw gases than it earns from finished products), Atmos itself won't see a meaningful return. This completely flips the old dynamic: instead of Atmos pumping endless gas to fund Cargo, Cargo now needs to generate funds through other sales to fuel Atmos's exotic gas production. Gas mixing becomes a mid-to-late game luxury rather than an early exploit.

This also kills the use of infinite free gas for power generation. Power setups like the TEG burn chamber will require real funding from the Atmos budget, meaning they are unlikely to run at scale early on. Overproduction will be punished - dumping excess heat into space for no gain just wastes precious gas. High-power gas-dependent generators will naturally become late-round projects that depend on a healthy Cargo economy and careful Atmos budgeting.

To manage the new resource flow, the **Atmospheric Reserves Computer** will be added - a dedicated terminal located in the Atmos department. It functions like a cargo request console but is exclusive to Atmos Techs. Through it, they spend their department budget to purchase gas directly from the renamed **Gas Suppliers** (formerly gas miners). You buy the desired volume of gas, then set the desired flow rate and maximum pressure (capped at 1600 mol/s and 2500 kPa) to control how much enters the holding tank.

Together, these changes turn station air supply into a real economic and logistical responsibility. Atmos Techs must balance keeping the crew alive with keeping their department solvent - rewarding careful planning, efficient recycling, and smart budgeting, while making wasteful or negligent play punishing.

## Motivation

Atmospherics is one of the most technically deep and computationally intensive systems in SS14. Gas flow, mixing, reactions, heat transfer, and pressure dynamics are baked into the core of the game engine - far more than most other mechanics. Yet right now, managing the station's atmosphere often feels like an afterthought: basic air distribution runs on autopilot with minimal oversight, exotic gas production turns into an infinite money printer for Cargo, and power generation can exploit endless free gas without meaningful cost or consequence. This leaves a rich, engaging, fully flesh-out atmospherics system either mechancically underutilized, or more often, actively abused.

These proposals attempt to change that by introducing the **Atmospheric Technician** as a dedicated, full-time role built around this complexity. The Atmos Tech will be the station's dedicated guardian of breathable air and gas resources, with every mole carrying real economic weight. This gives players a clear, high-impact purpose: keeping the crew alive through breaches, fires, and catastrophes while balancing a tight department budget. Success means ending the shift with a positive balance after refilling spaced sectors, salvaging CO₂ into oxygen, or turning limited funds into valuable exotics - or even coordinating with other departments to turn the station into a profitable gas powerhouse. It's the kind of job that rewards foresight, crisis management, clever recycling loops, and smart inter-department deals.

A core part of this overhaul is introducing scarcity and consequence where it matters most. Basic station air (heavy on cheap nitrogen) stays affordable and forgiving, so survival isn't punishing for new players or during rough rounds. But exotic mixing, burn chamber fuel, and large-scale power setups require real funding - no more infinite loops that drown Cargo in credits or overheat TEGs for free power. Instead, Atmos Techs will need to prove their value early with efficient basics, negotiate budget support from Cargo (who now drive funds through traditional sales), and scale up exotics only when the station economy allows it. This flips the dynamic: rather than Atmos subsidizing the entire station, a strong Cargo department enables Atmos to do its most exciting work.

Firefighting and emergency response get the spotlight they deserve. With only a handful of Atmos Techs on shift, clear ownership means no one can shrug off alerts - especially with the new PDA app pinging fires and warnings directly. These high-stakes moments become a fun and engaging part of the role: rushing in with backpacks, sealing breaches, and minimizing air loss during chaos, all while watching your budget disappear in front of you.

The changes appeal directly to the players who already love gas mixing and see value in contributing to the station - but who currently feel their efforts lack real stakes or come at the expense of other roles. By tying gas production to a dedicated budget, enforcing accountability on emergencies, and creating healthy interdependence with Cargo and Engineering, Atmos Techs can finally feel like they're meaningfully supporting the station's survival and prosperity, without overshadowing or trivializing anyone else.

This gives one of SS14's deepest and most interesting systems, the atmospherics engine, the dedicated role and real mechanical weight it deserves. The goal is to turn managing the station's air and gases into something genuinely rewarding that actually matters to the whole station, not just something people set and forget.

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

**Reasoning**  
Power generation belongs to Engineering, and it should work independently without pulling unlimited free gas from the atmos department. Round-start setups that feed directly from distro or infinite sources get removed or reworked into self-contained canister systems. Engineers buy the gas they use, so they have to think about waste and efficiency. 

- **TEG (Thermo-Electric Generator)**:
  - Remains a joint responsibility system
  - Burn chamber supply & maintenance is an **Atmos Tech primary responsibility** (direct mapped pipe connection from Atmos encouraged)
  - Loop setup can be done by either role
  - Running round-start on plasma rather than hydrogen wastes money needlessly
  - Oversupplying power burns money, acting as a natural economic limiter

**Reasoning**  
The TEG is the main point where Atmos and Engineering actually work together. Atmos Techs control the burn chamber and fuel supply - it's their budget that pays for the plasma or hydrogen going in. Engineers take care of the heat loop and power output. Because gas comes from limited funds now, you can't just run a TEG at full blast from round start; plasma is expensive, so it only makes sense later when Cargo is bringing in funds. If you produce more power than the station needs, you end up spacing heat for nothing and wasting budget. The system limits itself naturally and forces both departments to talk and coordinate.

- **HFR**:
  - Rebalance to cost significantly less to buy
  - Reduce the power costs of running it
  - Fuel cost (plasma/tritium/hydrogen) becomes the primary limiter

**Reasoning**  
Stations won't have endless cash anymore with the gas economy in place. Dropping the price of the HFR significantly brings it back into reach for mid-game Engineering projects. Fuel becomes the real limiter - plasma, tritium, or hydrogen all require funds and time to acquire, so running the HFR already depends on excess department funds. This keeps it a solid late-round goal while limiting early catastrophes out of Atmospherics.

### 5. New Tools and Atmospheric Device Adjustments

- **Pipe Sensors**:
  - Clicking a pipe sensor now shows the gas mixture inside the pipe (same interface as a gas analyzer)
  - Sprite blinks green (<4500 kPa), orange (>4500 kPa), or red (>9000 kPa) to indicate pressure

**Reasoning**  
Pipe sensors are already placed along major networks, so adding this functionality makes them more useful without needing a new item. Engineers and Atmos Techs can quickly check gas composition and pressure in loops or distro lines by just clicking the sensor - no more carrying a separate gas analyzer everywhere. The color-coded blinking gives an instant visual cue on whether a line is safe, overpressurized, or dangerously high. This helps debug clogs, spot waste, and monitor systems faster, especially during emergencies such as a Supermatter delamination. 

- **Temperature Gates**:
  - New pipe valve type: only opens within a configurable temperature range
  - Helps maintain safe return temperatures in recycling loops

**Reasoning**  
Recycling distro air back into production saves a lot of budget, but heat from burn chambers or reactions can wreck your mixtures fast. Temperature gates let you set a safe window so the loop only passes gas when it's at the right temp. This makes recycling reliable and cuts down on constant manual fixes. Atmos Techs can focus on keeping the station breathing and the budget in the green instead of babysitting every pipe for temperature spikes.

- **Electrolyzer**:
  - Remove "magic gas vanishing" balancing mechanic
  - Rework to require **plasma** or **uranium** fuel to operate (refueling needed)
  - Uranium provides significantly longer runtime than plasma

**Reasoning**  
The electrolyzer is the main way Atmos Techs produce oxygen and hydrogen on-site, especially for the recycling loop (water vapor in, O₂ and H₂ out, burn H₂, reclaim CO₂ with heat). It always took less power than the energy it was capable of producing. To mitigate that issue, it will need fuel to run - plasma for shorter runtimes, uranium for longer runtimes. 

- **Crystallizer**:
  - Rebalance all recipes for new gas economy (e.g., plasma recipe adjusted so input costs vs. output value make it profitable)
  - Add new recipes: basic air crystal, halon crystal (for firefighting grenades)
  - Crystals no longer act as standalone grenades - combine with empty air grenades to load effects
  - Add basic air crystal recipe to produce standard air grenades when loaded

**Reasoning**  
The crystallizer is one of the areas where Atmos Techs get to experiment and make money or interesting/useful materials once the basics are covered. With gas no longer free, recipes need tuning so that inputs and outputs balance out and stay profitable. New recipes add options: air crystals for emergency refills, halon crystals for fire suppression grenades. The new loading system works like this: craft the crystal in the crystallizer, craft an empty air grenade, combine them to load the effect. Trigger the grenade and it releases the payload - air, healium, N₂O, halon, etc., at different amounts or temperatures depending on the crystal. This keeps the crystallizer as an Atmos tool, ties into firefighting, and gives late-game play something fun and useful without breaking the economy.

### 6. Atmospheric Reserves Computer & Atmospheric Integrity Reserve (AIR) Budget
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

### Typical Atmos Tech Gameplay Loop (Intended Shift)
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

This loop emphasizes proactive management, economic awareness, and prioritization. No longer will Atmos techs be able to speedrun infinite amounts of all gases. Without a steady flow of income through cargo, they cannot simply mix gases endlessly. Although the station as a whole may profit by Atmos mixing gases, at 10% of the station budget, even gases they sell through cargo are not likely to make back their production cost for the AIR budget unless very careful steps are taken to prevent any waste. Atmos would rely on cargo producing a flow of cash to fund their own Atmos projects and gas production. Their priorities will consist primarily of finding ways of saving money while supplying a steady supply of air and any other gas needs the station may have. Mixing gases will be a secondary endeavor, still important to the Atmos tech, but done so carefully and at a small scale so as to not drain funds. 

### Economic & Progression Implications
- Early: Focus on cheap gases + basic oxygen/hydrogen production.
- Mid-game: Start on making exotic gases. Quickly run out of department funds. 
- Late-game: Cargo must actively work to provide station funds enabling further exotic gas production.
- If Cargo is inactive, station risks oxygen shortages and inability to produce interesting gases
- Future tie-in: Exotic gases could provide **research value** to Science department tying into this suggestion:
 https://github.com/funky-station/docs/pull/24/files?short_path=362209f#diff-362209f400135f73e1629d3831f35fa7f2e601cb41dec8504df42a46583f6d8a

Tying gas production to Cargo performance creates station-wide economic interdependence. Without cashflow from Cargo, Atmos just won't have the means to mix gases, including air. The Science tie-in (researching exotic gases and their reactions) offers future expansion potential, giving atmos tech's a reason to produce and keep some exotic gases on hand.

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
