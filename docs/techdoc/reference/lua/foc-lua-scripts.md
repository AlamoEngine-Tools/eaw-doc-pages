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
At startup the game enumerates `*.lua` in its own `Data\Scripts\AI`, `AI\SpaceMode`, `AI\LandMode`, `AI\StoryArc` and `Data\Scripts\Interventions` directories relative to the game directory, and then in the registered MegaFiles. A mod folder is not searched by that enumeration, so loose plan files in a mod directory are not loaded at startup. Plan files packed into a MegaFile the mod registers are expected to be enumerated (from the archive search; not tested). Scripts referenced by name later still resolve through the normal mod-aware script path.
Scripts in this folder are only recognized at startup if they are in the main game directory (i.e. not in a mod folder) or if a script of the same name is contained in a loaded .meg file. In the latter case the script from this folder overrides the one in the .meg.


# Evaluators
Scripts in this folder can be invoked by perceptions to run Lua commands to compute something. They contain a function `Evaluate` which is called when a perception invokes the script. Its return value is passed back to the perception.
They also contain a function `Clean_Up` to reset variables containing pointers. The game calls `Evaluator_Clean_Up`, which is implemented in PGBaseDefinitions and calls `Clean_Up`.


# FreeStore
The scripts in this folder handle the AI free store, i.e. they control those units that are not needed for any active AI plans.


# GameObject
Contains the unit scripts, which are attached to units with the `Lua_Script` tag. Each unit receives its own script state. States are pooled by default: when the unit dies, the game cleans the state with `Flush_G` and `Base_Definitions` and hands it to the next unit with the same script, so a number, string, boolean or function global that `Base_Definitions` does not reset carries over. [Lifecycle of one script state](lua-script-lifecycle.md#1-lifecycle-of-one-script-state) describes pooling, `ScriptPoolCount` and what `Flush_G` keeps.
The `main` function is called when the unit is spawned. Unit scripts usually require PGStateMachine, which implements the `main` function and offers state machine functionality, instead of defining their own.
Unit and structure scripts must set the variable `ServiceRate` to a number in the setup phase. If it is nil or not a number the script is never serviced at all and its `main` never runs. The shipped PGStateMachine library sets it to 0.2 before `Definitions` runs.


# Interventions
Here, the base game intervention scripts are defined. They are simply AI plans for the player that use some specific logic.


# Library
This folder contains library scripts that do not have a specific purpose on their own but rather provide common base functionality for other scripts.

Each library has its own page under Libraries, generated from the language server's Lua stubs,
with every function, its parameters and its globals; the one-line summaries that used to be
repeated here live in those stubs now.

* **PGDebug** ([`PGDebug.lua`](libraries/pgdebug.md)): Contains commands for debugging which are deactivated for the release build.
* **PGBase** ([`PGBase.lua`](libraries/pgbase.md)): Requires PGDebug. Defines some basic functionality.
* **PGBaseDefinitions** ([`PGBaseDefinitions.lua`](libraries/pgbasedefinitions.md)): Requires PGBase. Mainly defines/resets commonly used variables but also some additional functions.
* **PGCommands** ([`PGCommands.lua`](libraries/pgcommands.md)): Requires PGBaseDefinitions. Contains functions to set callbacks for certain events and some advanced unit/taskforce functionality.
* **PGAICommands** ([`PGAICommands.lua`](libraries/pgaicommands.md)): Requires PGCommands. Overrides `Base_Definitions` and sets values used in AI scripts. Also defines unit category contrast values for the AI.
* **PGTaskForce** ([`PGTaskForce.lua`](libraries/pgtaskforce.md)): Requires PGAICommands. Defines taskforce functions for AI scripts.
* **PGEvents** ([`PGEvents.lua`](libraries/pgevents.md)): Requires PGTaskForce. Defines default event handlers for taskforces and some helper functions.
* **PGStateMachine** ([`PGStateMachine.lua`](libraries/pgstatemachine.md)): Requires PGCommands. Implements a state machine.
* **PGStoryMode** ([`PGStoryMode.lua`](libraries/pgstorymode.md)): Requires PGStateMachine. Uses the state machine to handle story events.
* **PGMoveUnits** ([`PGMoveUnits.lua`](libraries/pgmoveunits.md)): Requires PGBaseDefinitions. Defines functions to use movement commands for unit lists.
* **PGSpawnUnits** ([`PGSpawnUnits.lua`](libraries/pgspawnunits.md)): Requires PGBaseDefinitions. Defines functions for reinforcing and to spawn a list of units.
* **PGInterventions** ([`PGInterventions.lua`](libraries/pginterventions.md)): Requires PGBaseDefinitions. Basic setup and helper functions for interventions.


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
