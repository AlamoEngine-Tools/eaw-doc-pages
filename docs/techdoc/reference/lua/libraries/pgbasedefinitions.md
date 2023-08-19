---
title: PGBaseDefinitions.lua
tags:
  - LUA Library
  - FoC
---

# `PGBaseDefinitions.lua`

`PGBaseDefinitions.lua` is called by pretty much every script in the game and introduces a wide array of generic variables that are being used throughout the scripts.

## Direct Imports

* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")

---

## Defined Globals

These values are valid throughout every script. It is advised to not change them unless you know exactly what you are doing.

```lua tab="Bad Weight"
BAD_WEIGHT = -1000000000000000000.0
```

```lua tab="Big FLoat"
BIG_FLOAT = 1000000000000000000.0
```

```lua tab="Garbage Collection"
collectgarbage(256)
```

---

## Functions

---

### `function Common_Base_Definitions()`

This function declares the variables that are commonly used throughout scripts and sometimes referenced in evaluations. Usually variables are either initialised with `nil` or as empty tables. Some of the values seem to be initialised from `C++` so changing them is not advised.

??? Note "Definitions"

    * `ThreadValue.Reset()`  
      Resets any set thread values for the given thread.
    * `GetEvent.Reset()`  
      Clears all events that might have fired for the given thread.
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
      Reference to the event's parameters
    * `block = nil`  
      Reference to the current function to block on.
    * `break_block = false`  
      Reference to the function to evaluate for premature block breaks.
    * `YieldCount = 0`  
      *[UNKNOWN]*: Presumably the amount of times the coroutine had to yield, but the purpose isn't clear.
    * `AITarget = nil`  
      The current AI target.
    * `Object = nil`  
      Reference to the object the script is attached to.
    * `Target = nil`  
      Reference to the current target is usually stored here.
    * `FreeStore = nil`  
      Object free store. Generally used for AI.
    * `PlayerObject = nil`  
      Reference to the current player object is usually stored here.
    * `LastService = nil`  
      *[UNKNOWN]* Presumably the timestamp of the last service.
    * `Budget = nil`  
      *[UNKNOWN]* Presumably the reference to the current AI budget.
    * `enemy = nil`  
      Usually used to store the reference to the current enemy.
    * `taskforce = nil`  
      The current task force.
    * `tfObj = nil`  
      *[UNKNOWN]* Presumably the reference to the current taskforce object.
    * `stage = nil`  
      *[UNKNOWN]*
    * `UnitType = nil`  
      *[UNKNOWN]*
    * `invade_status = nil`  
      *[UNKNOWN]*
    * `path = nil`  
      *[UNKOWN]*
    * `InvasionActive = false`  
      *[UNKOWN]*
    * `unit = nil`  
      *[UNKOWN]*
    * `hide_target = nil`  
      Reference to a nearby Nebula/Ion Storm/Asteroid field.
    * `healer = nil`  
      Reference to an object that can heal the unit.
    * `xfire_pos = nil`  
      *[UNKOWN]*
    * `kite_pos = nil`  
      *[UNKOWN]*
    * `friendly = nil`  
      Reference to the friendly player.
    * `block_table = {}`  
      The current block data is stored here.
    * `lib_anti_idle_block = nil`  
      *[UNKOWN]* Presumably anti-idle actions for the AI are stored here.

---

### `function Base_Definitions()`

The base constructor for every script object. It is called from `C++` and subsequently calls [`Common_Base_Definitions()`](#function-common_base_definitions "Common_Base_Definitions()") and [`Definitions()`]("Definitions") if present in the script object.

---

### `function Evaluator_Clean_Up()`

Cleans out the `Target` and `PlayerObject` references. Subsequently calls [`Clean_Up()`]("Clean_Up()") if present in the script object.

---

### `function UnitListIsObscured(unit_list)`

Tests whether the the entire list of units is in a obscuring field, with obscuring fields being nebulae, asteroid fields and ion storms.

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
