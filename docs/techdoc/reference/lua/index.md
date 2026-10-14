---
title: Lua
---

# Lua

The game runs Lua 5.0 scripts for units and structures, story plots, AI plans and evaluators,
free stores and the scoring hooks. Read in this order:

1. [Script lifecycle](lua-script-lifecycle.md): how a script state is created, serviced,
   pooled and reused, what a save game contains and what a load rebuilds, and the setup rules
   that follow from it. The one page every script author should read.
2. [Script categories](foc-lua-scripts.md): the script folders and what each kind of script
   is for, which entry points the game calls, and the dialog file syntax.
3. [Engine functions](luafunctions.md): every function and object the engine offers a script,
   with argument counts and types as the engine checks them. Generated from the language
   server's stubs.
4. [Libraries](libraries/index.md): the vanilla `PG*.lua` libraries most scripts require,
   one page each, in dependency order. Generated from the same stubs.
5. [Tips](eaw-lua-tips.md): practical notes on cameras, hyperspace, pooling and saving.
6. [Known issues and quirks](../../issues/lua/issues.md): engine behaviour that works against
   a script author, with what to do instead.
