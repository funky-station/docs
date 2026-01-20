# Condition-Based Medical System

| Designers | Implemented | GitHub Links |
| --- | --- | --- |
| Ven | :x: No | TBD |

## Overview

This proposal outlines a shift from numeric, damage-type-driven medical gameplay to a condition-based medical system. Instead of players interacting with abstract values (e.g., brute, burn, toxin), injuries and illnesses manifest as diagnosable conditions with symptoms, uncertainty, and varying severities. The goal is to make medical care feel intuitive, serious, and roleplay-forward while preserving mechanical depth under the hood.

## Background

Medical gameplay on Funky Station currently inherits a largely number-driven model. Players take damage, receive treatment that reduces numbers, and quickly return to duty. While functional, this model incentivizes risk-taking and devalues medical care as a meaningful part of the round. Medbay is easy to access, treatment is fast and deterministic, and non-medical players often understand their condition purely in terms of optimization rather than in-character health.

Recent discussion within the medical workgroup converged on an alternative approach: abstracting the information available to non-medical players while giving medical staff diagnostic authority. A crew member experiences symptoms ("my arm hurts," "I can’t stop coughing"), while trained medical staff determine whether that symptom corresponds to a sprain, fracture, infection, or other condition. Internally, numbers still exist to drive outcomes, but they are no longer the primary player-facing interface.

## Features to be Added

### Condition-Based Injury and Illness Representation
Player-facing medical states are represented as discrete conditions (e.g., broken arm, concussion, pneumonia) rather than numeric damage values. Conditions have severities, progression states, and potential complications, but these are abstracted away from non-medical players.

### Symptom-Driven Feedback
Non-medical players receive experiential feedback (pain, impaired movement, coughing, dizziness) instead of explicit diagnoses or numbers. This feedback is intentionally imprecise and may correspond to multiple possible conditions.

### Diagnostic Medical Gameplay
Medical staff gain the ability to examine patients, use tools, and apply training to determine the underlying condition. Diagnosis is a core gameplay loop rather than an automatic or instant reveal.

### Variable Treatment Paths
Most conditions support multiple treatment approaches:
- **Minimal care** to stabilize and return a patient to duty quickly
- **Maximal care** to fully resolve the condition and prevent complications

The choice of treatment depends on severity, time pressure, and Medbay workload.

### Condition Progression and Complications
Untreated or minimally treated conditions may worsen over time or develop complications (e.g., infection, organ damage), encouraging follow-up care and long-term consequences.

## Crit, Incapacitation, and Death

Under a condition-based medical system, **crit and death are outcomes of systemic failure**, not standalone conditions themselves. This proposal does not remove crit/dead states, it changes how injuries and illnesses contribute to reaching them.

### Vital vs Non-Vital Systems

Conditions can broadly be categorized by the systems they affect:

- **Non-vital conditions** (e.g., broken bones, soft tissue injuries, localized burns) are generally not immediately lethal on their own.
- **Vital system conditions** (e.g., oxygen deprivation, cardiac failure, brain trauma, severe organ damage) directly threaten a character’s ability to remain conscious or alive.

Non-vital conditions may indirectly contribute to crit or death over time through mechanisms such as blood loss, shock, pain, infection, or reduced mobility.

### Crit

Crit represents a state where one or more vital systems can no longer maintain normal function (for example: loss of consciousness, respiratory failure, cardiac arrest, or extreme shock). A character in crit is alive but systemically unstable, and requires intervention to prevent death.

### Death

Death occurs when vital system failure becomes irreversible. This may be caused by untreated cascading conditions, catastrophic organ damage, prolonged hypoxia, or other failures that exceed the body’s ability to recover.

### Repeated or Overlapping Injuries

When damage is applied to an already-injured body part, it does not create redundant conditions (e.g., “double-breaking” a bone). Instead, it worsens the existing condition or introduces secondary effects such as increased bleeding, tissue damage, nerve trauma, or heightened shock risk, placing additional strain on vital systems.

Internally, numeric values are still used to evaluate thresholds and progression, but these are abstracted away from the player-facing experience.

## Game Design Rationale

This system directly supports Funky Station’s core design principles:

- **Maintaining Authenticity**: Injuries feel grounded and understandable without relying on real-world medical simulation. Players interact with believable outcomes rather than abstract math.
- **Taking Things Slow**: Medical care and recovery scale naturally with Funky Station’s long round lengths, discouraging reckless behavior and instant resets.
- **Maximizing Roleplay Potential**: Diagnosis, triage, and uncertainty create organic interaction between patients and medical staff.
- **Avoiding QOL Slop**: By removing explicit numbers from the player-facing layer, the system discourages hyper-optimization and encourages judgment-based play.

Internally, numeric systems still exist to ensure balance, predictability, and tunability. The change is not the removal of numbers, but the removal of numbers as the primary way players understand their health.


## Roundflow & Player Interaction

This system is active every round and integrates naturally with existing sources of injury, illness, and antagonistic activity.

### Early Round
Minor injuries and early symptoms introduce uncertainty without immediately removing players from play. Crew may choose to ignore symptoms or seek early diagnosis.

### Mid to Late Round
As injuries accumulate and Medbay becomes busier, medical staff are pressured to triage and apply minimal care where appropriate. Some conditions may be deferred, leading to later complications or return visits.

### Intended Player Interaction
- Non-medical players should feel encouraged to seek medical help without fully understanding their condition.
- Medical players should be making judgment calls under time pressure rather than following a single optimal treatment path.
- Players should not be able to fully diagnose or optimize their treatment without medical involvement.

These interactions are mechanically enforced through information asymmetry and diagnostic requirements.


## Administrative & Server Rule Impact (if applicable)

This system does not introduce new rule categories but may change how existing situations are interpreted.

- Medical negligence becomes more contextual, as uncertainty and triage are expected parts of gameplay.
- Disputes may arise over quality of care, but these are grounded in roleplay rather than mechanical failure.
- The system mechanically limits self-diagnosis and instant recovery, reducing ambiguity around powergaming.


# Technical Considerations

- Numeric values remain in use internally to drive condition thresholds, severity, and progression.
- Existing damage types can be refactored to contribute to condition generation rather than direct player feedback.
- New or updated UI elements are required to present descriptive symptoms and diagnostic results.
- Performance impact is expected to be minimal, as conditions largely reuse existing damage and status systems.




## Open Questions

- How granular should conditions be at initial implementation?
- What diagnostic tools are required for medical staff?
- How are complications (e.g., infection) surfaced to players?
- How does this system interact with cybernetics and long-term injuries?

---

This document intentionally focuses on player experience and design intent rather than exact balance values or implementation details. Those are expected to be iterated on during development.

