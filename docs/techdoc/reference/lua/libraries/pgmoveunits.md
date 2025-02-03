---
title: PGMoveUnits.lua
tags:
  - LUA Library
  - FoC
---

# `PGMoveUnits.lua`

## Direct Imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

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
