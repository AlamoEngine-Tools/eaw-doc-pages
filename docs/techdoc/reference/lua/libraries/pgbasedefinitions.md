---
title: PGBaseDefinitions.lua
tags:
  - LUA Library
  - FoC
---

# `PGBaseDefinitions.lua`

`PGBaseDefinitions.lua` is used by nearly every script in the game and introduces a wide array of generic variables that are used throughout the scripts.

## Direct imports

* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")

---

## Defined globals

These values are valid throughout every script. Changing them is not advised without a specific reason.

```lua tab="Bad Weight"
BAD_WEIGHT = -1000000000000000000.0
```

```lua tab="Big Float"
BIG_FLOAT = 1000000000000000000.0
```

```lua tab="Garbage Collection"
collectgarbage(256)
```

---

## Functions

---

### `function Common_Base_Definitions()`

This function declares the variables that are commonly used throughout scripts and sometimes referenced in evaluations. Usually variables are either initialised with `nil` or as empty tables. `Object`, `Target`, `AITarget`, `FreeStore`, `PlayerObject`, `LastService` and `Budget` are set by the engine for the script kinds that use them, after `Base_Definitions()` has run, so changing them is not advised. Clearing them keeps the next owner of a reused pooled state from inheriting the previous owner's values; see [Lifecycle of one script state](../lua-script-lifecycle.md#1-lifecycle-of-one-script-state).

??? note "Definitions"

    * `ThreadValue.Reset()`  
      Clears the values stored with `ThreadValue.Set(...)`. The store belongs to the script state and survives reuse of a pooled state, so without this call the next owner would see the previous owner's thread values.
    * `GetEvent.Reset()`  
      Clears the script's whole event queue, for all of its threads. Like the thread values, the queue survives reuse of a pooled state.
    * `TimerTable = {}`  
      Creates the table used to register timer events.
    * `DeathTable = {}`  
      Creates the table used to keep track of death events.
    * `ProxTable = {}`  
      Creates the table used to keep track of proximity events.
    * `AttackedTable = {}`  
      Creates the table used to keep track of attack events.
    * `CurrentEvent = nil`  
      Reference to the currently fired event.
    * `EventParams = nil`  
      Reference to the event's parameters.
    * `block = nil`  
      Reference to the current block object (a command result with `IsFinished()` and `Result()`) to block on.
    * `break_block = false`  
      Flag set by `BreakBlock()`; `BlockOnCommand(...)` returns early when it is `true`.
    * `YieldCount = 0`  
      Counter that `PumpEvents()` increments on every yield. The library only uses it in commented-out debug messages.
    * `AITarget = nil`  
      The current AI target. Set by the engine for AI plan scripts.
    * `Object = nil`  
      Reference to the object the script is attached to. Set by the engine for unit scripts.
    * `Target = nil`  
      Reference to the current target is usually stored here. Set by the engine for AI plan and evaluator scripts.
    * `FreeStore = nil`  
      Object free store. Generally used for AI. Set by the engine for free store scripts.
    * `PlayerObject = nil`  
      Reference to the current player object is usually stored here. Set by the engine for AI plan, free store and evaluator scripts.
    * `LastService = nil`  
      Game time of the script's last service, compared with `ServiceRate` by the engine ([service rule](../lua-script-lifecycle.md#31-unit-and-structure-scripts-lua_script-on-a-game-object-type)). By that rule, if a reused pooled state kept the previous owner's `LastService`, its next owner would not be serviced until the new game time passed that value.
    * `Budget = nil`  
      The AI budget of the plan. Set by the engine for AI plan scripts.
    * `enemy = nil`  
      Usually used to store the reference to the current enemy.
    * `taskforce = nil`  
      The current task force.
    * `tfObj = nil`

        !!! info "Unverified"
            Reference to the current taskforce object.

    * `stage = nil`  
      *[UNKNOWN]*
    * `UnitType = nil`  
      *[UNKNOWN]*
    * `invade_status = nil`  
      *[UNKNOWN]*
    * `path = nil`  
      *[UNKNOWN]*
    * `InvasionActive = false`  
      *[UNKNOWN]*
    * `unit = nil`  
      *[UNKNOWN]*
    * `hide_target = nil`  
      Reference to a nearby Nebula/Ion Storm/Asteroid field.
    * `healer = nil`  
      Reference to an object that can heal the unit.
    * `xfire_pos = nil`  
      *[UNKNOWN]*
    * `kite_pos = nil`  
      *[UNKNOWN]*
    * `friendly = nil`  
      Reference to the friendly player.
    * `block_table = {}`  
      The pending reinforcement requests of `ReinforceList(...)` (PGSpawnUnits) are stored here.
    * `lib_anti_idle_block = nil`

        !!! info "Unverified"
            Anti-idle actions for the AI are stored here.

---

### `function Base_Definitions()`

The base constructor for every script. It is called from `C++` and subsequently calls [`Common_Base_Definitions()`](#function-common_base_definitions "Common_Base_Definitions()") and `Definitions()` if present in the script.
The engine calls it when a script state is created and again, after `Flush_G()`, each time a pooled state is released, before the engine-set globals (`Object`, `PlayerObject`, `Target`, ...) are available, so `Definitions()` cannot use them; [Script setup](../lua-script-lifecycle.md#5-script-setup) gives the exact timing, including reuse and save games.

---

### `function Evaluator_Clean_Up()`

The engine calls this function by name for evaluator scripts. Cleans out the `Target` and `PlayerObject` references. Subsequently calls `Clean_Up()` if present in the script.

---

### `function UnitListIsObscured(unit_list)`

Tests whether the entire list of units is in an obscuring field, with obscuring fields being nebulae, asteroid fields and ion storms.

???+ notes "Params"

    * `table unit_list`: The list of ships to test.

???+ notes "Returns"

    * `bool`: `true` if the entire unit list is concealed, `false` else.

---

### `function Cull_Unit_List(unit_list)`

Removes all invalid references from a unit list and returns that list.

???+ notes "Params"

    * `table unit_list`: The list to clean.

???+ notes "Returns"

    * `table`: The cleaned unit list.
