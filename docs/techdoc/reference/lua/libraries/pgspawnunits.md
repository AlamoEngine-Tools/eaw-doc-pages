---
title: PGSpawnUnits.lua
tags:
  - LUA Library
  - FoC
---

# `PGSpawnUnits.lua`

## Direct Imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

---

### `function Process_Reinforcements()`

Processes all reinforcements received. Do not call by hand.

---

### `function Add_Reinforcement(object_type, player)`

Adds a given object to the player's reinforcement pool.

???+ notes "Params"
    
    * `GameObjectType object_type`: The object type to reinforce.
    * `PlayerObject player`: The player to reinforce.

---

### `function ReinforceList(type_list, entry_marker, player, allow_ai_usage, delete_after_scenario, ignore_reinforcement_rules, callback)`

Adds a list of reinforcements to a given player's reinforcement pool.

???+ notes "Params"
    
    * `table<GameObjectType> type_list`: The list of reinforcement unit types to provide.
    * `LocationObject entry_marker`: The position to spawn the reinforcements at.
    * `PlayerObject player`: The player to reinforce.
    * `bool allow_ai_usage`: Is the AI allowed to use the reinforcements?
    * `bool delete_after_scenario`: If `true` the player may keep the reinforcements, else they will only available during the scenario.
    * `bool ignore_reinforcement_rules`: Should the reinforcements adhere to the reinforcement rules, or should they be spawned no matter what?
    * `[optional] function callback`: A function to call once the `ReinforceList(...)` has finished.

---

### `function SpawnList(type_list, entry_marker, player, allow_ai_usage, delete_after_scenario)`

Spawns a given list of units simultaneously.

???+ notes "Params"
    
    * `table<GameObjectType> type_list`: The list of reinforcement unit types to provide.
    * `LocationObject entry_marker`: The position to spawn the reinforcements at.
    * `PlayerObject player`: The player to reinforce.
    * `bool allow_ai_usage`: Is the AI allowed to use the reinforcements?
    * `bool delete_after_scenario`: If `true` the player may keep the reinforcements, else they will only available during the scenario.
