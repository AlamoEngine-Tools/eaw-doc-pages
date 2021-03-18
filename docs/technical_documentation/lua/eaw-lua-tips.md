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

**Upvalues:**
Upvalues, i.e. local variables defined outside of a function they are used in, crash the game when loading a save game. E.g.:
```
local a = 10
function wait()
  Sleep(a)
end
```

---

**Prevent_AI_Usage caveat:** If this is used on a unit whose faction has no AI assigned, the game crashes. This also means that SpawnList cannot be used in this situation.

---

**Resume_Hyperspace_In problems:** Can effectively only be used for the duration of the intro cinematic since fighter icons will appear on the map and the fleet will be spawned if the player uses cinematic mode.

---

# Tips and tricks
---

**AI activation in tactical battles:**
For performance reasons (probably), in tactical battles the engine only activates the AI for players that have units on the map at the very start of the battle. To activate the AI for a faction that has no units at the beginning, use the Enable_As_Actor command.

---

**Error handling:**
There are two fundamentally different types of errors: Lua errors and C++ exceptions. Lua errors are directly caused by Lua code (e.g. when trying to call a nil value or by using the `error` function) and will only crash the thread that they occured in. They can be caught using `pcall`. Exceptions can occur in C++ functions that the Lua code calls and will crash the entire script. There is (to my knowledge) no way to catch them.

The `error` and `pcall` functions seem to work normally with the small exception that when a string is passed to `error`, information on the line in which the error occured is added to it at the beginning. Other datatypes are not modified.

---

**Set/Transition Cinematic Camera/Target Key:**
These four commands make just about any camera shot possible. For all four the first parameter is a game object whose position functions as a reference point for the camera setting. For the transition functions the second parameter is the time they take to perform the transition to the new position. The remaining 7 parameters (in this order) do the following:

- 3 parameters are coordinates that determine the offset from the reference position. By default they are normal cartesian x,y,z coordinates (same orientation as in the map editor)
- The next parameter takes values 0 or 1. When set to 1 the 3 coordinate parameters are read as spherical coordinates with the first one being the distance and the last one the angle in the x-y-plane. 
- The next parameter takes 0 or a game object. If a game object is given the camera/target position is attached to it and follows its movements (e.g. for setting the camera to follow a moving ship). 
- The second to last parameter takes 0 or 1. If set to 1, the function will evaluate the given coordinate offset in the attached object's coordinate system instead of the map's coordinate system (only works if the function is attached to a game object with the previous parameter). 
- The last parameter plays the attached object's cinematic animation?

---

**TestValid:** This function is used to check if a game object is still valid, i.e. alive. It is always needed before using a game object variable for anything else since otherwise the script will crash if the unit died. This is not equivalent to and cannot be replaced by a simple nil check! An invalid game object variable can persist for a while before it gets deleted.

---

## AI scripting
**Upgrade selection:**
In the vanilla PurchaseLandUpgradesGeneric script something like `"E_Secure_Area_Upgrade = 0,10"` can be found. Even though only one upgrade can be chosen, the AI has a higher chance of choosing an upgrade from a list with a higher number.
Locutus: Everything with 10 basically gets researched as soon as its available, everything with 5 soon after and everything with 1 rather sporadic.

---

## Testing
**Reloading scripts:** When testing lua scripts, usually you don't need to restart the game after changing something. Story scripts are only loaded on battle/GC start, meaning that returning to the main menu is always enough to properly reload the script (also true for xml story files). It is slightly trickier for other scripts (like library scripts), but in general also possible except for evaluator scripts. Making the changes and telling the game to reload the script before returning to the main menu and restarting the scenario seems to help in some cases.

---

## Spawning units
---

**Collision:** To spawn units both `Spawn_Unit` and `Create_Generic_Object` can be used. The former respects collision and if there is already some object at the given position it will spawn the unit as close to the position as allowed by collision whereas the latter will always spawn the object precisely at the given location.

---

**SpawnList:** This function is defined in PGSpawnUnits and can be used to spawn entire unit lists at once. It can also automatically set AI usage for the spawned units, however this can cause problems when spawning units for a faction with no AI (see Prevent_AI_Usage in the reference).

---

**Hyperspacing in:** Spawning a unit via script from hyperspace at a pre-placed marker is usually done with this set of commands: 
```
unit = Spawn_Unit(object_type, player, marker_object)[1]
unit.Teleport_And_Face(marker_object)
unit.Hyperspace_In(delay)
```
The `Teleport_And_Face` makes sure the unit faces the same direction as the marker. The `[1]` is required since `Spawn_Unit` returns a table with the spawned game object in the first position. The `delay` is given in number of frames not seconds.

---

**Delayed hyperspace exit for tactical missions:** In tactical missions it is sometimes desired to delay the arrival of the attacking fleet. This can be done by setting `Reward_Param9` of the corresponding `LINK_TACTICAL` to `2`. This will prevent the attackers from arriving until the command `Resume_Hyperspace_In()` is called from lua.

---