# Paperwork

| Designers | Implemented | GitHub Links |
|---|---|---|
| SOP workgroup, written by scrambleking | :x: No | [Article 1](https://github.com/funky-station/docs/pull/108) |

## Overview

This PR focuses on the purpose and implementation of paperwork within the greater SOP workgroup rework.

## Background

Currently paperwork already plays a reasonably significant role on funky, whether its collecting copies of order forms as QM, IAA/NTR/Magistrate reports, Anomaly report documents, or the significant amount of paperwork that the HoP hands out every shift.

This document may use terms such as

XO Executive Officer (The paperwork half of HoP)

HD Hospitality Director (The Service half of HoP)

CL Corporate Liaison (Current Title for NTR)

## Features to be added

### Document Printers

Document Printers print pre-made standardised documents, preventing a need for every person who interacts with documents from having to download or create them separately.

These document printers should be stationed in specific areas such as HoP, the Library, and the Command Area.
Depending on their location the printers may have access to specific documents, such as the bridge having access to "command promotion" documents, or NDAs.

#### Fillable Form Fields

Fillable Form Fields are designated areas within "form" documents to be filled in that does not require searching through the often incomprehensible paper formatting code.

This will allow players to fill in Short Answers and Checkboxes for given questions with ease.

#### Command Stamps that flip

Provides a toggle on command stamps for a [Command X] [Command X Approved] and [Command X Denied] stamp variety.

### Reports

Reports are specifically for any "*unusual*" incidents of note. 
This can include an artifact exploding, an anomaly going critical, disease outbreaks, engines going critical or near critical, or other outstanding events.

**These reports would be filled *AFTER* the event occurs.**
It is not realistic to fill reports as they are happening, reasonable people would wait for the situation to calm down before writing them.

These are intended to keep command members on their toes about accidents occurring within their purview.
They will include the names of those held accountable, how they were held accountable, along with a general situation summary and the time of event occurrence.

### Permits

Provide permits for such exciting things as your required medications, uniform violations, construction and that juggernaut suit you "found"!

### Pre-Filled/"Scanner Print"

This category of documents are an expansion on the cargo request forms.
Additionally printouts from medical scanners, anomaly scanners, and artifact scanners will be made available where possible.

These will automatically be filled with the data from the scanner/other device that prints them.

These are intended to be used as reports of on-going activities on the station, and collected by their relevant head for filing.
This allows the departmental heads to keep track of the on-goings in their department, keeping a record for NT to review should something happen to the station (perish the thought).
Additionally for medical it provides an interaction vector for the dreaded *insurance RP* (Did you pay your premiums?).

### Legal/Contracts

This category includes everything from work contracts (Hiring/Firing), to NDAs, and even lawsuits.

### Other

This covers any paperwork that does not fit into other categories. Primarily this will be confronting paperwork that people wish to add, or commonly use, but are not required.
One such example of this is "request forms", allowing you to formally request something from a department such as a lathe print, or room construction.

### The Mime

The mime is granted leeway around forms due to writing being an oath violation, which would result in their firing. 
As such the relevant staff or command staff member will have to fill out required forms on their behalf.

## Game Design Rationale

While some Rationale is within the relevant documents, generally this is intended to create a more cohesive atmosphere.
Any large company such as NT would realistically have standardised forms for people to fill out, it means employees (and players) always know what they are going to be in for emphasising the themes.
Secondly these allow for smooth player integration into roles that already require paperwork without requiring out of game efforts.
Lastly this also removes the possibility of making "degenerate forms" which only serve to waste time and be confusing (wouldn't be me).

## Roundflow & Player interaction

During a regular round, paperwork is intended to act as a tool to emphasise what is "normal" for the station, providing a direct break from this normality in its suspension.

## Administrative & Server Rule Impact (if applicable)

This paperwork is expected to be treated the same as existing paperwork in the game.
While it may be taken into account for command compliance, it is not itself a reason to intervene.

# Technical Considerations

This PR only relies on the implementation of Document Printers. 
It does however greatly benefit from "Fillable Form Fields" as mentioned above.
Likewise, but to a lesser degree, "Command Stamps that flip" would provide more functionality for command personnel to interact with the paperwork.
