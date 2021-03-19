---
title: 3DS Max 6, 8 and 9
tags:
  - Tool
  - Official
  - EaW Compatible
  - FoC Compatible
  - Outdated
  - Superseded
---

# 3DS Max 6, 8 and 9

!!! warning "Tool severly outdated, use Blender instead!"

## About

Autodesk 3DS Max is a 3D modelling program originally used to create 3D assets for Empire at War and Forces of Corruption.
Since Empire at War and Forces of Corruption released in 2005, the only compatible 3DS Max versions are version 8 and 9.

The is an ALO-importer and ALO-exporter available that supports EaW's and FoC's animation formats.

!!! danger "Acquiring 3DS Max"
    3DS Max 8 and 9 are no longer sold by Autodesk, the only way to acquire them is through third-party vendors and second-hand.  
    Make sure that the third-party vendor you buy either a Disk Version (3DS Max 8/9 were often included with course books) or a key from can be trusted.

## Prerequisites

To ensure that the exporter works properly, please make ensure the following prerequisites are met before installing and using the exporter:

- If you're using 3ds Max 6, install Service Pack 1  
  If you've already installed SP1, it should say so in the window title when 3ds Max is started.
- If you're using 3ds Max 8, install Service Pack 3  
  If you've already installed SP3, it should say so in the window title when 3ds Max is started.
- If you're using 3ds Max 9, install Service Pack 2  
  If you've already installed SP2, it should say so in the window title when 3ds Max is started.

## Known Issues

Due to the age and severe lack of support there are several known problems which are listed below.

### Key Invalidation

Windows updates tend to cause 3DS Max registry problems, where the program needs a new activation code, which it then won't accept.  
To fix this, search for a `.dat` file in (C:\ProgramData\Autodesk\Software Licenses) that holds the licenses for 3DS Max 8/9, then delete the file.  
Doing this allows you to reenter your activation code.

### UI "Shadows" Stuck on Viewport

The use of the right-click context menu may leave the shape of the UI-Element stuck on the viewport effectively blocking it. The more ofthen you use the menu the less you can see the viewport.  
There are two ways to remedy this - a temporary fix that works reliably but needs to be reapplied every so often and a fix that doesn't work for all users but fixes the issue permanently if it does work.

- **Temporary workaround:** Click on the little part tot he far rifght of the taskbar to focus on the empty windows desktop, then ckick again to bring 3DS Max 8/9 back into focus. This should remove all stuck UI shadows.
- **Possible permanent fix:** Copy the 3DS Max executable next to the original executable and start 3DS Max fromt hat copy instead.
