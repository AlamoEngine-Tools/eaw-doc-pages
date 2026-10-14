---
title: Lua Tips
summary: General EaW Lua Tips
authors: Commander Cody
tags:
  - Lua
  - Scripting
---
# Engine issues and quirks
---

The [known issues](../../issues/lua/issues.md) page is the reference for engine bugs; the entries below summarise them.

!!! warning "Upvalues"
    A function that uses a local variable declared outside it (an upvalue) loses that binding when a save game is loaded: the save stores the function's code and the number of upvalues, not their values, and the game restores the function with undefined upvalue slots. The next use of such a variable after a load reads or writes through an invalid pointer, which crashes the game or corrupts memory silently. Functions that use only globals, their parameters and their own locals are unaffected. Treat any upvalue in a script that can be saved as a defect.

---

**Prevent_AI_Usage caveat:** Ends the whole script (the game does not crash) when the unit's owner has no active AI in the current mode, which also affects SpawnList in that situation; see [`Prevent_AI_Usage` caveat](../../issues/lua/issues.md#prevent_ai_usage-caveat).

---

**Resume_Hyperspace_In:** The function exists. It releases an attacking fleet that `LINK_TACTICAL` reward parameter 9 set to `2` holds in hyperspace, and it only acts in space battles; see [`Resume_Hyperspace_In` problems](../../issues/lua/issues.md#resume_hyperspace_in-problems).

---

# Tips and tricks
---

**AI activation in tactical battles:**
In tactical battles the engine only activates the AI for players that have units on the map at the very start of the battle. To activate the AI for a faction that has no units at the beginning, use the Enable_As_Actor command; this is the way to give a faction an AI presence in a battle.

!!! info "Unverified"
    The claim that the AI activates only for factions with units at battle start is not confirmed, and neither is the reason (performance).

---

**Error handling:**
There are two kinds of script errors. A Lua runtime error (a thrown error inside a thread, e.g. calling a nil value or using the `error` function) removes only the thread it occurred in. The engine writes the error text and the call stack to the AI log and keeps running the other threads of the same script. Such errors can be caught using `pcall`.

An argument error in an engine function (wrong parameter count or type, a function used in the wrong game mode, or `Prevent_AI_Usage` on an owner whose AI is not active in the current mode) is different. It is written to the AI log and then ends the whole script at the end of that service tick, the same as calling `ScriptExit()`. A pooled script goes back to the pool and the unit keeps running without a script. The game process does not crash.

Engine functions never throw C++ exceptions into Lua; Lua errors are the only error mechanism. The `error` and `pcall` functions are standard Lua; the engine adds no line number to `error()` messages.

---

**Set/Transition Cinematic Camera/Target Key:**
These four commands make nearly any camera shot possible. For all four the first parameter is a game object whose position functions as a reference point for the camera setting. For the transition functions the second parameter is the time they take to perform the transition to the new position. The remaining 7 parameters (in this order) do the following:

- 3 parameters are coordinates that determine the offset from the reference position. By default they are normal cartesian x,y,z coordinates (same orientation as in the map editor)
- The next parameter takes values 0 or 1. When set to 1 the 3 coordinate parameters are read as spherical coordinates with the first one being the distance and the last one the angle in the x-y-plane. 
- The next parameter takes 0 or a game object. If a game object is given the camera/target position is attached to it and follows its movements (e.g. for setting the camera to follow a moving ship). 
- The second to last parameter takes 0 or 1. If set to 1, the function will evaluate the given coordinate offset in the attached object's coordinate system instead of the map's coordinate system (only works if the function is attached to a game object with the previous parameter). 

The last parameter only matters together with an attached object: when set to 1 the key uses the centre of the object's world bounds instead of its position. It does not play an animation.

---

**TestValid:** This function is used to check if a game object is still valid, i.e. alive. It is always needed before using a game object variable for anything else since otherwise the script will crash if the unit died. This is not equivalent to and cannot be replaced by a simple nil check. An invalid game object variable can persist for a while before it gets deleted.

---

## AI scripting
**Upgrade selection:**
The vanilla PurchaseLandUpgradesGeneric script contains entries such as `"E_Secure_Area_Upgrade = 0,10"`. Even though only one upgrade can be chosen, the AI has a higher chance of choosing an upgrade from a list with a higher number.
According to Locutus, everything weighted 10 is researched almost as soon as it is available, everything weighted 5 soon after and everything weighted 1 sporadically.

---

## Testing
**Reloading scripts:** A change to a Lua script usually does not require a restart of the game. Story plot scripts are only loaded at the start of a battle or galactic campaign, so returning to the main menu is always enough to reload them (this also applies to XML story files). Other scripts, such as library scripts, are harder to reload but in general reloadable as well, except for evaluator scripts.

!!! info "Unverified"
    Making the changes and telling the game to reload the script before returning to the main menu and restarting the scenario helps in some cases.

The rules behind this, described in full under [Game-level transitions](lua-script-lifecycle.md#2-game-level-transitions):

- Story plot scripts are not pooled by default, so every campaign or mission start loads them from the file again.
- A pooled state never loads its file a second time, and returning to the main menu does not empty the pool, so an idle state from an earlier game still runs the code it was loaded with. Loading a save game or starting a skirmish, multiplayer or replay game empties the pool.
- When the game reloads a changed script, idle states of it are discarded at once; a state that is in use keeps its old code until the object it is attached to is gone.
- A save game contains the scripts' code, so changes to the file do not reach a game loaded from an existing save. Test script changes on a fresh start, not on an old save.

---

## Spawning units
---

**Collision:** To spawn units both `Spawn_Unit` and `Create_Generic_Object` can be used. The former respects collision and if there is already some object at the given position it will spawn the unit as close to the position as allowed by collision whereas the latter will always spawn the object precisely at the given location.

---

**SpawnList:** This function is defined in PGSpawnUnits and can be used to spawn entire unit lists at once. It calls `Prevent_AI_Usage` on every spawned unit (`Prevent_AI_Usage(true)` when `allow_ai_usage` is false, `Prevent_AI_Usage(false)` otherwise), however this can cause problems when spawning units for a faction with no AI (see [`Prevent_AI_Usage` caveat](../../issues/lua/issues.md#prevent_ai_usage-caveat)).

---

**Hyperspacing in:** Spawning a unit via script from hyperspace at a pre-placed marker is usually done with this set of commands: 
```
unit = Spawn_Unit(object_type, marker_object, player)[1]
unit.Teleport_And_Face(marker_object)
unit.Cinematic_Hyperspace_In(delay)
```
The `Teleport_And_Face` makes sure the unit faces the same direction as the marker. The `[1]` is required since `Spawn_Unit` returns a table with the spawned game object in the first position. `Spawn_Unit` takes the position second and the player third. The engine has no `Hyperspace_In` method on game objects; the method is `Cinematic_Hyperspace_In`. The `delay` is given in number of frames not seconds.

---

**Delayed hyperspace exit for tactical missions:** In tactical missions it is sometimes desired to delay the arrival of the attacking fleet. Older documentation states that this can be done by setting `Reward_Param9` of the corresponding `LINK_TACTICAL` to `2`, which would prevent the attackers from arriving until the command `Resume_Hyperspace_In()` is called from lua.

This is how it works: with `Reward_Param9` set to `2` the attacking fleet's units stay hidden and the arrival cinematic does not start until `Resume_Hyperspace_In()` is called. The function only acts in space battles.

---