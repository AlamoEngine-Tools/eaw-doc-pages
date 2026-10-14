---
title: PGMoveUnits.lua
tags:
  - LUA Library
  - FoC
---

# `PGMoveUnits.lua`

## Direct imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

All four functions accept either a table of units or a single object (for example a fleet or a task force) as `unit_list`. A table is first passed to `Cull_Unit_List(...)`, which removes invalid units from the caller's table; an empty table returns at once without blocking. The blocking is done with `BlockOnCommand(...)` (PGBase).

---

### `function Formation_Move(unit_list, target)`

This will move an entire unit list with simultaneous orders.  
They will block as a whole and pass when the last unit's move is complete.

???+ notes "Params"

    * `table unit_list`: The list of units.
    * `LocationObject target`: The movement target location.

---

### `function Formation_Attack(unit_list, target)`

This will order an entire unit list to attack a target simultaneously.  
They will block as a whole and pass when the last unit's attack is complete.  
When `unit_list` is a single object rather than a table, the function issues `Attack_Move(target)` instead of an attack order.

???+ notes "Params"

    * `table unit_list`: The list of units.
    * `GameObject target`: The attack target.

---

### `function Formation_Attack_Move(unit_list, target)`

This will order an entire unit list to perform an attack move towards a target location simultaneously.  
They will block as a whole and pass when the last unit's move is complete.

???+ notes "Params"

    * `table unit_list`: The list of units.
    * `LocationObject target`: The movement target location.

---

### `function Formation_Guard(unit_list, target)`

This will order an entire unit list to guard a target location.  
They will block as a whole and pass when the last unit's guard move is complete.

???+ notes "Params"

    * `table unit_list`: The list of units.
    * `GameObject target`: The target to defend.
