---
title: Known Issues and Quirks with EaW's LUA Engine
summary: LUA - Issues and Quirks
authors: Commander Cody
comments: true
tags:
  - Lua
  - Scripting
---

# Known issues and quirks with EaW's Lua engine

## Upvalues

!!! bug "Upvalues crash the game on load"
    A function that uses a local variable declared outside it (an upvalue) loses that binding when a save game is loaded: the save stores the function's code and the number of upvalues, not their values, and the game restores the function with undefined upvalue slots. The next use of such a variable after a load reads or writes through an invalid pointer, which crashes the game or corrupts memory silently. Functions that use only globals, their parameters and their own locals are unaffected. Treat any upvalue in a script that can be saved as a defect.

    Example for an upvalue:

    ```lua
    local a = 10
    function wait()
      Sleep(a)
    end
    ```

---

## `Prevent_AI_Usage` caveat

!!! bug "Script ends on factions without an active AI"
    `Prevent_AI_Usage` on a unit whose owner has no active AI in the current game mode is an argument error. An argument error in an engine function (wrong parameter count or type, a function used in the wrong game mode, or this case) is written to the AI log and then ends the whole script at the end of that service tick, the same as calling `ScriptExit()`. A pooled script goes back to the pool and the unit keeps running without a script. The game process does not crash. If the owner has no AI player at all, the call only writes a warning and returns nil. This also means that SpawnList, which calls `Prevent_AI_Usage` on every spawned unit, can end the script of the calling unit in this situation.

    This differs from a Lua runtime error (a thrown error inside a thread), which removes only that thread; the script's other threads keep running.

## `Resume_Hyperspace_In` problems

!!! bug "Only usable while the fleet is held in hyperspace"
    `Resume_Hyperspace_In` exists: it releases an attacking fleet that `LINK_TACTICAL` reward parameter 9 set to `2` holds in hyperspace, and it only acts in space battles. Older documentation states (unverified) that it can effectively only be used for the duration of the intro cinematic since fighter icons will appear on the map and the fleet will be spawned if the player uses cinematic mode.