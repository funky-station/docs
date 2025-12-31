# Atmos Departmental Budget & Gas Miner Control

## Overview

Atmos receives its own budget allocation on the Funding Allocation Computer, consistent with other departments.  

- Gas miners are now controlled through a dedicated **Gas Miner Control Console**.  
- Technicians can configure production rate (mols/second) and target pressure per gas, but every mole extracted deducts from the department's budget via a purchased pool of extraction credits.  

- Oxygen and nitrogen are low-cost gases.  
- Plasma is significantly more expensive.  
- Other minable gases scale in cost accordingly.

This change makes gases a finite resource with real cost, ties budget management to leak/spacing prevention, requires cooperation with Cargo for funding, and adds progression to Atmos gameplay.

## Current Situation

Gas miners currently produce at their component-limited rate with no recurring cost.  
After initial setup, they provide effectively unlimited gas for the entire round.  
This results in trivial access to important gases, reduces the impact of poor gas management, and makes Atmos feel like Engineering+ rather than a distinct role.

## Proposed Changes

### Departmental Budget

- Atmos gains its own budget entry on the Funding Allocation Computer.  
- Starting budget is set to comfortably support normal station air supply (primarily O₂ and N₂) for a full round, with reasonable headroom for moderate additional gas usage assuming no catastrophic losses.  
- Budget cannot go negative. When funds reach zero, gas miners shut down.

### Gas Miner Control Console

New console entity (suggested placement: near gas miner chambers):

- Toggle for each gas miner.  
- Configurable rate in mols/second per gas.  
- Target pressure setting (miner stops when connected network reaches the specified kPa).  
- Global enable/disable control.  
- Real-time display of estimated cost per second based on current settings.  
- Interface to purchase "gas credits" using department funds.  
- Tracks internal pool of gas credits.  
- Miners consume credits continuously while enabled and producing.  
- Automatic shutdown of all miners when gas credits reach zero.

**Cost Structure**  
Costs are per mole and vary by gas:  
- Oxygen, Nitrogen stays low cost (baseline air remains sustainable).  
- Plasma is high cost (typically the most expensive commonly minable gas).  
- Other gases scaled appropriately based on rarity/value.

### Failure and Risk States

- Gas lost to space (spacing, poor gas management) represents direct budget loss.  
- Inefficient TEGs, supermatter, or excessive waste burn through budget quickly.  
- When budget is depleted, miners stop. Funds must be restored to resume mining. 

## Design Goals

- Make gases a scarce, valuable resource.  
- Reward quick response to leaks and spacing events.  
- Introduce progression: start with basic air supply, scale up production as budget allows.  
- Require meaningful interaction with Cargo/HoP for budget priority.  
- Incentivize efficient power generation designs (TEG, supermatter).  
- Establish Atmos as a separate department with its own economic and security considerations.

## Round Flow Impact

- **Round Start** - Miners disabled, budget comfortable. Set up baseline O₂/N₂ supply, fill tanks, prepare chambers.  
- **Mid Round** - Budget accumulates from station activity. Increase rates, introduce higher-cost gases, optimize for power output.  
- **Late Round** - High production requires strict leak control and efficient usage to avoid depletion. Surplus budget enables aggressive experimentation.

Basic air supply remains viable even under budget pressure due to low O₂/N₂ costs. No emergency free tier for rare gases.

## Administrative & Rules Notes

No significant additional admin burden.  
Intentional budget sabotage (e.g. mass spacing to drain funds) falls under existing griefing/sabotage rules.  
The system is inherently self-limiting.

## Technical Notes

- Implement new console entity with UI for rate/pressure config, credit purchase, and cost preview.  
- Add budget consumption component to gas miners.  
- Rebalance per-gas costs to give oxygen and nitrogen value. 
- Track extraction credit pool as a simple float with depletion handled by the miner system.  
- Add auto-shutdown logic to miners when pool ≤ 0.  
- Register Atmospherics Budget on the Funding Allocation Computer. 
