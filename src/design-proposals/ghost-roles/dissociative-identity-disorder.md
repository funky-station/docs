
# Dissociative identity disorder
| Designers | Implemented | GitHub Links |
|---|---|---|
| vectorassembly | :warning: Partially | TBD |


## Overview

This adds a new ghostrole which is something that can be described as Dissociative identity disorder (DID).

## Background

None

## Features to be added

This PR will add a new character quirk which can be toggled on, the said quirk can be also automatically added to a character who has suffered a severe head trauma.
Players can also write a brief explanation of their character's behavior as a hint for the ghost player.

## Game Design Rationale

This ghost role exists on some Space Station 13 servers and can lead to some fun roleplay scenarios, loosing control over yourself and doing things you don't want, etc.

## Roundflow & Player interaction

DID can be toggled roundstart as a character quirk, as well as be a result of a head trauma.
Whenever the ghost role is taken, original player (Personal 1) will receive a notification, after this, the ghost (Persona 2) can take control over Persona 1 at will (after a certain cooldown of course), upon doing so, Personality 1 can regain control back after a cooldown or let their second personality do whatever they want until the click the specific action.

To avoid confusion, some flavor text could be added to a character who is under P2 control.

P1 and P2 can also communicate between each other at all times their own "Headspace" chat channel which cannot be seen by anyone else.

## Administrative & Server Rule Impact (if applicable)
As obvious as it is, this feature introduces a grief vector (like any other ghostrole), to make things smoother, players are encouraged to make some sort of a brief character explanation (which may be added into the character customization menu) to let P2 know how they should (or at least try to) play them, slight deviation is welcome. 

# Technical Considerations
This feature should not affect performance.
A new text field in the customization menu which explains character behavior might be needed, (could be a multiline text edit in the antag tab?)
