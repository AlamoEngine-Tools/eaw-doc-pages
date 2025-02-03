---
title: VS Code
tags:
 - Code Editor
 - EaW Compatible
 - FoC Compatible
 - Missing Info
---

# VS Code

Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.

## Download

Official Download from Microsoft: https://code.visualstudio.com

The official VS Code does include some telemetry and tracking that - if you're bothered by that - requires you to actively opt out via adding the following setting in the `settings.json` file:

```
"telemetry.enableTelemetry": false
```

Alternatively there is VS Codium which does not include the telemetry, but may not support all packages.

## Recommended Extensions

For installation instructions and requirements, please refer to the readmes of the packages.

- [XML Language Support by Red Hat (XML)](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml) - Enhances your XML-editing experience by providing:
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
    - vscode-lua-format (vscode-lua-format) - Provides auto-format capabilites.

## Additional Remarks

To complement the Lua plugin it is recommended to include the [latest version](https://github.com/AlamoEngine-Tools/eaw-emmyluadoc/releases) of [eaw-emmyluadoc](https://github.com/AlamoEngine-Tools/eaw-emmyluadoc) in your mod to further improve syntax highlighting, type checking and code completions.