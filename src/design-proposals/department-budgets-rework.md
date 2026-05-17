# Department budgets rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| Dusty_Plant and ThatOneMoon| :x: No | TBD |

## Overview

A key element of the design changes described in this document relies heavily on the implementation of the scrip system detailed in <https://github.com/funky-station/docs/blob/main/src/design-proposals/scrip.md>.

The features outlined in this document aim to fix issues with the current design of department budgets and station economy, using a debt and reward system that encourages consumerist behaviour in employees while minimalizing expenses for nanoTrasen, all the while boosting the station's economy.

## Background

Departmental budgets currently have a glaring flaw in their design, with departments very often having to rely on cargo to pay for work-related purchases while cargo itself sees its budget overflowing.
There is often a lack of communication between all the actors behind a purchase, decisions are sometimes made on the fly even when the purchase is unneeded or redundant.
This problem becomes worse when cargo technicians can see the existence of the department budget system as a reason to refuse orders from other departments, leading cargo to accumulate money for no reason.

Using two simple systems, department debt and payroll boost, we can fix the imbalance in department budgets while giving cargo somewhere meaningful to direct all their money and simplifying the order process to make communication smoother.

## Features to be added

### The department debt system
Departments are given the ability to purchase things beyond their budget, with the result being going in the red.
The money used to complete these purchases comes directly from the cargo budget, and departments can still make further purchases if in the red.
Cargo still has final authority on which orders are approved or denied using their purchase console, and are notified when a purchase would take money from their account.
Being in the red leads to the department's share of station revenue going to cargo's instead until the debt has been paid off.

Here is an example scenario to illustrate how the system works:
Science creates an order to buy something that costs 5000 spesos, using their purchase console. 
They only have 3000 spesos in the account. 
Upon the slip being given to cargo and the order completing, the 3000 spesos get taken from science, and the remaining 2000 spesos from cargo.
Science's budget now reads as -2000 spesos.
Then, cargo sells something and the station earns some spesos.
Cargo earns their usual share.
Science's usual share (let's say 500 spesos for this example) is transfered to cargo, repaying part of science's debt.
Science's budget now reads as -1500 spesos.
Science now creates an order to buy something that costs 1000 spesos.
Upon the order completing, once again, 1000 spesos are taken from cargo's budget and science goes a further 1000 spesos in the red.
Science's budget now reads as -2500 spesos.

### The debt management console
The quartermaster gains a debt management console.
This console shows department budgets, with an option to cancel debts immediately, setting the department's budget back to 0 and allowing it to start earning money again. This effectively acts as a direct money transfer from cargo to that department.

### The payroll boost system
This feature relies entirely on the scrip system outlined in <https://github.com/funky-station/docs/blob/main/src/design-proposals/scrip.md>.
The funding allocation computer moves from the HoP to the catpain and gains a payroll boost tab that displays cargo's current funds and allows for a flat amount or percentage of it to be transfered to the crew's next payroll as a bonus (this may be set to automatically trigger every payroll as a toggle in the UI).
This bonus is a conversion of spesos into scrip, with a large amount (since scrip has noit been implemented, the actual conversion rate cannot yet be assessed) being lost in the conversion (pocketed by NT).
The resulting amount of scrip is then divided according to each crewmember's pay (higher-paid employees recieve a bigger fraction, this of course includes the captain) and awarded in the next payroll.

## Game Design Rationale
The current state of department budgets does not encourage their use and leads to confusion as to why money is being made and where it should go. 
Indeed, the extra funds accumulated by cargo currently have no real use apart from armor and weapons purchases in case of a large scale attack on the station.
Furthermore, the HoP is never incentivized to use the funding allocation computer, it would make more sense to give this duty to the captain who is after all responsible for the way the station functions.
Letting the captain define which departments get to make purchases without having to rely on cargo's goodwill is important.
This new design preserves the ability for departments to make their own purchases while providing supply and the captain with more tools for organization and keeping track of expenses.
The addition of a stationwide bonus system relying on the cargo budget will also give more uses to extra cargo funds and might lower the amount of silly/useless purchases that detract from the feeling of immersion Funky wants to create.

### Seriously Silly
NanoTrasen is almost comically greedy, willing to squeeze its crew as much as possible for profit. This new design reinforces this idea with budget being given more weight and importance.

### Maintaining Authenticity
Discouraging reckless spending of funds on useless purchases with the payroll boost and debt systems highlights the importance given to money in a capitalist system.
The captain is given more importance by giving them the ability to allocate the station's funds and spend them on bonuses to crew, letting them win (or lose) the people's favour and engage in department politics. 

### Maximizing Roleplay Potential (Avoid QOL slop)
While this new design allows departments to make purchases more easily, it also introduces more points of friction with debt clearly displayed.
Members of the crew will look for who to shift the blame on when funds run low, especially if it means they are losing out on a potential bonus.

While the captain is given more opportunities to award bonuses to crew, crew may also shift their blame on that same authority figure when money runs low.
The supply department will no longer be able to accumulate funds without causing crew unrest, the Quartermaster and Captain will need to argue for their decisions (or rely on brute force) if they want to avoid rebellious behaviour among the crew.

### Dynamic Environment
Letting departments spend their money more freely and easily in exchange for debt allows for more crew activity without compromising the economy.
Crew will be able to undertake projects more easily, communicating intent will also be smoother since the amount of steps necessary for purchases will be lowered.
A more lively and dynamic economy will make the game feel more like a living system that everyone is a part of.

## Roundflow & Player interaction
Quartermasters can now tell their technicians not to approve purchases that would send a department a certain amount into debt; they can also transfer funds more easily to departments in need by clearing their debt.
Departmental order slips can finally be used for all work-related purchases, with unaffiliated civillians having to rely fully on the goodwill (or using scrip as a bargaining chip) of the cargo tech in charge of accepting orders to fulfill a non-essential purchase.
Crew will now be more mindful of department funds, knowing that a large bonus to their pay relies on them.
This may lead to interesting conflicts between a department needing purchases to function and greedy crew members trying to increase their bonus by lowering the amount of purchases. 
In general, cutting corners during repairs, manufacturing or medical work might start to become more commonplace in order to save money. 
Assistants may get hired by crew to collect resources from maintenance (or steal them from other departments ) in order to save on expenses.

## Administrative & Server Rule Impact (if applicable)
These changes may lead to more conflict between crew, which can lead to higher admin strain.

# Technical Considerations
Changes required:
- The addition of the debt system to the department funds system.
- UI changes for department order consoles, showing funds in red when in the negative.
- UI changes for the cargo ordering console, showing in red extra expenses when an order to be confirmed would eat into their budget.
- The addition of a debt management console to the code, allowing the Quartermaster to see each department's current budget and letting them settle debts.
- The addition of the Quartermaster's debt management console into their office for each map.
- The addition of the payroll boost system, converting spesos into scrip and distributing it between crew according to their pay.
- The addition of the payroll bonus tab to the funding allocation computer.
- The addition of the Captain's funding allocation computer into their office and its removal from the HoP's office for each map.











