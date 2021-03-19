---
title: FoC Lua Scripts
summary: FoC Lua Scripts and their usages
authors: Commander Cody
tags:
  - Lua
  - Scripting
---
# Forces of Corruption Lua Scripts
All scripts should have a function `Base_Definitions` defined, either directly or in one of their required scripts. This is called by the engine when the script is first loaded.


# AI
Contains all galactic AI plans as well as subfolders "LandMode" and "SpaceMode" which contain the plans for the corresponding game modes.
Note that scripts in this folder are only recognized by the game if they are in the main game directory (i.e. not in a mod folder) or if a script of the same name is contained in a loaded .meg file. In the latter case the script from this folder overrides the one in the .meg.


# Evaluators
Scripts in this folder can be invoked by perceptions to run Lua commands to compute something. They contain a function `Evaluate` which is called when a perception invokes the script. Its return value is passed back to the perception.
They also contain a function `Clean_Up` to reset variables containing pointers. The engine will actually call `Evaluator_Clean_Up` which is implemented in PGBaseDefinitions and calls `Clean_Up`.


# FreeStore
The scripts in this folder handle the AI freestore, i.e. they control those units that are not needed for any active AI plans.


# GameObject
Contains scripts that are attached to units with the `Lua_Script` tag. The game loads several instances of these scripts at once (given by the ScriptPoolCount) even if not all of them are needed. 
Each unit is assigned its own script instance. When a unit with a script dies, rather than discarding and reloading the script the game cleans up the script instance by calling `Flush_G` and `Base_Definitions` again and assigns it to the next unit that requires it.
The `main` function is called when the unit is spawned. Usually, object scripts simply require PGStateMachine which implements the `main` function and offers state machine functionality instead.
Object scripts require the variable `ServiceRate` to be set in the setup phase, otherwise the `main` function won't be run.


# Interventions
Here, the base game intervention scripts are defined. They are simply AI plans for the player that use some specific logic.


# Library
This folder contains library scripts that do not have a specific purpose on their own but rather provide common base functionality for other scripts.

## PGDebug
Contains commands for debugging which are deactivated for the release build.

| Function              | Arguments                          | Description                                                              |
|-----------------------|------------------------------------|--------------------------------------------------------------------------|
| DebugEventAlert(event, params) | event, list of parameters | Triggers a MessageBox with information on the event and parameters. |
| MessageBox(...)       | String and optionally values for formatting | Triggers a MessageBox with the formatted string. |
| ScriptMessage(...)    | String and optionally values for formatting | Logs the formatted string in the AI log. |
| DebugMessage(...)     | String and optionally values for formatting | Logs the formatted string in the AI log. |
| OutputDebug(...)      | String and optionally values for formatting | Logs the formatted string in the log file. |
| ScriptError(...)      | String and optionally values for formatting | Logs the formatted string in the log file and the AI log and exits the script. |
| DebugPrintTable(unit_table)  | table                       | Prints all values to the AI log. |

## PGBase
Requires PGDebug. Defines some basic functionality.

| Function               | Arguments                          | Description                                                              |
|------------------------|------------------------------------|--------------------------------------------------------------------------|
| ScriptExit()           | - | Immediately terminates the script without executing any other statements. |
| Sleep(time)            | time in seconds | Continue pumping events without doing anything else until the given game time has passed. |
| BlockOnCommand(block, max_duration, alternate_break_func) | block: an object that has methods `IsFinished` and `Result` | Waits until `block.IsFinished()` returns true, `alternate_break_func()` returns true or the given time runs out. If the block has finished, this returns `block.Result()`. Mainly used for unit movement commands and the reinforce command. |
|                        | max_duration in seconds (optional) |  |
|                        | alternate_break_func (optional)    |  |
| BreakBlock()           | -                                  | Breaks a BlockOnCommand (may have unexpected effects if a BlockOnCommand is running in multiple threads) |
| TestCommand(block)     | block: an object that has a method `IsFinished` | Runs `PumpEvents` once and returns `block.IsFinished()` |
| PumpEvents()           | -                                  | Implements threading and calls event handlers. Returns control to 'C' and continues on next service (i.e. after `ServiceRate` seconds). |
| TestValid(wrapper)     | wrapper: nil, game object          | Used to check validity of game objects. Returns `false` if `wrapper` is nil, doesn't have a function `Is_Valid` or `wrapper.Is_Valid()` is false.  |
| Clamp(value, min, max) | value, min, max: numbers           |  |
| Dirty_Floor(val)       | val: number                        | Returns `val` as string. Requires implicit string to int conversion of the return value. |
| Simple_Mod(a,b)        | a,b                                | Modulus function. |
| Chance(seed, percent)  | seed, percent                      | Requires a random `seed` between 0 and 99. Under those conditions it returns true with `percent` chance. |
| GetCurrentMinute()     | -                                  |  |
| GetAbilityChanceSeed() | -                                  | Just the current game time in seconds |
| GetChanceAllowed(difficulty) | -                            | Supposed to be difficulty dependent but always returns 100 |
| PlayerSpecificName(player_object, var_name) | player_object, var_name(string) | Returns `var_name` with a player specific prefix |
| Flush_G()              | -                                  | Used to reset object scripts. Deletes all tables except for a few 'very important' ones. Also deletes most userdata. |


## PGBaseDefinitions
Requires PGBase. Mainly defines/resets commonly used variables but also some additional functions.

| Function                      | Arguments | Description                                                             |
|-------------------------------|-----------|-------------------------------------------------------------------------|
| Common_Base_Definitions()     | -         | (Re)Sets all kinds of global variables. Only used in Base_Definitions() |
| Base_Definitions()            | -         | Calls `Common_Base_Definitions()` and `Definitions()` if it exists.     |
| Evaluator_Clean_Up()          | -         | Basic clean up function for evaluator scripts. Calls `Clean_Up()`.      |
| UnitListIsObscured(unit_list) | unit_list | Returns true if all given units are obscured by some space field.       |
| Cull_Unit_List(unit_list)     | unit_list | Removes all dead or otherwise invalid units from a list and returns it. |

## PGCommands
Requires PGBaseDefinitions. Contains functions to set callbacks for certain events and some advanced unit/taskforce functionality.

| Function                                 | Arguments | Description                                                             |
|------------------------------------------|-----------|-------------------------------------------------------------------------|
| WaitForever()                            | -         | Wait forever ... |
| Register_Timer(func, timeout, param)     | func, timeout, param(optional) | Sets up a callback `func(param)` after `timeout` (in seconds) has expired. |
| Process_Timers()                         | -         | Internal function to manage timers. |
| Cancel_Timer(func)                       | func      | Cancel timer for a given function. |
| Register_Death_Event(obj, func)          | obj, func | Sets up a call to `func` when the given object dies. |
| Process_Death_Events()                   | -         | Internal function to manage death callbacks. |
| Register_Attacked_Event(obj, func)       | obj, func | Sets up a call `func(true, attacker, obj)` when the given object is first attacked and a call `func(true, nil, obj)` when the given object is no longer under attack. The callback is not cancelled automatically at any point. |
| Process_Attacked_Events()                | -         | Internal function to manage attack callbacks. |
| Cancel_Attacked_Event(obj)               | obj       |  |
| Register_Prox(obj, func, range, player_filter) | obj, func, range, player_filter(optional) | Sets up a callback to `func(obj, trigger)`. The callback is executed continuously if not cancelled. Cancel by calling `obj.Cancel_Event_Object_In_Range(func)`. |
| Process_Proximities()                    | -         | Internal function that calls `Service_Wrapper` on units registered for proximity callbacks. |
| Pump_Service()                           | -         | Internal function that runs processing functions and `Story_Mode_Service` if it exists. Is called by `PumpEvents`. |
| Try_Ability(thing, ability_name, target) | thing, ability_name, target(optional, depends on ability) | `thing` can be a unit or taskforce. Activates ability if possible. Only activates ability if an ability dependent chance is successful. However, in vanilla that chance is always 100%. |
| Use_Ability_If_Able(thing, ability_name, target) | thing, ability_name, target(optional, depends on ability) | `thing` can be a unit or taskforce. Activates ability if possible. |
| Is_A_Taskforce(thing)                    | thing     |  |
| ConsiderDivertAndAOE(object, ability_name, area_of_effect, recent_enemy_units, min_threat_to_use_ability) | object, ability_name, area_of_effect(number), recent_enemy_units(unit list), min_threat_to_use_ability(number) | This will consider diverting the passed object in order to use an area of effect ability centered on the unit. |
| OneOrMoreInRange(origin_unit, target_unit_list, range) | origin_unit, target_unit_list, range | Returns true if at least one of `target_unit_list` is inside the given range of `origin_unit` |
| PruneFriendlyObjects(obj_table)          | obj_table | Removes any objects in `obj_table` that do not belong to `PlayerObject` and returns them in a new list. |
| Try_Garrison(tf, unit, offensive_only, range) | tf(optional), unit, offensive_only, range | Tries to garrison `unit`. Prefers places from which the unit can fire but will also find others if `offensive_only` is false. If `tf` is given, releases `unit` from `tf`. |
| Try_Deploy_Garrison(object, target, health_threshold) | object, target(optional), health_threshold(number) | Deploys units garrisoned in `object` if their health is high enough and there is no `target` or the garrisoned unit is good against the target. |
| Get_Special_Healer_Property_Flag(unit)   | unit      | Defines which heroes are healed by which type of healer. Also done for some special units. Used in free store and PGEvents. |
| Set_Land_AI_Targeting_Priorities(tf)     | tf        | Sets targeting priorities for the given taskforce. |
| Try_Weapon_Switch(object, target)        | object, target | Switches weapons if they are more effective against the given target. Requires a custom entry for each unit type that can switch weapons. |
| Determine_Magic_Wait_Duration()          | -         | Returns a wait duration for magic plans. |

## PGAICommands
Requires PGCommands. Overrides `Base_Definitions` and sets values used in AI scripts. Also defines unit category contrast values for the AI.

| Function                                 | Arguments | Description                                                             |
|------------------------------------------|-----------|-------------------------------------------------------------------------|
| Base_Definitions()                       | -         | Calls `Common_Base_Definitions`, sets some AI plan variables and resets taskforce variables. Also calls `Definitions` if it exists. |
| Set_Contrast_Values()                    | -         | Tells the AI how effective unit categories are against others. |

## PGTaskForce
Requires PGAICommands. Defines taskforce functions for AI scripts.

## PGEvents
Requires PGTaskForce. Defines default event handlers for taskforces and some helper functions.

## PGStateMachine
Requires PGCommands. Implements a state machine.

## PGStoryMode
Requires PGStateMachine. Uses the state machine to handle story events.

## PGMoveUnits
Requires PGBaseDefinitions. Defines functions to use movement commands for unit lists.

## PGSpawnUnits
Requires PGBaseDefinitions. Defines functions for reinforcing and to spawn a list of units.

## PGInterventions
Requires PGBaseDefinitions. Basic setup and helper functions for interventions.


# Miscellaneous
GameScoring, FleetEvents and random stuff


# Story
This is where all story scripts are as well as the .txt files that define the story logs.

## Lua Scripts
Scripts in here can be used for GCs or tactical missions by setting them in a story plot .xml file. 
`Base_Definitions` for these scripts is called during load of the GC/tactical mission. `main` is called when the respective game starts, however story scripts usually rely on PGStoryMode and PGStateMachine rather than implementing their own `main` functions.
Unlike object scripts, story scripts don't pool and are discarded when the game mode ends. As such, they are reloaded directly from the file when they are needed again.

## Dialog files
The dialog files in this folder are simple text files with a specific syntax that define the story log entries in GC. The first entry starts with `[CHAPTER 0]`, comments start with `#`.

| Command       | Arguments              | Description                                                              |
|---------------|------------------------|--------------------------------------------------------------------------|
| TITLE         | Textfile String        | The title shown directly over the main text body, not what is shown in the list of log entries.    |
| MOVIE         | Movies.xml entry       |     |
| WAIT          | Number (or `SPEECH`?)  |     |
| SFX           | Sfx event xml name     | Play SFX.  |
| TEXTCOLOR     | Four numbers 0-255     | Set text color of any text entries below this command using rgba color format.  |
| TEXT          | Textfile String        | Display textfile entry.    |
| NEWLINE       | Number                 | Add given number of empty lines   |
| EXTRA_TEXT    | -                      |               |
| DIALOG        | SpeechEvent xml name   |               |
| MOVIE_ONCE    | ?                      |               |
| MUSIC         | ?                      |               |
| ANIM          | ?                      |               |
| CLEARTEXT     | ?                      |                       |
| IMAGE         | ?                      |                       |
| CLEARIMAGE    | ?                      |                       |
| PAUSE         | ?                      |                       |
| LOADCINEMATIC | ?                      |                       |
| HIDECINEMATIC | ?                      |                       |
| STOPMOVIE     | ?                      |                       |
| WAIT_SPEECH   | ?                      |                       |
