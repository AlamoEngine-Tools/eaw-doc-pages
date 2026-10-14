---
title: Blender
tags:
  - Tool
  - Unofficial
  - Maintained
  - Freeware
---

# Blender

Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game creation.  
Blender is also compatible with modding 3D assets for Empire at War and Forces of Corruption thanks to Gaukler's Alamo Tools for Blender.

## Download

* [Gaukler/Blender-ALAMO-Plugin](https://github.com/Gaukler/Blender-ALAMO-Plugin): Gaukler's original repository (tested with Blender 2.82)
* [andrewfullard/Blender-ALAMO-Plugin](https://github.com/andrewfullard/Blender-ALAMO-Plugin): Recommended as the most actively supported fork of Gaukler's original plugin (tested with Blender 3.6)

Other forks: [https://github.com/Gaukler/Blender-ALAMO-Plugin/forks](https://github.com/Gaukler/Blender-ALAMO-Plugin/forks)

## Installation guide and tutorial

[![Installation Guide and Tutorial](https://img.youtube.com/vi/YholfWkvc5w/0.jpg)](https://www.youtube.com/watch?v=YholfWkvc5w "Installation Guide and Tutorial")

## Fixing non-manifolds

Selecting by Non Manifold requires Edit Mode with Vertex or Edge selection. Deselect everything first; otherwise Non Manifold is added to the existing selection.

![](https://raw.githubusercontent.com/yyhrs/non-manifold/main/resources/home.1.jpg)

Some non-manifold can be fixed automatically by Delete Loose, Degenerate Dissolve, Merge by Distance or Fill Holes. Delete Loose can solve automatically level 6 and 7. Merge by Distance can solve level 3 but can also produce a non-manifold like the ones shown in levels 8 and 9.

![](https://raw.githubusercontent.com/yyhrs/non-manifold/main/resources/home.2.jpg)

