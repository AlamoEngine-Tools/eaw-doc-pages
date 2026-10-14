---
title: FoC Lua Scripts
summary: FoC Lua Scripts and their usages
authors: Commander Cody
tags:
  - Lua
  - Scripting
---
# Forces of Corruption Lua scripts
All scripts should define a function `Base_Definitions`, either directly or in one of their required scripts. The game calls it when a script state is created and again each time a pooled state is released, before the host globals are set; the [Lua script lifecycle](lua-script-lifecycle.md#5-script-setup) page describes the exact timing and what a save game restores instead.


# AI
Contains all galactic AI plans as well as subfolders "LandMode" and "SpaceMode" which contain the plans for the corresponding game modes.
Note that scripts in this folder are only recognized by the game if they are in the main game directory (i.e. not in a mod folder) or if a script of the same name is contained in a loaded .meg file. In the latter case the script from this folder overrides the one in the .meg.


# Evaluators
Scripts in this folder can be invoked by perceptions to run Lua commands to compute something. They contain a function `Evaluate` which is called when a perception invokes the script. Its return value is passed back to the perception.
They also contain a function `Clean_Up` to reset variables containing pointers. The game calls `Evaluator_Clean_Up`, which is implemented in PGBaseDefinitions and calls `Clean_Up`.


# FreeStore
The scripts in this folder handle the AI free store, i.e. they control those units that are not needed for any active AI plans.


# GameObject
Contains the unit scripts, which are attached to units with the `Lua_Script` tag. Each unit receives its own script state. States are pooled by default: when the unit dies, the game cleans the state with `Flush_G` and `Base_Definitions` and hands it to the next unit with the same script, so a number, string, boolean or function global that `Base_Definitions` does not reset carries over. [Lifecycle of one script state](lua-script-lifecycle.md#1-lifecycle-of-one-script-state) describes pooling, `ScriptPoolCount` and what `Flush_G` keeps.
The `main` function is called when the unit is spawned. Unit scripts usually require PGStateMachine, which implements the `main` function and offers state machine functionality, instead of defining their own.
Unit scripts must set the variable `ServiceRate` in the setup phase; otherwise the `main` function is not run.


# Interventions
Here, the base game intervention scripts are defined. They are simply AI plans for the player that use some specific logic.


# Library
This folder contains library scripts that do not have a specific purpose on their own but rather provide common base functionality for other scripts.

This page lists each library file with a one-line summary per function; the linked library pages document the functions in full.

## PGDebug
Contains commands for debugging which are deactivated for the release build. See [`PGDebug.lua`](libraries/pgdebug.md).

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
Requires PGDebug. Defines some basic functionality. See [`PGBase.lua`](libraries/pgbase.md).

| Function               | Arguments                          | Description                                                              |
|------------------------|------------------------------------|--------------------------------------------------------------------------|
| ScriptExit()           | - | Sets the engine's exit flag for the whole script; from then on the engine resumes none of the script's threads. See [`ScriptExit()`](libraries/pgbase.md#function-scriptexit) for the behaviour inside and outside a thread. |
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
| GetAbilityChanceSeed() | -                                  | Just the current game time in seconds. The EaW copy of the library returns `Dirty_Floor(GetCurrentTime()/10) + 9` instead. |
| GetChanceAllowed(difficulty) | -                            | Supposed to be difficulty dependent but always returns 100. The EaW copy of the library returns 20 for "Easy", 100 for "Hard" and 60 otherwise. |
| PlayerSpecificName(player_object, var_name) | player_object, var_name(string) | Returns `var_name` with a player specific prefix |
| Flush_G()              | -                                  | Resets a pooled script state: deletes global tables and engine object references and keeps numbers, strings, booleans and functions. See [`Flush_G()`](libraries/pgbase.md#function-flush_g) and [what a released state keeps](lua-script-lifecycle.md#12-removed-on-release-to-the-pool). |


## PGBaseDefinitions
Requires PGBase. Mainly defines/resets commonly used variables but also some additional functions. See [`PGBaseDefinitions.lua`](libraries/pgbasedefinitions.md).

| Function                      | Arguments | Description                                                             |
|-------------------------------|-----------|-------------------------------------------------------------------------|
| Common_Base_Definitions()     | -         | (Re)Sets all kinds of global variables. Only used in Base_Definitions() |
| Base_Definitions()            | -         | Calls `Common_Base_Definitions()` and `Definitions()` if it exists.     |
| Evaluator_Clean_Up()          | -         | Basic clean up function for evaluator scripts. Calls `Clean_Up()`.      |
| UnitListIsObscured(unit_list) | unit_list | Returns true if all given units are obscured by some space field.       |
| Cull_Unit_List(unit_list)     | unit_list | Removes all dead or otherwise invalid units from a list and returns it. |

## PGCommands
Requires PGBaseDefinitions. Contains functions to set callbacks for certain events and some advanced unit/taskforce functionality. See [`PGCommands.lua`](libraries/pgcommands.md).

!!! note "Forces of Corruption only"
    The functions from `Try_Garrison` to `Determine_Magic_Wait_Duration` exist only in the FoC copy of the library.

| Function                                 | Arguments | Description                                                             |
|------------------------------------------|-----------|-------------------------------------------------------------------------|
| WaitForever()                            | -         | Wait forever ... |
| Register_Timer(func, timeout, param)     | func, timeout, param(optional) | Sets up a callback `func(param)` after `timeout` (in seconds) has expired. |
| Process_Timers()                         | -         | Internal function to manage timers. |
| Cancel_Timer(func)                       | func      | Cancel timer for a given function. |
| Register_Death_Event(obj, func)          | obj, func | Sets up a call to `func` when the given object dies. |
| Process_Death_Events()                   | -         | Internal function to manage death callbacks. |
| Register_Attacked_Event(obj, func)       | obj, func | Sets up a call to `func` when the given object is first attacked and when it is no longer under attack. See [`Register_Attacked_Event()`](libraries/pgcommands.md#function-register_attacked_eventobj-func) for the arguments, which differ between the EaW and FoC copies of the library. |
| Process_Attacked_Events()                | -         | Internal function to manage attack callbacks. |
| Cancel_Attacked_Event(obj)               | obj       |  |
| Register_Prox(obj, func, range, player_filter) | obj, func, range, player_filter(optional) | Sets up a callback to `func(obj, trigger)`. The callback is executed continuously if not cancelled. Cancel by calling `obj.Cancel_Event_Object_In_Range(func)`. Does nothing in galactic mode. |
| Process_Proximities()                    | -         | Internal function that calls `Service_Wrapper` on units registered for proximity callbacks. |
| Pump_Service()                           | -         | Internal function that runs processing functions and `Story_Mode_Service` if it exists. Is called by `PumpEvents`. |
| Try_Ability(thing, ability_name, target) | thing, ability_name, target(optional, depends on ability) | `thing` can be a unit or taskforce. Activates ability if possible. Only activates ability if a difficulty dependent chance is successful (see `GetChanceAllowed`). In the FoC library that chance is always 100%; in the EaW library it depends on the owner's difficulty. |
| Use_Ability_If_Able(thing, ability_name, target) | thing, ability_name, target(optional, depends on ability) | `thing` can be a unit or taskforce. Activates ability if possible. |
| Is_A_Taskforce(thing)                    | thing     |  |
| ConsiderDivertAndAOE(object, ability_name, area_of_effect, recent_enemy_units, min_threat_to_use_ability) | object, ability_name, area_of_effect(number), recent_enemy_units(unit list), min_threat_to_use_ability(number) | This will consider diverting the passed object in order to use an area of effect ability centered on the unit. |
| OneOrMoreInRange(origin_unit, target_unit_list, range) | origin_unit, target_unit_list, range | Returns true if at least one of `target_unit_list` is inside the given range of `origin_unit` |
| PruneFriendlyObjects(obj_table)          | obj_table | Returns a new list with the objects of `obj_table` that do not belong to `PlayerObject`, i.e. it removes the friendly objects. `obj_table` itself is not changed. |
| Try_Garrison(tf, unit, offensive_only, range) | tf(optional), unit, offensive_only, range | Tries to garrison `unit`. Prefers places from which the unit can fire but will also find others if `offensive_only` is false. If `tf` is given, releases `unit` from `tf`. |
| Try_Deploy_Garrison(object, target, health_threshold) | object, target(optional), health_threshold(number) | Deploys units garrisoned in `object` if their health is high enough and there is no `target` or the garrisoned unit is good against the target. |
| Get_Special_Healer_Property_Flag(unit)   | unit      | Defines which heroes are healed by which type of healer. Also done for some special units. Used in free store and PGEvents. |
| Set_Land_AI_Targeting_Priorities(tf)     | tf        | Sets targeting priorities for the given taskforce. |
| Try_Weapon_Switch(object, target)        | object, target | Switches weapons if they are more effective against the given target. Requires a custom entry for each unit type that can switch weapons. |
| Determine_Magic_Wait_Duration()          | -         | Returns a wait duration for magic plans: 2400 minus the current game time in seconds, but at least 60. |

## PGAICommands
Requires PGCommands. Overrides `Base_Definitions` and sets values used in AI scripts. Also defines unit category contrast values for the AI. See [`PGAICommands.lua`](libraries/pgaicommands.md).

| Function                                 | Arguments | Description                                                             |
|------------------------------------------|-----------|-------------------------------------------------------------------------|
| Base_Definitions()                       | -         | Calls `Common_Base_Definitions`, sets some AI plan variables, resets taskforce variables and calls `Definitions` if it exists. See [`Base_Definitions()`](libraries/pgaicommands.md#function-base_definitions) for when it calls `Set_Contrast_Values`. |
| Set_Contrast_Values()                    | -         | Tells the AI how effective unit categories are against others. |

## PGTaskForce
Requires PGAICommands. Defines taskforce functions for AI scripts.

## PGEvents
Requires PGTaskForce. Defines default event handlers for taskforces and some helper functions.

## PGStateMachine
Requires PGCommands. Implements a state machine. See [`PGStateMachine.lua`](libraries/pgstatemachine.md).

## PGStoryMode
Requires PGStateMachine. Uses the state machine to handle story events. See [`PGStoryMode.lua`](libraries/pgstorymode.md).

## PGMoveUnits
Requires PGBaseDefinitions. Defines functions to use movement commands for unit lists. See [`PGMoveUnits.lua`](libraries/pgmoveunits.md).

## PGSpawnUnits
Requires PGBaseDefinitions. Defines functions for reinforcing and to spawn a list of units. See [`PGSpawnUnits.lua`](libraries/pgspawnunits.md).

## PGInterventions
Requires PGBaseDefinitions. Basic setup and helper functions for interventions.


# Miscellaneous
GameScoring, FleetEvents and other scripts without a folder of their own.


# Story
This is where all story scripts are as well as the .txt files that define the story logs.

## Lua scripts
Scripts in here can be used for galactic campaigns or tactical missions by setting them in a story plot .xml file.
`Base_Definitions` for these scripts is called during load of the galactic campaign or tactical mission. `main` is called when the respective game starts; story plot scripts usually rely on PGStoryMode and PGStateMachine rather than implementing their own `main` functions.
Unlike unit scripts, story plot scripts are not pooled by default and are discarded when the game mode ends, so they are loaded from the file again when they are needed. [Story plot scripts](lua-script-lifecycle.md#32-story-plot-scripts-lua_script-on-a-story-plot) describes the pooling rule and what a save game restores.
The game passes story events to the script by calling its `Story_Event_Trigger(name)` function (implemented in PGStoryMode).

## Dialog files
The dialog files in this folder are simple text files with a specific syntax that define the story log entries in galactic campaigns. The first entry starts with `[CHAPTER 0]`, comments start with `#`.

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
