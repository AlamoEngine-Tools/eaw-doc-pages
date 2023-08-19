---
title: PGAICommands.lua
tags:
  - LUA Library
  - FoC
---

# `PGAICommands.lua`

## Direct Imports

* [`PGCommands.lua`](pgcommands.md "PGCommands.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Functions

---

### `function Base_Definitions()`

Declares several AI related variables and calls additional setup functionality.

---

### `function Set_Contrast_Values()`

Sets the AI contrast value by category types. If you change the game categories or change how categories affect each other, this function has to be updated accordingly.
The contrast describes how a unit of a given category approaches units of other categories, and how many objects of a given category the AI should bring along to encounter an object of a given category.

---
