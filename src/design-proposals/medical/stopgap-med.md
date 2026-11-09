# Recovery Med

| Designers | Implemented | GitHub Links |
|---|---|---|
| zergologist | :x: No | TBD |

## Overview

A fairly surface-level medical rework that intends to give medical more to do without necessarily adding in an entire medical system. Should be useful as a base for future medical system reworks given that this deepens the final step of healing, recovery.

## Background

Medical at the current moment, both on Funky and in Wizden, is largely chemical-dominated, with medical being a department almost entirely dependent on the chemists doing their jobs in order to actually heal people. While legacy Funky has surgery and pyrogenics to add in *something*, the additions are admittedly a bit shallow. Surgery has incredible potential for deepening medical's gameplay if integrated into the department's workflow, yet such a thing requires a significant framework to both allow for limb-specific surgery and improvised surgical implements to work, not to mention worries about infection, keeping things sterilized, and more. In my eyes, an ideal medical system would be something more akin to [conditionmed](https://github.com/funky-station/docs/pull/49), obfuscating what information doctors have and putting the bulk of their work into stabilizing a patient well enough so that they may recover on their own. Injuries should matter and improper treatment should run actual risks, with death mattering and being a harder threshold to cross in either direction. It should be noted that softcrit and CPR are making their way to Forky, both of those being important for how players interact with medical and health.

While I may not be able to address everything with fairly surface-level changes, this "Recovery Med" I'm proposing aims to slow down medical's gameplay and, hopefully, make medical less reliant on chemists in order to run. This rework also intends to deepen chemist gameplay similarly to how Funkychem made things more complicated to make, with them producing more complex and nuanced chemicals as opposed to bulk of fairly simple chems.

Given how this will likely touch medical's gameplay to the point of dramatically changing the responsibilities of doctors and chemists, discussion with the SOP workgroup will be required. Similar discussion with the Botany workgroup will also be required given how closely tied botany and chem are, with there even being a number of plant-specific healing chems that will need to be adressed with this recovery medical system.

## Features to be added

### Changing from Direct to Facilitative Healing

#### Natural Healing Changes

Natural healing should be the primary method in which crew members recover from injury. Natural healing should not be so strong as to invalidate combat entirely, but it should not be so weak as to make every injury effectively permanent throughout the shift. The rate of healing should be influenced by nutrition and hydration levels, with those parched and starving not naturally recovering. The rate of natural healing should also be affected by the application of certain topicals and chemicals independent of the food system, allowing for bruise packs and ointments to be primarily used to stabilize patients. Crit patients will need to be administered food and drink should they recover, and medical will need something to keep its patients stabilized.

Example Natural Healing Breakdown

Multipliers:
    Baseline Healing Multiplier: x0.33                  # Hungry and badly damaged
        Food Multiplier: x0.66                              # Hungry...
        Overall Damage Multiplier: x0.5                     # Painful.
    Damage Specific Healing Rate: x1.0                  # More of the base rate everything should be applied to
    Specific Damage Multiplier: x0.5                    # Really badly damaged
    Topical Multiplier: x2.5                            # Had their wound cleaned and dressed with topicals
        Base Topical Multiplier: x2.0                       # The effect of the topical on this specific damage
        Wound Cleaning Multiplier: x1.25                    # Recieved basic wound cleaning
    Chemical Multiplier: x1.5                           # Basic Chem administered
    Rest Multiplier: x1.33                              # Bedrest and perhaps resting in a chair
Multiplier Product: x0.83
Addends:
    Topical Healing: +0.05                              # Basic topical addend
    Chemical Healing: +0.1                              # Basic chem addend
Addends Healing Rate: x0.98
Healing Rate Cap: (Skipped since the sum is =< the lowest cap)
    Standard cap: x1.25                                 # Meant to be a baseline cap to prevent people from going hog wild without medical, depends per stat
    Bedrest cap: x1.33                                  # Meant to make bedrest better than not, not too high as it's the bare minimum that can be done
    Chemical cap: x1.33                                 # The effect of a simple chemical meant to provide healing for that specific damage type
    Topical cap: x1.5 <--- If engaged, Tested against   # A high cap meant to be stacked up to within medical for a specific damage type.
Natural Healing: Enabled                            # There should be tools/situations that can kill natural healing entirely, nost just give a x0 multiplier
Final Healing Rate: x0.98

This system could be extended with specific statuses affecting the natural healing rate of specific damage types as need be, and ideally the system would be extended to allow for certain statuses to prevent natural healing from healing below a certain threshold per damage type. There should also be caps on the base multiplier that is applied with the various topical and chemical multipliers, taking the higher of the multipliers and allowing for medical to actually expedite healing somewhat. Good food should provide a healing multiplier outside of just nullifying the effect of being hungry/thirsty. These specific multipliers should be hidden but there should be some indication for the most intuitive healing options.

No natural healing when you're dead. Either hope you died of causes easy enough to recover from or hope medical feels like spending the resources getting your ass back up. Genetic damage could apply a constant subtraction to healing other damage types under the "Addends," basically making it so that genetic damage is significantly more of a threat.

As for the hard numbers of what those multipliers affect, I think that base healing should generally lie somewhere between 3 and 6 units of damage healed per minute, the specific amount of damage healed in a type varying depending on species. Proper medical visits should last somewhere between 10 and 20 minutes.

Natural healing spread + caps for a Human per minute
    Brutes: x1.25 cap
        Blunt: 6
        Pierce: 4
        Slash: 4
    Burns: x1.25 cap
        Heat: 6
        Cold: 6
        Shock: 4
        Caustic: 3 x1.1 cap
    Airloss: x2.0 cap
        Asphyxiation: 15
        Bloodloss: 8
    Toxin: x1.5 cap
        Poison: 3
        Radiation: 3
    Genetic: 1 if at all, x1.0 cap

#### Chemical Changes

Chemicals will be primarily for augmenting healing, rarely healing directly. Omnizine sucks and should probably be commented out, being able to effectively ignore medical's job with one reagent is lame. Saline's blood regeneration ability will be removed, as not only will actual IVs be implemented in Forky, it just directly affecting blood level is boring - get a transfusion if the bloodloss is that bad. Chemicals could definitely be used in a stabilizing manner, say counteracting poison damage over a certain threshold or preventing so much asphyxiation/bloodloss from building up. Basic chemicals should be kind of bad at affecting the healing rate, with more sophisticated chemicals having better multipliers and a higher a cap on the multiplier.

#### Topical Changes

Topicals will largely be for stabilizing patients directly, allowing them to recover. They *may* heal a small amount normally, but their main allure should be that you can slap some ointment on a burnt engi *once* and make sure they eat enough and/or get the right mix of stabilizing chems so that they can actually heal. Topicals should not apply their healing bonus for more than ten minutes at a time, and stacking the same topicals does little outside of doing the extra healing they would have normally applied. Topicals apply their bonus per "topical condition," with topicals using the best multiplier for their slot - using a regenerative mesh on someone will get them healing much faster than if you just used ointment, and you are in fact able to use ointment to heal just a smidge of damage there and then. Topicals should be balanced in such a way where there are specific topicals for certain physical damage or damage types, with there being some that are stronger than others if available.

Having topicals applied should give you an alert that say what topical you recieved and have that alert change/dissapear upon recieving damage ticks - for example, recieving blunt damage with gauze could immediately make it bloody and need to be replaced, same with bruise packs. Ointment could get smeared away, sutures ripped, dressing torn. Topicals will generally need to be removed before new topicals can be applied barring certain exceptions.

There could be a step of wound cleaning before applying topicals, like rinsing an area out or swabbing it with a sterilizing chem, that could boost topical effectiveness *especially* within medical. Rinsing out an open wound could have like 2u of the cleaning solution enter the wound. May or may not actually just be a separate multiplier you'd have to apply before topicals.
    Additional modifiers that can only be done before applying a topical
        Applying reagent to a wound, 10u cost:
            water: x1.1
            saline: x1.25
            space cleaner: x1.25
            strong, pure liquors: x1.25
            ethanol: x1.33
            hydrogen peroxide: x1.33
            phenol: x1.33
            iodine: x1.5
            tincture of iodine: x1.5
            sterilizine: x1.5
        Applying reagent to wound directly: refers to reagent table, long doafter
            Most reagent containers should be able to apply reagent to a wound, albeit slowly
            Specialized spray bottles that allow for a shorter time applying reagent
        Small wounds only (Below 20 total damage in a category):
            sanitary wipe: x1.25 multiplier, short doafter
            swab: refers to reagent table, 5u cost, short doafter

By and large, these topical modifiers will be something medical is trained to use - they should start off with sanitary wipes in their belt and understand how to use squirt bottles in order to rinse large wounds with stuff like peroxide or iodine, tincture or sterilizine if chem does some work. Crew members are free to wash their wounds with water, space cleaner or even ethanol if they can get it, but medical will generally be the place to get your wounds properly sterilized and treated.

Topicals will also get dirty after being on someone for so long or if they suffer further damage, needing to be replaced or removed before they start causing problems, with there being a 120-ish second grace period to remove dirtied topicals.

Topical Types:
    Bruise Pack - A pack of compressive wound dressings and bandages good for treating brute damage, dirties after 300s
        For generic brute damage and blunt damage in specific
    Ointment - A tube of ointment meant to be spread over burn wounds, lasts for 210s or until significantly damaged
        For burn damage in general, less effective for caustic damage but doesn't impact multiplier caps
    Gauze - A roll of cotton gauze meant to be wrapped around burns and cuts alike, can absorb quite a bit of blood, dirties after 300s
        For treating misc physical damage and bleeding quickly, doesn't impact multiplier caps but has better addends than either bruise packs or ointments for almost everything
    Suture - A roll of sterilized suturing intended to stitch cuts closed, dirties after 300s
        Specifically for treating slash, pierce, and active bleeding, has higher addends and multiplier caps for them in specific. Slow to apply, can be applied under most other topicals.
    Hydrogel Dressing - Gauze prepared with a layer of hydrogel for specialized burn treatment, dirties after 210s
        For treating burn damage better than ointment or gauze alone

#### Bleeding Changes

As an existing status, bleeding should be made more dangerous and harder to treat outright. The ways bleeding is applied may not necessarily need to be changed, but the status should be harder to remove in an instant with some gauze. Bleeding should decrease over time as blood clots, with different blood clotting statuses affecting that. The level of bleeding should be tracked even as topicals are applied, with most topicals stopping bleeding and getting dirty much faster. Sutures can resolve this by being applied first, as they both take the bleeding status without issue and increase clotting, where, only upon removing the suture, will bleeding continue. Recovering from bloodloss should also be harder, with blood levels either needing transfusion or blood plasma infusion to immediately recover.

Most topicals, spare from sutures, will get dirtied significantly faster if they cover bleeding wounds. They may hide the bleeding status and keep an individual's blood in place, but they will need to be replaced sooner with worse bleeding. 

Cauterizing wounds with heat damage should be more of a tradeoff now, with heat damage stopping less bleeding than it currently does.

#### Cryogenics

Cryogenics under this system seems a bit odd - cryogenics should definitely be slow, maybe provide standardized healing independent of multipliers. Placing someone into the cryogenics tube and having them heal should need dedicated, somewhat hard to source chemicals; turning water and more water into infinite cryox is certainly not ideal, cryogenics should be costly. Cryogenics being for when a patient would otherwise regenerate at a glacial pace seems somewhat better, though using cryogenics on corpses should be heavily limited as to not make death effectively meaningless again.

### Chem Rework

See the auxillary [chemical rework](./chem-rework.md) document for reference. The overall intention is to make chem less integral to medical's operation yet still important for healing at a somewhat reasonable rate, as well as giving chemists more to do throughout the shift that they couldn't just do roundstart.

Chemicals will need to last significantly longer in the body for their multipliers and adjustments to the multiplier caps to mean anything.

### Scanners and Detecting Damage

The direct numbers that determine how much damage an individual has should be hidden, with medical scanners and medhuds largely being depreciated. In their place, it should be easier to see just how bad wounds with a dedicated inspection, though less visible damage types will need to be inferred from patient context and how they seem to react to certain things. Outerwear and face-covering headwear will need to be removed in order to properly inspect what damage a patient has.

## Game Design Rationale

Recovery Med intends to be an alteration to the medical system that would make it more authentic and slower, ideally being compartmentalized and expandable enough for future medical reworks down the line to work off of it and create a more realized medical system. While definitely not as involved or as far reaching as Condition Med, Recovery Med would prevent the average crew member from just walking away from grievous injuries near instantly because they had a shot of the right chemical injected into them, because they decided to spend a minute covering themselves up with topicals they grabbed from a nearby medkit, because botany made 1000u of omnizine and gave everyone free samples.

Damage matters and healing takes time, with medical actually having jobs to do when it comes to treating patients. Chemicals no longer being the end-all be-all of treatment makes it so that alternative methods towards recovery have to be sought, such as blood drives occuring so that medical can actually treat patients with severe bloodloss, and will otherwise need to stockpile specific materials. There would still be ways to recover without the need to visit medical for those who may not be able to afford treatment. The end of a bar fight might result in the loser asking for a glass of vodka and washing their cuts with it before hobbling off to find a first aid kit. Chem should also be a bit more interesting under this system, having progression throughout the shift and needing to interact with more people to acquire the materials that they need; advcanced chemicals will no longer be able to be made shift-start.

## Roundflow & Player interaction

While there are definitely considerations for medical SOP, the vast majority of this is mechanical changes that directly slow down healing. Players will be spending far more time in medical, where doctors should be checking up on their patients to make sure that they're healing properly. The initial admission to medical will be more involved than just apply gauze (optional), scan, and inject chems. Patients will need to take off protective clothing, having their wounds washed and sutured while they describe to their doctor just what happened, recieving further treatment as necessary and being moved to a bed so that they can rest. Doctors will need to offer them food and drink to make sure that they have the energy to recover, and could just throw patients out if they feel that they could recover on their own.

In the instance that medical gets overwhelmed, medical *will* need to prioritize certain people and they won't be able to save everyone. Tough decisions will have to be made during times of crisis.

## Administrative & Server Rule Impact (if applicable)

This is very much a mechanically focused rework of medical, where it's unlikely to create much administrative workload on its own.

# Technical Considerations

- The systems for natural healing will need to be extended to facilitate multipliers, addends, and the multiplier caps
- Topicals will need to be extended to allow for wound washing, topicals getting dirty and needing to be removed before reapplication, and all of the bleeding interactions
- Chemicals will need to have the natural healing changes extended to them as well
- The removal of the universal medical scanners and making the damage inspect systems more robust will also need to be considered
- The entirety of a chemistry rework that makes chem more interesting and less of something that chemists can just hide in a corner all shift to do.