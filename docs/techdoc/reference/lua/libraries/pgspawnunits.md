---
title: PGSpawnUnits.lua
tags:
  - LUA Library
  - FoC
---

# `PGSpawnUnits.lua`

## Direct imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

---

### `function Process_Reinforcements()`

Processes all reinforcements received. Do not call it manually. It is called by `Pump_Service()` (PGCommands), i.e. on every `PumpEvents()`, and issues the pending `Reinforce_Unit(...)` commands queued by `ReinforceList(...)`. A script that does not pump events never gets its `ReinforceList(...)` units.

---

### `function Add_Reinforcement(object_type, player)`

Adds a given object to the player's reinforcement pool.

???+ notes "Params"
    
    * `GameObjectType object_type`: The object type to reinforce. A type name (string) is accepted too and converted with `Find_Object_Type(...)`.
    * `PlayerObject player`: The player to reinforce.

---

### `function ReinforceList(type_list, entry_marker, player, allow_ai_usage, delete_after_scenario, ignore_reinforcement_rules, callback)`

Adds a list of reinforcements to a given player's reinforcement pool.
The function only queues the requests and returns at once; [`Process_Reinforcements()`](#function-process_reinforcements "Process_Reinforcements()") issues one `Reinforce_Unit(...)` per type on the following `PumpEvents()` calls and collects the arriving units.

???+ notes "Params"
    
    * `table<string> type_list`: The list of reinforcement unit type names to provide (each is passed to `Find_Object_Type(...)`).
    * `LocationObject entry_marker`: The position to spawn the reinforcements at.
    * `PlayerObject player`: The player to reinforce. Required; with `nil` the function shows a message box and returns.
    * `bool allow_ai_usage`: Whether the AI may use the reinforcements. If `true`, `Prevent_AI_Usage(false)` is called on each arriving unit.
    * `bool delete_after_scenario`: If `true`, `Mark_Parent_Mode_Object_For_Death()` is called on each arriving unit, so the player does not keep it after the scenario; if `false`, the player may keep the reinforcements.
    * `bool ignore_reinforcement_rules`: Whether the reinforcements ignore the reinforcement rules and are spawned regardless. Passed to `Reinforce_Unit(...)` inverted, as its last (obey zones) argument.
    * `[optional] function callback`: A function to call once the `ReinforceList(...)` has finished. It receives the list of arrived units.

---

### `function SpawnList(type_list, entry_marker, player, allow_ai_usage, delete_after_scenario)`

Spawns a given list of units simultaneously with `Spawn_Unit(...)` and returns the list of all spawned units.

???+ notes "Params"
    
    * `table<string> type_list`: The list of unit type names to spawn (each is passed to `Find_Object_Type(...)`).
    * `LocationObject entry_marker`: The position to spawn the reinforcements at.
    * `PlayerObject player`: The player to reinforce.
    * `bool allow_ai_usage`: Whether the AI may use the spawned units. `Prevent_AI_Usage(...)` is called on every spawned unit either way: with `false` when `allow_ai_usage` is `true`, with `true` otherwise.
    * `bool delete_after_scenario`: If `true`, `Mark_Parent_Mode_Object_For_Death()` is called on each spawned unit, so the player does not keep it after the scenario; if `false`, the player may keep the units.

???+ notes "Returns"

    * `table<GameObject>`: All spawned units.
