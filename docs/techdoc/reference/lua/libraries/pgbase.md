---
title: PGBase.lua
tags:
  - LUA Library
  - FoC
---

# `PGBase.lua`

## Direct imports

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")

## Functions

---

### `function ScriptExit()`

Sets a flag in `C++` that terminates the script the function has been called from. From then on the engine resumes none of the script's threads. When called inside a thread, the function also ends that thread immediately (`coroutine.yield(false)`); when called outside a thread (e.g. from `Base_Definitions`) it returns and execution continues.

---

### `function Sleep(time)`

Pauses the execution of the calling thread for a certain amount of game time. The engine has no sleep of its own: the function stores the start time in `ThreadValue` and calls [`PumpEvents()`](#function-pumpevents "PumpEvents()") until `GetCurrentTime()` has advanced by `time`, so event handlers, timers and proximity callbacks keep running while it waits, and the wait ends on the first service after the time has passed.
A galactic script gets no service while a tactical battle is running or while the galactic game is paused, so it cannot resume during that time (see [the service rule](../lua-script-lifecycle.md#31-unit-and-structure-scripts-lua_script-on-a-game-object-type)).

!!! example "Params"

    * `number time`: The time to pause the script in seconds.

---

### `function BlockOnCommand(block, max_duration, alternate_break_func)`

Blocks the execution until the execution of `block` has been finished or `max_duration` has expired. If `alternate_break_func` is provided, `block` will stop being serviced, once `alternate_break_func` returns `true`.
Calls [`PumpEvents()`](#function-pumpevents "PumpEvents()") while waiting. Returns `block.Result()` when the block has finished, and `nil` when `block` is `nil`, the time ran out, `alternate_break_func` returned `true` or [`BreakBlock()`](#function-breakblock "BreakBlock()") was called.

!!! example "Params"

    * `object block`: An object with the methods `IsFinished()` and `Result()`, as returned by movement commands and `Reinforce_Unit`. It is not a function.
    * `number max_duration`: The time `block` is allowed to run for.
    Set to `-1` to only use `alternate_break_func` to stop the execution of `block`.
    * `function alternate_break_func` [Optional]: If this function returns `true`, execution of `block` will stop.  
    **Required** if `max_duration` is set to `-1`.

---

### `function BreakBlock()`

Default function to call, if a `block` should be terminated. It sets the global flag `break_block`; the next loop of a running `BlockOnCommand(...)` returns `nil`. The flag is global to the script, so it affects whichever thread's `BlockOnCommand(...)` checks it first.

---

### `function TestCommand(block)`

Runs [`PumpEvents()`](#function-pumpevents "PumpEvents()") once and returns `block.IsFinished()`; returns `nil` when `block` is `nil`.

!!! example "Params"

    * `object block`: An object with the method `IsFinished()`, as returned by movement commands and `Reinforce_Unit`.

---

### `function PumpEvents()`

Services chained events. In order: calls `Object.Service_Wrapper()` when the script has an `Object`, calls `Pump_Service()` when it is defined (PGCommands: timers, death, proximity and attacked events), then yields to the engine. On the next service it takes every queued event from `GetEvent()` and calls each handler with the parameters from `GetEvent.Params()`. Calling it again while it is already running in the same thread raises a script error.

---

### `function TestValid(wrapper)`

Tests if a provided `GameObjectWrapper wrapper` is a valid `GameObject`. This function should always be called when working with native functions on any `GameObject`.
Returns `false` when `wrapper` is `nil` or has no `Is_Valid` member, otherwise `wrapper.Is_Valid()`.

---

### `function Clamp(value, min, max)`

Clamps a given value.

!!! example "Params"

    * `number value`: The value to clamp.
    * `number min`: The minimum value.
    * `number max`: The maximum value.

---

### `function Dirty_Floor(val)`

A workaround to simulate a floor function. It returns `string.format("%d", val)`, a string, and relies on Lua converting that string back to a number when it is used in arithmetic. The workaround exists because the game does not open Lua's `math` library, so `math.floor` is not available.

!!! example "Params"

    * `number val`: The value to floor.

---

### `function Simple_Mod(a,b)`

A simple modulus function.

!!! example "Params"

    * `number a`: Dividend.
    * `number b`: Divisor.

---

### `function Chance(seed, percent)`

Returns if something happened, given a % chance. The result is `(seed + 1) mod 100 < percent`; it is deterministic for a given seed.

!!! example "Params"

    * `number seed`: Random seed.
    * `number percent`: The chance of the event to happen.

!!! example "Returns"

    * `bool`: `true` if the event should happen, `false` else.

---

### `function GetCurrentMinute()`

Returns the current minute.

!!! example "Returns"

    * `number`: The current minute.

---

### `function GetAbilityChanceSeed()`

=== "Forces of Corruption"
    Returns the current time in seconds.

=== "Empire at War"
    Returns `Dirty_Floor(GetCurrentTime()/10) + 9`.

!!! example "Returns"

    * `number`: The current time in seconds.

---

### `function GetChanceAllowed(difficulty)`

Returns a chance based on difficulty.

=== "Forces of Corruption"
    !!! warning
        The function does not work as indicated and always returns a chance of 100%.

=== "Empire at War"
    Returns 20 for `"Easy"`, 100 for `"Hard"` and 60 otherwise.

!!! example "Params"

    * `string difficulty`: The current difficulty.

!!! example "Returns"

    * `number`: The chance for an event based on difficulty. Currently returns 100.

---

### `function PlayerSpecificName(player_object, var_name)`

Creates a player-specific name for a given variable: `"PLAYER" .. player_object.Get_ID() .. "_" .. var_name`.

!!! example "Params"

    * `PlayerObject player_object`: The `PlayerObject` to create a specific variable name for.
    * `string var_name`: The base name of the variable.

!!! example "Returns"

    * `string`: The player-specific variable name.

---

### `function Flush_G()`

Flushes `_G`. Deletes every global table except `_LOADED`, `coroutine`, `string`, `table`, `security`, `LuaWrapperMetaTable` and `_G`, and every global userdata whose `Is_Pool_Safe()` returns `false` (all game objects, players, object types, AI targets, budgets, task forces, story plots and story events). Engine commands are kept, and global numbers, strings, booleans and functions are not touched.

The engine calls `Flush_G()` and then `Base_Definitions()` when a pooled script state is released; see [Lifecycle of one script state](../lua-script-lifecycle.md#1-lifecycle-of-one-script-state).

!!! warning
    Do not call this function without understanding what `_G` is in Lua.

---
