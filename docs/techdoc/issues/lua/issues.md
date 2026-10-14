---
title: Known Issues and Quirks with EaW's LUA Engine
summary: LUA - Issues and Quirks
authors: Commander Cody
comments: true
tags:
  - LUA
  - Scripting
---

# Known issues and quirks with EaW's Lua engine

## Upvalues

!!! bug "Upvalues crash the game on load"
    Upvalues, i.e. local variables defined outside of a function they are used in, crash the game when loading a save game. Treat a change to a shipped script as save-breaking until tested; see [Practices to avoid](../../reference/lua/lua-script-lifecycle.md#52-practices-to-avoid).

    Example for an upvalue:

    ```lua
    local a = 10
    function wait()
      Sleep(a)
    end
    ```

---

## `Prevent_AI_Usage` caveat

!!! bug "Crash on factions without an AI"
    If this function is used on a unit whose faction has no AI assigned, the game crashes. This also means that SpawnList cannot be used in this situation.

## `Resume_Hyperspace_In` problems

!!! bug "Only usable during the intro cinematic"
    Can effectively only be used for the duration of the intro cinematic since fighter icons will appear on the map and the fleet will be spawned if the player uses cinematic mode.