---
title: PGStateMachine.lua
tags:
  - LUA Library
  - FoC
---

# `PGStateMachine.lua`

## Direct Imports

* [`PGCommands.lua`](pgcommands.md "PGCommands.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Functions

---

### `function Base_Definitions()`

This function is called once when the script is first created.  
Defines the basic variables required for the state machine.

??? Note "Globals"

    * `StateMachine = {}`:  
      Declares the State Machine's base table.
    * `StateMachineIndexes = {}`:  
      Declares the State Machine's index holder table.
    * `StateMachineIndexLookup = {}`:  
      Declares the State Machine's lookup table.
    * `OnEnter = 1`:  
      The `OnEnter` message that is received when an object enters a state.
    * `OnUpdate = 2`:  
      The `OnUpdate` message that is received when an object is in a state.
    * `OnExit = 3`:  
      The `OnExit` message an object receives when it leaves a state.
    * `ServiceRate = 0.2`:  
      The service rate: `1.0` services once a second, `0.2` services five times a second.

---

### `function Define_State(state, function_value)`

Defines a new state in the state machine table.

???+ Note "Params"

    * `string state`:  This is the tag used to identify the state.
    * `function function_value`: The function that will process all messages associated with the given state

---

### `function Advance_State()`

Advances to the next state, based on the order of state definition.

---

### `function Set_Next_State(state)`

Sets the next state to transition to.

???+ Note "Params"

    * `string state`:  This is the tag used to identify the next state.

---

### `function Get_Current_State()`

Returns the current state.

???+ Note "Returns"

    * `string`: The current state tag.

---

### `function Get_Next_State()`

Returns the next state.

???+ Note "Returns"

    * `string`: The next state tag.

---

### `function Process_States()`

This function is called to advance the State Machine through its states.

!!! warning "Do not call manually."

---

### `function main()`

This is the main thread function for this script.  
Upon return from this function the script will finish and be destroyed by the system.

---
