# Bartender Overhaul

| Designers | Implemented | GitHub Links |
|---|---|---|
| Delorphin | :x: No | https://github.com/funky-station/funky-station/pull/1948|

## Overview

The general goals of the revamp is to make the bartending experience feel more manual and true to life, increase the number of roleplaying opportunities, and encourage more player expression within the role. This is done through removing the primacy of the metamorphic glass, by removing the drinks dispensers, and by defining a standard that all drinks should conform to.

## Background

The service department is meant to be the roleplay department. I think that while it is fine for them to have less mechanical depth in comparison to the other departments, the sparcity of it gives little aid to players to help them roleplay or even just play their role accurately. Bartenders face this problem quite heavily. Bartenders and services workers have a tendency to attract players who see the bar as a place for easily accessible loot, getting kitted out with flash protection, armor, and a gun. Customers who come to the bar have a tendency to order the same drink each time without any motivation to change their order. Some bartenders have the habit of just flooding the counter with drinks. None of the above can be considered as conducive of roleplay.

When you look at the features associated with the bartender, it feels more like the attempt at a stereotypical saloon owner with bandaid systems that have been grandfathered in as the foundation of the role. The gun and armor, somehow, take center stage of the role rather than mixing drinks. The dispensers and metamorphic glasses feel like easy shorthands to get the base mechanics of the bar without the extra overhead of making it feel like one.

## Features to be added

### Jiggers

#### Implementation

Jiggers should be able to be flipped. Instead of a 20u capacity, one side should have a 10u capacity and the other 5u.

#### Motivation

Currently, jiggers are useless and don't match their real life use case, which was as a measuring tool. Most of the time, a bartender pours in 5u or 10u incremements. A shorthand to let them pour accurately without having to change the pour rate is to set it to a higher pour rate then the maximum, and pour it into the jigger. Theoretically, this would give the bartender access to 3 different pour amounts without ever having to adjust the bottle's pour rate.

This is something I do already with the dispensers to quickly make certain drinks. I would set the dispenser to dispense 20u of liquids. Dispensing tea and then ice will give you 20u tea and 10u ice, making 30u iced tea.

---

### Addition of mixing glass

#### Implementation

Mixing glass will be a resprited large beaker, 100u capacity.

#### Motivation

This is useful so that players are able to mix non 30u increments of drinks and do so in a way that's easily visible. There have been many times where a shaker is used for this purpose only for the other bartender to mistakenly use it as it is opaque.

### Bartender glasses changes

#### Implementation
Let beer goggles function similarly to chemical analysis glasses and replace sunglasses with cheap sunglasses.

#### Motivation
Choosing bartender or service worker tends to attract powergamers due to bartenders having access to armor, a gun, and flash protection. By removing the sunglasses. The addition of chemical analysis to beer goggles is to give bartenders the ability to see the contents of any vessel without having to put them into a dispenser.

### Removal of liquid dispensers from the bar

#### Implementation

Changes in all maps to remove the dispensers and replace it with alternative storage for both alcohol (such as through the alcohol cabinet) and for glasses and other paraphenalia. This may include respriting the jug to be transparent as well.

#### Motivation

The changes listed above to make it more convenient to hand pour and otherwise work the bar without the dispenser are all there to make up for dispensers being removed. This is done to accurately mimic the bartending experience and help make it more distinct from just being "chemist-lite". Sure, it may seem like this introduces an extra layer of inconvenience in the drink making process, but the kitchen operates in a similar manner, mixing regents by hand into a vessel to create various types of dough and having multiple steps to create a single food item. If anything, this will bring it more in line to the labour required with botany and the kitchen.

---

### Standardisation and expansion of tasting notes

#### Implementation
Rewriting of the flavours of cocktails so that they are, where possible, evocative imagery rather than the actual taste of the drink itself. The actual flavour of a drink, meanwhile, should be used primarily for base liquids.

#### Motivation

I am of the opinion that more metaphorical descriptions are more compelling to both read as well as utilise when mixing multiple cocktails together. A prime example, I think, is a cuba libre. The drink, historically, is in reference to revolution and rebellion and would be made more intersting if it had a taste alluding to that rather than just tasting "like a spiked cola". 

To illustrate the two different paradigms of naming flavours:

- Blue curacao + the martinez: tastes like orange flowers and like violets and citrus vodka (based on the actual flavours of the drink)
- The manhattan + gildlager + tequila: Tastes like looking out the window of a 5 star hotel, like the tsar’s gold, and like fermented death (based on imagery)

I believe the latter is more compelling to work with.

In addition to this, a variety of drinks have no "reward" for their creation. A posca "tastes bitter" while its description talks about it being a drink of ancient warriors. Non-alcoholic drinks, in general, do not have unique flavour profiles that help them stand out.


---
### Giving drinks themes in the guidebook

#### Implementation

In the guidebook description of each drinks, other than the lore, add in things like "classy", "strong", "bitter", etc to further categorise and describe the drinks like in VA-11 Hall-A.

#### Motivation

People who visit the bar tend to only order the same drink over and over again rather than varying their choices like people would do in real life. I think that part of this is due to the amount of analysis paralysis that a person has trying to read and navigate through the sheer number of different types of drinks in the handbook. By giving this way of simplification, they are more able to scan throguh the handbook and find drinks based on their mood as a character rather than what the player behind them finds easy to order. Conversely, the bartender may offer certain categories of drinks to a person to match their mood, giving them aid in roleplay in this aspect if they do not have a strong knowledge of all the types of drinks, their flavours, and the like.

---

### Completion of the non-metamorphic glass set

#### Implementation
Addition of, at minimum, a highball and a lowball glass.

#### Motivation

There already is a precedent set by the existence of the shot glass and the coupe glass. The thing is, I find that those two forms aren't always the best way to present the custom cocktails I want. Most bars, in real life, would have the aforementioned glasses for their drinks along with a variety of other stemmed glassware. With the changes to how metamorphic glasses work, more types of glasses are also need to match the different types of drinks that can be made.

---

### Sprite layers for non-metamorphic glasses

#### Implementation

Refactor code for non-metamorphic glasses to include sprite layers and the creation of items that utilise these layers. Similar to how, say, a janitor's cart works.

#### Motivation

To further increase the uniqueness of a drink beyond just choice of glass and the colour produced, additions such as staws, umbrellas, ice, etc. are all things that can make the drinks stand out. The initial impression of a custom cocktail will be the look, not the words that appear when it is drank, of course. I believe this would, with the above changes, allow for more personal expression in each individual barkeep beyond making the set drinks and increases roleplay opportunities as both the customer and the bartender can use the drink as a catalyst for conversation. It may also potentially draw more players to visit the bar due to it having more novelty and uniqueness on a round by round basis in comparison to the current system, where players are liable to order a regular drink and expect the same result, regardless of the bartender.

### Reworking the metamorphic glass meta

#### Implementation
Glasses will now have a whitelist for the kinds of drinks that will transform their appearance. This will not change the way the shape of the glass looks, instead changing the fill and possibly adding garnish or other elements to the glass. Additionally, it should also turn back to a regular glass with its normal fill method when there is more than one type of reagent within the solution.

It should be mentioned that I have already prototyped and created a working version of the glass whitelist portion of the rework. This can be ported first should the latter half of the functionality take too long to make.

#### Motivation
To me, this is one of the biggest parts of the bartender fantasy that is missing from the current system. Now, bartenders are motivated to be picky with their choice in glassware to fully create a given drink. At the same time, it also gives more room for people to actually  start experimenting and making more custom drinks as they are forced to engage with systems that facilitate them rather than use the metamorphic glass for every drink. The general customisability from this system, the variety of glasses, the different tasting notes, and the sprite layers, will all help give the bartender the tools they need to make cocktails outside of what the handbook offers, leading to more chances of roleplayy and personal expression.

---

### General respriting efforts

#### Implementation

Based on the rework above, all metamorphic glass sprites should be reworked to match the new vessels.

#### Motivation

General updates to match funky's general art style and provide more consistency and parity with other sprites and the new system for drink transformations.

---

### Bartender SOP updates

#### Implementation

Bartender SOP should have infromation actually detailing their work rather than just gun ownership. This should be styled after Japanese bartenders, emphasising proper ways of mixing drinks and a general demeanour of grace and elegance. It should also state that people getting drunk on shift would be the fault of the bartender. 

#### Motivation

The current bartender SOP feels more like a bandaid to curb LRP players as it only mentions the usage of the shotgun and the type of ammo that it is allowed to contain. Having a proper SOP will not only give bartenders guidance for how to act and encourage roleplay, it also gives IAAs more opportunity to interact with the bar within their capacity. 

The above guidelines were inspired by Japanese bartending, which known to be wholly focussed upon having a beautiful procedure in the creation of the cocktail. Due to that, they are both famously slow and discourage such behaviours such as getting drunk. It also matches the general context of funky as bartenders in Japan will serve a small amount of people at a time, with a bartender catering for around 5 people at most at a given point in time. I think that following or choosing to ignore the SOP in this case will lead to more interesting roleplay interactions.

---

## Game Design Rationale

### Seriously Silly

I believe that adding a SOP that, while possible to do, is unreasonable to maintain will lead to more interesting and fun interactions as bartenders now have to contend more with IAA as they are expected to follow a certain mode of conduct. With the ability to get alcohol in maints, drunk crewmembers may not necessarily be the bartender's fault but they will still be blamed for it.

### Maintaining Authenticity

By removing the dispensers and the metamorphic glass, it will make the bar more true to life as people are forced to pour out of bottles and choose the right glasses to properly make a drink rather than doing the equivalent of using a soda dispenser and a magic glass to make a gin and tonic.

### Take Things Slow
The changes above will make the amount of time and effort it takes to make a single drink increase. This will mean that people who visit the bar will have to linger a bit longer rather than just taking a drink and leaving straight away. It also prevents the bartender from easily mass producing drinks and filling the table with them.

### Maximizing Roleplay Potential (Avoid QOL slop)

For the same reasons above, taking more time to make a drink will mean that people are more likely to roleplay with one another as they wait. The process of drink making being more transparent means not only can the customer view and comment upon the process, the bartender can actually see the bar and see conversation instead of the game being obscured as they are in the dispernser UI. The added customisability to drinks encourages bartenders and customers to be more dynamic with their interactions and changes to flavours and drink categorsiations provide easier avenues to roleplay as well.

## Roundflow & Player interaction

A full implementation of the system won't really change the way a bartender would currently operate, other than having to content with the lack of dispensers. Instead, they would be using mixing glasses or actually wearing the beer goggles instead of the sunglasses to determine whether or not they made the right drink for the customer. They would be using the alcohol cabinet instead to access the drinks that they need. If the bartender was particularly in tune with the current system, they would be using the jigger in tandem with a bottle so they have access to 5u, 10u, and 15u pouring increments without having to access the transfer rates UI. Rather than selecting the same glass over and over again, bartenders would have to choose the correct glass if they want the drink to look correct rather than having the generic fill sprite for the given glass.

Those bartenders who are more experimental can focus on creating custom drinks based on the liquids or tasting notes they observe and pour them into the glasses to achieve unique tastes, looks, and colours. They can add things like straws and umbrellas via sprite layers to further customise the look.

Customers are more encouraged to order from a "secret" menu as they know they can get custom drinks from the bartender. On top of that, they also have an easier time varying their drink selection as drinks are given categories for them to select for rather than needing to read the description of every single drink.

## Administrative & Server Rule Impact (if applicable)

Should this be completely implemented, it will need a general oversight on all maps for the removal of dispensers and additional storage space for the bartender.

# Technical Considerations

One of the bigger things to consider is that drinks that are pulled from upstream will need to be reconfigured to fit the aforementioned standard for flavour profiles to maintain cohesion and enhance the custom drink experience.

Refactoring of the codebase will be needed to introduce sprite layers to etamorphic glasses.

Refactoring the way metamorphic glasses work for the new system.