---
title: PGDebug.lua
tags:
  - LUA Library
  - FoC
---
# `PGDebug.lua`

## Functions

---

### `function DebugEventAlert(event, params)`

Opens a message box that contains the handled event and its parameters.

!!! warning "Deactivated in the release game"

---

### `function MessageBox(...)`

Opens a message box that contains the input string.

!!! warning "Deactivated in the release game"

---

### `function ScriptMessage(...)`

Prints a message to the `AILog.txt` if the command `aiff script` has been used in the ingame console.

---

### `function DebugMessage(...)`

Prints a debug message to the `AILog.txt` if the command `aiff script` has been used in the ingame console.

---

### `function OutputDebug(...)`

Prints a debug message directly to the `LogFile.txt`.
Usually used as error log.

---

### `function ScriptError(...)`

Prints an error log to `LogFile.txt` and `AILog.txt` including a stack trace, then calls [`ScriptExit()`](pgbase.md#function-scriptexit "PGBase.ScriptExit()"), which stops the whole script.

---

### `function DebugPrintTable(unit_table)`

Unpacks a table and prints its content to the `AILog.txt` if the command `aiff script` has been used in the ingame console.

!!! warning
    Only designed to unwrap tables that directly contain objects. Not suitable to unwrap any table.

---
