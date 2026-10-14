---
title: 3DS Max 6, 8 and 9
tags:
  - Tool
  - Official
  - EaW Compatible
  - FoC Compatible
  - Outdated
---

# 3DS Max 6, 8 and 9

!!! warning "Tool severely outdated, use Blender instead"

## About

Autodesk 3DS Max is a 3D modelling program originally used to create 3D assets for Empire at War and Forces of Corruption.
Since Empire at War and Forces of Corruption were released in 2006, the only compatible 3DS Max versions are versions 6, 8 and 9.

There is an ALO-importer and ALO-exporter available that supports EaW's and FoC's animation formats.

!!! danger "Acquiring 3DS Max"
    3DS Max 6, 8 and 9 are no longer sold by Autodesk, the only way to acquire them is through third-party vendors and second-hand.  
    Make sure that the third-party vendor of a disk version (3DS Max 8/9 were often included with course books) or of a key can be trusted.

## Prerequisites

The exporter works properly only when the following prerequisites are met before it is installed and used:

- 3DS Max 6: install Service Pack 1  
  An installed SP1 is shown in the window title when 3DS Max is started.
- 3DS Max 8: install Service Pack 3  
  An installed SP3 is shown in the window title when 3DS Max is started.
- 3DS Max 9: install Service Pack 2  
  An installed SP2 is shown in the window title when 3DS Max is started.

## Known issues

Due to the age and severe lack of support there are several known problems, listed below.

### Key invalidation

Windows updates tend to cause 3DS Max registry problems, where the program needs a new activation code, which it then does not accept.  
To fix this, search for a `.dat` file in (C:\ProgramData\Autodesk\Software Licenses) that holds the licenses for 3DS Max 8/9, then delete the file.  
This allows the activation code to be entered again.

### UI "shadows" stuck on viewport

The use of the right-click context menu may leave the shape of the UI element stuck on the viewport, effectively blocking it. The more often the menu is used, the less of the viewport is visible.  
There are two ways to remedy this - a temporary fix that works reliably but needs to be reapplied every so often and a fix that doesn't work for all users but fixes the issue permanently if it does work.

- **Temporary workaround:** Click on the little part to the far right of the taskbar to focus on the empty Windows desktop, then click again to bring 3DS Max 8/9 back into focus. This should remove all stuck UI shadows.
- **Possible permanent fix:** Copy the 3DS Max executable next to the original executable and start 3DS Max from that copy instead.
