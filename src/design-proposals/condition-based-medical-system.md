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

### Condition-Based Representation
Player-facing medical states are represented as discrete conditions rather than numeric damage values. A condition is the underlying problem: a broken bone, a burn, an infection, alcohol poisoning. Conditions carry a severity and can progress, all abstracted away from non-medical players. Internally the existing damage values still drive these states. Enough blunt trauma to a limb crosses a threshold and becomes a fracture. The number is still there. The player just sees the fracture.

Conditions are tagged by how they were caused:

- **Combat-induced** conditions come from being hit: the break, the cut, the burn.
- **Ambient-induced** conditions come from the environment and the bloodstream: poison, radiation, temperature, drink, time. This is what would usually be called illness.

Every condition runs on the same three-stage severity, low to high, and the stage names are flavour for that condition. A wound reads as cut, then laceration, then gash. A bone reads as fracture, then broken, then shattered. The scale underneath is identical.

Conditions attach to parts, and which parts a condition can appear on depends on the condition. A broken bone needs a bone, so it only lands on limbs, never on a liver. An infection can take hold almost anywhere. A single part can carry several conditions at once, each at its own stage. Some conditions also spread from part to part, which is covered under progression.

### Symptom-Driven Feedback
Conditions and symptoms are two separate layers, and keeping them apart matters. A condition is the underlying problem: a fracture, pneumonia, a punctured lung. A symptom is what the body shows because of it: pain, a limp, coughing, dizziness, blurred vision. Non-medical players live in the symptom layer. They feel the symptoms and never see the condition or a number behind it. The feedback is deliberately imprecise, and a single symptom can point to more than one condition, which is what gives diagnosis its value.

A practical concern here is that subtle effects get missed. A five percent movement penalty is easy to overlook, and some players turn effects like dizziness all the way down for good reasons. So anything subtle or accessibility-sensitive should surface as a clear pop-up rather than relying on the player to notice a numeric drift or read a screen effect. A leg condition should tell you "your leg is dragging" in text, not just quietly slow you down. The existing stethoscope is a good proof of concept already in the game: it returns a flavorful description based on a patient's asphyxiation damage instead of a number. This generalizes that idea across the whole system.

### Suppression vs Treatment
This is the core of the rework, and the part that separates it from a reskin of damage types.

Every condition can be acted on in two fundamentally different ways:

- **Suppression** is fast, mostly field-available, usable by nearly anyone, and temporary. It eases or hides symptoms and buys time. It does not resolve the condition. Painkillers, adrenaline, tourniquets, bleeding control, CPR, and most chemicals fall here. Salic acid takes the edge off a wound, it does not close it. A tourniquet stops you bleeding out, it does not mend the artery.
- **Treatment** is slow, mostly medical, procedure-driven, and resolves the condition for good. Surgery, disinfection, setting and splinting a bone, draining a lung, and proper aftercare fall here. This is where the doctor's job lives, and where time genuinely has to pass.

The important consequence is that working out what is wrong with you does very little on its own if all you can do is suppress it. A security officer who reasons "blurry vision after a toolbox to the head, probably a concussion" is correct, and it does not help him, because he cannot resolve a concussion in a maintenance tunnel. He can dull it and keep moving. Sooner or later he has to see someone. That is the asymmetry the system runs on, and it is intentional.

### Diagnostic Medical Gameplay
Diagnosis is a gameplay loop, not an instant reveal, and it is gated behind tools and training rather than handed to everyone. There is no single magic scanner that reads everything out at once. Diagnosis is done with a kit of specific instruments, each revealing one kind of thing, and a good read comes from picking the right instrument for what you suspect. The stethoscope already in the game is the model: a tool you use and interpret, not a numeric dump. The toolset is meant to grow with the system, x-ray machines, bloodwork, and more, as new conditions need new ways to be found.

The body reads as two layers. On top are the limbs, where everything is external and visible: trauma, fractures, burns, bleeding. Underneath are the organs, housed inside the head and torso, where everything is hidden: organ damage, internal bleeding, disease, poison. Which layer an instrument reaches, and how plainly, is what separates the tools.

The surface reads are immediate. Hands and eyes, examination and palpation, cover the limb layer: external trauma, fractures you can feel, swelling, bleeding. They are fast, portable, available to anyone in medical, and for plainly external things they can be definite. A bone through the skin does not need confirming.

The hidden layer costs time, and those tools mostly live in medbay. An x-ray confirms bone and chest, a clean fracture, a shattered one, a collapsed lung, but it is a stationary machine and imaging takes time. Bloodwork is the slow road to poison, infection, and disease, none of which anyone eyeballs. The stethoscope sits between the two: portable and quick, but interpretive, it tells you the breathing is wet and shallow and the medic draws the conclusion.

That time cost is where triage bites. In a calm round the doctor runs the x-ray and knows for certain. In a packed medbay there is no time to image everyone, so the doctor works off the stethoscope, the symptoms, and a hunch, and treats on inference. They might be right. They might not. The certainty exists, it just costs time the round may not give, and deciding whether to spend it is part of the job. The split is deliberate: structural reads like the x-ray are fairly definite once taken, while the soft signs, the stethoscope and the symptoms themselves, stay interpretive, so judgment lives in the cases that are genuinely uncertain rather than in guessing at an obvious break.

This keeps the medical roles honestly different. A paramedic in the field works off hands, ears, and symptoms and has to make a call. A doctor in medbay has the x-ray and the bloodwork to settle it. Neither is handed the answer for free, and a medic can be wrong or simply not know yet. That uncertainty is a feature: if diagnosis could never fail or stall, self-optimizers would route around medical entirely.

The examine and inspection window carries some of this too. Right now obvious, dramatic injuries get flat descriptions. "Third degree burns all over the body" is the same line whether it is a patch or a charred torso. Examine text should scale with severity: "the left shin is bent at an odd angle" for a clean break, up to "the shin bone is through the skin" for a worse one. The more an injury would be obvious to a bystander, the more obvious it should read. Like the hands-on tools, examine only exposes the external limb layer, never the hidden organ layer underneath.

### Treatment and Healing
Treatment is built from a small shared set of actions rather than one cure per condition.

The actions are generic: stop bleeding, disinfect, set, splint, close, drain, operate, rest. Different conditions call for different actions, in different combinations and orders. A punctured lung and a fractured arm play completely differently, but they are assembled from the same handful of verbs. The uniqueness comes from the patient's particular stack of conditions, not from a bespoke procedure built for every injury, and reading that stack correctly is what diagnosis is for. This keeps the system buildable while making each patient genuinely different.

Most conditions are not fixed by a procedure at all. They are supported while the body fixes itself. That mirrors real life, where the large majority of injuries heal on their own with rest and time while medicine mostly manages the symptoms. Treatment runs on an escalation ladder, and severity decides how far up it a condition forces you:

- **Support and recover.** The low end, and the most common. Diagnose it, manage the symptoms, let time do the work. A cracked rib or a minor cut needs the right read and some rest, not an operating table. The gameplay here is in the knowing, which is why diagnosis and triage carry this whole tier.
- **Hands-on procedures.** The middle. Stop the bleed, set the bone, close the wound, dress the burn, drain the fluid. Real manual field and clinic work, but nothing that requires opening the patient up.
- **Surgery.** The top, and only the top. Reserved for conditions the body cannot resolve alone or that sit somewhere unreachable without cutting, a bullet in the gut, a collapsed lung. Surgery is the deep end, reached only when nothing lighter will resolve a condition.

Because the actions gate each other, order matters. Close a wound before disinfecting it and you seal contamination in, which becomes an infection. Splint a bone before setting it and it knits crooked, leaving a lasting condition that has to be redone properly later. The deeper a stack of conditions, the less room there is to get the sequence wrong, so difficulty scales with severity on its own without needing a separate hard mode.

### Variable Treatment Paths
Most conditions support more than one approach, and the choice depends on severity, time pressure, and how slammed medbay is.

- **Minimal care** suppresses and stabilizes, then returns the patient to duty fast. The condition persists and may resurface later.
- **Maximal care** fully resolves the condition through proper treatment and heads off complications.

In a quiet round a doctor sets the bone properly. Mid-round with three gunshot patients waiting, the same doctor tourniquets, drugs, and sends the walking wounded back out, knowing some of them will be back worse. That trade is the point.

### Condition Progression and Complications
Untreated or minimally treated conditions worsen over time and can develop complications such as infection, organ damage, or shock. If you know you have a deep gash in your arm and you let it sit for a long time, it should escalate to the point where it is treatment or a serious risk of death. This rewards follow-up care and gives short-term fixes a real cost down the line.

Progression also governs repeated injury. You cannot "double break" an already broken leg. New damage of the same kind stacks the existing condition up to its next severity rather than creating a redundant second condition, and higher severity introduces secondary effects: heavier bleeding, nerve trauma, more shock, more strain on vital systems. Higher severity also raises the complexity of treatment, which feeds directly into the next section.

Some conditions spread. An infection is the clearest case: left untreated in a wound, it does not only deepen in place, it travels, into neighbouring parts and inward toward the organs. A shot to the leg that festers can carry an infection up the limb and into the organs of the torso, so a wound that was never near anything vital can end up threatening an organ if it is ignored long enough. This is the main way combat damage reaches an organ at all, since nothing in a fight targets an organ directly. A neglected wound simply gets there the long way. Spreading takes time and neglect, which makes it avoidable: treat the wound and it never gets the chance.

### Ambient-Induced Conditions
Not every condition comes from being hit. Ambient-induced conditions come from how a character lives and what they are exposed to rather than from a single blow: radiation, cold, bad air, smoke, drink, toxins, time. This is medbay's other job, the background caseload that exists when nobody is bleeding on the table, and it is where most of medical's work sits before anyone is seriously hurt.

These are ordinary conditions with the same three stages as everything else. They just enter the body a different way, and that difference matters: because the source is in the blood or the air rather than aimed at a part, ambient conditions are the main way an organ picks up a condition at all. You cannot target a liver, but you can poison one. Drink lands on the liver, bad air on the lungs, radiation across the body. The careless engineer patching breaches in a freezing section and the crew member drinking through their shift both earn something for it, which makes dangerous habits and dangerous work cost something, and it is strong roleplay fuel.

The three stages run the same low-to-high scale, with effects that depend on the condition:

- **Stage one** is symptoms and debuffs only. Nausea, vomiting, shakes, fatigue, whatever fits. Disruptive but not harmful in itself.
- **Stage two** is those effects plus real but capped harm, the condition starting to wear the body down without yet threatening it.
- **Stage three** is the severe end, where a fully neglected condition is at its most debilitating. Whether stage three can actually kill, or stops at failing-but-not-fatal, is left open as a balance decision for later.

The everyday loop lives in stages one and two, which keeps ambient conditions mostly a matter of debuffs and clinic visits, with stage three the price of ignoring one all round.

Treatment leans on real medicine more than combat injuries do. Where a break is mostly setting and time, an ambient condition is where actual cures live, the antibiotics and specific drugs that are the exception to "medicine only suppresses." You need the right meds to push one back down its stages, plus rest and time for the body to finish.

One boundary to be clear about: contagion, catching a condition from another character, stays out of scope here as event and virologist territory. Ambient conditions are self-inflicted and environmental, not something that passes between people. Spreading within a single body, an infection moving from a wound into an organ, is a different thing and is covered under progression.

### Pain and Symptoms
Pain is not just a status bar. It is a symptom in its own right, and it can produce further symptoms, which gives it a real place in the loop.

Take a limp. A limp is a symptom, never a condition, and it can be produced two ways. A painful leg injury can make a character limp because of the pain, and because that limp is pain-derived, it lifts the moment the pain is suppressed. A shot of adrenaline or a strong painkiller clears it on the spot, and it returns when the suppression wears off. That is a clean field play: a wounded operative dropping adrenaline to run on a bad leg, then seizing up again once it burns off.

A limp can also come from the underlying condition itself. A leg mangled badly enough limps because of the structural damage, not the pain, so no painkiller touches it. It stays until the condition is actually treated, if it can be. Same symptom, two different causes, and telling them apart is exactly the kind of thing diagnosis is for.

For communicating pain itself, the goal is to convey that the character hurts, keep it hard to forget, and not nag the player or pretend the player is their character. The approach is periodic low-friction feedback that scales with severity, a pop-up or examine state rather than a constant screen filter, and it is suppressible, which doubles as a gameplay hook. A player can buy quiet by taking the edge off, at the cost of hiding what is actually wrong.

### Improvised and Unlicensed Treatment
Real treatment should be possible outside a sterile operating theatre, it just should not be good.

A glass shard can stand in for a scalpel. Surgery can happen on a maintenance floor with the wrong tools and no anaesthetic. Unlicensed, improvised care is allowed and sometimes the only option an antagonist or a cut-off survivor has. But it carries higher risk: greater chance of infection, more bleeding, botched outcomes, and worse results than doing it properly with the right equipment and a trained hand. The harder a condition is to treat, the more an improvised attempt is likely to go wrong, which ties improvised care back to severity and keeps proper medical care worth seeking.

## Conditions

A starting list, not a final one, and names only. Stages, effects, numbers, and the exact parts each condition reaches are subject to change, and the balancing is for later.

Every condition has three stages, low to high, and the stage names are flavour where the condition has a natural progression and a plain stage one, two, three otherwise. Each condition is tagged by cause, combat-induced or ambient-induced, and by which parts it can appear on. Some spread. Symptoms (pain, coughing, dizziness, a limp) are a separate layer and are not listed here; these are the underlying conditions, not what the patient feels.

| Condition | Stages | Appears on | Cause | Spreads |
| --- | --- | --- | --- | --- |
| Broken bone | fracture, broken, shattered | parts with bone (limbs) | combat | no |
| Wound | cut, laceration, gash | external parts (limbs) | combat | no |
| Burn | first, second, third degree | external parts (limbs) | combat | no |
| Internal bleeding | three stages, names TBD | head and torso | combat | no |
| Infection | local, spreading, septic | almost any part | a neglected wound | yes |
| Alcohol poisoning | three stages, names TBD | liver | ambient (drink) | no |
| Radiation sickness | three stages, names TBD | body and organs | ambient (radiation) | no |
| Respiratory condition | three stages, names TBD | lungs | ambient (cold, bad air) | no |

The table above is the list of conditions, what each one is. The grids below are the other way round: which parts can carry which, at a glance.

**Limbs.** Any limb can be broken, cut, or burned. Only the head and torso, where the organs and major vessels sit, bleed internally. (A check means the condition can occur on that part; blank means it cannot.)

| Limb | Broken bone | Wound | Burn | Internal bleeding |
| --- | --- | --- | --- | --- |
| Head | ✓ | ✓ | ✓ | ✓ |
| Torso | ✓ | ✓ | ✓ | ✓ |
| Arms, hands, legs, and feet | ✓ | ✓ | ✓ | |

**Organs.** Organs are never hit directly, so they carry no combat conditions. They pick up conditions from ambient sources aimed at them, or from infection spreading inward. Most of the per-organ list is still open; what is settled so far:

| Organ | Conditions |
| --- | --- |
| Lungs | respiratory condition (ambient), infection (spread) |
| Liver | alcohol poisoning (ambient), infection (spread) |
| Brain, heart, kidneys, stomach, eyes, ears | infection (spread); their own conditions still open |

Infection can reach any part by spreading, and radiation sickness sits across the whole body rather than on a single part, so neither is tied to one row above.

This list will grow, and the per-organ conditions in particular are still open. Heavier, longer-arc conditions like cancer or genetic damage are candidates but raise bigger questions about origin and timescale, better settled once the basic loop is in. The appendix and the tongue have no condition worth giving them yet and are left out; appendicitis is a natural future fit for the appendix if a spontaneous internal condition layer gets built.

## Symptoms

Symptoms are what non-medical players actually feel, the layer they live in instead of conditions and numbers. They are deliberately imprecise: one symptom can point to several conditions, and that ambiguity is what diagnosis exists to resolve. A few examples to show the shape, not the whole set, since this grows as conditions do:

| Symptom | Could point to |
| --- | --- |
| Pain | almost anything: a wound, a broken bone, a burn |
| Limp | a leg wound, a broken leg, or just the pain from either |
| Coughing | a chest wound, a respiratory condition, smoke exposure |
| Coughing blood | internal bleeding, or a badly damaged lung |
| Dizziness | blood loss, failing circulation, poor oxygen, a head injury |
| Shortness of breath | a lung condition, oxygen trouble, a chest injury |
| Nausea | radiation sickness, alcohol poisoning, a stomach condition |
| Pale and clammy | blood loss or shock |

The more specific the symptom, the fewer things it points to. Pain is everywhere and tells a medic little on its own; coughing blood narrows the field fast. Reading which conditions a cluster of symptoms points to, then confirming with the right instrument, is the diagnostic loop.

## Crit, Incapacitation, and Death

Under a condition-based system, crit and death are outcomes of systemic failure, not standalone conditions. This proposal does not remove crit or dead states. It changes how injuries and illnesses contribute to reaching them.

### Vital vs Non-Vital Systems
Conditions divide broadly by the systems they affect.

- **Non-vital conditions** (broken bones, soft tissue injuries, localized burns) are generally not immediately lethal on their own.
- **Vital system conditions** (oxygen deprivation, cardiac failure, brain trauma, severe organ damage) directly threaten consciousness or life.

Conditions attach to specific parts, and each limb and organ tracks its own state rather than draining one shared health pool. Each vital organ governs a single thing: the heart drives circulation, the lungs oxygenation, the brain consciousness. That is where "vital" actually lives. Damage a vital organ enough and the thing it governs starts to fail, which is what pushes a character toward crit. Combat does not reach an organ directly, since a weapon hits a part and not the organ behind it, but severe damage to a limb can spread inward to the organs it houses, the same slow way a neglected wound spreads. That is the route by which a beating or an untreated injury can eventually threaten a vital organ, rather than a single hit doing it outright.

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

Antagonist healing works differently. Syndicate and other hostile tech does not need an in-fiction explanation. It is the other. The crew is not meant to understand how a piece of syndicate medical gear works, and that opacity is already the in-game reason crew are not supposed to rely on stolen syndi equipment. The same goes for the cult, which draws on powers its own members do not fully understand. These can stay unexplained without it being a gap in the design.

In broad strokes, what the tools themselves might be is worth sketching at a concept level, without pinning numbers or charges to anything.

- **Traitors** lean on single-use items from their uplink and on whatever crew care they can get or coerce. Think a stabilizer injector that drags someone out of crit, a combat stim that buries pain and keeps them upright through a fight, or a rarer one-shot item that actually closes a wound. The defining trait is that they run out, so each use is a real decision rather than a refillable habit.
- **Nukies** carry portable, reusable, expensive kit a station would never field, built to keep a strike team moving without a medbay behind them. A medical beam that stabilizes and suppresses an ally at range fits the role, something that keeps the squad pushing rather than curing anyone. Less a cure, more a way to stay mobile while hurt.
- **Cultists** heal through ritual rather than equipment, a rune or a channeled ability paid for in the cult's own currency of time, blood, or proximity to their structures, drawing on power they neither control fully nor are meant to understand.

There is one real design question buried in this, and it ties straight back to the asymmetry: do antagonist tools actually resolve conditions, or do they just suppress and stabilize better and more independently than crew field care can? Leaning toward the latter keeps the asymmetry intact. Antags stay mobile and dangerous but still carry the damage, while a few rare, expensive, deliberately unexplained items can genuinely resolve as the exception that proves the rule. That call is worth making deliberately, but it lives at the balance layer.

Whether NanoTrasen itself fields a restricted item of its own, something command-only or otherwise locked down, is left open. It might be needed, it might not.

Beyond that, this stays out of specifics. How strong these options are, how many uses they get, how available they should be, all of it is balance and out of scope. The design point is only this: the crew's medicine stays grounded, the other side is allowed to stay a mystery, and each side's tools should fit how that side actually plays.

## Worked Examples

### Field stabilization versus treatment

A security officer takes a bullet to the leg during a firefight.

- **The hit.** He gets a pop-up that his leg is badly hurt and bleeding, and he starts to slow. No numbers, no "you took 34 brute."
- **Field stabilization.** A squadmate slaps on a tourniquet and hits him with a painkiller. The bleeding stops, the pain drops, and he can run again. Nothing has been healed. The wound is still open under the tourniquet, and the bullet is still in there.
- **The choice.** He can keep fighting on borrowed time or pull back. He keeps fighting, because the threat is live.
- **Consequences mounting.** The painkiller wears off mid-fight. Pain returns, and with it a limp from the pain. He hits adrenaline to clear it and pushes through one more time.
- **Medbay, eventually.** Back in medical, an x-ray finds the retained bullet and the open wound speaks for itself. Proper treatment is surgery to remove the bullet, disinfection to head off the infection that was already starting, and the wound closed and dressed. That takes real time, which medbay may or may not have to spare.
- **If he never shows.** The wound progresses. The early infection becomes a real one. What was a clean surgical job becomes a serious, possibly limb-threatening problem, and the limp he kept suppressing turns out to be partly structural after all.

The same incident under the current system is a bandage and two chems at a bed, then back to duty in under a minute. The difference is the entire point.

### Treating a combination of conditions

An engineer is caught in a small explosion in atmospherics and makes it to medbay on their own, holding one arm against their chest. This walks through what treating them actually looks like.

- **What shows up.** The patient is in heavy pain, the left arm is bleeding and burned, and they cannot grip with that hand. No numbers appear anywhere. The patient, and anyone watching, sees symptoms rather than a diagnosis: pain, bleeding, an arm held wrong.
- **What is actually wrong.** The arm carries three separate conditions, each climbing its own ladder independently: a broken bone (bone family, middle tier), a third-degree burn (burn family, top tier), and a laceration (wound family, middle tier).
- **Diagnosis.** Everything here is external, on a limb, so this part is fast. A look and a hands-on check are enough, and no x-ray or bloodwork is needed because nothing is hidden inside an organ. For this patient, diagnosis is the easy part. The whole challenge is in the treatment, and specifically in which actions to apply and in what order.
- **Stabilization, which resolves nothing.** First pass is stopping the bleeding and managing the pain. Fast, field-available, doable by anyone with the kit. Afterward the arm is still broken, still burned, still cut open. The symptoms are quiet, the conditions remain. In an emergency this is where it stops until there is time for more.
- **Treatment, composed from the shared actions.** The combination forces a rough order, and the order is where it goes wrong. Clean before closing: disinfect the wound and the burned tissue first, because closing the laceration over contamination seals it in and produces an infection, and burned tissue is the most infection-prone part of the arm. Set before splinting: reduce the fracture back into place, because immobilizing it unset leaves an improperly-set bone that has to be re-broken and redone later. Then close the laceration now that it is clean, dress the burn, which at third-degree is the heavy version and not a quick salve, splint the set bone, and let it recover over real time.
- **Where the difficulty comes from.** None of those steps is a bespoke "burned, broken, lacerated arm" procedure sitting in a list. They are the same generic actions a single cut would use, just more of them, pulled together by this patient's particular stack of conditions. A lone cut is clean-and-close, done. This combination is the same vocabulary with far more ways to make it worse by acting out of order, and correct diagnosis is what tells you which actions the stack calls for.
- **The line with surgery.** Nothing here required opening the patient up, because every condition was reachable from outside. It is all hands-on field and clinic work. Surgery only enters when a condition sits somewhere unreachable without cutting, like a collapsed lung or a bullet lodged in the gut.

## Administrative & Server Rule Impact

This system does not add new rule categories, but it changes how some existing situations read, mostly by moving them out of the admin queue and into the round.

The key shift is that uncertainty is there by design, not by mistake. Because misdiagnosis, triage, and judgment calls are expected parts of how medical works, they stop being administrative problems and become in-character ones. Today, a body left unrevived reads as "this player walked past me and refuses to help," and it lands in ahelps. Under this system the same moment reads in-fiction: maybe the patient is past saving, maybe medbay is swamped and the doctor is working on someone more likely to pull through, maybe someone with better insurance is ahead in the queue. The drama stays in the world instead of escalating to staff.

- Medical negligence becomes contextual, since uncertainty and triage are expected rather than exceptional.
- Disputes over quality of care will still happen, but they are grounded in roleplay rather than mechanical failure, and resolved there most of the time.
- Self-diagnosis and instant recovery are mechanically limited, which reduces ambiguity around powergaming.

## Technical Considerations

- Numeric values stay in use internally to drive condition thresholds, severity, and progression.
- Conditions and health live per part. Each limb and organ tracks its own state rather than draining a shared pool, which is what lets one organ govern one parameter (heart to circulation, lungs to oxygenation, and so on).
- The parameter model should be built abstract from the start, so a species can differ in how a parameter is satisfied (a Vox needing nitrogen rather than oxygen, for instance) without rewriting the system. Actual species content stays out of scope, but the hooks for it should exist early.
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
- Contagion between characters: catching a condition from another person, outbreaks, and disease that passes from body to body. Spreading within a single body, an infection moving from a wound into an organ, is in scope and covered under progression. Person-to-person contagion is a separate, event-driven and virologist-facing system that needs its own document.
- The insurance, scrip, and cybernetics layer around treatment access and limb replacement.

## Open Questions

- How granular should conditions be at first implementation, and what is the minimum viable set to ship the loop?
- How punishing should treatment ordering be? Should skipping or misordering a step spawn a new condition like infection, or just slow recovery and worsen the outcome?
- How are complications like infection surfaced so they feel like a consequence rather than a surprise?
- How should pain feedback be tuned to stay present without becoming noise, and how does that interact with accessibility settings?
- Which revival consequences are interesting versus merely punishing, and where does the "far gone" threshold sit?
- How do combat-oriented antagonists keep functioning under gated self-resolution, and how is their healing access tuned so it preserves the asymmetry rather than bypassing it? Does NanoTrasen need a restricted option of its own?

---

This document focuses on player experience and design intent rather than exact balance values or implementation details. Those are expected to be iterated on during development.
