# Cargo Overhaul

| Designers | Implemented | GitHub Links |
|---|---|---|
| Joaco545 | :x: No | TBD |

Special thanks to ThatOneMoon, literallyablueberryguy, Sophia Impetus, [Goobie](https://github.com/pirakaplant), Moxie_Is_Moxie, and UristMcWiki. You helped flesh out this idea a ton <3


## Overview

Overhauls how cargo works by replacing the ATS with Traders that visit the station over the shift.

## Background

Cargo 2.0’s objective is to remove the “bluespacing” magic of things from normal rounds, making bluespace a more mysterious force, leaving it for the station’s purpose of researching it.
The replacement for the game's magic instant teleportation comes in the form of Traders that visit the station, maintaining a more authentic way of how things would work on a real life space station.

Initially inspired by https://static.slugcat.systems/salvage/

## Features to be added

### Traders
Trader ships will start visiting the station and FTLing to a nearby position in space. Each ship will stay for some amount of time before leaving.
During the time they are near the station, they can be contacted by cargo to check the ship's manifest and buy things from them.
Traders can be haggled with to get a better deal, or pay extra to gain better favor (Reduce annoyance).
Traders who are going to the station to make deliveries may also carry mail for the station's workers.
Traders may advertise different missions that the station can take.
- Traders may advertise increased prices for certain items they are looking for (bounties). While you can haggle for bounty prices, they run out of patience much sooner.
- Traders may advertise a Hold mission, where cargo needs to hold onto some crates for a bit while another ship comes to take them later. The "holding price" can be haggled too.
- Other mission types may be added later.

### Deliveries
When things are bought through the station's cargo request terminal, a delivery will be generated. After enough time passes, a delivery ship will be sent to the station with both deliveries and mail.
There are 2 options for deliveries:
- A NanoTrasen delivery ship:tm: that delivers the cargo and then leaves.
- A Trader that was going that way anyway, so it might as well deliver the goods to stay on NT's good side.

Traders that are going to the station anyways (are not contacted by FTL-Comms) may also carry regular mail deliveries.


Once Scrip is added, players could also buy things with Scrip, and get delivered by a non-NT trader or delivery ships. (NT would be acting as the intermediate party, letting their emploees use Scrip to buy small silly things)
Traitors could also get their things delivered by traders, being smuggled onto the station this way, but after a discussion (https://discord.com/channels/1276640157511979008/1276653734767755294/1465387091998281769), the idea grew enough to become its own design doc for further down the line.

### FTL Antenna
A static device like the station’s anchor, which, when powered, can be used to scan signals from FTL ships

### FTL Communications Computer
The FTL-C Computer is a new computer that allows cargo to scan FTL space in search of trader signals.
If a signal is found, it would allow them to check a trader's manifest and communicate with the trader to call them over.
Needs to be connected to an FTL Antenna via a networking tool

### External Radio Communications Computer
The ERC Computer is a new computer that allows cargo to communicate with nearby trader ships, letting them check their manifest, place buy orders, and track any mission they have.

### Haggling
Traders can be haggled with in order to get better prices for buying or selling. Each trader has a preset price change tolerance and a range of possible patience values. Traders will haggle you back, so the actual value of the offer after haggling will be somewhere in the middle of the original price and your offer.
All traders have a "final offer" line that they will say when they are out of patience, but they may try to fake you out by using this line when they are still willing to haggle more.

### Annoyance
Annoying a trader won't have much effect, but annoying many traders will spread the word that this station is not worth the trouble.

### Ship Types
Flagships - THE Flaghship. Has all the luxary for whoever owns it - Only for admemes (Think NT Super-VIP visit, probably has a death squad protecting them)

Traders
  - Big - Ships with tons of cargo space, they exist for moving freight across the vast distances of space
  - Intermediate - Most common type of trader ship. Designed to go station to station, trading for goods
  - Independent/Small - Small ships offering limited things

Mail Carriers - Ships dedicated to moving large ammounts of mail through a territory.
  - In between Intermediate and Small, designed for last light year (last mile) delivery


- After consulting with the lore people, I was told it would not be common for the competition to sell stuff directly, as such new companies will need to be created. Eg: CarpPro, a company that sells fishing products; MorningStar Dynamics, a company that resells mercenary gear
  - After even more consultation with the lore people, it has been determined that traders under Sol Gov could be a thing (as in registered under Sol Gov)


## Game Design Rationale

Removing the magic teleportation of things/spawning out of thin air to make a more authentic game, while making things slower by having to wait for the traders to deliver the goods.
This also introduces some round variation, as each trader will buy and sell different things. Maybe you can get a discounted artifact from some local archaeologist, or sell a used artifact to a research company just passing by!


## Roundflow & Player interaction

The first random traders will start showing up soon after the round starts (minimum 5 minute wait time to give players some prep time?)

Having to wait for all their batched orders to arrive will be a slowing factor for cargo, but it will also introduce variations into the rounds as each trader will be different than the last (With a big enough trader ship pool).

Cargo is expected to buy things needed by the station from the traders, plus things that they plan to sell to the highest bidder.
As different companies have different needs, they need to recognize who will buy things over the market price (bounties) to generate the most profit possible.

As a way to de-incentivize certain behaviours, an "annoyance counter" will be added, representing how annoyed traders are at the station's cargo department.


## Administrative & Server Rule Impact (if applicable)

Cargo SOP will need to be amended to take into account the time it takes for Traders to appear after things are bought on the cargo console.


## Technical Considerations

### Trader Ships
- Each trader ship will start with a random timer designating how long they will stay near the station.
  - Soft ship limit can be enforced by not having any more trade ships on the FTL-C, or allow cargo to buy things till the current delivery ship is cleared

- A trader will have a list of things they sell. That is their manifest.
  - A hidden manifest can be implemented for antags to use. They usually contain contraband items.
    - This feature is mostly for other people to build on. (eg: Urist's Fence support antag on his thief rework proposal, or the Interdyne Chemist to get some special restocks).

- Each trader will come with a list of missions the station can partake in.
  - For now, they will be heavily weighted towards Bounties, until enough mission types can be added to make it more interesting.
  - Some missions will need to be completed before the trader leaves, while others will have different triggers for completion.


### Delivery ships
- Unlike traders, delivery ships won't have anything to offer but what has been asked for.

- They will arrive, announce themselves, and leave as soon as the ship is clear of any people and deliveries.
  - They will get annoyed if they are left waiting for too long


### Mapping Trader Ships
- Different styles for each corporation
  - A corporation could have a fleet of smaller and larger ships.
    - This depends on corporation size and lore (Megacorp (NT), Big (Cybersun/Gorlex), Medium (Animal rights consortium), Small (random independent traders))
    - Each corporation should have it's own set of decals to make each ship theirs (eg: big NT logo, or red highlights for syndicate)

  - Ships could share shape (ship model), but with different paint jobs.
  - Smaller traders could have more cozy ships, or repurposed vessels? (eg: Big Ore Trader using a standard ship vs Local Salvaging Crew having a scrappy salvage vessel).

- Use a modified ATS spawning and sell zones in a hidden compartment to hide the spawning of crates and selling of bounties. Usage of conveyors and airtight flaps is encouraged.
  - Spawn zones modified to have a buy queue (Kills "not enough space" error message).
    - Spawns crates from the queue in an interval to simulate cargo being moved on the back of the ship.
  - Sell areas modified to instantly sell any crates placed on them.

### FTL Antenna
- A big device that needs to be powered and connected to the FTL-C Computer with a networking tool
  - (Optional) When a connection is started, power usage increases
    - (Optional) The power usage could depend on how high the signal gain is


### FTL-Commnications Computer
- Requires the FTL Antenna to be connected via a networking tool to function (Look at how artifact scanners work).

- Minigame that lets you tune the antenna's FTL comms to find traders that are "warping" (not spawned) near the station.
  - Adjust Azimuth and Elevation, read radio gain, and adjust again till you hit a trader with a high enough gain to connect.

- When tuned lets you see the cargo manifest of a ship and also allows you to call it to the station for trade.
  - Emmaging enables looking at the hidden manifest of ships that have it.


### External Radio Communications Computer
2 Tabs:
- Ship Manifests Tab:
  - Allows you to see the manifests of nearby ships and place orders on them.
    - Emmaging enables looking at the hidden manifest of ships that have it.
    - You can haggle the price of the order. Bigger orders can get a bigger discount.
      - Being too unreasonable (haggling too far or too many attempts) will annoy the trader, who may refuse to complete the order and leave as soon as they can.

  - Will allow you to see the remaining time before they warp away.
  - Will allow you to dismiss the trader early, freeing up a spot for another trader to come (soft trader limit).

- Missions Tab:
  - Let's you track active bounties on the different ships.
  - Let's you track other missions (like hold orders).


### Haggling
- Each trader has 2 values:
  - Price Change Tolerance: How much they are willing to go over or under the price for selling and buying, respectively.
  - Patience: How many attempts the player gets before getting annoyed and rejecting the haggle outright.

- Traders haggling back will take a value between the original price and your offer.
  - Exception: The offer is in their favor (you sell cheap or buy high).


### Annoyance
- Annoyance is a counter that increases when players act in ways that are not good for the traders, and decreases when favorable deals are struck with the traders.

- When the annoyance counter is high enough, traders will stop allowing haggling.
  - If the annoyance counter keeps increasing, they will stop visiting the station if they don't have a purpose. This includes refusing to come over when contacted, and stop allowing trade altogether.
    - It is a QM's job not allow this to happen.

- Each trader has their own annoyance threshold. This is done to make sure that the station is not suddenly cut off from trade.

- Annoyance triggers:
  - If a player is on a trading ship, the ship will not FTL away. If you leave traders waiting to leave for a long time they, will get annoyed.
  - Failed haggling attempts will annoy traders.
  - Failing missions (may also incur a fine).
  - Damage to trader ships will ANNOY traders a lot.
    - This includes hacking doors.
    - If damage is serious enough, they may hightail it. Any players remaining on board will be round removed as their body left with the trader ship.
      - (To determine later) Display a message on the common channel about them leaving? Play some claxon to indicate the ship is emergency warping away soon?


### Removals
- Remove the ATS.
- Remove the Mail Teleporter.
- Remove the bounties computer in favor of the missions.
