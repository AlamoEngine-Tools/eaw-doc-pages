---
title: PGStoryMode.lua
tags:
  - LUA Library
  - FoC
---

# `PGStoryMode.lua`

## Direct Imports

* [`PGStateMachine.lua`](pgstatemachine.md "PGStateMachine.lua")
* [`PGSpawnUnits.lua`](pgspawnunits.md "PGSpawnUnits.lua")
* [`PGMoveUnits.lua`](pgmoveunits.md "PGMoveUnits.lua")

## Indirect Dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Defined Globals

These values are valid throughout every script that is importing `PGStoryMode.lua`. It is advised to not change them unless you know exactly what you are doing.

```lua
ScriptPoolCount = 0
```

## Functions

---

### `function PG_Story_Mode_Init()`

Initialises the story mode. It is a wrapper around the [`Define_State(...)`](pgstatemachine#function-define_statestate-function_value "See PGStateMachine.Define_State(...)") function that ensures a valid setup for story scripts. It will use the `StoryModeEvents` table that has to be defined in every story script to initialise valid states.

---

### `function Story_Event_Trigger(name)`

Advances the story state if a given event has been triggered.

???+ notes "Params"
    
    * `string name`: The story event name.

---

### `function PG_Story_State_Init(message)`

The default `OnInit` function.
