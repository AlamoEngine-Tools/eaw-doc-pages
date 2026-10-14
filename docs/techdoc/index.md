---
title: Technical Documentation
---

# Technical Documentation

How the Alamo engine behaves: what it does with a Lua script, how it reads its XML, and where it
departs from what a modder would expect. Where a statement was measured on the game itself the
page says so; the rest is community knowledge, and an "unverified" note marks a claim nobody has
checked yet.

<div class="grid cards" markdown>

-   :material-script-text-outline: __Lua__

    ---

    The script lifecycle (creation, pooling, saving, restoring), the script categories, the
    engine's function reference, the vanilla libraries, tips and known issues.

    [:octicons-arrow-right-24: Lua](reference/lua/index.md)

-   :material-code-tags: __XML__

    ---

    Which tags the game parses, and the story events and rewards with every parameter.

    [:octicons-arrow-right-24: XML](reference/xml/index.md)

</div>

The Lua function reference and the library pages are generated from the Lua stubs the
[Empire at War language server](https://github.com/AlamoEngine-Tools/eaw-schema) ships, so the
editor and this site say the same thing.
