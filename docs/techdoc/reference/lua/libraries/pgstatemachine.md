---
title: PGStateMachine.lua
tags:
  - LUA Library
  - FoC
---

# `PGStateMachine.lua`

## Direct imports

* [`PGCommands.lua`](pgcommands.md "PGCommands.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Functions

---

### `function Base_Definitions()`

The engine calls this function when the script state is created and again, after `Flush_G()`, each time a pooled state is released; see [Script setup](../lua-script-lifecycle.md#5-script-setup) for the exact timing.  
Defines the basic variables required for the state machine. It first calls `Common_Base_Definitions()`, then sets the globals below, then calls `Definitions()` and `PG_Story_Mode_Init()` if they are defined.

??? note "Globals"

    * `StateMachine = {}`:  
      Declares the state machine's base table.
    * `StateMachineIndexes = {}`:  
      Declares the state machine's index holder table.
    * `StateMachineIndexLookup = {}`:  
      Declares the state machine's lookup table.
    * `OnEnter = 1`:  
      The `OnEnter` message that is received when an object enters a state.
    * `OnUpdate = 2`:  
      The `OnUpdate` message that is received when an object is in a state.
    * `OnExit = 3`:  
      The `OnExit` message an object receives when it leaves a state.
    * `CurrentStateIndex = 1`, `DefineStateIndex = 1`, `NextState = nil`, `CurrentState = nil`, `_curproc = nil`, `StoryModeEvents = nil`:  
      The state machine's bookkeeping.
    * `ServiceRate = 0.2`:  
      The service rate: `1.0` services once a second, `0.2` services five times a second. The engine reads this global from the script ([service rule](../lua-script-lifecycle.md#31-unit-and-structure-scripts-lua_script-on-a-game-object-type)).

---

### `function Define_State(state, function_value)`

Defines a new state in the state machine table. The first state defined becomes the initial state. Defining an existing state again replaces its function and keeps its position in the order.

???+ note "Params"

    * `string state`:  This is the tag used to identify the state.
    * `function function_value`: The function that will process all messages associated with the given state

---

### `function Advance_State()`

Advances to the next state, based on the order of state definition.

---

### `function Set_Next_State(state)`

Sets the next state to transition to. A state that has not been defined is ignored silently; `nil` ends the state machine after the current state exits.

???+ note "Params"

    * `string state`:  This is the tag used to identify the next state.

---

### `function Get_Current_State()`

Returns the current state.

???+ note "Returns"

    * `string`: The current state tag.

---

### `function Get_Next_State()`

Returns the next state.

???+ note "Returns"

    * `string`: The next state tag.

---

### `function Process_States()`

This function is called to advance the state machine through its states. For each state it calls the state function with `OnEnter`, then repeatedly with `OnUpdate`, calling `PumpEvents()` after each `OnUpdate` while no transition is pending, and finally with `OnExit` once the next state differs. It returns when the next state is `nil`. An undefined state raises a script error.

!!! warning "Do not call manually."

---

### `function main()`

This is the main thread function for this script.  
Upon return from this function the script will finish.
It runs `Process_States()` and then calls `ScriptExit()`, which stops every thread of the script, not only the main thread. The script state itself stays loaded until the object or plot it belongs to releases it.

---
