# Chem Rework

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers        | Implemented | GitHub Links |
| ---------------- | ----------- | ------------ |
| QueerCats, Catty | :x: No      | TBD          |
## Overview

Total reworking of the current Chem system, with a focus on increasing the variety and complexity of Chemistry gameplay. 

## Background

Chem gameplay at the moment is too monotonous, and too centralised around the ChemMaster. The main reason for this is that almost every action that Chemists need to do can be done in the ChemMaster. The only exception is heating chemicals, but the ChemMaster even renders that mostly frivolous as it stores heat perfectly. 

https://discord.com/channels/1276640157511979008/1382026970065408182

## Features to be added

ChemMaster should no longer have an infinite size non-reacting chemical buffer. At minimum, the buffer should be limited to maybe 400u. This makes its primary purpose once again to make pills and fill bottles and patches (with the recent ChemMaster update). 

Add a new Reaction Hood machine. This machine should be able to fit a reaction vessel (described below) for performing the main reaction, two beakers one for input and output, and two bottles or vials for holding an acid and a base respectively, and the ability to set a desired temperature that it will try to move the main buffer towards. 

Addition of a 400u Reaction Vessel for use with the Reaction Hood, requiring two hands to move.

More reactions should gave a required minimum or maximum temperature. 

Reagents should degrade into different reagents if over a certain temperature. 

More exothermic and endothermic reactions that require more active temperature management.

Similar principles for pH, using the acid/base buffers to adjust the reaction buffer to the appropriate pH. 

Assign all chemicals a vaporisation temperature, density, and state of matter (primarily solid and liquid)

Distillation Chamber, Separator Funnels, and Filtration Units that can separate chemicals based on their vaporisation temp, density, and state of matter, respectively. 

If chemical hits its vaporisation temperature outside of a sealed container, it foams, causing part of that chemical to be lost (possibly making a lesser foam effect, but implementing that would be out of scope).

Centrifuge and electrolysis will retain their current functionality of splitting reagents into more basic components, but with more utility in an average shift, particularly for recovering reagents from byproducts and failed reactions.

Basic chems (eg libital, probital, airui, lenturi, hyronalin, etc) should be produceable with simple mixing. A small amount of their precursors will be made available roundstart to ensure medical has access to early chems even with an absent or new chemist. 

Advanced and specialised chems (arithrazine, pyrazine, bruizine, leporazine, salbutamol, etc), along with precursors for basic chems, should require at minimum raising the mixture's temperature or setting the right bugger pH for the reaction to occur, and utilising precursor chems that are not available roundstart and have to be manufactured, or gotten from Botany. The reaction itself should require no more than three steps (in general, mixing, setting the right conditions, then extraction).

For exotic chems and chems that are not expected nor intended to be used in an ordinary shift, there should be no upper limit to the complexity or potential hazard of the reaction. 

To accomodate the increased complexity of the chemistry process, all chems should have their base effectiveness increased by 5 times, to allow Chemists to still supply the medbay and station with required chems. Additionally, syringes should have their minimum injection reduced to 1u to compensate. 

Moving away from elements as the reagents available roundstart to more complex precursor chems. 

In conjunction with the proposed botany changes [here](botany-changes.md), plants which produce advanced chems directly should be made available with a great deal of investment and time, while botanical reagents that serve as chemical precursors to those same chems should be made available much earlier, with chemist support.

Interaction with using plants to purify chemicals should be looked at to ensure it does not overshadow the intended methods of separating chemicals.

Limit the use of gaseous chemicals, as that causes conflicts with Atmos work. 
## Game Design Rationale

Seriously Silly: Adding more complexity to gameplay simply provides more ways for Chemists (and tiders working with less precise equipment) to mess up in dramatic and funny ways. 

Maintaining Authenticity: The chief goal of this rework is to increase authenticity, without slipping into the tedium that simulating realistic chemistry would cause. Finding the right balance between the two for each of the proposed mechanics, and for the rework in general, will likely require extensive playtesting and iteration, however. 
## Roundflow & Player interaction

The full suite of basic meds should be regularly achievable by a skill Chemist within the first 15 minutes of a round, and it is expected that they will be produced most, if not all, shifts.

Advanced meds should be achievable without external support within 10 minutes of being required, but assisstance from botany or other departments (implenting those is out of scope) should make them more achieveable. Expected that at least some would be produced most shifts, depending on the needs of the station (eg, if lots of people are getting radiation sickness, make arithrazine, if lots of people are suffering heat damage, pyrazine, etc).

Exotic chems should require at least some external help to produce, or be producible from scratch with great effort. Most shouldn't be made most shifts, and they should only appear because the chemical is desperately needed (eg, natus or siever for incurable amounts of genetic and radiation damage), or the station is doing particularly well (omnizine and stasizium as very potent general healing chems)

# Technical Considerations

- Are there any anticipated performance impacts?
Hopefully not
- Does the feature require new systems, UI elements, or refactors of existing ones?
Oh god, yes. I'm not a UI person though
