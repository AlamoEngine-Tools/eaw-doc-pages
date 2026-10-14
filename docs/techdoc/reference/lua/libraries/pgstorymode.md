---
title: PGStoryMode.lua
tags:
  - LUA Library
  - FoC
---

# `PGStoryMode.lua`

## Direct imports

* [`PGStateMachine.lua`](pgstatemachine.md "PGStateMachine.lua")
* [`PGSpawnUnits.lua`](pgspawnunits.md "PGSpawnUnits.lua")
* [`PGMoveUnits.lua`](pgmoveunits.md "PGMoveUnits.lua")

## Indirect dependencies

* [`PGDebug.lua`](pgdebug.md "PGDebug.lua")
* [`PGBase.lua`](pgbase.md "PGBase.lua")
* [`PGBaseDefinitions.lua`](pgbasedefinitions.md "PGBaseDefinitions.lua")

## Defined globals

These values are valid throughout every script that is importing `PGStoryMode.lua`. Changing them is not advised without a specific reason.

```lua
ScriptPoolCount = 0
```

This assignment turns pooling off for every script that requires `PGStoryMode.lua`, directly or indirectly, so its globals never carry over to another plot or object; see [Story plot scripts](../lua-script-lifecycle.md#32-story-plot-scripts-lua_script-on-a-story-plot).

## Functions

---

### `function PG_Story_Mode_Init()`

Initialises the story mode. It is a wrapper around the [`Define_State(...)`](pgstatemachine.md#function-define_statestate-function_value "See PGStateMachine.Define_State(...)") function that ensures a valid setup for story scripts. It will use the `StoryModeEvents` table that has to be defined in every story script to initialise valid states.
It is called from `Base_Definitions()` of `PGStateMachine.lua`, after `Definitions()`, so `StoryModeEvents` has to be set in `Definitions()`. It first defines `PG_Story_State_Init` as the initial state, then one state per `StoryModeEvents` entry, keyed by the event name. A missing `StoryModeEvents` table is skipped; an entry that is not a function produces a message box.

---

### `function Story_Event_Trigger(name)`

Advances the story state if a given event has been triggered. The engine calls this function by name to pass a story event to the script. If `StoryModeEvents[name]` is a function and no other transition is pending, the state machine's next state becomes `name`; a trigger that arrives while another transition is still pending is dropped.

???+ notes "Params"
    
    * `string name`: The story event name.

---

### `function PG_Story_State_Init(message)`

The initial state of every story script. It only writes a debug message on `OnEnter` and otherwise does nothing; the script stays in this state until a new state is set, normally by `Story_Event_Trigger(...)`.
