# Company Scrip

| Designers | Implemented | GitHub Links |
|---|---|---|
| taydeo | :x: No | TBD |

## Overview

Scrip, a currency for regular crew to gamble with, purchase goods and services, and pressure heads of staff! Scrip is only valid on NanoTrasen stations.

## Background

Spesos are fine and dandy as currency that is used with the TSF, but in-lore NanoTrasen is a chartered corporation that is given a complete monopoly on authority on its stations and any planets it may colonize. This concept is more accurately reflected when workers are paid in Company Scrip rather than Spesos. This falls in-line with the long term vision maintainers have for the lore of NanoTrasen. NanoTrasen now becomes a paternalistic entity that can be compared to the coal and timber companies of the United States during the 1900's. This also helps us form a more coherent narrative of NanoTrasen being more overtly evil.

Scrip now also adds a lot of dynamic interactions with crew, as there is now a viable currency that players can be bribed with.

## Features to be added

For company scrip to be given the proper attention it deserves, it requires a large overhaul of these systems:

* Vending Machines
* New PDA Cartridge

Additional Systems should be added, for example:

* On-Demand Payment Square
* ATMs
* Station-wide Payout System
* Kiosks ran by Service Workers
* BankApp (CashApp rip off)
* Currency Exchanger

Scrip will also have an exchange rate of 3,000 to 1 speso. Yeah, it's worthless outside of NanoTrasen stations. 

### Vending Machines

Vending Machines need to automatically withdraw from a players spesos balance. This also means that Vending Machines should either have a flat price of all of the items they contain, or a method of specifying which items cost what. Vending Machines should also just not work when the ACC wire is snipped.

### PDA Cartridge

PDA's should now come with a banking app that outlines how much Scrip they are getting next pay routine, their transactions, and their balance.

### On-Demand Payment Square

An item that accepts payments when prompted by a user. These are handheld devices that can be used by Tidershops, Service Workers, etc. NanoTrasen issued payment squares have their funds sent to the Station Scrip Bank Account, which is then used as a means to pay out workers. Squares owned by individual people will have their funds deposited to their bank account, with a 5% tax.

### Station-wide Payout System

The Station-wide Payout System is a system that, every 10 minutes, issues a set amount of scrip to the station. That money is then sorted through and given out to everyone. Salaries can be set by the HoP and bonuses can be given out by heads of staff if they observed their workers doing great work. It could also be used for anything else, for example, embezzeled by the Captain.

### BankApp

The BankApp is another cartridge that players can aquire through Cargo or through the HoP. This Cartridge allows players to send funds to eachother, with the funds being recorded on the Station Records computer.

Players can use the BankApp to pay each other for favors, or whatever. A new entry to Space Law should be added, something along Circumventing Taxes. This law only applies if someone is considered to be running a business and using a non-NanoTrasen approved method to accept payment for goods or services, in order to avoid taxes.

### Currency Exchanger

The currency exchanger bluespaces scrip out of the station and gives the player an appropriate amount of spesos; charged to their balance with a 2% conversion fee.

## Game Design Rationale

### Seriously Silly

Company Scrip sets the tone for what NanoTrasen is. Adding another tool that shows the player how evil NanoTrasen is and a tool that can be used as leverage against someone is perfect for this Seriously Silly sentiment.

### Maintaining Authenticity

As said in Seriously Silly, Company Scrip sets the atmosphere. It reinforces the idea that you really are just a cog in a larger machine that's designed to make money. Exploited and easily replaced. This sentiment is what makes the atmosphere of Space Station 14 unique. 

### Dynamic Environment

Company Scrip can mean different things to different people. Some people don't care, others want to get rich quick. Adding another medium that can allow players to express themselves gives more weight to this dynamic environment as scrip could be used to brag, bribe, or not be used at all.

## Roundflow & Player interaction

I don't forsee this having any major impact on round flow persay, an antagonist will still antagonize, but between players, this new feature opens up the door to many potential roleplay opportunities.

Bribes will have more of a weight to them, because scrip can be converted to spesos.

## Administrative & Server Rule Impact (if applicable)

No additional stuff needed. Maybe more lenience for players who do choose to accept a bribe for a reasonable amount. No accepting bribes for 1 scrip or something.

# Technical Considerations

Several new UI windows need to be made.

* BankApp
* ATM
* Balance App
* Vending Machines now need to display how much an item is worth in Scrip

A mass rebalancing of Cargo things need to take place as well, as there will be a way to generate spesos from Scrip.

More input will be required from the maintainers.