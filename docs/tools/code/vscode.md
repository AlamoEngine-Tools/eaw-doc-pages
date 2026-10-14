---
title: VS Code
tags:
 - Code Editor
 - EaW Compatible
 - FoC Compatible
---

# VS Code

Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.

## Download

Official Download from Microsoft: https://code.visualstudio.com

The official VS Code includes telemetry and tracking. To opt out, add the following setting to the `settings.json` file:

```
"telemetry.telemetryLevel": "off"
```

The older setting `"telemetry.enableTelemetry": false` is deprecated and has been replaced by `telemetry.telemetryLevel`.

Alternatively there is [VSCodium](https://vscodium.com/), a community build of VS Code with telemetry disabled, but it may not support all extensions.

## Recommended extensions

The readmes of the packages give the installation instructions and requirements.

- [Alamo Engine Tools - Empire at War Edit](https://marketplace.visualstudio.com/items?itemName=AlamoEngineTools.aet-eaw-edit) - Extension and language server made for Empire at War and Forces of Corruption mod development ([repository](https://github.com/AlamoEngine-Tools/pg-starwarsgame-lsp), [releases](https://github.com/AlamoEngine-Tools/pg-starwarsgame-lsp/releases)). Preview release; Windows x64 only, requires VS Code 1.107 or later. Provides:
    - XML completions, hover, diagnostics, go to definition, find all references and rename for the game's XML files
    - Lua completion, navigation and rename for mod scripts
    - Story, localisation and model preview tooling
    - After installing, set `aet-eaw-edit.lsp.enabled` to `true` and place a `.pgproj` project file at the root of the mod; see the extension's README for the project file format and all settings
- [XML Language Support by Red Hat (XML)](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml) - Enhances XML editing by providing:
    - Syntax error reporting
    - General code completion
    - Auto-close tags
    - Automatic node indentation
    - Symbol highlighting
    - Document folding
    - Document links
    - Document symbols and outline
    - Renaming support
    - Document Formatting
    - DTD validation
    - DTD completion
    - DTD formatting
    - XSD validation
    - XSD based hover
    - XSD based code completion
    - XSL support
    - XML catalogs
    - File associations
    - Code actions
    - Schema Caching
- [Lua (Lua)](https://marketplace.visualstudio.com/items?itemName=sumneko.lua) - Enhances the support for Lua by providing:
    - Goto Definition
    - Find All References
    - Hover
    - Diagnostics
    - Rename
    - Auto Completion
    - IntelliSense
    - Signature Help
    - Document Symbols
    - Workspace Symbols
    - Syntax Check
    - Highlight
    - Code Action
    - EmmyLua Annotation
    - Multi Workspace
    - Semantic Tokens
- [vscode-lua-format](https://marketplace.visualstudio.com/items?itemName=Koihik.vscode-lua-format) - Provides auto-format capabilities for Lua.

## Additional remarks

To complement the Lua plugin, include the [latest version](https://github.com/AlamoEngine-Tools/eaw-emmyluadoc/releases) of [eaw-emmyluadoc](https://github.com/AlamoEngine-Tools/eaw-emmyluadoc) in the mod to further improve syntax highlighting, type checking and code completions.