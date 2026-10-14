---
title: PGAICommands.lua
tags:
  - LUA Library
  - FoC
---

# `PGAICommands.lua`

## Direct imports

* [`PGCommands.lua`](pgcommands.md "PGCommands.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Functions

---

### `function Base_Definitions()`

Declares several AI related variables and calls additional setup functionality. Replaces the `Base_Definitions()` of `PGBaseDefinitions.lua`. In order it sets `InSpaceConflict`, `MagicPlan`, `MinContrastScale`, `MaxContrastScale`, `PerFailureContrastAdjust` and the contrast tables, calls `Common_Base_Definitions()`, sets every global named in the plan's `TaskForce` table to `nil`, calls [`Set_Contrast_Values()`](#function-set_contrast_values "Set_Contrast_Values()") only while the engine is loading the plan definition (the global `PlanDefinitionLoad` is set), clears `PlanDefinitionLoad`, and finally calls `Definitions()` if present.

---

### `function Set_Contrast_Values()`

Sets the AI contrast value by category types. A change to the game's categories or to how categories affect each other requires a matching update of this function.
The contrast describes how a unit of a given category approaches units of other categories, and how many objects of a given category the AI should bring along to encounter an object of a given category.
The weights differ between the EaW and FoC copies of the library for the enemy categories `Corvette`, `Frigate` and `Capital`.

---
