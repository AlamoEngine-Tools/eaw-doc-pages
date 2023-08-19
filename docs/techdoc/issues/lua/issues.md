---
title: Known Issues and Quirks with EaW's LUA Engine
summary: LUA - Issues and Quirks
authors: Commander Cody
comments: true
tags:
  - LUA
  - Scripting
---

# Known Issues and Quirks with EaW's LUA Engine

## Upvalues

Upvalues, i.e. local variables defined outside of a function they are used in, crash the game when loading a save game.

Example for an upvalue:

```lua
local a = 10
function wait()
  Sleep(a)
end
```

---

## `Prevent_AI_Usage` Caveat

If this funciton is used on a unit whose faction has no AI assigned, the game crashes. This also means that SpawnList cannot be used in this situation.

## `Resume_Hyperspace_In` Problems
Can effectively only be used for the duration of the intro cinematic since fighter icons will appear on the map and the fleet will be spawned if the player uses cinematic mode.