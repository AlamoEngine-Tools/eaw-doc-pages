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

Triggers when the specified planet is corrupted.

---
#### STORY_OPEN_CORRUPTION
* Parameter 1: Planet

Triggers when the corruption menu for the specified planet is opened with a defiler.

---
#### STORY_CORRUPTION_TACTICAL_FAILED
* Parameter 1: Planet(?)

Never used.

---
#### STORY_CORRUPTION_TACTICAL_COMPLETE
* Parameter 1: Planet(?)

Never used.

---
#### STORY_GALACTIC_SABOTAGE
* Parameter 1: Building/orbital structure

Triggers when the specified building is destroyed using the sabotage ability.

---
#### STORY_BUY_BLACK_MARKET
* Parameter 1: Tech
 
Triggers once the given tech is bought. Tech is presumably the xml name of the tech type as defined in BlackMarketItems.

---
#### STORY_GARRISON_UNIT

Never used.

---
#### STORY_CORRUPTION_CHANGED
* Parameter 1: Planet
* Parameter 2: [Corruption type](#corruption-types)

---
#### STORY_CAPTURE_STRUCTURE
* Parameter 1: ?
* Parameter 2: ?

Parameters are probably structure type and faction.

---
#### STORY_OBJECTIVE_TIMEOUT

Never used. Would probably take an objective text string like the rewards setting objectives and the timeout.

---
#### STORY_INVASION_BOUNCED
* Parameter 1: Planet
* Parameter 5: ? (Used in demo script)

---
#### STORY_MISSION_LOST
* Parameter 1: File name of tactical plot

---
#### STORY_FLEET_BOUNCED
* Parameter 1: Planet

---
#### STORY_MOVIE_DONE

No parameters. Triggers when a movie started by `START_MOVIE` finishes.

---
#### STORY_VICTORY
* Parameter 1: Faction

Triggers when the specified faction wins.

---
#### STORY_CHECK_DESTROYED
* Parameter 1: Faction
* Parameter 2: [Destruction type](#destruction-types)

---
#### STORY_LOAD_TACTICAL_MAP

Never used. Uses Planet, Hero, GROUND/SPACE?

---
#### STORY_FLAG
* Parameter 1: Flag name
* Parameter 2: Number
* Parameter 3: [Comparison type](#comparison-types)

Triggers when the comparison becomes true. Flags can be set and manipulated by `SET_FLAG` and `INCREMENT_FLAG`. Note that the event can stop working if the flag name is too long (32 character limit (?)).

---
#### STORY_DIFFICULTY_LEVEL

Never used. Presumably, the difficulty level has to be specified in some way.

---
#### STORY_UNIT_PROXIMITY
* Parameter 1: Unit type?
* Parameter 2: Unit type
* Parameter 3: Distance

Used without parameter 1 in campaign. Without parameter 1 it triggers for every player unit?

---
#### STORY_GUARD_UNIT
* Parameter 1: Unit type
* Parameter 2: Unit type

---
#### STORY_ATTACK_HARDPOINT
* Parameter 1: Hard point name

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
* Parameter 3: Number (Probably distance, optional)

---
#### STORY_SELECT_UNIT
* Parameter 1: Unit type

---
#### STORY_AI_NOTIFICATION
* Parameter 2: String identifier

Triggered by calling the `Story_Event` function from Lua with the identifier as parameter. According to the story scripting tutorial that came with the map editor it also takes a comma separated list of planets. This might work if `Story_Event` actually takes a planet object as second parameter.

---
#### STORY_TRIGGER

No parameters. Triggers immediately (once the prerequites are met).

---
#### STORY_GENERIC
* Parameter 1: [Generic event type](#generic-event-types)

Multiple whitespace-separated event types can be specified?

---
#### STORY_FOG_POSITION_REVEAL

Never used.

---
#### STORY_FOG_OBJECT_REVEAL

Never used. Causes random crashes.

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
* Parameter 1: ? (optional if used at all)
* Parameter 2: Planet

---
#### STORY_REINFORCE

Never used.

---
#### STORY_RETREAT

Never used.

---
#### STORY_LOSE_BATTLES
* Parameter 1: Number
* Parameter 2: GROUND/SPACE
* Parameter 3: [Filter](#filter-types)

---
#### STORY_WIN_BATTLES
* Parameter 1: Number
* Parameter 2: GROUND/SPACE
* Parameter 3: [Filter](#filter-types)

---
#### STORY_DEFEAT_HERO
* Parameter 1: Unit type

---
#### STORY_CAPTURE_HERO

Never used, most likely a left-over.

---
#### STORY_ELAPSED
* Parameter 1: Number (seconds)

Triggers after the given time has passed.

---
#### STORY_CONQUER_COUNT
* Parameter 1: Number

Never used. Tends to be broken, use Lua instead.

---
#### STORY_ACCUMULATE
* Parameter 1: Number

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

Never used, probably left-over.

---
#### STORY_TECH_LEVEL
* Parameter 1: Number

---
#### STORY_BEGIN_ERA

Nver used, probably left-over.

---
#### STORY_TACTICAL_DESTROY
* Parameter 1: Unit type (comma separated list as "or" condition)
* Parameter 3: Number

---
#### STORY_DESTROY_BASE

Never used. Takes a planet, SPACE/GROUND/EITHER and a [filter](#filter-types)(?)

---
#### STORY_DESTROY
* Parameter 1: Unit type
* Parameter 2: Planet?
* Parameter 3: Number

According to the map editor doc there are also parameters for who does the destroying and for a filter.

---
#### STORY_CONSTRUCT_LEVEL
* Parameter 1: Planet
* Parameter 2: Number
* Parameter 3: GROUND/SPACE
* Parameter 4: [Filter](#filter-types)(?)

---
#### STORY_CONSTRUCT
* Parameter 1: Unit type
* Parameter 2: Number
* Parameter 3: [Filter](#filter-types)

Multiple unit types can be set (whitespace separated), however the counting behaves strangely. The event will trigger if the given number of units of the first type is built or one unit of the other types.

---
#### STORY_CONQUER
* Parameter 1: Planet
* Parameter 3: [Filter](#filter-types)

---
#### STORY_LAND_ON
* Parameter 1: Planet
* Parameter 2: [Filter](#filter-types)
* Parameter 3: Unit type
* Parameter 4: Unit type (required orbiting unit?)

---
#### STORY_ENTER
* Parameter 1: Planet (can be whitespace separated list)
* Parameter 2: [Filter](#filter-types)
* Parameter 3: Unit type (Comma or whitespace separated list for "and" condition)
* Parameter 4: Unit type (Units that must be present iirc)
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

---
#### GIVE_BLACK_MARKET
* Parameter 1: Black market item

---
#### REMOVE_CORRUPTION
* Parameter 1: Planet
* Parameter 2: Number (transition time)

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

Marks a tutorial as completed.

---
#### HIDE_STEAL_SLOT

No parameter.

---
#### SHOW_STEAL_SLOT
* Parameter 1: Planet

---
#### HIDE_RAID_SLOT

No parameter.

---
#### SHOW_RAID_SLOT
* Parameter 1: Planet

---
#### HIDE_SMUGGLE_SLOT

No parameter.

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

No parameters. Might be tutorial specific.

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

Never used.

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

No parameters. I don't think this does anything anymore.

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
* Parameter 6: Text color (r,g,b)
* Parameter 7: Text color scheme (`Task`, `Hint`, `System`, `Speech`, `Alien_Speech`)
* Parameter 8: Speech from SpeechEvents.xml
* Parameter 9: Movie from Movies.xml (Hologram shown by the droid advisor)
* Parameter 10: 1/0 (Loop the movie?; stop using `STOP_COMMANDBAR_MOVIE`)

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

Never used.

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

---
#### USE_RETRY_DIALOG

No parameters. Will cause the retry dialog to open if the player loses. The retry option will load the last (auto?) save. On steam this is currently somewhat broken since the auto-saves were disabled.

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

Can trigger events across plots (?)

---
#### SET_SPAWN
* Parameter 1: ? (Probably indigenous spawner type)
* Parameter 2: Number (Spawn percentage of some form)

Never used.

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
* Parameter 1: Planet
* Parameter 2: GROUND/SPACE
* Parameter 3: Faction (Attacker)
* Parameter 4: Map file name
* Parameter 5: Faction (Defender)
* Parameter 6: Unit type (pathfinder)
* Parameter 7: Plot file name
* Parameter 8: 1/0 (Use sandbox units; only for the player, AI will never have their sandbox units iirc)
* Parameter 9: 1/0/2 (Use default intro camera squence. `2` will keep the fleet in hyperspace until `Resume_Hyperspace_In` is called from lua; note that certain player actions will also cause the fleet to jump in so controls must be locked while the fleet is suspended in hyperspace)
* Parameter 10: 1/0 (Start faded out)
* Parameter 11: 1/0 (Start letterboxed)
* Parameter 12: [Battle result](#battle-result-types) (Only executed if the player wins, iirc)
* Parameter 13: 1/0 (Show battle pending dialog)
* Parameter 14: 1/0 (Allow pathfinder)

---
#### RESET_EVENT
* Parameter 1: Xml event name

Reset an event so it can be triggered again

---
#### RESET_BRANCH
* Parameter 1: Branch name
* Parameter 2: Event name

Reset all events of an entire branch so they can be triggered again. Also appears to trigger an optional event.

---
#### DISABLE_REINFORCEMENTS
* Parameter 1: 1/0
* Parameter 2: Faction

Applies to all players if no faction is specified.

---
#### REVEAL_ALL_PLANETS
* Parameter 1: 1/0

---
#### STORY_GOAL_COMPLETED
* Parameter 1: Story goal tag

---
#### HIGHLIGHT_OBJECT
* Parameter 1: Object type
* Parameter 2: 1/0
* Parameter 3: Number (Radar ID (?))

Highlights first found object. If Parameter 3 is not `-1`, a radar blip is added at the objects position

---
#### INCREMENT_FLAG
* Parameter 1: Flag name
* Parameter 2: Number (amount)

The given amount to increment can be positive or negative.

---
#### SET_FLAG
* Parameter 1: Flag name
* Parameter 2: Number

---
#### DUAL_FLASH
* Parameter 1: Number (duration in seconds)?
* Parameter 2: Number (delay between flashes)?

Never used. According to the map editor doc it requires two additional flash events afterwards which will then be flashed alternately back and forth.

---
#### REVEAL_PLANET
* Parameter 1: Planet
* Parameter 2: 1/0

Cannot be used to force un-reveal a planet that would is revealed because the player borders it.

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
* Parameter 2: 1/0 (`1` will not show the victory text or play the VO)

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

Disabled.

---
#### DISABLE_AUTORESOLVE

Disabled.

---
#### SET_TACTICAL_MAP
* Parameter 1: Map name
* Parameter 2: GROUND/SPACE/EITHER
* Parameter 3: Faction (Map owner)

Never used.

---
#### REMOVE_POWER_FROM_ALL
* Parameter 1: Unit type
* Parameter 2: Ability name

---
#### NEW_POWER_FOR_ALL
* Parameter 1: Unit type
* Parameter 2: Ability name

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

---
#### INVADE_PLANET
* Parameter 1: Planet
* Parameter 2: Unit type (optional)

---
#### DISABLE_BRANCH
* Parameter 1: Branch identifier
* Parameter 2: 1/0

---
#### DISABLE_STORY_EVENT
* Parameter 1: Event name
* Parameter 2: 1/0 (disable)
* Parameter 3: 1/0 (global)

Parameter three (should) allow disabling either the given event in the same plot or all events with this name in any plot.

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

Never used.

---
#### ZOOM_OUT

No parameters.

---
#### ZOOM_IN

No parameters.

---
#### SWITCH_SIDES
* Parameter 1: Faction

Switch the player controlled faction.

---
#### PICK_PLANET
* Parameter 1: [Filter](#filter-types)
* Parameter 2: Tag

Never used. This takes a [filter](#filter-types) and an identifier. The event will assign a planet that fulfills the filter condition to the identifier which can then be used e.g. in the Story_Var tag.

---
#### ENABLE_EVENT
* Parameter 1: [Tutorial event type](#tutorial-event-types)
* Parameter 2: Event type parameter (e.g. GUI element)

---
#### DISABLE_EVENT
* Parameter 1: [Tutorial event type](#tutorial-event-types)
* Parameter 2: Event type parameter (e.g. GUI element)

---
#### SCREEN_TEXT
* Parameter 1: Text file identifier
* Parameter 2: Number (seconds), defaults to 5
* Parameter 3: Unit type (variable that is inserted into the text; use `%s` as placeholder in the text)
* Parameter 4: `remove`
* Parameter 5: 1/0 (Use teletyping?)
* Parameter 6: Text color (r,g,b)
* Parameter 7: Text color scheme (`Task`, `Hint`, `System`, `Speech`, `Alien_Speech`)

Shows a text in the upper left corner for the given number of seconds. Use `-1` to keep the text on-screen indefinitely. The text can be removed again by using the event again with the same text file identifier and non-empty parameter 4.

---
#### HIDE_TUTORIAL_CURSOR
* Parameter 1: Identifier

Remove a flash.

---
#### FLASH_PLANET_GUI
* Parameter 1: Planet
* Parameter 2: [Flash type](#flash-types)
* Parameter 3: Fleet number (0,1,2(?))
* Parameter 4: Identifier (see `HIDE_TUTORIAL_CURSOR`)
* Parameter 5: True/False (should persist?)

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

Never used. The ground base changes don't seem to work. The starbase change seems to work but it throws an assertion error.

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
* REGION_ORGANIZE - consists of fleet slots, land slots, special structure slots in that order (?)
* REGION_NONE


# Unit categories

* CLASS_SUPER
* CLASS_CAPITAL
* CLASS_FRIGATE
* CLASS_CORVETTE
* CLASS_TRANSPORT
* CLASS_BOMBER
* CLASS_FIGHTER


# Contains filters

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

Possible values for the generic story event:

* retreat_complete
* retreat_clicked
* battle_end_closed
* click
* right_click
* slice_slot
* ability_slot(?)
* slice_dialog
* slice
* open_black_market_menu
* open_galactic_sabotage_menu
* start_fleet_drag
* start_land_drag
* land_to_space
* merge_fleets
* drag_land_to_space
* corruption_dialog
* increase_corruption
* decrease_corruption(?)
* super_laser_fired
* start_bombard
* CLOSE_STORY_DIALOG
* fleet_tooltip
* land_tooltip
* start_hyperspace
* zoomed_in
* zoomed_out
* activate_deployed_ability
* hero_neutralized
* drag_select


# Planet visibility modifiers<a name="planet-visibility-types"></a>

* Maximum
* None (removes any previously applied modifiers)

To be tested (some are definitely relics from earlier stages of the game):

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
