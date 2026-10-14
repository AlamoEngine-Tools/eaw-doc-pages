---
title: FoC XML events
summary: A reference for XML Story events and rewards in FoC
tags:
  - Xml
  - Events
---
# Events

#### STORY_CORRUPTION_INCREASED
* Parameter 1: Planet
* Parameter 2: [Corruption type](#corruption-types) (optional)

Another name for `STORY_CORRUPTION_CHANGED`: the game treats both names as the same event type, so it also triggers when the corruption of the planet decreases, not only when it increases.

---
#### STORY_OPEN_CORRUPTION
* Parameter 1: Planet

Triggers when the corruption menu for the specified planet is opened with a defiler.

---
#### STORY_CORRUPTION_TACTICAL_FAILED
* Parameter 1: Planet
* Parameter 2: [Corruption type](#corruption-types) (optional)

Never used. Triggers when a corruption tactical mission on the planet fails. Takes the same parameters as `STORY_CORRUPTION_CHANGED`.

---
#### STORY_CORRUPTION_TACTICAL_COMPLETE
* Parameter 1: Planet
* Parameter 2: [Corruption type](#corruption-types) (optional)

Never used. Triggers when a corruption tactical mission on the planet is completed. Takes the same parameters as `STORY_CORRUPTION_CHANGED`.

---
#### STORY_GALACTIC_SABOTAGE
* Parameter 1: Building/orbital structure

Triggers when the specified building is destroyed using the sabotage ability.

---
#### STORY_BUY_BLACK_MARKET
* Parameter 1: Tech
 
Triggers once the given tech is bought.

Tech is the `Name` of an item in `BlackMarketItems.xml`. Several names can be listed and the comparison ignores case. The two vanilla `Cloaking_Tech` events of the underworld focus demo campaign match no item (the item is `Vehicle_Cloaking_Tech`), so they can never trigger.

---
#### STORY_GARRISON_UNIT
* Parameter 1: Unit type
* Parameter 2: Number (count, optional)
* Parameter 3: [Filter](#filter-types) (optional)

Never used. Triggers when a unit of the given type is garrisoned. Parameters 2 and 3 are read the same way as for `STORY_DEFEAT_HERO`.

---
#### STORY_CORRUPTION_CHANGED
* Parameter 1: Planet
* Parameter 2: [Corruption type](#corruption-types)

---
#### STORY_CAPTURE_STRUCTURE
* Parameter 1: Structure type
* Parameter 2: Faction

The parameters are the structure type and the faction that captures it; the game looks up both names and requires the faction to exist.

---
#### STORY_OBJECTIVE_TIMEOUT
* Parameter 1: Number (seconds)
* Parameter 2: Objective text identifier (as used by `ADD_OBJECTIVE`)

Never used. Triggers when the objective has not been completed within the given time.

---
#### STORY_INVASION_BOUNCED
* Parameter 1: Planet
* Parameters 2 to 7: as for `STORY_ENTER`; the demo script's parameter 5 is the stealth flag.

---
#### STORY_MISSION_LOST
* Parameter 1: File name of tactical plot

---
#### STORY_FLEET_BOUNCED
* Parameter 1: Planet
* Parameters 2 to 7: as for `STORY_ENTER`

Triggers when a fleet is bounced away from a planet, e.g. one restricted with `SET_PLANET_RESTRICTED`.

---
#### STORY_MOVIE_DONE

No parameters. Triggers when a movie started by `START_MOVIE` finishes. `START_MOVIE` pauses the game, and evaluating this event is what resumes it.

---
#### STORY_VICTORY
* Parameter 1: Faction

Triggers when the specified faction wins.

---
#### STORY_CHECK_DESTROYED
* Parameter 1: Faction
* Parameter 2: [Destruction type](#destruction-types)
* Parameter 3: Object type

---
#### STORY_LOAD_TACTICAL_MAP

* Parameter 1: Planet
* Parameter 2: Hero unit type (optional)
* Parameter 3: GROUND/SPACE

Never used. Triggers when a tactical battle on the planet is loaded.

---
#### STORY_FLAG
* Parameter 1: Flag name
* Parameter 2: Number
* Parameter 3: [Comparison type](#comparison-types)

Triggers when the comparison becomes true. Flags can be set and manipulated by `SET_FLAG` and `INCREMENT_FLAG`. Flag names are case-insensitive and cut to 31 characters, so two names that only differ after the 31st character are the same flag. Flags are shared by all plots, galactic and tactical alike. `NOT_EQUAL_TO` is accepted but never triggers the event.

---
#### STORY_DIFFICULTY_LEVEL
* Parameter 1: Difficulty level name

Never used. Triggers when the game is played at the given difficulty level. An unrecognised name is reported as a warning.

---
#### STORY_UNIT_PROXIMITY
* Parameter 1: Unit type (optional, list)
* Parameter 2: Unit type (list)
* Parameter 3: Distance

Used without parameter 1 in campaign.

Without parameter 1 it checks every unit of the local player; with parameter 1 only units of the listed types. It triggers once a unit of a parameter 2 type is closer than the distance to such a unit. Projectiles are ignored and other players' units never trigger it.

---
#### STORY_GUARD_UNIT
* Parameter 1: Unit type (guard)
* Parameter 2: Unit type (guarded)

Triggers when a unit of the first type is ordered to guard a unit of the second type. With lists, the game pairs the n-th guard type only with the n-th guarded type; single values work as expected.

---
#### STORY_ATTACK_HARDPOINT
* Parameter 1: Hard point name

Triggers when the player orders units to attack the hard point, not when the hard point takes damage.

---
#### STORY_FULL_STOP

Never used.

---
#### STORY_UNIT_ARRIVED

Never used.

---
#### STORY_COMMAND_UNIT
* Parameter 1: Unit type
* Parameter 2: Unit type (optional)
* Parameter 3: Number (optional)

Parameter 3 is a distance and is only used together with parameter 2: the event then triggers when the commanded unit is of a parameter 1 type and a unit of a parameter 2 type is closer than the distance to the command's target position. Without parameter 2, or with a distance of 0, any command to a parameter 1 unit triggers it.

---
#### STORY_SELECT_UNIT
* Parameter 1: Unit type

---
#### STORY_AI_NOTIFICATION
* Parameter 1: Planets (list, optional)
* Parameter 2: Trigger strings (list)

Triggered by calling the `Story_Event` function from Lua with a trigger string as parameter. Planets go in parameter 1 and the trigger strings in parameter 2, as the vanilla files use it.

The planet list requires that `Story_Event` is called with the planet (or any other object whose type name is listed) as its second parameter. With a planet list, a `Story_Event` call without an object does not trigger the event; without a planet list, a call with an object does not trigger it either. Names are compared ignoring case.

---
#### STORY_TRIGGER

No parameters. Triggers immediately (once the prerequisites are met).

---
#### STORY_GENERIC
* Parameter 1: [Generic event type](#generic-event-types)

Multiple whitespace-separated event types can be specified; any one of them triggers the event. The names are compared case-insensitively.

---
#### STORY_FOG_POSITION_REVEAL
* Parameter 1: Position (three numbers: x y z)

Never used. Triggers when the position is revealed from the fog of war.

---
#### STORY_FOG_OBJECT_REVEAL
* Parameter 1: Object type

Never used. Triggers when an object of the given type is revealed from the fog of war. Causes random crashes.

---
#### STORY_SPEECH_DONE
* Parameter 1: Speech name from SpeechEvents.xml

---
#### STORY_CLICK_GUI
* Parameter 1: GUI element from CommandBarComponents.xml

---
#### STORY_ZOOM_OUT_PLANET
* Parameter 1: Planet

Never used.

---
#### STORY_ZOOM_INTO_PLANET
* Parameter 1: Planet

---
#### STORY_SELECT_PLANET
* Parameter 1: Planet

---
#### STORY_LAND_TACTICAL
* Parameter 1: Plot (xml file name) (optional)
* Parameter 2: Planet (optional)

Triggers when a land battle at the specified planet is triggered and loads the given plot for the battle.

---
#### STORY_SPACE_TACTICAL
* Parameter 1: Plot (xml file name) (optional)
* Parameter 2: Planet (optional)

Triggers when a space battle at the specified planet is triggered and loads the given plot for the battle.

---
#### STORY_PLANET_DESTROYED
* Parameter 1: Planet (optional; empty matches any planet)
* Parameter 2: [Filter](#filter-types)

The game reads this event with the parameters of `STORY_ENTER`, so the planet goes into parameter 1. The vanilla script puts the planet name into parameter 2, where it is read as a filter name; with parameter 1 empty, that event follows from these rules to trigger for any destroyed planet.

---
#### STORY_REINFORCE
* Parameter 1: Unit type
* Parameter 2: Number (count, optional)
* Parameter 3: [Filter](#filter-types) (optional)

Never used. Triggers when units of the given type are brought in as reinforcements in a tactical battle.

---
#### STORY_RETREAT
* Parameter 1: [Filter](#filter-types)

Never used. Triggers when a side retreats from a tactical battle.

---
#### STORY_LOSE_BATTLES
* Parameter 1: Number
* Parameter 2: GROUND/SPACE/EITHER
* Parameter 3: [Contains filter](#contains-filters) followed by [unit categories](#unit-categories) (optional)
* Parameter 4: Planet (optional)

Parameter 3 is only read when it holds at least two entries (a contains filter and one or more unit categories); a single entry such as `FILTER_FRIENDLY_ONLY`, as used in the vanilla scripts, is ignored.

---
#### STORY_WIN_BATTLES
* Parameter 1: Number
* Parameter 2: GROUND/SPACE/EITHER
* Parameter 3: [Contains filter](#contains-filters) followed by [unit categories](#unit-categories) (optional)
* Parameter 4: Planet (optional)

Parameter 3 is only read when it holds at least two entries (a contains filter and one or more unit categories); a single entry such as `FILTER_FRIENDLY_ONLY`, as used in the vanilla scripts, is ignored.

---
#### STORY_DEFEAT_HERO
* Parameter 1: Unit type
* Parameter 2: Number (count, optional)
* Parameter 3: [Filter](#filter-types) (optional)

---
#### STORY_CAPTURE_HERO
* Parameter 1: Unit type
* Parameter 2: Number (count, optional)
* Parameter 3: [Filter](#filter-types) (optional)

Never used, a left-over: the game never raises this event, so it can never trigger.

---
#### STORY_ELAPSED
* Parameter 1: Number (seconds)

Triggers after the given time has passed. The time is counted from the moment the event becomes active (its prerequisites are met), not from the start of the campaign. Time during which the galactic game is paused does not count.

---
#### STORY_CONQUER_COUNT
* Parameter 1: Number

Never used. Unreliable; Lua is the recommended alternative.

---
#### STORY_ACCUMULATE
* Parameter 1: Number
* Parameter 2: [Comparison type](#comparison-types) (optional)

Triggers when the given number of credits have been accumulated by the player.

---
#### STORY_MOVE
* Parameter 1: Unit type
* Parameter 2: Planet

---
#### STORY_DEPLOY
* Parameter 1: Unit type
* Parameter 2: Planet

---
#### STORY_POLITICAL_CONTROL

Never used, a left-over. The game has no implementation for this event type: an event of this type is dropped when the plot is loaded.

---
#### STORY_TECH_LEVEL
* Parameter 1: Number

---
#### STORY_BEGIN_ERA
* Parameter 1: Number (era)

Never used. Shares its implementation with `STORY_TECH_LEVEL`.

It is not a left-over. The era is the highest tech level any player has reached and is checked every frame, whereas `STORY_TECH_LEVEL` triggers on a single player's tech level change. Parameter 1 set to `-1` triggers on the next era change after the event became active.

---
#### STORY_TACTICAL_DESTROY
* Parameter 1: Unit type (comma separated list as "or" condition)
* Parameter 2: Planet (leave empty)
* Parameter 3: Number
* Parameter 4: [Filter](#filter-types) (optional)

The vanilla scripts leave parameter 2 empty. With an empty planet the event counts the destroyed objects directly; the planet and filter are only consulted when a planet is given.

---
#### STORY_DESTROY_BASE
* Parameter 1: Planet (optional)
* Parameter 2: SPACE/GROUND/EITHER
* Parameter 3: [Filter](#filter-types) (owner of the base)

Never used.

---
#### STORY_DESTROY
* Parameter 1: Unit type
* Parameter 2: Planet (optional)
* Parameter 3: Number
* Parameter 4: [Filter](#filter-types) (optional)

---
#### STORY_CONSTRUCT_LEVEL
* Parameter 1: Planet
* Parameter 2: Number
* Parameter 3: GROUND/SPACE

A parameter 4 (as in the vanilla tutorial script) is not read by the game.

---
#### STORY_CONSTRUCT
* Parameter 1: Unit type
* Parameter 2: Number
* Parameter 3: [Filter](#filter-types)

Multiple unit types can be set (whitespace separated), however the counting is irregular. The event triggers if the given number of units of the first type is built or one unit of the other types.

---
#### STORY_CONQUER
* Parameter 1: Planet
* Parameter 2: Number (count, optional)
* Parameter 3: [Filter](#filter-types)

---
#### STORY_LAND_ON
* Parameter 1: Planet
* Parameter 2: [Filter](#filter-types)
* Parameter 3: Unit type
* Parameter 4: Unit type (units already in orbit at the planet)
* Parameters 5 to 7: as for `STORY_ENTER`

Read with the same parameters as `STORY_ENTER`.

---
#### STORY_ENTER
* Parameter 1: Planet (can be whitespace separated list)
* Parameter 2: [Filter](#filter-types)
* Parameter 3: Unit type (Comma or whitespace separated list for "and" condition)
* Parameter 4: Unit type (Units that must already be in orbit at the planet, not in the arriving fleet)
* Parameter 5: 1/0 (Allow stealth units)
* Parameter 6: 1/0 (Allow only specified units to enter)
* Parameter 7: 1/0 (Allow only raid fleets)


# Rewards

#### ENABLE_CAMPAIGN_VICTORY_MOVIE
* Parameter 1: 1/0

---
#### UPDATE_OBJECTIVE
* Parameter 1: Old objective text string
* Parameter 2: New objective text string

Replaces the old text with the new one (doesn't change the numbering of the shown objectives).

---
#### ENABLE_GALACTIC_CORRUPTION_HOLOGRAM
* Parameter 1: Planet
* Parameter 2: 1/0

Turn on/off the holo message that plays after corrupting a planet.

---
#### RESTRICT_AUTORESOLVE
* Parameter 1: Planet
* Parameter 2: 1/0

---
#### ENABLE_COMBAT_CINEMATIC
* Parameter 1: 1/0

Never used.

---
#### ENABLE_FLEET_COMBINE
* Parameter 1: 1/0

---
#### RESTRICT_SABOTAGE
* Parameter 1: Planet
* Parameter 2: 1/0

---
#### RESTRICT_BLACK_MARKET
* Parameter 1: Planet
* Parameter 2: 1/0

Never used.

---
#### RESTRICT_CORRUPTION
* Parameter 1: Planet
* Parameter 2: 1/0

---
#### RESTRICT_ALL_ABILITIES
* Parameter 1: Planet
* Parameter 2: 1/0

Never used.

---
#### ENABLE_INVASION
* Parameter 1: Planet
* Parameter 2: 1/0

---
#### FLASH_ADVANCED_MAP_OBJECT
* Parameter 1: Unit/building type

For highlighting objects when zoomed into a planet.

---
#### ENABLE_SABOTAGE
* Parameter 1: 1/0

Never used.

---
#### SABOTAGE_STRUCTURE
* Parameter 1: Planet
* Parameter 2: Building

---
#### SHOW_SPECIAL_SLOT
* Parameter 1: Planet
* Parameter 2: [Ability slot](#galactic-ability-slots)
* Parameter 3: 1/0

`NEUTRALIZE_HERO_SLOT` is accepted but does nothing.

---
#### GIVE_BLACK_MARKET
* Parameter 1: Black market item

---
#### REMOVE_CORRUPTION
* Parameter 1: Planet
* Parameter 2: Number (transition time in seconds, defaults to 10)

Never used.

---
#### DISABLE_BOUNTY_COLLECTION

No parameters. Disables collecting credits for killed enemies in tactical battles.

---
#### ENABLE_BOUNTY_COLLECTION

No parameters. Enables collecting credits for killed enemies in tactical battles.

---
#### BOMBARD_DELAY
* Parameter 1: Number

---
#### FINISHED_TUTORIAL
* Parameter 1: Campaign name

Marks a tutorial as completed. The name is stored in the player profile exactly as written, without case folding; the vanilla scripts write it in upper case (`TUTORIAL_ONE`).

---
#### HIDE_STEAL_SLOT

No parameter. Undoes `SHOW_STEAL_SLOT`: the slot is no longer forced to be shown.

---
#### SHOW_STEAL_SLOT
* Parameter 1: Planet

---
#### HIDE_RAID_SLOT

No parameter. Undoes `SHOW_RAID_SLOT`: the slot is no longer forced to be shown.

---
#### SHOW_RAID_SLOT
* Parameter 1: Planet

---
#### HIDE_SMUGGLE_SLOT

No parameter. Undoes `SHOW_SMUGGLE_SLOT`: the slot is no longer forced to be shown.

---
#### SHOW_SMUGGLE_SLOT
* Parameter 1: Planet

---
#### LOCK_PLANET_SELECTION
* Parameter 1: 1/0

---
#### HIDE_CURSOR_ON_CLICK
* Parameter 1: 1/0

---
#### ENABLE_BUILDABLE
* Parameter 1: Unit/building type

Make a unit buildable again after it has been disabled using `DISABLE_BUILDABLE`.

---
#### DISABLE_BUILDABLE
* Parameter 1: Unit/building type

Disable a unit from being built. It will remain in the build bar greyed out.

---
#### HIDE_AUTORESOLVE

No parameter. Hides the autoresolve option when clicking retreat in tactical battles.

---
#### SHOW_COMMAND_BAR
* Parameter 1: 1/0

---
#### STOP_CINEMATIC_MODE

No parameters.

---
#### START_CINEMATIC_MODE

No parameters. Starts the galactic planet tour used by the tutorials; it lasts until `STOP_CINEMATIC_MODE`.

---
#### SET_ADVISOR
* Parameter 1: 1/0

Turn off the advisor by setting the parameter to 0.

---
#### RESET_GALACTIC_FILTERS

No parameters.

---
#### SKIRMISH_RULES
* Parameter 1: 1/0

---
#### SCROLL_LOCK
* Parameter 1: 1/0

---
#### FORCE_RESPAWN
* Parameter 1: Hero team

---
#### SET_SANDBOX_OBJECTIVES

No parameters.

---
#### ENABLE_OVERWHELMING_ODDS
* Parameter 1: 1/0

Never used. Does nothing: the game accepts the reward name but has no action wired to it.

---
#### UNPAUSE_GALACTIC

No parameters. Never used.

---
#### PAUSE_GALACTIC

No parameters. Never used.

---
#### TUTORIAL_PLAYER
* Parameter 1: Faction

Enables tutorial mode, in particular build times are much faster.

---
#### SET_MAX_TECH_LEVEL
* Parameter 1: Faction
* Parameter 2: Number

---
#### FLASH_SPECIAL_ABILITY
* Parameter 1: Ability type
* Parameter 2: Identifier

---
#### FLASH_PRODUCTION_CHOICE
* Parameter 1: Unit type
* Parameter 2: Identifier

For the hint to be seen, a planet where the unit can be built as well as the right build tab need to be selected.

---
#### FORCE_CLICK_GUI
* Parameter 1: GUI element from CommandBarComponents.xml

---
#### SELECT_PLANET
* Parameter 1: Planet

---
#### FLASH_FLEET_WITH_UNIT
* Parameter 1: Unit type
* Parameter 2: Identifier

---
#### ENABLE_OBJECTIVE_DISPLAY
* Parameter 1: 1/0

---
#### DISABLE_DIRECT_INVASION

No parameters.

It has no effect on play: the reward sets a flag that the game stores in save games but never reads. The same holds for the enable counterpart.

---
#### ENABLE_DIRECT_INVASION

Never used.

---
#### OBJECTIVE_FAILED
* Parameter 1: Text file string

Mark the given objective as failed on the objectives display.

---
#### REMOVE_ALL_OBJECTIVES

No parameters.

---
#### OBJECTIVE_COMPLETE
* Parameter 1: Text file string

Mark the given objective as completed on the objectives display.

---
#### REMOVE_OBJECTIVE
* Parameter 1: Text file string

Remove the objective from the display.

---
#### ADD_OBJECTIVE
* Parameter 1: Text file identifier

Add the text as objective on the objectives display.

---
#### PAUSE_GALACTIC_GAME
* Parameter 1: 1/0

Never used.

---
#### SET_PLANET_VISIBILITY_LEVEL
* Parameter 1: Planet
* Parameter 2: Faction
* Parameter 3: [Visibility modifier](#planet-visibility-types)
* Parameter 4: Tag
* Parameter 5: Number (duration)

---
#### MULTIMEDIA
* Parameter 1: Text file identifier
* Parameter 2: Number (duration; -1 to keep indefinitely; remove using `SCREEN_TEXT`)
* Parameter 3: Unit type (variable that is inserted into the text; use `%s` as placeholder in the text; other values may be possible as well)
* Parameter 4: 1/0 (use to remove a text; `remove` may also be a possible value)
* Parameter 5: 1/0 (Use teletype display)
* Parameter 6: Text color (three space-separated numbers: r g b)
* Parameter 7: Text color scheme (`Task`, `Hint`, `System`, `Speech`, `Alien_Speech`)
* Parameter 8: Speech from SpeechEvents.xml
* Parameter 9: Movie from Movies.xml (Hologram shown by the droid advisor)
* Parameter 10: 1/0 (unverified: loop the movie; stop using `STOP_COMMANDBAR_MOVIE`)

Functionally just a combination of `SCREEN_TEXT`, `SPEECH` and `COMMANDBAR_MOVIE`.

---
#### SET_PLANET_RESTRICTED
* Parameter 1: Planet
* Parameter 2: 1/0 (restrict planet)
* Parameter 3: 1/0 (restrict abilities)
* Parameter 4: 1/0 (turn red)

---
#### FORCE_RETREAT
* Parameter 1: Faction

Never used. Only has an effect in a tactical battle, and is skipped while a retreat is already underway.

---
#### LOCK_UNIT
* Parameter 1: Unit type

Make a unit non-buildable by removing it completely from the build bar.

---
#### PLANET_FACTION
* Parameter 1: Planet
* Parameter 2: Faction

Turn over a planet to a faction.

---
#### SET_WEATHER

Doesn't do anything.

---
#### STOP_COMMANDBAR_MOVIE

No parameters. Stops movies like the droid advisor holograms.

---
#### COMMANDBAR_MOVIE
* Parameter 1: Movie from Movies.xml
* Parameter 2: 1/0 (loop)

---
#### SET_PLANET_SPAWN
* Parameter 1: Planet
* Parameter 2: Indigenous spawn building
* Parameter 3: Number (float; Spawn percentage)

---
#### START_MOVIE
* Parameter 1: Movie from Movies.xml

Pauses the game while the movie plays. The game is resumed when a `STORY_MOVIE_DONE` event is evaluated, so a plot using this reward should have a `STORY_MOVIE_DONE` event armed; without one the game can stay paused.

---
#### USE_RETRY_DIALOG

No parameters. Will cause the retry dialog to open if the player loses. The retry option loads the last auto-save. On Steam this is partly broken, because the auto-saves were disabled.

---
#### ACTIVATE_RETRY_DIALOG

No parameters. Never used.

---
#### ENABLE_GALACTIC_REVEAL
* Parameter 1: 1/0

Enables or disables the automatic planet reveal in galactic mode.

---
#### TRIGGER_EVENT
* Parameter 1: Event name

It triggers the named event in every plot of the current game mode, including plots that are not active.

---
#### SET_SPAWN
* Parameter 1: Indigenous spawner type
* Parameter 2: Number (Spawn percentage of some form)

Never used. Both parameters are required; otherwise the reward only reports an error. Changes the indigenous spawn distribution.

---
#### SET_TECH_LEVEL
* Parameter 1: Faction
* Parameter 2: Number (level)

Also increases the player's max tech level if necessary.

---
#### DISABLE_SPECIAL_STRUCTURE
* Parameter 1: Object type
* Parameter 2: 1/0

Never used. Disables/enables shield behavior of first found object. 

---
#### RANDOM_STORY

No parameters. Never used. There are game constants entries that look like configuration for this.

---
#### LINK_TACTICAL
* Parameter 1: Planet (required)
* Parameter 2: SPACE/LAND (required)
* Parameter 3: Faction (Attacker; required)
* Parameter 4: Map file name (required)
* Parameter 5: Faction (Defender; required)
* Parameter 6: Hero unit type (optional)
* Parameter 7: Script name (optional)
* Parameter 8: 1/0 (Use sandbox units; only for the player; optional, default 0)

    Only a human player's units are carried into the battle; an AI side never gets its sandbox units.

* Parameter 9: Pre-battle cinematic mode (0 = no pre-battle cinematic, 1 = default cinematic, 2 = the attacking fleet is held in hyperspace until `Resume_Hyperspace_In()` is called from Lua; default 1, any other value behaves as 1)

* Parameter 10: 1/0 (Start faded out; default 0)
* Parameter 11: 1/0 (Start letterboxed; default 0)
* Parameter 12: [Battle result](#battle-result-types) (post-battle resolution name; an unknown name falls back to the default resolution and is logged)

    The resolution is only applied when the local player wins the battle; after a defeat the default outcome applies.

* Parameter 13: 1/0 (Show battle pending dialog; default 1)
* Parameter 14: 1/0 (Allow pathfinder; default 1)

If the game is currently in galactic mode the battle starts immediately, otherwise it is queued.

---
#### RESET_EVENT
* Parameter 1: Xml event name

Reset an event so it can be triggered again

---
#### RESET_BRANCH
* Parameter 1: Branch name
* Parameter 2: Event name

Reset all events of an entire branch so they can be triggered again. If parameter 2 is given, that event is triggered after the reset.

---
#### DISABLE_REINFORCEMENTS
* Parameter 1: 1/0
* Parameter 2: Faction

Applies to all players if no faction is specified.

---
#### REVEAL_ALL_PLANETS

No parameters. Reveals all planets on the galactic map for the local player.

---
#### STORY_GOAL_COMPLETED
* Parameter 1: Story goal tag

---
#### HIGHLIGHT_OBJECT
* Parameter 1: Object type
* Parameter 2: 1/0
* Parameter 3: Number (Radar ID)

Parameter 3 is the identifier of the radar blip; the same identifier removes the blip again when parameter 2 is `0`. `-1` or an empty parameter 3 adds no blip.

Highlights first found object. If Parameter 3 is not `-1`, a radar blip is added at the object's position.

---
#### INCREMENT_FLAG
* Parameter 1: Flag name
* Parameter 2: Number (amount)

The given amount to increment can be positive or negative. The flag must have been created with `SET_FLAG` first; incrementing an undefined flag is reported as an error.

---
#### SET_FLAG
* Parameter 1: Flag name
* Parameter 2: Number

Creates the flag if needed and sets it to the value. Flag names are case-insensitive and cut to 31 characters, so two names that only differ after the 31st character are the same flag. All plots share the same flags.

---
#### DUAL_FLASH
* Parameter 1: Number (duration in seconds)
* Parameter 2: Number (delay between flashes)

Never used. Both parameters are required; if either is empty the reward does nothing. According to the map editor doc it requires two additional flash events afterwards which will then be flashed alternately back and forth.

---
#### REVEAL_PLANET
* Parameter 1: Planet
* Parameter 2: 1/0

Cannot be used to force un-reveal a planet that is revealed because the player borders it.

---
#### FLASH_UNIT
* Parameter 1: [Commandbar region](#commandbar-regions)
* Parameter 2: Unit type

Never used.

---
#### DISABLE_RETREAT
* Parameter 1: Faction
* Parameter 2: 1/0

---
#### SWITCH_CONTROL
* Parameter 1: Faction
* Parameter 2: AI player or `Human`/`ScriptableHuman`

---
#### VICTORY
* Parameter 1: Faction
* Parameter 2: 1/0 (`1` will not show the victory text or play the VO, and shortens the delay before the victory from 7 to 1 second)

---
#### DESTROY_OBJECT
* Parameter 1: Unit type

Destroys the first found object of the given type.

---
#### CHANGE_OWNER
* Parameter 1: Object type
* Parameter 2: Faction
* Parameter 3: Number (0 meaning all)

---
#### REMOVE_STORY_GOAL
* Parameter 1: Story goal tag

---
#### DISABLE_MOVIES
* Parameter 1: 1/0

---
#### ENABLE_AUTORESOLVE

Disabled. Does nothing except write a log line; use `RESTRICT_AUTORESOLVE` per planet instead.

---
#### DISABLE_AUTORESOLVE

Disabled. Does nothing except write a log line; use `RESTRICT_AUTORESOLVE` per planet instead.

---
#### SET_TACTICAL_MAP
* Parameter 1: Map name
* Parameter 2: GROUND/SPACE/EITHER
* Parameter 3: Faction (Map owner): one of `Rebel`, `Empire`, `Pirates`, `Underworld` or `Hutts`, compared case-insensitively

Never used.

---
#### REMOVE_POWER_FROM_ALL
* Parameter 1: Unit type
* Parameter 2: Ability name

Despite the name, only affects the plot's local player.

---
#### NEW_POWER_FOR_ALL
* Parameter 1: Unit type
* Parameter 2: Ability name

Despite the name, only affects the plot's local player.

---
#### SET_HEALTH
* Parameter 1: Unit type
* Parameter 2: Percent (i.e. max 100)
* Parameter 3: Number of units (0 means all)

Never used.

---
#### FLASH_TERRAIN
* Parameter 1: Duration

Never used.

---
#### LOAD_CAMPAIGN
* Parameter 1: Campaign name (128 characters maximum)
* Parameter 2: Number (faction index)

Both parameters are required. The campaign that is started is the first campaign in the same `Campaign_Set` as the named one whose `Starting_Active_Player` is the faction at the given position in the faction list (counting from 0 in the order of Factions.xml), which is not necessarily the named campaign itself.

---
#### INVADE_PLANET
* Parameter 1: Planet
* Parameter 2: Unit type (optional)

Parameter 2 does not filter anything: a transport whose unit type differs is only noted in the log, and the invasion is issued either way.

---
#### DISABLE_BRANCH
* Parameter 1: Branch identifier
* Parameter 2: 1/0

---
#### DISABLE_STORY_EVENT
* Parameter 1: Event name
* Parameter 2: 1/0 (disable)
* Parameter 3: 1/0 (global)

Parameter 3 set to `1` disables every event with this name in all plots; otherwise only the event of the reward's own plot is affected. Parameters 1 and 2 are required.

---
#### TRIGGER_AI
* Parameter 1: Flag for Lua (see `Check_Story_Flag`)
* Parameter 2: Faction
* Parameter 3: Planet (optional)

---
#### MOVE_FLEET
* Parameter 1: Planet (from)
* Parameter 2: Planet (to)
* Parameter 3: [Filter](#filter-types) must be friendly only or enemy only.

All eligible fleets are merged and moved to the target.

---
#### ENABLE_VICTORY
* Parameter 1: 1/0

Works as a counter: every `0` adds one lock on victory and every `1` removes one, so two `0` rewards need two `1` rewards before a victory can be declared again.

---
#### ENABLE_FOW
* Parameter 1: 1/0

---
#### FLASH_OBJECT
* Parameter 1: Object type

Flashes the first found object.

---
#### SCROLL_CAMERA
* Parameter 1: Planet

---
#### LOCK_CONTROLS
* Parameter 1: 1/0

---
#### POSITION_CAMERA
* Parameter 1: Planet
* Parameter 2: Offset (e.g. `0,0,0`)

---
#### TUTORIAL_DIALOG
* Parameter 1: Text file identifier
* Parameter 2: 1/0 (`1` allows quit only)

---
#### FLASH_PLANET
* Parameter 1: Planet

Never used.

---
#### PAUSE_GAME

Never used. Opens the options menu rather than pausing the game directly; a second `PAUSE_GAME` closes it again.

---
#### ZOOM_OUT

No parameters.

---
#### ZOOM_IN

No parameters.

---
#### SWITCH_SIDES
* Parameter 1: Faction

Switch the player controlled faction. Does nothing in multiplayer games.

---
#### PICK_PLANET
* Parameter 1: [Filter](#filter-types)
* Parameter 2: Tag

Never used. This takes a [filter](#filter-types) and an identifier. The event will assign the first planet (in object order, not a random one) that fulfills the filter condition to the identifier which can then be used e.g. in the Story_Var tag.

---
#### ENABLE_EVENT
* Parameter 1: [Tutorial event type](#tutorial-event-types)
* Parameter 2: Event type parameter (e.g. GUI element)
* Parameter 3: Second event type parameter (optional)

---
#### DISABLE_EVENT
* Parameter 1: [Tutorial event type](#tutorial-event-types)
* Parameter 2: Event type parameter (e.g. GUI element)
* Parameter 3: Second event type parameter (optional)

---
#### SCREEN_TEXT
* Parameter 1: Text file identifier
* Parameter 2: Number (seconds), defaults to 5
* Parameter 3: Object type (optional; variable that is inserted into the text; use `%s` as placeholder in the text)
* Parameter 4: Any non-empty value removes the text of parameter 1 instead of showing it (the vanilla `remove` value is that form)
* Parameter 5: 1/0 (default 1; unverified: use teletyping)
* Parameter 6: Text color (three space-separated numbers: r g b)
* Parameter 7: Text style (`HINT`, `SYSTEM`, `TASK`, `ALIEN_SPEECH`, `SPEECH`)

Shows a text in the upper left corner for the given number of seconds. Use `-1` to keep the text on-screen indefinitely. The text can be removed again by using the event again with the same text file identifier and non-empty parameter 4.

---
#### HIDE_TUTORIAL_CURSOR
* Parameter 1: Identifier

Remove a flash.

---
#### FLASH_PLANET_GUI
* Parameter 1: Planet
* Parameter 2: [Flash type](#flash-types)
* Parameter 3: Fleet number

    The fleet number is 0, 1 or 2 and is only used for `FLASH_FLEET`.

* Parameter 4: Identifier (see `HIDE_TUTORIAL_CURSOR`)
* Parameter 5: Any non-empty value makes the tutorial cursor persistent; the text itself is not evaluated.

---
#### FLASH_GUI
* Parameter 1: GUI element
* Parameter 2: Identifier (see `HIDE_TUTORIAL_CURSOR`)

---
#### SPEECH
* Parameter 1: Speech event

---
#### SFX
* Parameter 1: SFX event

Never used.

---
#### STATISTIC_CHANGE
* Parameter 1: [Statistic type](#statistics-types)
* Parameter 2: Value
* Parameter 3: Planet

Never used.

`MAX_GROUND_BASE_LEVEL` and `MAX_SPECIAL_STRUCTS` do nothing: the game has no working setter for them. `MAX_STARBASE_LEVEL` works; setting it below the planet's `Max_Starbase_Level` from the XML is reported to raise an assertion error.

---
#### STORY_ELEMENT
* Parameter 1: Story file name (without extension)

Activate a story element that is currently suspended.

---
#### INFORMATION

Does nothing.

---
#### SPAWN_HERO
* Parameter 1: Hero team
* Parameter 2: Planet

Behaves exactly like `UNIQUE_UNIT` (same handler).

---
#### CREDITS
* Parameter 1: Number

---
#### REMOVE_UNIT
* Parameter 1: Unit type
* Parameter 2: If not set, only the first found unit of this type will be removed, otherwise all units of this type will be removed

---
#### UNIQUE_UNIT
* Parameter 1: Unit type
* Parameter 2: Planet
* Parameter 3: Number

Despite the name multiple units of the same type can be spawned.

---
#### BUILDABLE_UNIT
* Parameter 1: Unit type
* Parameter 2: Unit type to lock

Makes a locked unit buildable and optionally locks a unit to replace at the same time.


# Corruption types<a name="corruption-types"></a>

* CORRUPTION_ANY
* BONDED_CITIZENS
* BLACK_MARKET
* BRIBERY
* CORRUPT_MILITIA
* RACKETEERING
* KIDNAPPING
* PIRACY
* INTIMIDATION
* CORRUPTION_NONE


# Special ability slots<a name="galactic-ability-slots"></a>

* NEUTRALIZE_HERO_SLOT
* REMOVE_CORRUPTION_SLOT
* CORRUPTION_SLOT
* SABOTAGE_SLOT
* BLACK_MARKET_SLOT
* STEAL_SLOT
* SMUGGLE_SLOT
* RAID_SLOT


# Tactical battle result types<a name="battle-result-types"></a>

* DESTROY_AI
* RETREAT_AI
* RETREAT_PLAYER


# Destruction types<a name="destruction-types"></a>

* DESTROY_ALL_INDIGENOUS_SPAWNERS
* DESTROY_ALL_STRUCTURES
* DESTROY_ALL_UNITS
* DESTROY_ALL


# Commandbar regions<a name="commandbar-regions"></a>

* REGION_SELECTION
* REGION_PRODUCTION
* REGION_ORGANIZE

    Consists of fleet slots, land slots and special structure slots, searched in that order.

* REGION_NONE


# Unit categories<a name="unit-categories"></a>

* CLASS_SUPER
* CLASS_CAPITAL
* CLASS_FRIGATE
* CLASS_CORVETTE
* CLASS_TRANSPORT
* CLASS_BOMBER
* CLASS_FIGHTER


# Contains filters<a name="contains-filters"></a>

* ENEMY_ONLY_CONTAINS
* ENEMY_CONTAINS
* FRIENDLY_ONLY_CONTAINS
* FRIENDLY_CONTAINS


# Comparison types<a name="comparison-types"></a>

* LESS_THAN_EQUAL_TO
* GREATER_THAN_EQUAL_TO
* NOT_EQUAL_TO
* EQUAL_TO
* LESS_THAN
* GREATER_THAN


# Tutorial event types<a name="tutorial-event-types"></a>

* TUTORIAL_ALL
* TUTORIAL_ZOOM
* TUTORIAL_DRAG_FLEET
* TUTORIAL_CLICK_PLANET
* TUTORIAL_CLICK_GUI


# Flash types<a name="flash-types"></a>

* FLASH_PLANET
* FLASH_ABILITY_SLOT
* FLASH_WEATHER
* FLASH_PLANET_VALUE
* FLASH_SMUGGLED
* FLASH_SMUGGLER
* FLASH_COINS
* FLASH_PRODUCTION
* FLASH_CREDITS
* FLASH_BASE_BARS
* FLASH_PLANET_NAME
* FLASH_TROOPS
* FLASH_FLEET
* FLASH_AFFILIATION


# Planet statistics types<a name="statistics-types"></a>

* MAX_GROUND_BASE_LEVEL
* MAX_STARBASE_LEVEL
* MAX_SPECIAL_STRUCTS
* POLITICAL_CONTROL
* CREDIT_VALUE


# Filters<a name="filter-types"></a>

* FILTER_FRIENDLY_AND_ENEMY
* FILTER_ENEMY_AND_NEUTRAL
* FILTER_FRIENDLY_AND_NEUTRAL
* FILTER_ENEMY_ONLY
* FILTER_NEUTRAL_ONLY
* FILTER_FRIENDLY_ONLY
* FILTER_NONE


# Generic event types<a name="generic-event-types"></a>

Possible values for the generic story event. These are the names the game raises by itself; they are compared case-insensitively. A `STORY_GENERIC` event naming anything else can only be triggered by `TRIGGER_EVENT` or from Lua.

* retreat_complete
* retreat_clicked
* battle_end_closed
* click
* slice_slot
* ability_slot
* slice_dialog
* slice
* open_black_market_menu
* open_galactic_sabotage_menu
* start_fleet_drag
* start_land_drag
* land_to_space
* merge_fleets
* drag_land_to_space
* drag_unit
* corruption_dialog
* choose_corruption_option
* close_corruption_dialog
* increase_corruption
* decrease_corruption
* super_laser_fired
* start_bombard
* CLOSE_STORY_DIALOG
* fleet_tooltip
* land_tooltip
* tooltip
* start_hyperspace
* zoomed_in
* zoomed_out
* next_planet
* prev_planet
* previous_planet
* activate_deployed_ability
* hero_neutralized
* drag_select
* end_setup
* Continue_Tutorial

`right_click` is not raised by the game.


# Planet visibility modifiers<a name="planet-visibility-types"></a>

* Maximum
* None (removes any previously applied modifiers)

Untested values (some are relics from earlier stages of the game):

* Planet_Owner
* Underworld_Default
* Good_Default
* Evil_Default
* Super_Weapons
* Force_Sensitive_Heroes
* Most_Powerful_Ship
* Credit_Income_Breakdown
* Enemy_Major_Stealth_Heroes
* Enemy_Minor_Stealth_Heroes
* Object_Under_Production
* Political_Control_Breakdown
* Political_Control
* Special_Structures
* Ground_Company_Contents
* Num_Ground_Companies
* Fleet_Contents
* Num_Fleets
* Fleet_Presence
* Credit_Income
* Ground_Base_Level
* Starbase_Level
* Planet_Ownership
