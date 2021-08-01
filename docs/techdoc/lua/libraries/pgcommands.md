---
title: PGCommands.lua
tags:
  - Lua Library
---

# `PGCommands.lua`

## Direct Imports

* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")

## Functions

---

### `function ProduceForce(taskforce)`

!!! Error "Deprecated"

Produces a taskforce.

???+ notes "Params"

    * `object taskforce`: The taskforce to produce.

---

### `function ProduceObject(player, objecttype, where)`

!!! Error "Deprecated"

Starts the production of an object.

???+ notes "Params"

    * `PlayerObject player`: The player to produce the object for.
    * `GameObjectType objecttype`: The type of the object to produce.
    * `PGameObject where`: The facility to produce the object.

???+ notes "Returns"

    * `GameObject`: The produced object.

---

### `function WaitProduceObject(objecttype, where)`

!!! Error "Deprecated"

Waits for the object to be produced.

???+ notes "Params"

    * `GameObjectType objecttype`: The type of the object to produce.
    * `PGameObject where`: The facility to produce the object.

???+ notes "Returns"

    * `GameObject`: The produced object.

---

### `function WaitForever()`

The name's pretty accurate. That thing actually waits forever.

---

### `function Register_Timer(func, timeout, param)`

Registers a function for delayed execution.

???+ notes "Params"

    * `function func`: The function to execute.
    * `number timeout`: The time in seconds to wait.
    * `object param`: The function's parameter(-s)

---

### `function Process_Timers()`

!!! Warning "Do not call manually"

Processes the timers.

---

### `function Cancel_Timer(func)`

Cancels a function that has been registered for delayed execution.

???+ notes "Params"

    * `function func`: The function to cancel.

---

### `function Register_Death_Event(obj, func)`

Registers a death event for a given object.

???+ notes "Params"

    * `GameObject obj`: The object that triggers the function by dying.
    * `function func`: The function to execute.

---

### `function Process_Death_Events()`

!!! Warning "Do not call manually"

Processes death events.

---

### `function Register_Attacked_Event(obj, func)`

Registers an attacked event for a given object.

???+ notes "Params"

    * `GameObject obj`: The object that triggers the function by being attacked.
    * `function func`: The function to execute.

---

### `function Process_Attacked_Events()`

!!! Warning "Do not call manually"

Processes attacked events.

---

### `function Cancel_Attacked_Event(obj)`

Cancels a registered attacked event for a given object.

???+ notes "Params"

    * `GameObject obj`: The registered object to remove.

---

### `function Register_Prox(obj, func, range, player_filter)`

???+ notes "Params"

    * `GameObject obj`: The object that triggers the function by being attacked.
    * `function func`: The function to execute.
    * `number range`: The proximity in game units.
    * `PlayerObject player_filter` [optional]: Only objects owned by the player trigger a proximity event.

---

### `function Process_Proximities()`

!!! Warning "Do not call manually"

Processes proximity events.

---

### `function Pump_Service()`

!!! Warning "Do not call manually"

Calls all `Process_...` functions.

---

### `function Try_Ability(thing, ability_name, target)`

Tries to fire a given ability if the difficulty allows it.

???+ notes "Params"

    * `GameObject thing`: The thing that should activate the ability.
    * `string ability_name`: The name of the ability to activate.
    * `GameObject target` [optional]: The ability's target if applicable.

???+ notes "Returns"

    * `bool`: `true` if ability was activated, `false` if not.

---

### `function Use_Ability_If_Able(thing, ability_name, target)`

Activates the ability for a unit or a taskforce's units if able. Optionally uses ability on a target.

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

    * `bool`: `true` if `thing` is a `TaskForce`, `false` else.

---

### `function ConsiderDivertAndAOE(object, ability_name, area_of_effect, recent_enemy_units, min_threat_to_use_ability)`

This will consider diverting the passed object in order to use an area of effect ability centered on the unit.

???+ notes "Params"

    * `GameObject object`: The game object to use the ability.
    * `string ability_name`: The ability to use.
    * `number area_of_effect`: The area of effect.
    * `number recent_enemy_units`: The number of recently tracked enemy units.
    * `number min_threat_to_use_ability`: The minimum threat level.

---

### `function OneOrMoreInRange(origin_unit, target_unit_list, range)`

Test whether at least one of the given objects is in range.

???+ notes "Params"

    * `GameObject origin_unit`: The unit that wants to know the range.
    * `table<GameObject> table_unit_list`: the objects that should be in range.
    * `number range`: The range to test.

???+ notes "Returns"

    * `bool`: `true` if at least one object is in range, `false` else.
---

### `function PruneFriendlyObjects(obj_table)`

Clean a table of all friendly objects.

???+ notes "Params"

    * `table<GameObject> obj_table`: The list to clean.

???+ notes "Returns"

    * `table<GameObject> obj_table`: The cleaned list.

---

### `function Try_Garrison(tf, unit, offensive_only, range)`

Tries to garrison a unit from a given task force.

???+ notes "Params"

    * `TaskForce tf`: The task force the unit belongs to.
    * `GameObject unit`: The unit to garrison.
    * `bool offensive_only`: Should only store in offensive objects; aka. objects the garrisoned units can fire from.
    * `number range`:  The maximum distance to the target garrison.

???+ notes "Returns"

    * `bool`: `true` if successfully garrisoned, `false` else.

---

### `function Try_Deploy_Garrison(object, target, health_threshold)`

Tries to deploy a garrisoned unit.

???+ notes "Params"

    * `GameObject object`: The object to deploy.
    * `GameObject target`: The object's target.
    * `number health_threshold`: Minimum amount of health for the object to deploy.

???+ notes "Returns"

    * `bool`: `true` if the unit was deployed, `false` else.

---

### `function Get_Special_Healer_Property_Flag(unit)`

Gets the proper property flag for certain special units.

!!! Warning
    There is no clear reason as to why that is done via a script function instead of the appropriate Xml-Tag.  
    Assumption is that it's due to the fact that those objects are teams.

???+ notes "Params"

    * `GameObject`: The unit to get the property flag for.

???+ notes "Returns"

    * `string`: The property flag or `nil`.

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

Generates a magic number to wait for.

???+ notes "Returns"

    * `number`: The magic wait time.

---
