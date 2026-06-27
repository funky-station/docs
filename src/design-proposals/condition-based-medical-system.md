# Condition-Based Medical System

| Designers | Implemented | GitHub Links |
| --- | --- | --- |
| Ven | :x: No | TBD |

## Overview

This proposal replaces numeric, damage-type-driven medical gameplay with a condition-based system. Instead of reading and reacting to abstract values like brute, burn, and toxin, players experience injuries and illnesses as diagnosable conditions: a fracture, a concussion, pneumonia, a punctured lung. Each condition has a severity, can progress, and can develop complications, but those details sit under the hood. A crew member feels symptoms. A trained medic works out what is actually wrong.

The change runs deeper than presentation. It rests on one rule borrowed from how medicine works in real life: chemicals and field care suppress symptoms and buy time, they do not heal the underlying injury. Painkillers let you walk on a broken leg. They do not set it. The body recovers with time, and proper resolution (surgery, disinfection, setting a bone, aftercare) lives mostly in medical. Numbers still run everything internally. They simply stop being the way players understand their own health.

## Background

Medical gameplay on Funky Station currently inherits a largely number-driven model. Players take damage, receive treatment that reduces numbers, and return to duty almost immediately. The loop is "read the damage, apply the matching chem, discharge." It is functional and arguably well balanced, but few people enjoy it. Medbay is easy to access, treatment is fast and deterministic, and non-medical players understand their condition as an optimization problem rather than as something happening to their character.

The deeper issue is that healing is too simple. Right now a chemical undoes an injury wholesale. That is not how medicine works. In real life most medicine suppresses symptoms and supports the body while the body does the recovering. Antibiotics are close to the only thing that actively cures, and chemotherapy works by poisoning you slowly and hoping healthy cells win the race. You can treat a broken leg, but you walk away with a limp, or a long recovery, or both. You never really heal. You recover.

That distinction is the foundation of this proposal. A crew member experiences symptoms ("my arm hurts," "I can't stop coughing"), and trained medical staff determine whether that symptom is a sprain, a fracture, an infection, or something worse. Quick fixes still exist so players keep the battlefield feeling of intense, improvised care, but a quick fix is temporary by design. Painkillers let a marine ignore a broken leg long enough to finish the fight. The leg is still broken. To actually treat the underlying condition you need time, procedures, and usually a doctor.

This makes medical matter. It makes people take fewer risks. It makes self-sacrifice mean something again, because being dragged back from the edge comes at a cost rather than a five-minute detour to medbay.

## Features to be Added

### Condition-Based Injury and Illness Representation
Player-facing medical states are represented as discrete conditions (broken arm, concussion, pneumonia, punctured lung) rather than numeric damage values. Conditions carry a severity, a progression state, and possible complications, all abstracted away from non-medical players. Internally the existing damage values still drive these states. Enough blunt trauma to a limb crosses a threshold and becomes a fracture. The number is still there. The player just sees the fracture.

### Symptom-Driven Feedback
Non-medical players receive experiential feedback (pain, impaired movement, coughing, dizziness, blurred vision) rather than diagnoses or numbers. This feedback is deliberately imprecise and can point to more than one condition, which is what gives diagnosis its value.

A practical concern here is that subtle effects get missed. A five percent movement penalty is easy to overlook, and some players turn effects like dizziness all the way down for good reasons. So anything subtle or accessibility-sensitive should surface as a clear pop-up rather than relying on the player to notice a numeric drift or read a screen effect. A leg condition should tell you "your leg is dragging" in text, not just quietly slow you down. The existing stethoscope is a good proof of concept already in the game: it returns a flavorful description based on a patient's asphyxiation damage instead of a number. This generalizes that idea across the whole system.

### Suppression vs Treatment
This is the core of the rework, and the part that separates it from a reskin of damage types.

Every condition can be acted on in two fundamentally different ways:

- **Suppression** is fast, mostly field-available, usable by nearly anyone, and temporary. It eases or hides symptoms and buys time. It does not resolve the condition. Painkillers, adrenaline, tourniquets, bleeding control, CPR, and most chemicals fall here. Salic acid takes the edge off a wound, it does not close it. A tourniquet stops you bleeding out, it does not mend the artery.
- **Treatment** is slow, mostly medical, procedure-driven, and resolves the condition for good. Surgery, disinfection, setting and splinting a bone, draining a lung, and proper aftercare fall here. This is where the doctor's job lives, and where time genuinely has to pass.

The important consequence is that working out what is wrong with you does very little on its own if all you can do is suppress it. A security officer who reasons "blurry vision after a toolbox to the head, probably a concussion" is correct, and it does not help him, because he cannot resolve a concussion in a maintenance tunnel. He can dull it and keep moving. Sooner or later he has to see someone. That is the asymmetry the system runs on, and it is intentional.

### Diagnostic Medical Gameplay
Diagnosis is a gameplay loop, not an instant reveal, and it is gated behind tools and training rather than handed to everyone.

The depth of information scales with the tool. A quick handheld scanner, the Star-Trek-style "wave it over them" device, reads surface-level symptoms fast: visible trauma, obvious fractures, heavy bleeding. It is the right tool for a paramedic triaging in the field. It does not diagnose disease, poison, or subtle internal damage. Doing that needs the fuller kit back in medbay: a body scanner or analyzer that can see internals, run the equivalent of bloodwork, and distinguish a punctured lung from bruised ribs.

A useful mental model for the interface is a paper-doll layout. External conditions show on the body map from examination and a basic scan. Internal conditions (organ damage, internal bleeding, disease, poison) stay hidden until the right equipment is used. A medic can be wrong, or simply not yet know, and that uncertainty is a feature. If diagnosis could never fail or stall, self-optimizers would route around medical entirely.

The examine and inspection window should carry more of this weight too. Right now obvious, dramatic injuries get flat descriptions. "Third degree burns all over the body" is the same line whether it is a patch or a charred torso. Examine text should scale with severity: "the left shin is bent at an odd angle" for a clean fracture, up to "the shin bone is through the skin" for a compound one. The more an injury would be obvious to a bystander, the more obvious it should read.

### Variable Treatment Paths
Most conditions support more than one approach, and the choice depends on severity, time pressure, and how slammed medbay is.

- **Minimal care** suppresses and stabilizes, then returns the patient to duty fast. The condition persists and may resurface later.
- **Maximal care** fully resolves the condition through proper treatment and heads off complications.

In a quiet round a doctor sets the bone properly. Mid-round with three gunshot patients waiting, the same doctor tourniquets, drugs, and sends the walking wounded back out, knowing some of them will be back worse. That trade is the point.

### Condition Progression and Complications
Untreated or minimally treated conditions worsen over time and can develop complications such as infection, organ damage, or shock. If you know you have a deep gash in your arm and you let it sit for a long time, it should escalate to the point where it is treatment or a serious risk of death. This rewards follow-up care and gives short-term fixes a real cost down the line.

Progression also governs repeated injury. You cannot "double break" an already broken leg. New damage of the same kind stacks the existing condition up to its next severity rather than creating a redundant second condition, and higher severity introduces secondary effects: heavier bleeding, nerve trauma, more shock, more strain on vital systems. Higher severity also raises the complexity of treatment, which feeds directly into the next section.

### Pain and Secondary Conditions
Pain is not just a status bar. It is an active driver of other conditions, and that gives it a real place in the loop.

A leg injury produces pain, and that pain can produce a secondary condition such as a limp. Because the limp here is pain-derived, it lifts when the pain is suppressed. A shot of adrenaline or a strong painkiller can clear it on the spot, and it returns when the suppression wears off. That is a clean field play: a wounded operative dropping adrenaline to run on a bad leg, then seizing up again once it burns off.

Structural damage is different. A limb that has been mangled, not merely hurt, produces a limp that is not about pain at all, so no amount of painkiller touches it. That is a permanent condition until it is properly treated, if it can be treated. Same symptom, two very different causes, and the difference is exactly the kind of thing a diagnosis is for.

For communicating pain itself, the goal is to convey that the character hurts, keep it hard to forget, and not nag the player or pretend the player is their character. The approach is periodic low-friction feedback that scales with severity, a pop-up or examine state rather than a constant screen filter, and it is suppressible, which doubles as a gameplay hook. A player can buy quiet by taking the edge off, at the cost of hiding what is actually wrong.

### Improvised and Unlicensed Treatment
Real treatment should be possible outside a sterile operating theatre, it just should not be good.

A glass shard can stand in for a scalpel. Surgery can happen on a maintenance floor with the wrong tools and no anaesthetic. Unlicensed, improvised care is allowed and sometimes the only option an antagonist or a cut-off survivor has. But it carries higher risk: greater chance of infection, more bleeding, botched outcomes, and worse results than doing it properly with the right equipment and a trained hand. The harder a condition is to treat, the more an improvised attempt is likely to go wrong, which ties improvised care back to severity and keeps proper medical care worth seeking.

## Crit, Incapacitation, and Death

Under a condition-based system, crit and death are outcomes of systemic failure, not standalone conditions. This proposal does not remove crit or dead states. It changes how injuries and illnesses contribute to reaching them.

### Vital vs Non-Vital Systems
Conditions divide broadly by the systems they affect.

- **Non-vital conditions** (broken bones, soft tissue injuries, localized burns) are generally not immediately lethal on their own.
- **Vital system conditions** (oxygen deprivation, cardiac failure, brain trauma, severe organ damage) directly threaten consciousness or life.

Non-vital conditions can still kill indirectly, over time, through blood loss, shock, pain, infection, or reduced mobility piling onto the vital systems. Breaking every bone in someone's body will not flip a "dead" flag by itself, but the bleeding, shock, and immobility stacking up from all of it can drive the vital systems past the point of recovery.

### Crit
Crit is a state where one or more vital systems can no longer maintain normal function: loss of consciousness, respiratory failure, cardiac arrest, extreme shock. The character is alive but systemically unstable and needs intervention to avoid death.

### Death
Death occurs when vital system failure becomes irreversible: untreated cascading conditions, catastrophic organ damage, prolonged hypoxia, or anything that pushes the body past what it can recover from.

### Revival and Consequences
Revival should not be a routine reset, and death should carry weight. Not every revival needs to cost something. Someone brought back quickly and cleanly can walk away fine. But the further gone a patient is, the more revival should leave a lasting mark, a debuff or a permanent condition that reflects the damage done.

This puts a real decision in the doctor's hands: is this person far enough gone that bringing them back leaves them barely functional, and is it even worth it. It makes self-sacrifice matter, because throwing yourself at a threat is no longer free when you know being dragged back might leave you with a permanent limp, reduced lung capacity, or worse. And it gives "stay dead" an honest meaning, since dying twice should leave you in a state where staying down is the reasonable choice. Exact debuffs and thresholds are a balance question for later. The principle is the part that matters now: you recover, at a cost, and sometimes you do not fully recover at all.

## Game Design Rationale

This system supports Funky Station's core design principles.

- **Maintaining Authenticity**: Injuries feel grounded and legible without leaning on real-world medical simulation. Players deal with believable outcomes instead of arithmetic.
- **Taking Things Slow**: The slow part is resolution and recovery, not input speed. Emergencies still allow fast stabilization, so a firefight does not turn into waiting on a progress bar. You pay for the speed afterward, in follow-up care and consequences, which is where the round length naturally absorbs it.
- **Maximizing Roleplay Potential**: Diagnosis, triage, and uncertainty create real interaction between patient and medic. The patient describes symptoms, the doctor investigates, and neither is just watching a number tick down.
- **Avoiding QOL Slop**: Removing numbers from the player-facing layer discourages hyper-optimization and rewards judgment.

Numbers still run the show internally, for balance, predictability, and tuning. The change is not deleting numbers. It is removing them as the primary way players read their own health.

## Roundflow & Player Interaction

This system is active every round and slots into existing sources of injury, illness, and antagonist activity.

### Early Round
Minor injuries and early symptoms add uncertainty without pulling players out of the round. Crew can ignore a symptom or get it looked at early.

### Mid to Late Round
As injuries pile up and medbay gets busier, staff are pushed to triage and suppress where they cannot fully treat. Conditions get deferred, which means complications and return visits later.

### Intended Player Interaction
- Non-medical players should feel fine seeking help without fully understanding what is wrong with them.
- Medical players should be making judgment calls under pressure rather than walking a single optimal path.
- Players should not be able to fully diagnose or resolve their own treatment without medical involvement.

### Players Without Access to Medical
A recurring and fair concern is offmed: antagonists and security often cannot reach professional care. A prisoner is cuffed in the brig, nukies stay on the move, heretics and syndies going loud are capped by their own kit, and medbay is frequently overwhelmed or outright hostile to them.

The answer is the suppression and treatment split. Field stabilization is accessible to nearly everyone. You can dull pain, stop bleeding, run CPR, and buy yourself time with drugs and equipment, on yourself or an ally, without ever seeing a doctor. What you cannot do is permanently resolve a serious condition alone. That is the intended asymmetry, and it is also the source of the drama. An operative can keep fighting on adrenaline and a tourniquet, but the broken body underneath is still broken, and eventually that bill comes due. The pressure valve for balance is making stabilization genuinely accessible, not letting people self-cure.

## Antagonists and Grounded Technology

A guiding rule for this system is that technology the crew understands and fields should stay relatively grounded. There is no cure-all that quietly undoes an injury the way chems do today, because removing that shortcut is the whole premise. The medicine the station runs on suppresses and supports, and resolution takes procedures and time. Keeping understood technology down to earth is what holds the rest of the system together.

Antagonist healing is treated differently, and on purpose. Syndicate and other hostile tech does not need an in-fiction explanation. It is the other. The crew is not meant to understand how a piece of syndicate medical gear works, and that opacity is already the in-game reason crew are not supposed to rely on stolen syndi equipment. The same goes for the cult, which draws on powers its own members do not fully understand. These can stay unexplained without it being a gap in the design.

In broad strokes, what the tools themselves might be is worth sketching at a concept level, without pinning numbers or charges to anything.

- **Traitors** lean on single-use items from their uplink and on whatever crew care they can get or coerce. Think a stabilizer injector that drags someone out of crit, a combat stim that buries pain and keeps them upright through a fight, or a rarer one-shot item that actually closes a wound. The defining trait is that they run out, so each use is a real decision rather than a refillable habit.
- **Nukies** carry portable, reusable, expensive kit a station would never field, built to keep a strike team moving without a medbay behind them. A medical beam that stabilizes and suppresses an ally at range fits the role, something that keeps the squad pushing rather than curing anyone. Less a cure, more a way to stay mobile while hurt.
- **Cultists** heal through ritual rather than equipment, a rune or a channeled ability paid for in the cult's own currency of time, blood, or proximity to their structures, drawing on power they neither control fully nor are meant to understand.

There is one real design question buried in this, and it ties straight back to the asymmetry: do antagonist tools actually resolve conditions, or do they just suppress and stabilize better and more independently than crew field care can? Leaning toward the latter keeps the asymmetry intact. Antags stay mobile and dangerous but still carry the damage, while a few rare, expensive, deliberately unexplained items can genuinely resolve as the exception that proves the rule. That call is worth making on purpose, but it lives at the balance layer.

Whether NanoTrasen itself fields a restricted item of its own, something command-only or otherwise locked down, is left open. It might be needed, it might not.

Beyond that, this stays out of specifics. How strong these options are, how many uses they get, how available they should be, all of it is balance and out of scope. The design point is only this: the crew's medicine stays grounded, the other side is allowed to stay a mystery, and each side's tools should fit how that side actually plays.

## Worked Example

A security officer takes a bullet to the leg during a firefight.

- **The hit.** He gets a pop-up that his leg is badly hurt and bleeding, and he starts to slow. No numbers, no "you took 34 brute."
- **Field stabilization.** A squadmate slaps on a tourniquet and hits him with a painkiller. The bleeding stops, the pain drops, and he can run again. Nothing has been healed. The wound is still open under the tourniquet, and the bullet is still in there.
- **The choice.** He can keep fighting on borrowed time or pull back. He keeps fighting, because the threat is live.
- **Consequences mounting.** The painkiller wears off mid-fight. Pain returns, and with it a limp from the pain. He hits adrenaline to clear it and pushes through one more time.
- **Medbay, eventually.** Back in medical, a body scan shows the retained bullet and the open wound. Proper treatment is surgery to remove the bullet, disinfection to head off the infection that was already starting, and the wound closed and dressed. That takes real time, which medbay may or may not have to spare.
- **If he never shows.** The wound progresses. The early infection becomes a real one. What was a clean surgical job becomes a serious, possibly limb-threatening problem, and the limp he kept suppressing turns out to be partly structural after all.

The same incident under the current system is a bandage and two chems at a bed, then back to duty in under a minute. The difference is the entire point.

## Administrative & Server Rule Impact

This system does not add new rule categories, but it changes how some existing situations read, mostly by moving them out of the admin queue and into the round.

The key shift is that uncertainty is there by design, not by mistake. Because misdiagnosis, triage, and judgment calls are expected parts of how medical works, they stop being administrative problems and become in-character ones. Today, a body left unrevived reads as "this player walked past me and refuses to help," and it lands in ahelps. Under this system the same moment reads in-fiction: maybe the patient is past saving, maybe medbay is swamped and the doctor is working on someone more likely to pull through, maybe someone with better insurance is ahead in the queue. The drama stays in the world instead of escalating to staff.

- Medical negligence becomes contextual, since uncertainty and triage are expected rather than exceptional.
- Disputes over quality of care will still happen, but they are grounded in roleplay rather than mechanical failure, and resolved there most of the time.
- Self-diagnosis and instant recovery are mechanically limited, which reduces ambiguity around powergaming.

## Technical Considerations

- Numeric values stay in use internally to drive condition thresholds, severity, and progression.
- Existing damage types can be refactored to feed condition generation rather than direct player feedback.
- The current limb system inherited from shitmed is not something to build on long term. Supporting condition-based medical will likely need it replaced or significantly reworked, though that replacement is out of scope for this proposal.
- New and updated UI is required: the symptom pop-ups, severity-scaled examine and inspection text, and the paper-doll diagnostic interface with its external versus internal split.
- Performance impact should be minimal, since conditions largely reuse existing damage and status systems.

## Out of Scope

These are acknowledged dependencies and follow-ups, to be handled in their own documents so this proposal stays focused on the core system:

- The shitmed limb system rework.
- The full chemical rework that suppression versus treatment implies.
- Role differentiation (paramedic, MD, virologist) and the equipment balancing that comes with it.
- Species-specific conditions and interactions, once a baseline exists.
- The insurance, scrip, and cybernetics layer around treatment access and limb replacement.

## Open Questions

- How granular should conditions be at first implementation, and what is the minimum viable set to ship the loop?
- Where exactly is the line between handheld and full-kit diagnostics, and which conditions sit on each side?
- How are complications like infection surfaced so they feel like a consequence rather than a surprise?
- How should pain feedback be tuned to stay present without becoming noise, and how does that interact with accessibility settings?
- Which revival consequences are interesting versus merely punishing, and where does the "far gone" threshold sit?
- How do combat-oriented antagonists keep functioning under gated self-resolution, and how is their healing access tuned so it preserves the asymmetry rather than bypassing it? Does NanoTrasen need a restricted option of its own?

---

This document focuses on player experience and design intent rather than exact balance values or implementation details. Those are expected to be iterated on during development.
