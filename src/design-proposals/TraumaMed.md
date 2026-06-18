# Trauma Med

| Designers | Implemented | GitHub Links |
|---|---|---|
| Scrambleking | :x: No | TBD |


## Overview

Trauma-Med is a combined forensic and treatment system with a focus on medical care.

The document leans heavily on attricion, medical treatments, and works within our current damadge system.

## Background

Cybermed is no longer being developed, we now have nu-body.

This doc is designed to work along side, but not require, https://github.com/funky-station/docs/pull/114.
Specificaly the "treated" there would be directly connected to the treatment of Traumas here.

This document draws upon sources such as Casualties Unkown, Operation, and some old flashgames for insparation.

This document does not impliment diseases, though it recomends designing areas for such systems to fit in upon implimentation.

## Features to be added

### Trauma
Traumas occur on the instance of a damadge. For instance when you are shot with a gun, you gain one bullet wound trauma.
The trauma persists untill "treated".
These traumas, depending on the source, can also trigger diffrent versions of said trauma requireing seperate treatments (bullet passes through, vs hitting an organ vs bullet gets lodged in).
While afflicted by a trauma, the associated damadge cannot be healed by (standard) chemicals, requiring more indepth medical care to to be able to recover the health loss.

Some traumas depending on severity may only partualy stop healing (such as a 10 damadge injury naturaly healing to 5), while some may heal naturaly on their own (such as a 1 damadge papercut self-healing).
This is not defined by the severity of the trauma, but by the trauma itself.

Additionaly traumas should roll according to the damadge dealt after resistances, so the injury to an unarmoured person should be much more severe than a jugsuit.

#### Un/Defined Traumas

Defined damadges are damadges that are explicitly defined in what Trauma they may produce in addition to further effects they may have.
These can be specific to the involved trauma (such as barotrauma), or be catagorised under a group of traumas (such as bullet wounds) or annother such group.
There are also undefined Traumas, intended for interactions with systems that have yet to gain their own identified traumas.

##### Catagorised/Instance Traumas

Instance traumas involve a scale for how severe of an outcome they may produce based off of the damadge given.
As an example, a gunshot that deals less than 10 damadge is more likely to leave a "bullet in" trauma than an antimaterial rifle shot, which might leave a "gaping bullet wound" that is harder to fix than a regular "bullet wound".
These are tracked seperately, and 2 wounds of the same severity (such as a 5 and 10 damadge small bullet wound) would require the same level of treatment but each would track how much healing they are blocking seperately.

##### Stacking Traumas

Stacking traumas consist of damadges such as organ damadge, pressure damadge, being a bad tempriture too long and the like.
These do not require seperate treatments as they all count as the same damadge source, though with enough severity they may require a more intense method of treatment.
As an example being in a slightly too hot room for a moment may only require some ointment, but walking through the burnchamber nude would require surgery and likely advanced chemical treatment.

##### Undefined Traumas

Undefined traumas are a catch all for damadge sources that do not define what trauma they may inflict. 
As an example, if you make an icicle gun and dont define it, it will deal "unidentified peircing trauma" and "Unidentified Cold Trauma" which counts as a stacking trauma source.
Additionaly some damadge may only be partualy defined for their traumas such as defining the icicle as a "bullet trauma catagory" but with "unidentified cold" with it, or even a more unique trauma that covers 2 damadges.

Of note: Metashielded topics should not be noted past what is within the trauma type, and descriptions of traumas should generaly be vauge.
A cosmic cultist sword may cause "A Sword Wound Covered in Frostbite" but it wont cause "A Cosmic Cult Sword Wound" trauma.

##### Secondary Traumas

Secondary traumas are most commonly associated with Organ, bone, or Limb damadge.
These traumas would have a chance to roll both for general damadge of a given type (breaking bones with blunt) and for specific Trauma sources (The Bone Breaker Gun TM).
Secondary Traumas all come with secondary effects, such as a broken bone causing a slowdown in movement, accidentaly dropping items, or something else simular.

#### Treated traumas

Treated traumas continue to exist until fully healed, acting as evidance of treatment.
The treatment of trauma will instantly heal a portion of the damadge inflicted from the trauma, though it will still require time, sped up through chemicals, to heal fully.

#### Trauma Timers

Certain traumas may have timers innately on them that worsens the injury with time, or else festers causing the need for additional medical care.
This is intended to work with a proper disease system, but without the implimentation of one it can simply provide poison damadge on the wound, requiring cleaning or even more advanced processes to heal.

This system also works to staunch bleeding by having a "fresh" wound bleed as it slowly clots on an indevidual level.

#### Trauma Locations

Each time a trauma is inflicted it will roll a location between the head, torso, arms, or legs.
This system will primarily be used in trauma identification as expanded on later, but will also exist to alow for more secondary trauma effects depending on location, and additionaly work as a tie-in for future surgical systems.

### Identifying Trauma

Identification of trauma comes in 3 forms, with increasing levels of effort to preform.

1. Basic Inspection
Basic inspection is essentialy what we currently have with the shift-click to see health system, only identifying the surface level wounds when not covered (such as by an EVA suit).
Each Trauma would have an associated clothing that will cause it to be hidden, such as gloves hiding arm wounds, shoes hiding leg wounds, and shirts hiding torso wounds.

2. Medical Inspection
Medical inspection opens a proper body-UI via a medical scanner to show injuries in given locations.
This UI can then be used to determine optimal treatment methods by clicking on wounds listed by location (or visualy shown should it prove viable).
This method of inspection will also hide injuries depending on clothing.
Using this method should also suggest the possiblity of internal trauma, though not explicitly what it is.

3. Advanced Medical Inspection
Advanced medical inspections can be done via the use of additional tools such as the stethascope and provide further information on internal trauma.

5. Mechanical Inspection
Mechanical Inspections are done via a proper scanning machine.
These take time to proceede and are most often used to identify internal traumas such as damadged organs, lodged bullets or broken bones.

### Treatment

There are 3 stages of treatment implimentation intended with this document for treatment.
With the exeption of chemical treatments, each injury must be indevidualy treated.
As an example, if someone has 3 bullet wounds you should be applying 3 bandages to treat them all.

1. Raw/Topicals

Raw treatment methods heal traumas without the need for surgical intervention.
Many traumas will be satisfied with this level of treatment, but for heavier or more complicated injuries will require surgical treatment, or even possibly chemical.

2. Surgical

When Raw Treatment is not enough, surgical treatment will be required.
Surgical treatment involves a larger step by step process that results in additional traumas that must then be further tended to by Raw/Topcial methods.
A barebones implimentation would be fairly simular to shitmed in implimentation working through a UI menue for specific treatments, but would be intended to work as a Minigame-style surgery system in it's full form.

4. Chemical

Normal use of chemicals within this system hasten recovery post-treatment.
Some traumas (See Organs, Toxin Damadge, Genetic Damadge) require chemicals to heal, but these are rare and expensive.
Exotic style chemicals may be able to treat traumas directly, but these would be prohibitively expensive.

#### Interaction Type

Interaction types are how players will interact with the treatment system in game.

1. Do-after

Do after systems are simple "click button to do thing" as they are now.
Some treatment methods (such as applying ointment) may be left at this degree of healing, while other treatments are planned to be further expanded into "Minigame" treatments.

3. Minigame

Minigame treatment is intended as the final stage of implimentation.
Done entierly through UI this would involve such methods as "pulling glass shards out", "Taking a bullet out of a wound", "Stitching the wound" and "surgical" treatments.

#### Treatment Types

1.  Full Treatment

In the case of a bullet-in injury, a full treatment may require taking out the bullet, staunching the additional bleeding, then applying a bandage.
This would alow the wound to fully heal over time, though use of better or worse tools may effect the natural healing speed, or if they are bad enough cause damadge and/or count as partual treatment.

As an example, using cloth or hand-crafted banadages may inflect "poison" upon the patient, possibly rolling disseases should such a system be implimented.

2.  Partial Treatment

In the case of the same bullet-in injury, you may chose to simply wrap the wound with a bandage, alowing the wound to partualy heal from the injury. 

### Organs, Toxin Damadge, Genetic Damadge

With the existance of nubody systems the possibility of organ damadge becomes an option for use.
Generaly organ damadge will result in the connected system causing continual issues (such as a lung injury causing a growing airloss and speach issues)
Organ health and organ Trauma should be dealt with the same as body health and body trauma, where they are seperate systems that work together.
In order to repair organ health (before surgical replacements) you utilise chemicals to regenerate the effected organ through cryogenics.
With the addition of surgery it will primarily be done surgicaly with replacement organs that themselves come with compatability trauma, suppressed through chems (though expensive cryogenic cures will still exist).

Additionaly "Toxins" (Poison and Radiation) as a damadge will effect organs directly, and require Mechanical Inspection in order to identify for proper treatment.
Genetic damadge on the other hand will be removed as a damadge type and be changed to an effect-only trauma.
Genetic Trauma will cause continual damadge to internal organs until treated through advanced methods, effectively working as a continual cancer/virus within the body to support it being a meta-level punishemnt.

### Species specific trauma
Certain species require seperate trauma tables from standard species, such as aracnids exoskeleton. 
Initialy implimentation with these species may not be as perfect as is ideal, however depending on the species they should be able to roll on an acording trauma table as would be appropriate for their pysiology.
In the case of no species specific trauma table however it should always default to a standard table.

In some cases trauma may entierly not function as a system *stares at slimes*.
These species can intialy function with the standard trauma rules, but should be worked with to create a system connected to the trauma tables, even if it involves a blanket table override for each damadge type.
In the case of slimes, having specific chem metabolism with regen and additional hunger requirements may satisfy this.
They should still roll on tables, but Slime Trauma is likely to look entierly diffrent from every other species.

### Borgs
Thats right, im including borgs in this.
Borgs while being reletively simple to repair can also easily be included in this system, and identification only has to be at a surface level.
Their repair methods will of course not be the same as standard treatment, but there is no reason why a borg beaten by a toolbox should be repaired with a welder. 
As such they *too* will get their own trauma tables, with such treatment as "banging back the metal" and "replacing sheets".
The largest diffrence in treatment is that borg-treatment will immediately heal them instead of requiring additional recovery time.

### Death, CPR, and Airloss

As with the current system, the body must be healed below their death threashold to be revived, requireing CPR to recover that state and assist in fixing traumas associated with Airloss such as "hypoxia".

### Antagnoists
Antagonists still need a way to heal, and existing measures can still be used within the current system, though with some changes.

1. Passive healing sources
Current passive healing sources such as the BC pylon can still be used to heal trauma, and over the course of healing may provide may automaticaly reduce the severity of trauma, or eventualy completely negate them.
They do not however "treat" them

2. Active healing sources
Active healing sources (like if we gave a person a collosus type heal) will have to be balanced on a case by case basis, but until they are they can be assumed to automaticaly heal everything within the damadge range of the heal.

3. Healing Chems
For Nuclear operatives, syndicate agents, and other non-magical roles, a big source of antag-based healing will come from "advanced interdyne chems" or a simular equivilent which will be able to bypass the majority of trauma treatment.

## Game Design Rationale

Each level of this system is meant to provide more immersion and layers to the world's medical and health systems, slowing down treatment and making it more indepth and engaging to those interacting with it.
Additionaly this systems forces combatants to actualy heal between engagements instead of slapping 2 bandages on themselves and calling it good, making atricion without proper preparedness to be a far greater issue.
Lastly it means that people cannot simply ignore injuries, and are far more likely to avoid combat when able to so that they dont have to go to medical for treatment.

## Roundflow & Player interaction

Over the course of a round this will create a *vastly* more complete triage system within the game, encouraging the proper use of medical supplies creating a more noticeable gameplay loop than just "oh yea bandage me so I can run right back in."

Idealy this results in the following styles of interaction:
1. A gunfight occurs
A security officer is downed and 2 civilians are hit.
The officer is bandaged by the paramedic to staunch the bleeding as a priority patient, and given a stabilising medication.
The civilians are healed if they are in a dangerous situation, if not they head to medical.
At medical the officer is checked for secondary injuries as they have sustained the most damadge
The Civilians are given a basic once over to see if they have taken any secondary injuries, and are either taken in for better care, or given some chems to heal the remainder of the damadge.
The Officer having bullets lodged in themselves has to have them removed, along with having to be given some chemicals to deal with minor organ damadge as they leave.
They spend some time recovering in the ward before heading back out.

2. 
The syndicate heads to maints to heal themselves after the fight.
After getting to a quiet room they lather on some ointment on their burns, its not perfect but itl let them hide the pain and start it healing.
They then wear additional clothing to hide their injuries and identity as they head back to work, pretending like nothing happend.

## Administrative & Server Rule Impact (if applicable)

This is likely to have an effect on powergaming rulings around med-huds becoming much more strict as it becomes possible to hide your wounds through clothing.
Additionaly a general look at powergaming around randomly holding topicals will need to be reviewed.

# Technical Considerations

There are many techincal and preformance issues with this implimentation as it is wide reaching.
First is the implimentation of a damadge handeling system that works between the the entity taking damadge and the actual health of the entity itself, along with the timer systems inherent in that.
Trauma itself could probably be handled through Components given to entities accordingly, but would then require the ability to stack components accordingly.
The UI need is vast, even if the current scanner UI is mostly re-used a full implimentation would require much more effort than the current system, especialy if you include "treatment minigames".
Prediction in the system will also have to be accounted for, perhaps using an RNG for each character that is initialised on spawn, and synched with client whenever the body is inhabited.
