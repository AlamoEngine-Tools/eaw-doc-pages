---
title: PGCommands.lua
tags:
  - LUA Library
  - FoC
---

# `PGCommands.lua`

## Direct imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

---

### `function ProduceForce(taskforce)`

!!! error "Deprecated"
    The function is commented out in both the EaW and the FoC copy of the library and is therefore not defined. Calling it raises a Lua error.

Produces a taskforce.

???+ notes "Params"

    * `object taskforce`: The taskforce to produce.

---

### `function ProduceObject(player, objecttype, where)`

!!! error "Deprecated"
    The function is commented out in both the EaW and the FoC copy of the library and is therefore not defined. Calling it raises a Lua error. The engine command it wrapped, `_ProduceObject(player, object_type, object)`, is still registered.

Starts the production of an object.

???+ notes "Params"

    * `PlayerObject player`: The player to produce the object for.
    * `GameObjectType objecttype`: The type of the object to produce.
    * `PGameObject where`: The facility to produce the object.

???+ notes "Returns"

    * `GameObject`: The produced object.

---

### `function WaitProduceObject(objecttype, where)`

!!! error "Deprecated"
    The function is commented out in both the EaW and the FoC copy of the library and is therefore not defined. Calling it raises a Lua error.

Waits for the object to be produced.

???+ notes "Params"

    * `GameObjectType objecttype`: The type of the object to produce.
    * `PGameObject where`: The facility to produce the object.

???+ notes "Returns"

    * `GameObject`: The produced object.

---

### `function WaitForever()`

Waits forever.

---

### `function Register_Timer(func, timeout, param)`

Registers a function for delayed execution. The function is called once, as `func(param)`, from the first [`PumpEvents()`](pgbase.md#function-pumpevents "PGBase.PumpEvents()") after `timeout` seconds of game time have passed. The same function can be registered several times; each registration fires once.

???+ notes "Params"

    * `function func`: The function to execute.
    * `number timeout`: The time in seconds to wait.
    * `object param`: The function's parameter(-s)

---

### `function Process_Timers()`

!!! warning "Do not call manually"

Processes the timers.

---

### `function Cancel_Timer(func)`

Cancels a function that has been registered for delayed execution. All pending registrations of `func` are cancelled.

???+ notes "Params"

    * `function func`: The function to cancel.

---

### `function Register_Death_Event(obj, func)`

Registers a death event for a given object. `func` is called once, without arguments, on the first [`PumpEvents()`](pgbase.md#function-pumpevents "PGBase.PumpEvents()") after the object is no longer valid. An object can only be registered once.

???+ notes "Params"

    * `GameObject obj`: The object that triggers the function by dying.
    * `function func`: The function to execute.

---

### `function Process_Death_Events()`

!!! warning "Do not call manually"

Processes death events.

---

### `function Register_Attacked_Event(obj, func)`

Registers an attacked event for a given object.

=== "Forces of Corruption"
    When `FindDeadlyEnemy(obj)` first returns an enemy, `func(true, enemy, obj)` is called; when it returns nothing again, `func(false, nil, obj)` is called.

=== "Empire at War"
    The EaW copy of the library calls `func(true, enemy)` and `func(false)`, without `obj`.

This repeats for every new attack. The registration ends only when the object becomes invalid or [`Cancel_Attacked_Event(obj)`](#function-cancel_attacked_eventobj "Cancel_Attacked_Event(obj)") is called.

???+ notes "Params"

    * `GameObject obj`: The object that triggers the function by being attacked.
    * `function func`: The function to execute.

---

### `function Process_Attacked_Events()`

!!! warning "Do not call manually"

Processes attacked events.

---

### `function Cancel_Attacked_Event(obj)`

Cancels a registered attacked event for a given object.

???+ notes "Params"

    * `GameObject obj`: The registered object to remove.

---

### `function Register_Prox(obj, func, range, player_filter)`

Sets up a proximity callback through `obj.Event_Object_In_Range(func, range, player_filter)`. `func(obj, trigger_object)` is called for objects in range on every service until it is cancelled with `obj.Cancel_Event_Object_In_Range(func)` or `obj` becomes invalid. Does nothing in galactic mode. In the FoC copy of the library an invalid `obj` raises a script error, which stops the script.

???+ notes "Params"

    * `GameObject obj`: The object around which the proximity is checked.
    * `function func`: The function to execute.
    * `number range`: The proximity in game units.
    * `PlayerObject player_filter` [optional]: Only objects owned by the player trigger a proximity event.

---

### `function Process_Proximities()`

!!! warning "Do not call manually"

Processes proximity events.

---

### `function Pump_Service()`

!!! warning "Do not call manually"

Calls all `Process_...` functions. Called by [`PumpEvents()`](pgbase.md#function-pumpevents "PGBase.PumpEvents()"). In order: `Process_Timers()`, `Process_Death_Events()`, `Process_Proximities()`, `Process_Attacked_Events()`, then `Process_Reinforcements()` (PGSpawnUnits) and `Story_Mode_Service()` if they are defined.

---

### `function Try_Ability(thing, ability_name, target)`

Tries to fire a given ability if the difficulty allows it, using `Chance(GetAbilityChanceSeed(), GetChanceAllowed(difficulty))` (PGBase).

=== "Forces of Corruption"
    In the FoC copy of the library that chance is always 100%.

=== "Empire at War"
    In the EaW copy it depends on the owner's difficulty.

Then calls [`Use_Ability_If_Able(...)`](#function-use_ability_if_ablething-ability_name-target "Use_Ability_If_Able(...)").

???+ notes "Params"

    * `GameObject thing`: The thing that should activate the ability (a unit or a task force).
    * `string ability_name`: The name of the ability to activate.
    * `GameObject target` [optional]: The ability's target if applicable.

???+ notes "Returns"

    * `bool`: `true` if ability was activated, `false` if not.

---

### `function Use_Ability_If_Able(thing, ability_name, target)`

Activates the ability for a unit or a taskforce's units if able. Optionally uses ability on a target. For a unit, the ability must exist, be ready and not be active; a task force is not checked. With a target that is no longer valid nothing is activated, but the function still returns `true`.

???+ notes "Params"

    * `GameObject thing`: The thing that should activate the ability.
    * `string ability_name`: The name of the ability to activate.
    * `GameObject target` [optional]: The ability's target if applicable.

???+ notes "Returns"

    * `bool`: `true` if ability was activated, `false` if not.

---

### `function Is_A_Taskforce(thing)`

Tests whether a thing is a Taskforce.

???+ notes "Params"

    * `object thing`: The object to test.

???+ notes "Returns"

    * A true value (the task force's `Get_Unit_Table` member) if `thing` is a `TaskForce`, a false value (`nil` or `false`) else.

---

### `function ConsiderDivertAndAOE(object, ability_name, area_of_effect, recent_enemy_units, min_threat_to_use_ability)`

This will consider diverting the passed object in order to use an area of effect ability centered on the unit.

???+ notes "Params"

    * `GameObject object`: The game object to use the ability.
    * `string ability_name`: The ability to use.
    * `number area_of_effect`: The area of effect.
    * `table<GameObject> recent_enemy_units`: The list of recently tracked enemy units (passed to `Find_Best_Local_Threat_Center`).
    * `number min_threat_to_use_ability`: The minimum threat level.

---

### `function OneOrMoreInRange(origin_unit, target_unit_list, range)`

Tests whether at least one of the given objects is in range.

???+ notes "Params"

    * `GameObject origin_unit`: The unit that wants to know the range.
    * `table<GameObject> table_unit_list`: the objects that should be in range.
    * `number range`: The range to test.

???+ notes "Returns"

    * `bool`: `true` if at least one object is in range, `false` else.

---

### `function PruneFriendlyObjects(obj_table)`

Cleans a table of all friendly objects, i.e. all objects owned by `PlayerObject`. The result is a new list; `obj_table` itself is not changed.

???+ notes "Params"

    * `table<GameObject> obj_table`: The list to clean.

???+ notes "Returns"

    * `table<GameObject>`: A new list with the objects of `obj_table` that are not owned by `PlayerObject`.

---

### `function Try_Garrison(tf, unit, offensive_only, range)`

Tries to garrison a unit from a given task force.

!!! note "Forces of Corruption only"
    This function and all functions below it on this page exist only in the FoC copy of the library.

???+ notes "Params"

    * `TaskForce tf` [optional]: The task force the unit belongs to. If valid, the unit is released from it and its orders are locked.
    * `GameObject unit`: The unit to garrison.
    * `bool offensive_only`: Whether to use only offensive objects, i.e. objects the garrisoned units can fire from.
    * `number range`:  The maximum distance to the target garrison.

???+ notes "Returns"

    * `bool`: `true` if successfully garrisoned, `false` else.

---

### `function Try_Deploy_Garrison(object, target, health_threshold)`

Tries to deploy the units garrisoned in `object`. Every garrisoned unit whose `Get_Hull()` is above `health_threshold` leaves the garrison if `target` is not valid or the unit `Is_Good_Against(target)`.

???+ notes "Params"

    * `GameObject object`: The garrison (container) whose units should deploy.
    * `GameObject target` [optional]: The target the deployed units should be good against.
    * `number health_threshold`: Minimum health (as returned by `Get_Hull()`) for a garrisoned unit to deploy.

???+ notes "Returns"

    * `bool`: `true` if at least one unit was deployed, `false` else.

---

### `function Get_Special_Healer_Property_Flag(unit)`

Gets the proper property flag for certain special units.

!!! warning
    The reason this is done in a script function instead of the corresponding XML tag is unknown.  
    The assumed reason is that those objects are teams.

???+ notes "Params"

    * `GameObject`: The unit to get the property flag for.

???+ notes "Returns"

    * `string`: The property flag (`"HealsInfantry"` or `"HealsVehicles"`, looked up by the unit's type name) or `nil`.

---

### `function Set_Land_AI_Targeting_Priorities(tf)`

Sets up the AI Targeting priorities for ground units in a given task force.

???+ notes "Params"

    * `TaskForce tf`: The task force to set the priorities for.

---

### `function Try_Weapon_Switch(object, target)`

Tries to swap weapons for a given unit, if it's a good idea to use the alternate weapons against another unit.

???+ notes "Params"

    * `GameObject object`: The object to attempt the weapon switch for.
    * `GameObject target`: The target to use the weapons against.

---

### `function Determine_Magic_Wait_Duration()`

Generates a magic number to wait for: 2400 minus the current game time in seconds, but at least 60.

???+ notes "Returns"

    * `number`: The magic wait time.

---
