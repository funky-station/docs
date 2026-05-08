


# Station Protocol Rework / Nanotrasen Colonial Law and Procedure
| Designers | Implemented | GitHub Links |
|---|---|---|
| SOP Workgroup | :x: | TBD |

Leader: Catty
Members: Joaco545, Alicios, Scrambledking, Gamercodeleo1/funkycmm, Goobie (and many other that I need to read chat to get)
Many thanks to the Admin team and Tay for pitching in

## Overview

A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds".

## Background

Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.

## Features to be added

Add a series of books and gudebook entries under the name of Nanotrasen Colonial Law and Procedure

Nanotrasen Colonial Law and Procedure is split into 5 parts, called articles:
### Article 1 - Station Regulations
Covers general station behaviour: Alert levels, Permits, Paperwork, Hiring, Promotions and more

*[Design Document: Article 1 - Station Regulations](./station_protocol_rework/article-1_design_doc.md)*
*[Article 1 - Station Regulations](./station_protocol_rework/Article%201%20-%20Station Regulations.md)*
### Article 2 - Corporate law
To better realize the idea of NT's opression, Space Law has been re-written, expanded, and rebranded as Corporate Law.

*[Design Document: Article 2 - Corporate Law](./station_protocol_rework/article-2_design_doc.md)*
*[Article 2 - Corporate Law](./station_protocol_rework/Article%202%20-%20Corporate%20Law.md)*
### Article 3 - Standard Operating Procedure
SOP has to be overhauled to better fit the themes and expectations of Funky Station. All SOP is to receive a rewrite and new guiding principals.

*[Design Document: Article 3 - Standard Operating Prodedure](./station_protocol_rework/article-3_design_doc.md)*
*[Article 3 - Standard Operating Procedure](./station_protocol_rework/Article%203%20-%20Standard%20Operating%20Procedure.md)*
### Article 4 - Unions

*[Design Document: Article 4 - Unions](./station_protocol_rework/article-4_design_doc.md)*
*[Article 4 - Unions](./station_protocol_rework/Article%204%20-%20Unions.md)*
### Article 5 - Trials and Hearings

*[Design Document: Article 5 - Trials and Hearings](./station_protocol_rework/article-5_design_doc.md)*
*[Article 5 - Trials and Hearings](./station_protocol_rework/Article%205%20-%20Sentencing,%20Trials,%20and%20Hearings.md)*


### Extra considerations
"Behavior follows incentives"
While this PR focuses only on the regulations themselves, many supporting changes will need to be done to mechanically enforce the new vision Funky Station has.
The SOP workgroup is working on other design docs that should help change that situation and align mechanics with the text and intent behind them.

## Game Design Rationale

Consider addressing:
- How does the feature align with our [Core Design Principles](../design/design-principles.md) and game philosphy?

Mention:
New Theming
Escalation Oportunities by non antags, and more options for antags
Seriously Silly (clown exemption :godo:)
Autenticity increased with:
- The use of some legaleese
- More atuned to the theme and NT's opression
Take things slow (point at trials)
Maximixing RP Potential is all over the place in this doc
Dynamic Environment respected, as it all depends on where players want to take this

## Roundflow & Player interaction

All of the changes done here will affect every shift. The players will have to interact with all the changes proposed here as SOP, Corporate Law, Trials, and Unions will permiate every round on Forky.
While how much each individual part affects each round varies, it all depends on the players roleplaying to see the direction the round will take.
Mechanically speaking Sec, IAAs, and Department Heads will be the ones enforcing the changes proposed here, as they have the power to enact IC punishment on the people who break SOP or Corpo Law.

## Administrative & Server Rule Impact (if applicable)

We expect the workload for the admins to increase for a bit while the players get used to the new changes, but it should go back to baseload after that
Most things done here are expected to be broken by players with a "play your character" mindset. The proposed changes add more ways for escalation to happen, and that may cause some OOC player friction, but we trust Funky Station players are mature enough to interact with this and enjoy the storylines formed on a round


## Technical Considerations

Check each individual PR to see the technical considerations.
95% of the changes proposed here are YAML or FTL/Text changes
