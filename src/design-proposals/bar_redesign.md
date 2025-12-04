# Bartender Overhaul

| Designers | Implemented | GitHub Links |
|---|---|---|
| Delorphin | Yes | https://github.com/funky-station/funky-station/pull/1948|

## Overview

Revamps to bartending to make it more authentic to real life, allow for more chances of player expression and roleplay opportunities, and making it more distinct from chemistry. The general themes of the overhaul can be largely separated into two categories: versimulitude and player expression.

## Background

The bar, as it stands, is not a good representation of how it works in reality. The use of dispensers, primarily, doesn't really represent how the bar works and makes the overall engagment with the activity

## Features to be added

### Jiggers

#### Implementation

Jiggers should be able to be flipped. Instead of a 20u capacity, one side should have a 10u capacity and the other 5u.

#### Motivation

Currently, jiggers are useless and don't match their real life use case, which was as a measuring tool. Most of the time, a bartender pours in 5u or 10u incremements. A shorthand to let them pour accurately without having to change the pour rate is to set it to a higher pour rate then the maximum, and pour it into the jigger. Theoretically, this would give the bartender access to 3 different pour amounts without ever having to adjust the bottle's pour rate.

This is something I do already with the dispensers to quickly make certain drinks. I would set the dispenser to dispense 20u of liquids. Dispensing tea and then ice will give you 20u tea and 10u ice, making 30u iced tea.

---

### Addition of mixing glass and potential updates to beer goggles

#### Implementation
Addition of a mixing glass that lets you examine the chemical composition of the drink or updates to the beer goggles so that you can examine the composition of any vessel. The mixing glass, even if it doesn't let you see the composition of a liquid, will still be added as a different method of storing 100u of liquid.

#### Motivation
As it stands, the only way for a bartender to see the composition of liquids is to put it in a dispenser or otherwise enter another UI. This has proved an inconvenience for me when I was making drinks and verifying that it was correct. 

The reason why the mixing glass is added is as well as another form of liquid storage. Some recipes produce non-30u amounts of liquid, leading to excess. This is better seen visually when in a transparent vessel over a shaker. This is also useful for determining at a glass if a vessel has liquid, which is important in cases where you need to produce large amounts of a certain beverage without having to resort to sourcing beakers as it is more in line with the bartender's set of equipment.

### Removal of liquid dispensers from the bar

#### Implementation

Changes in all maps to remove the dispensers and replace it with alternative storage for both alcohol (such as through the alcohol cabinet) and for glasses and other paraphenalia.

#### Motivation

The changes listed above to make it more convenient to hand pour and otherwise work the bar without the dispenser are all there to make up for dispensers being removed. This is done to accurately mimic the bartending experience and help make it more distinct from just being "chemist-lite". Sure, it may seem like this introduces an extra layer of inconvenience in the drink making process, but the kitchen operates in a similar manner, mixing regents by hand into a vessel to create various types of dough and having multiple steps to create a single food item. If anything, this will bring it more in line to the labour required with botany and the kitchen.

---

### Standardisation and expansion of tasting notes

#### Implementation
Rewriting of the flavours of cocktails so that they are, where possible, evocative imagery rather than the actual taste of the drink itself. The actual flavour of a drink, meanwhile, should be used primarily for base liquids.

#### Motivation

I am of the opinion that more metaphorical descriptions are more compelling to both read as well as utilise when mixing multiple cocktails together. A prime example, I think, is a cuba libre. The drink, historically, is in reference to revolution and rebellion and would be made more intersting if it had a description alluding to that rather than just tasting "like a spiked cola". 

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

People who visit the bar tend to only order the same drink over and over again rather than varying their choices like people would do in real life. With this, it could start encouraging people to ask for broad categories of drinks or to change their choices based on their character's mood as it gives them a more applicable description to roleplay with.

---

### Completion of the non-metamorphic glass set

#### Implementation
Addition of, at minimum, a highball and a lowball glass.

#### Motivation

There already is a precedent set by the existence of the shot glass and the coupe glass. The thing is, I find that those two forms aren't always the best way to present the custom cocktails I want. Most bars, in real life, would have the aforementioned glasses for their drinks along with a variety of other stemmed glassware.

---

### Sprite layers for non-metamorphic glasses

#### Implementation

Refactor code for non-metamorphic glasses to include sprite layers and the creation of items that utilise these layers. Similar to how, say, a janitor's cart works.

#### Motivation

To further increase the uniqueness of a drink beyond just choice of glass and the colour produced, additions such as staws, umbrellas, ice, etc. are all things that can make the drinks stand out. The initial impression of a custom cocktail will be the look, not the words that appear when it is drank, of course. I believe this would, with the above changes, allow for more personal expression in each individual barkeep beyond making the set drinks and increases roleplay opportunities as both the customer and the bartender can use the drink as a catalyst for conversation. It may also potentially draw more players to visit the bar due to it having more novelty and uniqueness on a round by round basis in comparison to the current system, where players are liable to order a regular drink and expect the same result, regardless of the bartender.

### Reworking the metamorphic glass meta

#### Implementation
Rather than drinks being created in a metamorphic glass, the drink and its respective look will instead be determined by a combination of the correct glass and liquid. There can only be one liquid in the glass. For example, putting a gin and tonic in a coupe glass will give the liquid color and be identified as a coupe glass. Putting it in a collins glass wil label it as a gin and tonic, add the lemon, and possibly have a custom color to match the glass. The metamorphic glass will retain its use only for the more strange drinks like cogchamp or the Manhattan Project. It will also be changed to be more magical or otherwise fantastical in its appearance and  a renaming to suit. 

The metmorphic glass actually works like this in some capacity. For certain liquids, it doesnt change the sprite but instead just adds the fill layers which mix colors as liquids are added and finally update theres a liquid with a valid sprite. The main difference in this newer system would be to revert to the unsprited state when there is more than one liquid type in the vessel as well.

#### Motivation
To me, this is one of the biggest parts of the bartender fantasy that is missing from the current system. Now, bartenders are motivated to be picky with their choice in glassware to fully create a given drink. At the same time, it also gives more room for people to actually  start experimenting and making more custom drinks as they are forced to engage with systems that facilitate them.

---

### General respriting efforts

#### Implementation

Make more bar related items visible in hand, update the sprites to match funky's art direction, add fill levels for drinks that are missing such sprites.

#### Motivation

A general update of the looks of the bar is needed to make it more appealing for everyone to visit. Additionally, making things visible in hand would make the drink making process more transparent and viewable to the customer, otherwise it would be just as invisble as the current system. Giving various drinks is also a necessary task as it is just plain oversight that they have not been implemented yet, making it impossible to tell that certain drinks have been consumed without examining them.

---

## Game Design Rationale

So then, why put all this effort to change bartending? Why do I think its a worthwhile endeavour from a design perspective? Well, service is meant to be the roleplaying department. The bar, in particular, is meant to be a nexus of social interaction. It is unfortunate then that the mechanics that that surround the bar do not facilitate meaningful roleplay. 

There are two main types of bartenders: the first is the type to make drinks on an ad-hoc basis, the other makes many drinks in advance and places them on the table. The latter type, I feel, takes away from the roleplay experience as people are more willing to just take a drink rather than communicate and talk with the bartender. By slowing down the process by making it more in line with real life it will discourage the mass production of drinks. 

On the topic of slowing down the process, the current way of making drinks drinks is wholly inauthentic. A bartender making cocktails would not be using dispensers to pour out drinks unless they're pouring beer from a tap. The overreliance on the dispenser not only reduces the feeling of being a bartender as you are just pressing buttons on a machine, it also makes the customer feel like they aren't in a bar. Instead, it feels like they are sitting in front of a vendor who is standing in front of a dispenser without seeing much in the way of progress. In real life, watching the bartender work is part of the appeal of sitting at the counter.

Adding better flavour notes and introducing more ways of creating custom drinks is also just better for roleplay and player expression. In the current system, I have seen bartenders other than myself try to make things unique by making things drinks with absurdly long flavour descriptions or different flavoured ice cream by combining it with other liquids, which changes the colour of the dessert. I have also had customers at the bar ask for a drink of my choice or make a wholly new drink, which spins off to more roleplaying opportunities based solely around the drink. By introducing more customisation, it will only increase the level of engagement both the bartender and the rest of the crew have with the bar experience by giving them more reasons to interact and more reasons to visit.

## Roundflow & Player interaction

A full implementation of the system won't really change the way a bartender would currently operate, other than having to content with the lack of dispensers. Instead, they would be using mixing glasses or actually wearing the beer goggles instead of the sunglasses to determine whether or not they made the right drink for the customer. They would be using the alcohol cabinet instead to access the drinks that they need. If the bartender was particularly in tune with the current system, they would be using the jigger in tandem with a bottle so they have access to 5u, 10u, and 15u pouring increments without having to access the transfer rates UI.

Those bartenders who are more experimental can focus on creating custom drinks based on the liquids or tasting notes they observe and pour them into non-metamorphic glasses to achieve unique forms and colours. They can add things like straws and umbrellas via sprite layers to further customise the look.

On the customer end, this encourages them to go to the bar and ask for custom drinks rather than a set drink that they would order regardless of the bartender. This would encourage more social interaction as they are more likely to roleplay and react to something tailored to them.

## Administrative & Server Rule Impact (if applicable)

Should this be completely implemented, it will need a general oversight on all maps for the removal of dispensers and additional storage space for the bartender.

# Technical Considerations

One of the bigger things to consider is that drinks that are pulled from upstream will need to be reconfigured to fit the aforementioned standard for flavour profiles to maintain cohesion and enhance the custom drink experience.

Refactoring of the codebase will be needed to introduce sprite layers to non-metamorphic glasses.
