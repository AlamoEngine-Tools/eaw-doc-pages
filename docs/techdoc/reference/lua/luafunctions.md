---
title: FoC Lua Commands
summary: "A list of all hardcoded lua commands in Star Wars Empire at War: Forces of Corruption"
authors: Commander Cody
tags:
  - Lua
  - Scripting
---
# Forces of Corruption Lua commands
This is a list of the hardcoded Lua commands in Star Wars Empire at War: Forces of Corruption. The list aims to be complete, but individual commands may be missing. Missing commands and mistakes can be reported in the forums: https://stargate-eaw.de/forum.
The list only contains hardcoded commands that are specific to the game. It does not include functions that are part of the standard Lua library or that are defined in the game's Lua files, including the library.
The list is a reference only; comments are given only where useful information beyond what is obvious from the name is available. A question mark indicates that the accuracy of the given information is uncertain.


# Global variables

| Variable                    | Script type                | Content                                                                  |
|-----------------------------|----------------------------|--------------------------------------------------------------------------|
| Script                      | All                        | The current script itself, set by the engine in every script. It is not a LuaScriptWrapper: its methods are those listed under `Script.` in the LuaScriptWrapper section below, and it survives `Flush_G`. |
| LUA_PATH                    | All                        | The search path `require` uses, set by the engine: `./?.lua;./?.lc;` followed by `<dir>?.lua;<dir>?.lc;` for each script directory (Library, GameObject, FreeStore, Miscellaneous, Story, AI, AI/LandMode, AI/SpaceMode, AI/StoryArc, Interventions, Evaluators, in this order). All directories share one module namespace, so a file name must be unique across them. |
| ServiceRate                 | All(?)                     | The amount of time (in seconds) the script is suspended after a coroutine yield (i.e. call to PumpEvents). This is adjusted to an integer number of frames and is always at least 1 frame or 0.033 seconds. Can be adjusted at any point in the script(?).     |
| UnitServiceRate             | Free-store scripts         | The amount of time in seconds between consecutive calls to `On_Unit_Service`(for same unit?) |
| LuaThreadTable              | All?                       | Table whose keys are objects of type thread and whose entries are booleans. The first entry contains the main thread.  |
| LuaWrapperMetaTable         | All(?)                     | The meta table for all GameObjectWrappers and PlayerWrappers and maybe all other objects. Has entries for __call, __gc, __eq, __tostring and __index.     |
| PlayerObject                | AI, free-store and evaluator scripts  | The AI player the script is attached to                       |
| Target                      | AI and evaluator scripts   | The target considered (game object at least in galactic mode; nil when the AI goal has no object)            |
| AITarget                    | AI plan scripts            | AITargetLocationWrapper (use .Get_Game_Object() to get corresponding game object if there is one, e.g. the planet in galactic mode). Not set for evaluator scripts.  |
| Budget                      | AI plan scripts            | The plan's BudgetWrapper (see BudgetWrapper below).                      |
| FreeStore                   | Free-store scripts         | The free store object (see the FreeStore functions below).                        |
| LastService                 | Unit and free-store scripts | Game time of the script's last service, written by the engine and compared with `ServiceRate`; see [unit and structure scripts](lua-script-lifecycle.md#31-unit-and-structure-scripts-lua_script-on-a-game-object-type) for the service rule. |
| Object                      | Unit scripts               | The GameObjectWrapper the script is attached to.                         |
| ScriptPoolCount             | All?                       | How many states of a script file the game loads at once; not a limit, and `0` turns pooling off (PGStoryMode sets it to 0 for story plot scripts). See [Lifecycle of one script state](lua-script-lifecycle.md#1-lifecycle-of-one-script-state).  |



# General functions

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| GetEvent()                         | -                               | Used to run event handlers like `Default_Space_Conflict_Begin`. Removes and returns the next queued event handler function of the current thread, or nil when the queue is empty. Only AI plan task force events are queued here; `PumpEvents` (PGBase) drains the queue.   |
| GetEvent.Params()                  | -                               | Returns a list with the parameters for the function call                 |
| GetEvent.Reset()                   | -                               | Clear out any thread events. Empties the queue of every thread of the script. The queue is part of the script state and survives pooled reuse and save games; `Common_Base_Definitions` (PGBaseDefinitions) calls this function. |
| lc(?)                              | -                               | LuaConsolePrint. Its output goes to the output window of an attached Lua debugger. It is not one of the commands the engine registers into every script.  |
| DumpCallStack()                    | -                               | Returns the call stacks for all threads of this lua script. |
| GetThreadID()                      | -                               | Unverified: equivalent to Thread.Get_Current_ID()                        |
| _OuputDebug(X)                     | X = string                      | Prints to _LogFile.txt. The name is misspelled.                          |
| _MessagePopup(X)                   | X = string                      | Trigger a message popup window                                           |
| _CustomScriptMessage(X,Y)          | X = string(file name), Y = string | Print to X. (X can only be a file name, no path)                       |
| _DebugBreak(?)                     | -                               | Halts game execution. Requires a lua debugger to be attached to resume execution.  |
| _ScriptMessage(X)                  | X = string                      | Prints to the AILog if it is enabled                                     |
| _ScriptExit()                      | -                               | Sets a flag for the engine to terminate the script. The script will not be killed immediately, only after the next yield. From then on the engine resumes none of the script's threads. |
| StringCompare(X,Y)                 | X = string, Y = string          | -                                                                        |
| BlockForever(?)                    | -                               | -                                                                        |
| Is_Multiplayer_Mode()              | -                               | -                                                                        |
| Get_Game_Mode()                    | -                               | Returns "Land", "Space" or "Galactic"                                    |
| Is_Campaign_Game()                 | -                               | True for galactic campaign games                                         |
| Lock_Controls(X)                   | X = 0,1                         | (Un)Lock all player controls                                             |
| Suspend_AI(X)                      | X = 0,1                         | -                                                                        |
| Cancel_Fast_Forward()              | -                               | Stops fast forward                                                       |
| Resume_Hyperspace_In()             | -                               | In tactical missions when reward parameter 9 of LINK_TACTICAL is set to 2, this will trigger the arrival of the attacking fleet. Fighter icons will appear on the map anyway and the fleet will be spawned if the player uses cinematic mode.  |
| Game_Message(X)                    | X = text string from dat file   | Displays the text entry as a droid advisor hint                          |
| Add_Objective(X,Y)                 | X = text string, Y = bool       | For Y = true the objective is added under the heading "Battle Information", for Y = false it is added under the heading "Mission Objectives"      |
| Remove_Planet_Highlight(X)         | X = string                      | -                                                                        |
| Add_Planet_Highlight(X,Y)          | X = planet object, Y = string   | -                                                                        |
| Remove_Radar_Blip(X)               | X = string(identifier) or game object | Removes the radar blip identified by X (see Add_Radar_Blip)              |
| Add_Radar_Blip(X,Y)                | X = game object, Y = string(identifier) | Add a radar blip at X with identifier Y                          |
| Hide_Sub_Object(X,Y,Z)             | X = game object, Y = 0,1, Z = string | -                                                                   |
| Hide_Object(X,Y)                   | X = game object, Y = 0,1        | -                                                                        |
| Assemble_Fleet(X)                  | X = list of game object         | Assembles the passed objects into a fleet and returns the fleet object   |
| Is_Point_In_Asteroid_Field(?)      | -                               | -                                                                        |
| Is_Point_In_Ion_Storm(?)           | -                               | -                                                                        |
| Is_Point_In_Nebula(?)              | -                               | -                                                                        |
| Are_On_Opposite_Sides_Of_Shield(X,Y) | X = game object, Y = game object | -                                                                     |
| Are_On_Opposite_Sides_Of_Shield(X,Y,Z,U) | X = game object, Y = game object, Z = player, U = bool | Returns a bool.                             |
| Activate_Retry_Dialog(?)           | -                               | -                                                                        |
| WaitForStarbase(X,Y)               | X = planet object, Y = number(base level) | -                                                              |
| WaitForGroundbase(X,Y)             | X = planet object, Y = number(base level) | -                                                              |
| GetNextGroundbaseType(X)           | X = planet object               | -                                                                        |
| GetNextStarbaseType(X)             | X = planet object               | -                                                                        |
| Create_Position(X, Y, Z)           | X = number, Y = number, Z = number | Creates a PositionWrapper object from the given coordinates and returns it. Exists in steam version only since the January 2021 patch.  |
| GUI_Component_Visibility(X,Y)      | X = string(component id), Y = bool | Not available in older versions of the game.                          |
| GUI_Component_Enable(X,Y)          | X = string(component id), Y = bool | Not available in older versions of the game.                          |
| GUI_Component_Text(X,Y)            | X = string(component id), Y = string(text identifier) | Not available in older versions of the game.       |
| GUI_Component_Play_Anim(X,Y,Z,U)   | X = string(component id), Y = string(animation name), Z = number(anim subindex), U = bool(looping?) | Not available in older versions of the game. |
| GUI_Component_Stop_Anim(X)         | X = string(component id)        | Not available in older versions of the game.                             |
| GUI_Component_Color(X,R,G,B,A)     | X = string(component id), R,G,B,A = numbers | Not available in older versions of the game.                 |
| GUI_Component_Blink(X,Y,Z,U)       | X = string(component id), Y,Z,U = bool | Not available in older versions of the game.                      |
| GUI_Component_Flash(X,Y,Z,U)       | X = string(component id), Y = bool, Z = number, U = number | Not available in older versions of the game.  |
| GUI_Component_Stop_Flash(X)        | X = string(component id)        | Not available in older versions of the game.                             |
| GUI_Text_Color(X,R,G,B,A)          | X = string(component id), R,G,B,A = numbers | Not available in older versions of the game.                 |
| GUI_Button_Icon(X,Y,R,G,B,A)       | X = string(component id), Y = string(icon), R,G,B,A = numbers | Not available in older versions of the game. |

## Game time
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| GetCurrentTime()                   | -                               | Returns game time in seconds                                             |
| GetCurrentTime.Frame()             | -                               | -                                                                        |
| GetCurrentTime.Galactic_Time()     | -                               | -                                                                        |

## Finding game objects etc.
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Find_Player(X)                     | X = faction name                | Returns a PlayerWrapper object                                           |
| Find_Object_Type(X)                | X = type name                   | Returns a GameObjectTypeWrapper object                                   |
| Find_All_Objects_Of_Type(X)        | X = property flag, player, type name or category | Literally finds all objects of this type. That may include projectiles or other unexpected objects.     |
| Find_All_Objects_Of_Type(X,Y)      | X = property flag, Y = player   | -                                                                        |
| Find_All_Objects_Of_Type(X,Y)      | X = player , Y = category       | Categories can be piped together </br> (e.g. `"Frigate | Capital"`).     |
| Find_First_Object(X)               | X = string(type name)           | Returns the first object of the given type. Possibly finds objects in reverse spawn order.     |
| FindDeadlyEnemy(X)                 | X = game object or taskforce    | Returns (the most powerful?) unit attacking X if there is one. Has turned out somewhat unreliable in some cases.      |
| Find_Hint(X,Y)                     | X = string(type name) or game object type, Y = string(hint) | Find an object with a given hint (as set in the map editor).     |
| Find_All_Objects_With_Hint(X)      | X = string(hint)                | -                                                                        |
| Find_Nearest(X,Y)                  | X = game object (or taskforce or ai target?), Y = type name | Returns the nearest object to X that is of type Y. May return nil. Tactical only.         |
| Find_Nearest(X,Y,Z)                | X = game object, ai target or taskforce, Y = player, Z = bool | Returns the nearest unit to X belonging to Y if Z == true. Otherwise it will return the closest unit belonging to an enemy of Y. Tactical only. |
| Find_Nearest(X,Y,Z,U)              | X = game object, ai target or taskforce, Y = string(property flag or category mask), Z = player, U = bool | Tactical only.               |
| Find_Nearest_Space_Field(X,Y)      | X = game object or taskforce, Y = "Asteroid"/"Nebula"/"Ion_Storm"? | -                                     |
| Find_Best_Local_Threat_Center(X,Y) | X = unit list, Y = number(distance) | Returns position and combined threat of units (from the unit list) in range of the position.    |
| Get_Most_Defended_Position(X,Y)    | X = ai target location, Y = player | Tactical only. Returns a position.                                     |
| Project_By_Unit_Range(X,Y)         | X = game object, Y = game object or taskforce | Tactical only. Returns a position outside the range of X   |
| Find_Path(X,Y,Z)                   | X = player, Y = planet object, Z = planet object | Galactic only. Only for AI players. Returns a list of planet objects.   |
| FindPlanet(X)                      | X = string(planet name)         | Galactic only                                                            |
| FindPlanet.Get_All_Planets()       | -                               | Galactic only                                                            |

## Spawning objects
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Spawn_Special_Weapon(X,Y)          | X = string, Y = player          | Space only. Spawns a special weapon like "Ground_Ion_Cannon" and returns it. Can be fired using `Fire_Special_Weapon` but is not available to the player.   |
| Spawn_From_Reinforcement_Pool(X,Y,Z) | X = type, Y = position, Z = player | Spawns a unit from the reinforcement pool without hyperspace animation and returns a table containing the spawned unit. Unit faces the center of the map(?). If no unit of the given type is in the reinforcement pool, nothing is spawned (no error). Respects collision. |
| Create_Generic_Object(X,Y,Z)       | X = game object type/type name, Y = position, Z = player | This spawns X at Y without regard for collision. Be sure to use a position for Y, using a game object can often crash the script. |
| Spawn_Unit(X,Y,Z)                  | X = game object type, Y = position or game object, Z = player | Spawns a unit respecting collision. If something blocks the spawn, the unit will be spawned as close to the spawn location as possible. Returns a list whose first entry is the spawned object.    |
| Reinforce_Unit(X,Y,Z,U,V)          | X = type, Y = position or false, Z = player, U = bool, V = bool (obey_zones) | If Y is false, the unit type is added to the reinforcements pool. Returns a CommandBlock.      |

## Command block functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Result()                          | -                               | Get result of action (e.g. spawned units from Reinforce_Unit)            |
| .IsFinished()                      | -                               | Check if action (e.g. unit movement) has finished                        |

## Any userdata (unverified)
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Is_Valid()                        | -                               | Usually used on game objects to test if they are still in the game       |
| .Is_Pool_Safe()                    | -                               | Returns whether the value may stay in a pooled script state when the state is reused; `Flush_G` (PGBase) deletes every global userdata for which it returns false. Game objects, object types, players, AI targets, budgets, task forces, story plots, story events, script wrappers and command block objects return false; engine commands and `Script` return true. |

## Camera and cinematics
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Start_Cinematic_Space_Retreat(X,Y) | X = number(playerID), Y = number(delay) | Starts a retreat for the given player with all retreatable units. The units are teleported to the retreat position and start moving. At the end of the delay, they jump to hyperspace. No cinematic camera is initiated. Neither is there a retreat countdown nor will the battle end. |
| End_Cinematic_Mode()               | -                               | -                                                                        |
| Start_Cinematic_Mode()             | -                               | -                                                                        |
| Set_Cinematic_Environment(X)       | X = bool                        | Used for the opening cinematic of the campaigns |
| Promote_To_Space_Cinematic_Layer(X) | X = game object                | Used for the opening cinematic of the campaigns   |
| Create_Cinematic_Transport(X,Y,Z,U,V,W,R,S,T) | X = string(object type), Y = number(playerID), Z = position, U = number(angle), V = number(phase), W = number, R = number, S = number, T = hint(?) | -                             |
| Cinematic_Zoom(X,Y)                | X = transition time(number), Y = zoom factor(number) | Zoom in for Y < 1, out for Y > 1. X sets the time for the transition to the zoomed state. Crashes the script if used when cinematic camera is off.  |
| Transition_To_Tactical_Camera(X)   | X = number(time)                | -                                                                        |
| Transition_Cinematic_Camera_Key(X,Y,Z,U,V,W,R,S,T) | X = position, Y = time, Z = x coord, U = y coord, V = z coord, W = 0,1, R = game object or 0, S = 0,1, T = 0,1(?) | Transition the camera position to a new position. Setting W to 1 switches Y,Z,U from cartesian coordinates to spherical coordinates (Y being the radius and U being the angle in the x-y-plane).   |
| Set_Cinematic_Camera_Key(X,Y,Z,U,V,W,R,S) | X = position, Y = x coord, Z = y coord, U = z coord, V = 0,1, W = game object or 0, R = 0,1, S = 0,1(?) | Set a camera position                             |
| Transition_Cinematic_Target_Key(X,Y,Z,U,V,W,R,S,T) | X = position, Y = time, Z = x coord, U = y coord, V = z coord, W = 0,1, R = game object or 0, S = 0,1, T = 0,1(?) | Transition the camera target  (what the camera is pointing at) to a new position in Y seconds.   |
| Set_Cinematic_Target_Key(X,Y,Z,U,V,W,R,S) | X = position, Y = x coord, Z = y coord, U = z coord, V = 0,1, W = game object or 0, R = 0,1, S = 0,1(?) | Set a target position for the camera to point at. If W is given, the camera will follow its movements. Without W the parameters R and S(?) won't work. If R is 1, the function uses W's coordinate system.        |
| End_Cinematic_Camera()             | -                               | -                                                                        |
| Start_Cinematic_Camera(X)          | X = bool(default is true)       | -                                                                        |
| Point_Camera_At(X)                 | X = game object or position     | -                                                                        |
| Rotate_Camera_To(X,Y,Z)            | X = number(z angle), Y = number(time), Z = number(optional) | Rotates the tactical camera to the new angle. The rotation takes the given amount of time. Can be used during camera sequences but only affects the tactical camera. |
| Rotate_Camera_By(X,Y)              | X = number(z angle), Y = number(time) | Rotates the tactical camera around the z axis by the given amount of degrees. The sign of the angle determines the direction of the rotation. The rotation takes the given amount of time. |
| Zoom_Camera(X,Y)                   | X = number<1(zoom), Y = 0 or 1        | Zooms in the tactical camera. For X = 0 it is fully zoomed in, for X = 1 it is fully zoomed out. If Y is 1, the zoom happens immediately, if it is 0 there is a short transition like zooming in manually. |
| Camera_To_Follow(X,Y)              | X = game object, Y = number(immediate, optional) | -                                                       |
| Scroll_Camera_To(X)                | X = game object or position     | Scroll the tactical camera to the given position                                      |
| Fade_Screen_Out(X)                 | X = number(time)                | Fade screen into blackness                                               |
| Fade_Screen_In(X)                  | X = number(time)                | Fade screen back from blackness                                          |
| Fade_Off()                         | -                               | Turn off blackness from fade                                             |
| Fade_On()                          | -                               | Make screen black immediately                                            |
| Letter_Box_Out(X)                  | X = number(time)                | Move black bars at the top and bottom out of the screen                  |
| Letter_Box_In(X)                   | X = number(time)                | Move black bars at the top and bottom into the screen                    |
| Letter_Box_Off()                   | -                               | Get rid of black bars immediately                                        |
| Letter_Box_On()                    | -                               | Show black bars immediately                                              |
| Do_End_Cinematic_Cleanup()         | -                               | Hide and disables all units not marked by In_End_Cinematic. Ignores space stations and structures.  |

## Media and environment
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Weather_Audio_Pause(X)             | X = bool                        | -                                                                        |
| Master_Volume_Restore(?)           | -                               | Throws "preserved_volume != VOLUME_INVALID". Tried with no arguments and a number as argument. |
| Allow_Localized_SFX(X)             | X = bool                        | -                                                                        |
| SFXManager.Allow_Ambient_VO(X)     | X = bool                        | -                                                                        |
| SFXManager.Allow_Enemy_Sighted_VO(X) | X = bool                      | -                                                                        |
| SFXManager.Allow_HUD_VO(X)         | X = bool                        | -                                                                        |
| SFXManager.Allow_Unit_Reponse_VO(X) | X = bool                       | The name is misspelled.                                                  |
| SFXManager.Allow_Localized_SFXEvents(X) | X = bool                   | -                                                                        |
| Remove_All_Text()                  | -                               | Removes screen texts.                                                       |
| Stop_All_Speech()                  | -                               | -                                                                        |
| Resume_Mode_Based_Music()          | -                               | -                                                                        |
| Stop_All_Music()                   | -                               | -                                                                        |
| Play_Music(X)                      | X = string(music event)         | Plays a music event from MusicEvents.xml                                                       |
| Stop_Bink_Movie()                  | -                               | -                                                                        |
| Play_Bink_Movie(X)                 | X = string(movie)               | Plays a movie event from Movies.xml                                                |
| Set_New_Environment(X)             | X = integer                     | Unverified: the integer refers to map environments, which are defined as an enum.    |
| Force_Weather()                    | -                               | Turn on weather effects                                                  |
| Enable_Distance_Fog(X)             | X = bool                        | -                                                                        |
| Enable_Fog(X)                      | X = bool                        | -                                                                        |
| Play_Lightning_Effect(X,Y,Z)       | X = string(effect), Y = position, Z = position | Creates a lightning effect from LightningEffectTypes.xml between the two given positions. Returns a LightningEffectBlockStatus. Duration of the effect may be limited. |


## Randomization
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| GameRandom(X, Y)                   | X = integer, Y = integer        | Returns random integer between X and Y (uses game time as seed)          |
| GameRandom.Get_Float()             | -                               | Returns random float between 0 and 1                                     |
| GameRandom.Get_Float(X, Y)         | X = number, Y = number          | Returns random float between X and Y                                     |
| GameRandom.Free_Random(X, Y)       | X = integer, Y = integer        | Returns random integer between X and Y (unverified: uses real time as seed)  |


## Multithreading

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Create_Thread(X, Y)                | X = function name as string or a function, Y = anything     | Starts the function X (more precisely, the function at _G[X]; a function value is accepted as well) in a new thread on the next frame with parameter Y and returns the thread ID (an integer). A string that does not name a function is a script error. A thread is resumed once per service of its script. A save game holds every live thread, and each resumes where it was saved (see [Game-level transitions](lua-script-lifecycle.md#2-game-level-transitions)). If Y is a table, its contents will be copied into a new list which is given to the function, the keys of the original table will be lost.      |
| Thread(X, Y)                       | X = function name as string, Y = anything     | Unverified: the same as Create_Thread                      |
| Thread.Create(X, Y)                | X = function name as string, Y = anything     | Unverified: the same as Create_Thread                      |
| Thread.Kill(X)                     | X = thread ID (integer)         | Stops the thread with ID X                                               |
| Create_Thread.Kill(X)              | X = thread ID (integer)         | -                                                                        |
| Thread.Kill_All()                  | -                               | -                                                                        |
| Create_Thread.Kill_All()           | -                               | -                                                                        |
| Thread.Is_Thread_Active(X)         | X = thread ID (integer)         | -                                                                        |
| Create_Thread.Is_Thread_Active(X)  | X = thread ID (integer)         | -                                                                        |
| Thread.Get_Name(X)                 | X = thread ID (integer)         | Returns the name of the main function ("main" or the function name passed to Create_Thread)     |
| Create_Thread.Get_Name(X)          | X = thread ID (integer)         | -                                                                        |
| Thread.Get_Current_ID()            | -                               | Returns the ID of the current thread                                     |
| Create_Thread.Get_Current_ID()     | -                               | -                                                                        |

## Global values
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| GlobalValue.Get(X)                 | X = string                      | Get a copy of the value set for X, or nil if X was never set. See [The GlobalValue store](lua-script-lifecycle.md#4-the-globalvalue-store). |
| GlobalValue.Set(X,Y)               | X = string, Y = value           | Set a copy of value Y for identifier X, accessible to all Lua scripts. See [The GlobalValue store](lua-script-lifecycle.md#4-the-globalvalue-store) for the accepted values, copying and lifetime.     |

## Thread values
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| ThreadValue(X)                     | X = string                      | Get the value set for X                                                  |
| ThreadValue.Get(X)                 | X = string                      | Get the value set for X                                                  |
| ThreadValue.Set(X,Y)               | X = string, Y = value           | Set a value Y for identifier X. This value is specific to a thread as defined by Create_Thread.    |
| ThreadValue.Reset()                | -                               | Takes no argument and clears the stored thread values. The store is part of the script state and survives pooled reuse; `Common_Base_Definitions` (PGBaseDefinitions) calls this function. |

## Discrete distributions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| DiscreteDistribution.Create()      | -                               | Returns a discrete distribution object                                   |

### Discrete distribution object
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Insert(X,Y)                       | X = anything?, Y = number       | -                                                                        |
| .Sample()                          | -                               | -                                                                        |

## Weighted type lists
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| WeightedTypeList.Create()          | -                               | Returns a weighted type list object                                      |
| EvaluateTypeList(X,Y,Z)            | X = player, Y = game object, Z = weighted type list | returns a list                                       |

### Weighted type list object
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Parse(X,Y)                        | X = list of types(or categories?), Y = list of numbers | -                                                 |

## Fog of war reveal
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| FogOfWar.Reveal_All(X)             | X = player                      | Reveals the entire map for player X. Returns a reveal handle object that can be used to undo the reveal. |
| FogOfWar.Reveal(X,Y,Z)             | X = player, Y = position, Z = number(radius)    | Reveals FoW at Y with radius Z for player X (in some vanilla source scripts a 4th parameter is used; unverified: it has no effect). Returns a reveal handle object that can be used to undo the reveal.      |
| FogOfWar.Temporary_Reveal(X,Y,Z)   | X = player, Y = position, Z = number(radius)    | Reveals FoW at Y with radius Z for player X for about 5 seconds.    |
| FogOfWar.Disable_Rendering(X)      | X = bool                         | X = true makes units visible that should be hidden by the Fog of War.   |

### Reveal handle functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Undo_Reveal()                     | -                               | -                                                                        |


# XML event manipulation
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Story_Event(X,Y)                   | X = string, Y = game object?(optional)    | Trigger a STORY_AI_NOTIFICATION event                          |
| Check_Story_Flag(X,Y,Z,U)          | X = player, Y = string, Z = game object, U = bool |Checks if corresponding reward type TRIGGER_AI has fired.    |
| Get_Story_Plot(X)                  | X = string (story_file_name.xml)     | Returns the story file as StoryPlotWrapper object. The parameter is case sensitive.   |

## StoryPlotWrapper functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Get_Event(X)                      | X = string(Event name)          | Returns the xml event as StoryEventWrapper object.                       |
| .Suspend()                         | -                               | Suspends the plot                                                        |
| .Activate()                        | -                               | Activates the plot                                                       |
| .Reset()                           | -                               | Resets all events of the plot                                            |

## StoryEventWrapper functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Set_Reward_Type(X)                | X = string(reward type)         | -                                                                        |
| .Set_Reward_Parameter(X,Y)         | X = number, Y = something that makes sense   | Sets Reward_Param(X+1) as Y (X is 0 for Reward_Param1).     |
| .Set_Event_Parameter(X,Y)          | X = number, Y = something that makes sense   | Sets Event_Param(X+1) as Y (X is 0 for Event_Param1).       |
| .Set_Dialog(X)                     | X = string(dialog file name)    | Sets the dialog file.                                                    |
| .Clear_Dialog_Text()               | -                               | -                                                                        |
| .Add_Dialog_Text(X,...)            | X = string(text identifier from dat file) | The text will be formatted with any additional parameters given.     |

## PositionWrapper functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Get_XYZ()                         | -                               | Returns the three coordinate values of the position. Exists in steam version only since the January 2021 patch.       |

# GameObjectWrapper functions

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Despawn()                         | -                               | Removes the object from the game                                         |
| .Get_Planet_Location()             | -                               | Returns the planet object (galactic only)                                      |
| .Move_To(X)                        | X = Object or Position          | Moves the Object to X, returns a UnitMovementBlockStatus object          |
| .Move_To(X, Y)                     | X = Unit_List, Y = Object       | Moves Unit_List to Y in formation (does Object have to be contained in X?), returns a UnitMovementBlockStatus object    |
| .Attack_Move(X)                    | X = Object/Position             | Returns a UnitMovementBlockStatus object                                 |
| .Attack_Move(X, Y)                 | X = Unit_List, Y = Object/Position  | Returns a UnitMovementBlockStatus object                             |
| .Attack_Target(X)                  | X = Object                      | Attack X, returns a UnitMovementBlockStatus object. Tactical only.       |
| .Attack_Target(X, Y)               | X = Unit_List, Y = Object       | Attack Y with Unit_List (does the object have to be part of Unit_List?), returns a UnitMovementBlockStatus object    |
| .Guard_Target(X)                   | X = PositionsObject             | Returns a UnitMovementBlockStatus object                                 |
| .Guard_Target(X, Y)                | X = Unit_List, Y = Object       | Guard Y with Unit_List (does the object have to be part of Unit_List?), returns a UnitMovementBlockStatus object    |
| .Can_Move()                        | -                               | Returns true if the unit can currently move (is false e.g. during hyperspace in)    |
| .Stop()                            | -                               | Stops the unit. Tactical only.                                           |
| .Suspend_Locomotor(X)              | X = true / false                | movability on or off                                                     |
| .Get_Position()                    | -                               | Returns Position of the Object                                           |
| .Enable_Behavior(X, Y)             | X = Number of behavior, Y = true / false | Enables specific behavior                                       |
| .Activate_Ability(X, Y)            | X = AbilityName (string), Y = true / false  | Activates untargeted ability                                 |
| .Activate_Ability(X, Y)            | X = AbilityName (string), Y = Object or location | Activates targeted ability                              |
| .Reset_Ability_Counter()           | -                               | Finishes ability cooldown                                                |
| .Set_Single_Ability_Autofire(X, Y) | X = AbilityName (string), Y = true / false  | -                                                            |
| .Set_All_Abilities_Autofire(X)     | X = bool                        | -                                                                        |
| .Is_Ability_Autofire(X)            | X = AbilityName (string)        | Returns true or false                                                    |
| .Is_Under_Effects_Of_Ability(X)    | X = AbilityName (string)        | Returns true or false                                                    |
| .Is_Ability_Active(X)              | X = AbilityName (string)        | Returns true or false                                                    |
| .Is_Ability_Ready(X)               | X = AbilityName (string)        | Returns true or false                                                    |
| .Has_Ability(X)                    | X = AbilityName (string)        | Returns true or false                                                    |
| .Force_Ability_Recharge(X, Y)      | X = string, Y = number(optional)| -                                                                        |
| .Cancel_Ability(X)                 | X = string(ability)             | -                                                                        |
| .Take_Damage(X, Y)                 | X = Damage points               | -                                                                        |
| -                                  | Y(optional) = Hardpoint(string) | -                                                                        |
| .Are_Engines_Online()              | -                               | Returns true or false                                                    |
| .Override_Max_Speed(X)             | X = number                      | -                                                                        |
| .Cinematic_Hyperspace_In(X)        | X = integer (number of frames)  | Makes unit hyperspace into battle with delay by X frames (unverified: spawning many units with different delays at the same time spawns all units with the same delay anyway)  |
| .Hyperspace_Away(X)                | X = true/false (default is true)| Makes unit leave into hyperspace. If X is true, the unit gets deleted from the galactic campaign    |
| .Cancel_Hyperspace()               | -                               | -                                                                        |
| .Prevent_AI_Usage(X)               | X = true / false                | Allow or prevent AI usage. In tactical battles this crashes the game if the unit has no active AI. When the factions AI changes, the unit is AI usable again.   |
| .Hide(X)                           | X = true / false                | (Un)Hides the object                                                     |
| .Play_Animation(X, Y, Z)           | X = Animation name (string)     | -                                                                        |
| -                                  | Y = bool                        | -                                                                        |
| -                                  | Z = integer                     | -                                                                        |
| .Change_Owner(X)                   | X = PlayerObject                | Sets objects owner to new faction                                        |
| .In_End_Cinematic(X)               | X = true / false                | Shall object be displayed in Cinematic?                                  |
| .Teleport(X)                       | X = PositionsObject             | Teleport object to X. Tactical only.                                     |
| .Teleport_And_Face(X)              | X = Object or position          | Teleport object to X and make it face the same way as X. Tactical only.  |
| .Face_Immediate(X)                 | X = PositionsObject             | Make unit face toward X immediately                                      |
| .Turn_To_Face(X)                   | X = PositionsObject             | Make unit turn to face toward X                                          |
| .Prevent_Opportunity_Fire(X)       | X = true / false                | Prevent automatically firing at targets in range                         |
| .Prevent_All_Fire(X)               | X = true / false                | Completely prevent a unit from firing                                    |
| .Make_Invulnerable(X)              | X = true / false                | Stops object from taking any damage. Tactical only.                      |
| .Set_Check_Contested_Space(X)      | X = true / false                | Make the unit/fleet not trigger space tactical battles?                  |
| .Get_Parent_Object()               | -                               | For fleets this is a PlanetObject, for units in galactic mode it's the fleet, for ground forces it's the transport?, for fighters it's the squadron |
| .Lock_Current_Orders()             | -                               | Only for units belonging to AI players                                   |
| .Unlock_Current_Orders()           | -                               | Only for units belonging to AI players                                   |
| .Is_In_Asteroid_Field()            | -                               | -                                                                        |
| .Is_In_Ion_Storm()                 | -                               | -                                                                        |
| .Is_In_Nebula()                    | -                               | -                                                                        |
| .Get_Type()                        | -                               | Returns the unit's type (GameObjectTypeWrapper object)                   |
| .Is_Corrupted()                    | -                               | Use on planets                                                           |
| .Enable_Dynamic_LOD(X)             | X = bool                        | -                                                                        |
| .Invade()                          | -                               | Only for fleets with land units in orbit over an enemy planet (is used in the FoC campaign; unverified: does not work in a regular galactic campaign)                 |
| .Set_In_Limbo(X)                   | X = bool                        | -                                                                        |
| .Get_All_Projectile_Types()        | -                               | Returns a list of the projectile types (GameObjectTypeWrappers) the unit uses    |
| .Is_Selectable()                   | -                               | -                                                                        |
| .Set_Selectable(X)                 | X = bool                        | Sets a unit to be selectable or not selectable by the player             |
| .Get_Current_Projectile_Type()     | -                               | Returns the projectile type the unit is currently using                  |
| .Should_Switch_Weapons(X)          | X = game object or ai target    | Returns true if alternate weaponry of the unit is better against (?)  X  |
| .Is_Good_Against(X)                | X = game object or ai target    | Determines if a unit is strong against another unit by using the Set_Contrast_Values() function in PGAICommands. If the value is smaller than 1 it returns false, if it's greater or 1, it returns true                                                                        |
| .Is_In_Garrison()                  | -                               | Is the unit garrisoned                                                   |
| .Get_Garrisoned_Units()            | -                               | Returns a list of units garrisoned inside the object                     |
| .Has_Garrison()                    | -                               | Returns true if the object contains any garrisoned units                 |
| .Eject_Garrison()                  | -                               | Eject all garrisoned units                                               |
| .Leave_Garrison()                  | -                               | Make a garrisoned unit leave its garrison           |
| .Can_Garrison_Fire()               | -                               | -                                                                        |
| .Can_Garrison(X)                   | X = game object or ai target    | Can the unit be garrisoned in X?                  |
| .Garrison(X)                       | X = game object or ai target    | Garrison the unit in X                                                         |
| .Get_Attack_Target()               | -                               | -                                                                        |
| .Can_Land_On_Planet(X)             | X = game object (planet)        | Can the unit land on planet X?                      |
| .Get_Is_Planet_AI_Usable()         | -                               | Can only be used on planets                                                         |
| .Play_Cinematic_Engine_Flyby()     | -                               | -                                                                        |
| .Stop_SFX_Event(X,Y)               | X = string, Y = number(optional)| -                                                                        |
| .Attach_Particle_Effect(X,Y)       | X = type or type name, y = string(optional) | -                                                                        |
| .Has_Attack_Target()               | -                               | -                                                                        |
| .Show_Emitter(X, Y)                | X = string(emitter), Y = bool   | -                                                                        |
| .Highlight_Small(X, Y)             | X = bool, Y = number(optional)  | Put a small arrow highlight on top of the object              |
| .Highlight(X, Y)                   | X = bool, Y = number(optional)  | Put an arrow highlight on top of the object                 |
| .Explore_Area(X)                   | X = ai target location          | -                                                                        |
| .Disable_Capture(X)                | X = bool                        | -                                                                        |
| .Force_Test_Space_Conflict()       | -                               | Enforce check if a space battle should be initiated, e.g. after spawning a fleet at an enemy planet (only works on fleets and planets)                  |
| .Play_SFX_Event(X,Y)               | X = string, Y = number(optional)| Plays an SFX event. For Y = 0 the sound is played normally, for higher values it becomes louder over time until it reaches full volume. Caution: only a limited number of SFX events can be played at a time (defined by the Max_Instances tag of the preset). Trying to play more than the allowed number will crash the script, even if the command is called for different units or from different scripts. |
| .Set_Cannot_Be_Killed(X)           | X = bool                        | Keep a unit from dying (it can still be damaged)     |
| .Get_Hint()                        | -                               | -                                                                        |
| .Set_Garrison_Spawn(X)             | X = bool                        | Turn spawn of garrison units on/off                    |
| .Fire_Tactical_Superweapon()       | -                               | Fire death star in tactical                                                        |
| .Is_Tactical_Superweapon_Ready()   | -                               | Test if death star is ready to fire                   |
| .Get_Bone_Position(X)              | X = string(bone name)           | -                                                                        |
| .Lock_Build_Pad_Contents(X)        | X = bool                        | -                                                                        |
| .Is_Planet_Destroyed()             | -                               | -                                                                        |
| .Get_Affiliated_Indigenous_Type(X) | X = player                      | Use on planets. Returns the indigenous unit type of that planet affiliated with X            |
| .Is_On_Diversion()                 | -                               | -                                                                        |
| .Has_Property(X)                   | X = string(property flag)       | -                                                                        |
| .Destroy_Contained_Objects(X)      | X = number                      | Only use on fleets                                                               |
| .Contains_Object_Type(X)           | X = game object type            | Only use on fleets                                                      |
| .Get_Contained_Object_Count()      | -                               | Only use on fleets                                                       |
| .Has_Active_Orders()               | -                               | -                                                                        |
| .Get_AI_Power_Vs_Unit(X)           | X = game object                 | (tactical only)                                                                        |
| .Divert(X,Y)                       | X = object or position, Y = number(optional)  | -                                                                        |
| .Get_Next_Starbase_Type()          | -                               | Use on planets                                                            |
| .Mark_Parent_Mode_Object_For_Death() | -                             | Use in tactical. This kills the corresponding galactic object       |
| .Set_Importance(X)                 | X = number                      | -                                                                        |
| .Service_Wrapper()                 | -                               | -                                                                        |
| .Cancel_Event_Object_In_Range(X)   | X = function                    | -                                                                        |
| .Event_Object_In_Range(X,Y,Z)      | X = function, Y = number(distance), Z = player(optional) | Calls X(self, trigger_object) continually for each trigger_object affiliated with Z in range |
| .Get_Final_Blow_Player()           | -                               | Used on planets, returns a player                   |
| .Get_Starbase_Level()              | -                               | Only used on planets(?)                                                          |
| .Get_Owner()                       | -                               | -                                                                        |
| .Sell()                            | -                               | Possibly only for build pad contents                  |
| .Get_Build_Pad_Contents()          | -                               | Use on build pads or MDUs                                                             |
| .Get_Distance(X)                   | X = position                    | Returns a number                                                      |
| .Get_Contained_Heroes()            | -                               | Only for fleets?                                                          |
| .Contains_Hero()                   | -                               | Only for fleets                                                          |
| .Fire_Special_Weapon(X,Y)          | X = game object(target), Y = player(user)  | Use on space station apparently          |
| .Get_Rate_Of_Damage_Taken()        | -                               | -                                                                        |
| .Get_Time_Till_Dead()              | -                               | -                                                                        |
| .Set_Targeting_Stickiness_Time_Threshold(X)  | X = number            | -                                                                        |
| .Set_Targeting_Priorities(X)       | X = string(targeting priority set) | -                                                                        |
| .Set_Prefer_Ground_Over_Space(X)   | X = bool                        | Object needs UNIT_AI behavior               |
| .Get_Game_Scoring_Type()           | -                               | -                                                                        |
| .Is_Category(X)                    | X = string(category name)       | Can use pipe to concatenate categories             |
| .Get_Shield()                      | -                               | Normalized wrt total shield points (i.e. returns number between 0 and 1). Tactical only.          |
| .Get_Energy()                      | -                               | Normalized wrt units total energy. Tactical only. |
| .Get_Health()                      | -                               | Normalized wrt units total health. Tactical only. |
| .Get_Hull()                        | -                               | Normalized wrt units total health. Tactical only. `Get_Health` and `Get_Hull` are the same function.  |
| .Is_Transport()                    | -                               | Use in galactic                                                               |
| .Release()                         | -                               | -                                                                        |
| .Build(X,Y)                        | X = type or type name, Y = bool(optional)? | Use on buildpads and MDUs               |
| .Get_Name()                        | -                               | -                                                                        |
| .Get_Object_ID()                   | -                               | Returns the object's ID (a number). Not available in older versions of the game. |
| .Get_Parent_Mode_Object()          | -                               | In a tactical battle, returns the corresponding object of the parent (galactic) game mode. Not available in older versions of the game. |
| .Get_Parent_Mode_Object_ID()       | -                               | Returns the object ID of that parent mode object (a number). Not available in older versions of the game. |


# GameObjectTypeWrapper functions
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Get_Name()                        | -                               | Returns the name of the game object type (the xml name)      |
| .Get_Combat_Rating()               | -                               | Returns the AI_Combat_Power      |
| .Is_Hero()                         | -                               | Returns true/false          |
| .Get_Build_Cost()                  | -                               | Returns build cost          |
| .Get_Tech_Level()                  | -                               | Returns required tech level |
| .Get_Base_Level()                  | -                               | Returns level of a starbase type     |
| .Is_Affiliated_With(X)             | X = player                      | -                           |
| .Is_Build_Locked(X)                | X = player                      | -                           |
| .Is_Obsolete(X)                    | X = player                      | -                           |
| .Get_Tactical_Build_Cost()         | -                               | -                           |
| .Get_Score_Cost_Credits()          | -                               | -                           |
| .Get_Max_Range()                   | -                               | -                           |
| .Get_Min_Range()                   | -                               | -                           |
| .Get_Bribe_Cost(X)                 | X = game object                 | Returns a number            |
| .Is_Affected_By_Missile_Shield()   | -                               | This is used only for projectile types       |
| .Is_Affected_By_Laser_Defense()    | -                               | This is used only for projectile types       |

# PlayerWrapper functions
| Function                      | Parameters              | Usage                          |
|-------------------------------|-------------------------|--------------------------------|
| .Enable_Advisor_Hints(X, Y)   | X = "space" or "ground" | Enables Advisor Hints          |
| -                             | Y = true / false        | -                              |
| .Get_ID()                     | -                       | returns ID of PlayerObject     |
| .Get_Enemy()                  | -                       | Returns an enemy player (unverified: it only ever returns Rebel or Empire; in any case it is of little use outside the base EaW, though it might be related to the Primary Enemy tag)   |
| .Select_Object(X)             | X = Object              | Forces player to select object |
| .Enable_As_Actor()            | -                       | Activates the AI for that player   |
| .Retreat()                    | -                       | Enables retreat event          |
| .Get_Name()                   | -                       | returns the displayed faction name |
| .Get_Faction_Name()           | -                       | returns xml faction name       |
| .Get_Tech_Level()             | -                       | -                              |
| .Is_Human()                   | -                       | -                              |
| .Give_Random_Sliceable_Tech() | -                       | -                              |
| .Give_Money(X)                | X = amount (integer/float?) | -                          |
| .Make_Ally(X)                 | X = player              | Gets reset with any game mode changes, in particular at the end of every tactical battle.     |
| .Make_Enemy(X)                | X = player              | Gets reset with any game mode changes, in particular at the end of every tactical battle.   |
| .Get_Space_Station()          | -                       | Returns the player's space station in space tactical       |
| .Get_Team()                   | -                       | Team ID in skirmish            |
| .Get_Clan_ID()                | -                       | Clan ID in skirmish            |
| .Remove_Orbital_Bombardment(X) | X = bool               | -                              |
| .Disable_Orbital_Bombardment(X) | X = bool              | -                              |
| .Set_Sabotage_Tutorial(X)     | X = bool                | -                              |
| .Set_Black_Market_Tutorial(X) | X = bool                | -                              |
| .Get_Difficulty()             | -                       | Returns "Easy", "Normal" or "Hard"     |
| .Disable_Bombing_Run(X)       | X = bool                | X = false disables bombing run for the given faction in ground tactical, X = true enables it     |
| .Is_Ally(X)                   | X = player              | -                              |
| .Is_Enemy(X)                  | X = player              | -                              |
| .Unlock_Tech(X)               | X = GameObjectTypeWrapper | Fixed in steam version with the January 2021 patch. |
| .Lock_Tech(X)                 | X = GameObjectTypeWrapper | Added to steam version with the January 2021 patch. |
| .Get_GameSpy_Stats_Player_ID() | -                      | -                              |
| .Get_Credits()                | -                       | -                              |
| .Release_Credits_For_Tactical(X)| X = Number (optional?) | For AI player (with galactic AI) only. Releases credits for spending in (land only?) mode.                             |
| .Set_Tech_Level(X)            | X = Number               | -                              |
| .Is_Neutral()                 | -                       | -                              |
| .Is_Valid()                   | -                       | -                              |

# AI

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Evaluate_In_Galactic_Context(X,Y)  | X = string(perception), Y = player | For tactical battle (tactical only). Evaluates the perception at galactic level and returns a number. |
| Apply_Markup(X,Y,Z)                | X = player, Y = game object, ai target or list, Z = number | The engine checks for exactly three arguments.                |
| Purge_Goals(X)                     | X = player                      | -                                                                        |
| GiveDesireBonus(X,Y,Z,U,V)         | X = player, Y = string(goal(set?)), Z = ai target, U = number, V = number | -                              |
| EvaluatePerception(X,Y,Z)          | X = string(perception), Y = player, Z = game object/ai target | Evaluates a perception and returns the result. Y and Z are needed if and only if the perception uses Variable_Self and Variable_Target, respectively.  |
| _FindStageArea(X,Y,Z)              | X = player, Y = game object/ai target, Z = taskforce | Deprecated but may still work as intended           |
| _ProduceObject(X,Y,Z)              | X = player, Y = game object type (name?), Z = planet/ ai target | Deprecated but may still work as intended   |
| FindTarget(X,Y,Z,U,V)              | X = taskforce, Y = perception, Z = goal application flag, U = number(probability), V = number(range) | Find a target for a taskforce. Tries to find the one that the perception returns the highest value on.     |
| FindTarget.Reachable_Target(X,Y,Z,U,V,W,R) | X = player, Y = perception, Z = goal application, U = reachability, V = probability, W = ai target, R = range | Find a target for an aiplayer. Tries to find the one that the perception returns the highest value on.    |
| FindTarget.Best_Of(X,Y,Z)          | X = taskforce, Y = list of game objects/ai targets, Z = string(perception?) | -        |

## AITargetLocationWrapper
| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Get_Game_Object()                 | -                               | Returns corresponding game object if there is one (e.g. a targeted unit or planet).   |
| .Get_Distance(X)                   | X = position                    | -                                                                        |

## FreeStore functions

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| FreeStore.Is_Object_On_Free_Store(X) | X = game object               | -                                                                        |
| FreeStore.Get_Object_Count(X)      | X = bool(optional)              | Returns a number                                                         |
| FreeStore.Is_Unit_Safe(X)          | X = game object                 | Galactic only(?)                                                            |
| FreeStore.Is_Unit_In_Transit(X)    | X = game object                 | Galactic only(?)                                                                 |
| FreeStore.Move_Object(X,Y)         | X = game object, Y = planet     | Galactic only(?)                                                                 |


## Task force functions

| Function                           | Parameters                      | Usage                                                                    |
|------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| .Get_Goal_Type_Name()              | -                               | -                                                                        |
| .Test_Target_Contrast(X)           | X = bool                        | -                                                                        |
| .Get_Self_Threat_Sum()             | -                               | -                                                                        |
| .Get_Self_Threat_Max()             | -                               | -                                                                        |
| .Get_Unit_Table()                  | -                               | -                                                                        |
| .Clear_Opportunity_Fire_Event_Subscriptions() | -                    | -                                                                        |
| .Remove_Opportunity_Fire_Event_Subscription(X) | X = string          | -                                                                        |
| .Add_Opportunity_Fire_Event_Subscription(X)    | X = string          | -                                                                        |
| .Set_Plan_Result(X)                | X = bool                        | Sets plan to successful (true) or failed (false)                         |
| .Are_All_Units_On_Free_Store()     | -                               | Check if all required units are available in the free store              |
| .Get_Stage()                       | -                               | -                                                                        |
| .Unblock_Goal_Proposal()           | -                               | -                                                                        |
| .Block_Goal_Proposal()             | -                               | -                                                                        |
| .Collect_All_Free_Units()          | -                               | Add all units from the free store to the taskforce                       |
| .Release_Unit(X)                   | X = game object                 | -                                                                        |
| .Withdraw_Units()                  | -                               | Retreat                                                                  |
| .Release_Forces(X)                 | 0 < X < 1.0                     | -                                                                        |
| .Set_As_Goal_System_Removable(X)   | X = bool                        | (Dis)allow hardcoded AI systems to terminate the goal (and plan)         |
| .Get_Force_Count()                 | -                               | -                                                                        |
| .Produce_Force(X,Y)                | X = stage(optional), Y = bool(optional) | Assemble the taskforce a the given stage by building units or collecting them from the free store   |
| .Form_Units()                      | -                               | Forms a fleet object with the taskforces units                           |
| .Add_Force(X)                      | X = game object                 | Adds a unit to the taskforce                                             |
| .Get_Type_Of_Unit(X)               | X = number(index)               | -                                                                        |
| .Leave_Garrison()                  | -                               | -                                                                        |
| .Can_Garrison(X)                   | X = game object                 | -                                                                        |
| .Garrison(X)                       | X = game object                 | -                                                                        |
| .Set_All_Abilities_Autofire()      | -                               | -                                                                        |
| .Set_Single_Ability_Autofire(X,Y)  | X = string(ability name), Y = bool | -                                                                     |
| .Get_AI_Power_Vs_Unit(X)           | X = game object or ai target    | Tactical only. Returns a number.                                         |
| .Set_Targeting_Stickiness_Time_Threshold(X) | X = number             | -                                                                        |
| .Set_Targeting_Priorities(X)       | X = string(targeting priority set) | -                                                                     |
| .Move_To(X,Y,Z)                    | X = game object/position, Y = number(threat)(optional), Z = string(space fields)(optional) | Tactical only |
| .Attack_Move(X,Y,Z(?))             | X = game object/position, Y = number(threat)(optional), Z = string(space fields)(optional) | Tactical only |
| .Guard_Target(X,Y,Z(?))            | X = game object/taskforce, Y = number(threat)(optional), Z = string(space fields)(optional) | Tactical only |
| .Attack_Target(X,Y,Z)              | X = game object, Y = number(threat)(optional), Z = string(space fields)(optional) | Tactical only          |
| .Attack_Target(X,Y,Z)              | X = game object, Y = string (hardpoint type), Z = number (threat?)(optional?) | Tactical only              |
| .Release_Reinforcements(?)         | -                               | Tactical only                                                            |
| .Get_Reserved_Build_Pads()         | -                               | Tactical only                                                            |
| .Build_All()                       | -                               | Tactical only                                                            |
| .Reinforce(X,Y)                    | X = position, Y = number(optional) | Tactical only. Y is "maximum wait time".                              |
| .Prepare_Ambush(X,Y,Z,U,V?)        | X = position, Y = string(back, front, right, left?), Z = number>0, U = number, V = bool? | Tactical only (not used)  |
| .Find_Closest_Enemy(X,Y)           | X = string, Y = ?(optional)     | Tactical only                                                            |
| .Enable_Attack_Positioning(X)      | X = bool                        | Tactical only                                                            |
| .Explore_Area(X)                   | X = ai target location          | Tactical only                                                            |
| .Get_Distance(X)                   | X = position                    | Tactical only                                                            |
| .Fire_Special_Weapon(X,Y)          | X = string, Y = ai target/game object | Tactical only                                                      |
| .Build(X,Y)                        | X = string, Y = game object(build pad) | Tactical only                                                     |
| .Activate_Ability(X,Y)             | X = string(ability name), Y = bool | Tactical only                                                         |
| .Fire_Orbital_Bombardment(X)       | X = position                    | Land only                                                                |
| .Bombing_Run(X)                    | X = ai target or game object    | Land only                                                                |
| .Move_To(X)                        | X = game object(planet)         | Galactic only                                                                  |
| .Activate_Ability()                | -                               | Galactic only                                                                  |
| .Raid(X)                           | X = game object(planet)         | Galactic only                                                                  |
| .Is_Raid_Capable()                 | -                               | Galactic only                                                                  |
| .Refit_To_Definition(X,Y)          | X = game object(planet), Y = number | Galactic only                                                              |
| .Launch_Units()                    | -                               | Launches (land) units into orbit. Galactic only                                |
| .Land_Units()                      | -                               | Lands units on a planet. Galactic only                                         |
| .Invade()                          | -                               | Starts a ground invasion (unverified: requires very specific circumstances to work). Galactic only   |
| .Force_Test_Space_Conflict()       | -                               | Galactic only                                                                  |


## BudgetWrapper

| Function                                 | Parameters                      | Usage                                                                    |
|------------------------------------------|---------------------------------|--------------------------------------------------------------------------|
| Budget.Flush_Category(X)                 | X = string(goal category)       | -                                                                        |
| Budget.Flush_All_Resources()             | -                               | -                                                                        |
| Budget.Flush_Unallocated_Resources()     | -                               | -                                                                        |
| Budget.Take_Resources_From_Goal(X,Y)     | X = number>0, Y = string        | -                                                                        |
| Budget.Give_Resources_To_Goal(X,Y)       | X = number>0, Y = string        | -                                                                        |
| Budget.Wait_For_Unallocated_Resources(X) | X = number                      | -                                                                        |
| Budget.Wait_For_Spendable_Resources(X)   | X = number                      | -                                                                        |
| Budget.Allocate_Resources(X)             | X = number                      | -                                                                        |
| Budget.Get_Spendable_Resources()         | -                               | -                                                                        |
| Budget.Get_Unallocated_Resources()       | -                               | -                                                                        |


# LuaScriptWrapper

| Function                                | Parameters                      | Usage                                                                    |
|-----------------------------------------|---------------------------------|---------------------------------------|
| Script.Debug_Should_Issue_Event_Alert() | -                               | Method of the `Script` global (the script itself, not a LuaScriptWrapper). `PumpEvents` (PGBase) calls it after each event to decide whether to show `DebugEventAlert`. |
| .Is_Valid()                             | -                               | Returns true or false                 |
| .Call_Function(X, ...)                  | X = string, further arguments optional | -                              |
| .Set_Variable(X, Y)                     | X = string, Y = value           | -                                     |
| .Get_Variable(X)                        | X = string                      | -                                     |


# Task force events

Shown in the table are the default event handlers. Taskforce specific handlers can be defined by replacing the "Default" in the name with the taskforce name. These event handlers are not C functions provided for Lua but functions that can be defined in Lua (AI scripts) and are called by the engine under the respective circumstances.

| Function                                | Parameters                      | Usage                                                                    |
|-----------------------------------------|---------------------------------|---------------------------------------|
| Default_Production_Failed(X, Y)         | X = taskforce, Y = object type  | -                                     |
| Default_Unit_Destroyed()                | -                               | -                                     |
| Default_No_Units_Remaining()            | -                               | -                                     |
| Default_Original_Target_Owner_Changed(X, Y, Z) | X = taskforce, Y = old player, Z = new player | -                |
| Default_Current_Target_Owner_Changed(?) | ?                               | Unverified                            |
| Default_Special_Weapon_Online(X, Y)     | X = taskforce, Y = special weapon | -                                   |
| Default_Hardpoint_Target_In_Range(X, Y, Z) | X = taskforce, Y = unit, Z = target | -                              |
| Default_Hardpoint_Opportunity_Target_Acquired(?) | ?                      | Unverified                            |
| Default_Unit_Move_Finished(X, Y)        | X = taskforce, Y = unit         | -                                     |
| Default_Unit_Ability_Finished(X, Y)     | X = taskforce, Y = unit         | -                                     |
| Default_Unit_Diversion_Finished(X, Y)   | X = taskforce, Y = unit         | -                                     |
| Default_Unit_Ability_Cancelled(X, Y, Z) | X = taskforce, Y = unit, Z = ability name | -                           |
| Default_Unit_Ability_Ready(X, Y, Z)     | X = taskforce, Y = unit, Z = ability name | -                           |
| Default_Unit_No_Threat(?)               | ?                               | Unverified                            |
