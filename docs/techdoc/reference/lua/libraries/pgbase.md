---
title: PGBase.lua
tags:
  - LUA Library
  - FoC
---

# `PGBase.lua`

## Direct Imports

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")

## Functions

---

### `function ScriptExit()`

Sets a flag in `C++` that terminates the script the function has been called from.

---

### `function Sleep(time)`

Pauses the execution of a given script for a certain amount of time.

!!! example "Params"

    * `number time`: The time to pause the script in seconds.

---

### `function BlockOnCommand(block, max_duration, alternate_break_func)`

Blocks the execution until the execution of `block` has been finished or `max_duration` has expired. If `alternate_break_func` is provided, `block` will stopped being serviced, once `alternate_break_func` returns `true`.

!!! Example "Params"

    * `function block`: The function to service.
    * `number max_duration`: The time `block` is allowed to run for.
    Set to `-1` to only use `alternate_break_func` to stop the execution of `block`.
    * `function alternate_break_func` [Optional]: If this function returns `true`, execution of `block ` will stop.  
    **Required** if `max_duration` is set to `-1`.

---

### `function BreakBlock()`

Default function to call, if a `block` should be terminated.

---

### `function TestCommand(block)`

Tests if a `block` is valid.

!!! example "Params"

    * `function block`: The function to test.

---

### `function PumpEvents()`

Services chained events.

---

### `function TestValid(wrapper)`

Tests, if a provided `GameObjectWrapper wrapper` is a valid `GameObject`. This function should always be called when working with native functions on any `GameObject`.

---

### `function Clamp(value, min, max)`

Clamps a given value.

!!! example "Params"

    * `number value`: The value to clamp.
    * `number min`: The minimum value.
    * `number max`: The maximum value.

---

### `function Dirty_Floor(val)`

A workaround to simulate a floor function by calling the default `tostring(...)` and converting back to a number.

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

Returns if something happened, given a % chance.

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

Returns the current time in seconds.

!!! example "Returns"

    * `number`: The current time in seconds.

---

### `function GetChanceAllowed(difficulty)`

Returns a chance based on difficulty.

!!! Warning
    The function does not work as indicated and always returns a chance of 100%.

!!! example "Params"

    * `string difficulty`: The current difficulty.

!!! example "Returns"

    * `number`: The chance for an event based on difficulty. Currently returns 100.

---

### `function PlayerSpecificName(player_object, var_name)`

Creates a player-specific name for a given variable.

!!! example "Params"

    * `PlayerObject player_object`: The `PlayerObject` to create a specific variable name for.
    * `string var_name`: The base name of the variable.

!!! example "Returns"

    * `string`: The player-specific variable name.

---

### `function Flush_G()`

Flushes `_G`.

!!! Warning
    If you have no idea what `_G` is in `LUA` don't use this function.

---
