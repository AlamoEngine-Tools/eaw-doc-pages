"""Generate the Lua reference pages from the Lua stub files of the schema repository.

The schema's lua/ directory (https://github.com/AlamoEngine-Tools/eaw-schema, lua/*.d.lua and
lua/entrypoints.json) is the single source for what the engine and the vanilla libraries offer
to a script. This script turns it into

    docs/techdoc/reference/lua/luafunctions.md           the engine API (api.d.lua, globals.d.lua,
                                                         stdlib.d.lua, entrypoints.json)
    docs/techdoc/reference/lua/libraries/<library>.md    one page per vanilla library (pg*.d.lua)

The generated pages are committed, so the site builds without the schema checkout; run this
after the schema changed and commit the result together with the schema version it came from.

usage: python tools/gen_lua_reference.py <path to the schema's lua directory>
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(os.path.dirname(HERE), "docs", "techdoc", "reference", "lua")
EOL = "\r\n"

LIBRARY_TITLES = {
    "pgaicommands": "PGAICommands", "pgbase": "PGBase", "pgbasedefinitions": "PGBaseDefinitions",
    "pgcommands": "PGCommands", "pgdebug": "PGDebug", "pgevents": "PGEvents",
    "pginterventions": "PGInterventions", "pgmoveunits": "PGMoveUnits", "pgspawnunits": "PGSpawnUnits",
    "pgstatemachine": "PGStateMachine", "pgstorymode": "PGStoryMode", "pgtaskforce": "PGTaskForce",
}


# ---------------------------------------------------------------------------------------------
# a small reader for ---@meta stub files: text blocks, functions, typed globals, classes

def parse_stub(path):
    """-> list of items: ("text", [lines]) | ("function", info) | ("global", info) | ("class", name)"""
    items = []
    doc, ann = [], []
    for raw in io.open(path, encoding="utf-8").read().split("\n"):
        line = raw.rstrip()
        if line.startswith("---@class "):
            items.append(("class", line[len("---@class "):].strip()))
            doc, ann = [], []
            continue
        if line.startswith("---@"):
            ann.append(line[4:])
            continue
        if line.startswith("---"):
            doc.append(line[3:].strip())
            continue
        if line.startswith("--"):
            continue                                    # a plain comment, not documentation
        m = re.match(r"^function\s+([A-Za-z_][\w.:]*)\s*\(([^)]*)\)\s*end\s*$", line)
        if m:
            items.append(("function", build_function(m.group(1), m.group(2), doc, ann)))
            doc, ann = [], []
            continue
        g = re.match(r"^([A-Za-z_]\w*)\s*=\s*(nil|\{\})\s*$", line)
        if g:
            if g.group(2) == "{}" and items and items[-1][0] == "class" and items[-1][1] == g.group(1):
                doc, ann = [], []
                continue                                # the class's own table
            items.append(("global", build_global(g.group(1), doc, ann)))
            doc, ann = [], []
            continue
        if not line.strip():
            if doc:
                items.append(("text", doc))
            doc, ann = [], []
    if doc:
        items.append(("text", doc))
    return items


def build_function(name, args, doc, ann):
    params, returns, deprecated, vararg = [], [], False, None
    refs = {}
    last_param = None
    for a in ann:
        if a.startswith("param "):
            parts = a[6:].split(None, 2)
            pname, ptype = parts[0], parts[1] if len(parts) > 1 else "any"
            pdoc = parts[2] if len(parts) > 2 else ""
            params.append({"name": pname.rstrip("?"), "optional": pname.endswith("?"), "type": ptype, "doc": pdoc})
            last_param = params[-1]
        elif a.startswith("vararg "):
            vararg = a[7:].strip()
        elif a.startswith("return "):
            parts = a[7:].split(None, 1)
            returns.append({"type": parts[0], "doc": parts[1] if len(parts) > 1 else ""})
        elif a.startswith("aetref ") and last_param is not None:
            last_param["ref"] = a[7:].strip()
        elif a.startswith("deprecated"):
            deprecated = True
    return {"name": name, "args": [x.strip() for x in args.split(",") if x.strip()], "doc": doc,
            "params": params, "vararg": vararg, "returns": returns, "deprecated": deprecated}


def build_global(name, doc, ann):
    gtype = "any"
    for a in ann:
        if a.startswith("type "):
            gtype = a[5:].strip()
    return {"name": name, "type": gtype, "doc": doc}


# ---------------------------------------------------------------------------------------------
# markdown helpers

def cell(text):
    return text.replace("|", "\\|").replace("\n", " ").strip() or "-"


def signature(fn):
    return "%s(%s)" % (fn["name"], ", ".join(fn["args"]))


def doc_text(lines):
    """Join doc lines into markdown; a `- ` line stays a list item (rendered with <br> in tables)."""
    out = []
    for l in lines:
        out.append(l)
    return "<br>".join(out) if any(l.startswith("- ") for l in lines) else " ".join(out)


def params_cell(fn):
    bits = []
    for p in fn["params"]:
        t = "`%s %s`" % (p["type"], p["name"])
        if p.get("optional"):
            t += " (optional)"
        if p.get("doc"):
            t += ": " + p["doc"]
        bits.append(t)
    if fn["vararg"]:
        bits.append("`... %s`" % fn["vararg"])
    return "<br>".join(bits) if bits else "-"


def returns_cell(fn):
    return "<br>".join(("`%s`" % r["type"]) + ((": " + r["doc"]) if r["doc"] else "") for r in fn["returns"]) or "-"


def table(rows, header):
    L = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        L.append("| " + " | ".join(cell(c) for c in r) + " |")
    return L


def write(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = EOL.join(lines).rstrip() + EOL
    for ch in text:
        if ord(ch) > 127:
            raise SystemExit("non-ASCII character in generated output for %s" % path)
    io.open(path, "w", encoding="ascii", newline="").write(text)


# ---------------------------------------------------------------------------------------------
# the engine reference page

def engine_page(lua_dir):
    api = parse_stub(os.path.join(lua_dir, "api.d.lua"))
    globals_ = parse_stub(os.path.join(lua_dir, "globals.d.lua"))
    entry = json.load(io.open(os.path.join(lua_dir, "entrypoints.json"), encoding="utf-8"))["entryPoints"]

    L = ["---", "title: FoC Lua Commands",
         'summary: "The engine\'s Lua API of Star Wars Empire at War: Forces of Corruption, generated from the schema\'s Lua stubs"',
         "tags:", "  - Lua", "  - Scripting", "---",
         "# Forces of Corruption Lua commands", "",
         "This page is GENERATED by `tools/gen_lua_reference.py` from the Lua stub files of the",
         "[schema repository](https://github.com/AlamoEngine-Tools/eaw-schema) (`lua/api.d.lua`,",
         "`lua/globals.d.lua`, `lua/entrypoints.json`), which the Empire at War language server ships as",
         "its completion and hover source. Edit the stubs there, not this page. The stubs record what",
         "each engine binding checks, casts and returns, so an argument count or type here is the",
         "engine's own; the prose was curated by hand on top of that.", "",
         "The vanilla script libraries (`PGBase`, `PGCommands`, ...) have their own pages under",
         "[Libraries](libraries/pgbase.md); how a script state lives, pools and saves is on",
         "[Lua script lifecycle](lua-script-lifecycle.md).", ""]

    # globals
    L += ["# Global variables", "",
          "Globals the engine maps into a script before it runs. Which ones a script gets depends on",
          "the script kind (see the lifecycle page).", ""]
    rows = []
    for kind, item in globals_:
        if kind == "global":
            rows.append(["`%s`" % item["name"], "`%s`" % item["type"], doc_text(item["doc"])])
    for kind, item in api:
        if kind == "global":
            rows.append(["`%s`" % item["name"], "`%s`" % item["type"], doc_text(item["doc"]) or "Set by the engine in every script state."])
    L += table(rows, ["Variable", "Type", "Content"]) + [""]

    # functions, grouped by the stub's own section lines and classes
    L += ["# Functions", ""]
    section = None
    pending_rows = []
    last_was_heading = False

    def flush():
        if pending_rows:
            L.extend(table(pending_rows, ["Function", "Parameters", "Returns", "Description"]))
            L.append("")
            del pending_rows[:]

    for kind, item in api:
        if kind == "text":
            if len(item) == 1 and len(item[0]) < 90 and not item[0].endswith("."):
                flush()
                section = item[0]
                L.append("## " + section)
                L.append("")
                last_was_heading = True
                continue
            elif section is None:
                continue                                # the file header
            else:
                flush()
                L.append(" ".join(item))
                L.append("")
        elif kind == "class":
            if not last_was_heading:                    # a class right after a section line keeps that heading
                flush()
                L.append("## " + item)
                L.append("")
        elif kind == "function":
            pending_rows.append(["`%s`%s" % (signature(item), " (deprecated)" if item["deprecated"] else ""),
                                 params_cell(item), returns_cell(item), doc_text(item["doc"])])
        elif kind == "global":
            pass
        last_was_heading = False
    flush()

    # entry points
    L += ["# Entry points", "",
          "Functions a script defines for the game or a vanilla library to call by name. Plan event",
          "handlers are looked up as `<TaskForceName>_<Event>` first, then `Default_<Event>`.", ""]
    rows = []
    for e in entry:
        who = e["caller"] if e["caller"] == "engine" else "library (%s)" % ", ".join(e.get("libraries", []))
        rows.append(["`%s`" % e["name"], who, ", ".join(e["kinds"]), e["description"]])
    L += table(rows, ["Function", "Called by", "Script kinds", "Description"]) + [""]
    write(os.path.join(DOCS, "luafunctions.md"), L)


# ---------------------------------------------------------------------------------------------
# one page per library

def library_page(lua_dir, base):
    title = LIBRARY_TITLES[base]
    items = parse_stub(os.path.join(lua_dir, base + ".d.lua"))
    L = ["---", "title: %s.lua" % title, "tags:", "  - Lua Library", "  - FoC", "---", "",
         "# `%s.lua`" % title, "",
         "GENERATED by `tools/gen_lua_reference.py` from `lua/%s.d.lua` of the" % base,
         "[schema repository](https://github.com/AlamoEngine-Tools/eaw-schema); edit the stub, not this page.", ""]
    first_text = True
    requires = []
    globals_rows = []
    functions = []
    for kind, item in items:
        if kind == "text":
            if first_text:
                first_text = False
                for l in item:
                    m = re.match(r"^Requires:\s*(.*)\.$", l)
                    if m:
                        requires = [r.strip() for r in m.group(1).split(",") if r.strip() and r.strip() != "nothing"]
                continue                                # the file header
            for l in item:
                if l.startswith("## "):
                    L.append(l)
                    L.append("")
                elif l in ("Functions", "Globals the library assigns (at load time or in its definitions function)"):
                    continue
                else:
                    L.append(l)
                    L.append("")
        elif kind == "global":
            globals_rows.append(["`%s`" % item["name"], "`%s`" % item["type"], doc_text(item["doc"])])
        elif kind == "function":
            functions.append(item)
    if requires:
        L += ["## Direct imports", ""]
        for r in requires:
            key = r.lower()
            L.append("* [`%s.lua`](%s.md)" % (LIBRARY_TITLES.get(key, r), key) if key in LIBRARY_TITLES else "* `%s`" % r)
        L.append("")
    if globals_rows:
        L += ["## Defined globals", ""] + table(globals_rows, ["Global", "Type", "Meaning"]) + [""]
    L += ["## Functions", ""]
    for fn in functions:
        L += ["---", "", "### `function %s`" % signature(fn), ""]
        if fn["deprecated"]:
            L += ['!!! error "Deprecated"', "    Not defined by the library as shipped; a call raises a Lua error.", ""]
        for d in fn["doc"]:
            if d.startswith("- "):
                L.append(d)
            elif d.endswith(":") and len(d) < 40:
                L.append("")
                L.append("**%s**" % d.rstrip(":"))
                L.append("")
            else:
                L.append(d)
        L.append("")
        if fn["params"] or fn["vararg"]:
            L += ['???+ note "Params"', ""]
            for p in fn["params"]:
                L.append("    * `%s %s`%s%s" % (p["type"], p["name"], " [optional]" if p["optional"] else "",
                                                  (": " + p["doc"]) if p["doc"] else ""))
            if fn["vararg"]:
                L.append("    * `... %s`" % fn["vararg"])
            L.append("")
        if fn["returns"]:
            L += ['???+ note "Returns"', ""]
            for r in fn["returns"]:
                L.append("    * `%s`%s" % (r["type"], (": " + r["doc"]) if r["doc"] else ""))
            L.append("")
    write(os.path.join(DOCS, "libraries", base + ".md"), L)


LIBRARY_ORDER = ["pgdebug", "pgbase", "pgbasedefinitions", "pgcommands", "pgaicommands", "pgtaskforce",
                 "pgevents", "pgstatemachine", "pgstorymode", "pgmoveunits", "pgspawnunits", "pginterventions"]
LIBRARY_SUMMARY = {
    "pgdebug": "Debug output: message boxes and log lines, off in the release build.",
    "pgbase": "The basics every script uses: ScriptExit, Sleep, PumpEvents, BlockOnCommand, TestValid, Flush_G.",
    "pgbasedefinitions": "The globals Common_Base_Definitions resets, and the base Base_Definitions.",
    "pgcommands": "Timers, death, attack and proximity callbacks; abilities, garrisons, weapon switching.",
    "pgaicommands": "Base_Definitions for AI plans, and the unit category contrast values.",
    "pgtaskforce": "Task force behaviour for AI plans: assembling, moving, invading, escorting, reinforcing.",
    "pgevents": "The default plan event handlers and their helpers (healing, kiting, good ground).",
    "pgstatemachine": "The state machine unit and story scripts run on, with its main function.",
    "pgstorymode": "Story scripts: the state per story event and the Story_Event_Trigger entry point.",
    "pgmoveunits": "Formation moves for unit lists.",
    "pgspawnunits": "Reinforcing and spawning unit lists.",
    "pginterventions": "Setup and helpers for intervention plans.",
}


def library_index(lua_dir):
    """The libraries' landing page: what each is for and the require chain, from the stubs."""
    requires = {}
    for base in LIBRARY_ORDER:
        items = parse_stub(os.path.join(lua_dir, base + ".d.lua"))
        req = []
        for kind, item in items:
            if kind == "text":
                for l in item:
                    m = re.match(r"^Requires:\s*(.*)\.$", l)
                    if m:
                        req = [r.strip().lower() for r in m.group(1).split(",") if r.strip() and r.strip() != "nothing"]
                break
        requires[base] = req
    L = ["---", "title: Libraries", "---", "", "# Libraries", "",
         "The vanilla `PG*.lua` libraries under `Data/Scripts/Library`. A script requires one of them",
         "and gets that library's whole chain: requiring `PGStateMachine` loads `PGCommands`,",
         "`PGBaseDefinitions`, `PGBase` and `PGDebug` with it. Every function and global a library",
         "defines is on its page, generated from the language server's stubs.", "",
         "```mermaid", "flowchart BT"]
    for base in LIBRARY_ORDER:
        L.append("    %s[%s]" % (base, LIBRARY_TITLES[base]))
    for base in LIBRARY_ORDER:
        for r in requires[base]:
            if r in LIBRARY_TITLES:
                L.append("    %s --> %s" % (base, r))
    L += ["```", "", "Arrows point at the library a file requires.", "", "| Library | Purpose | Requires |", "|---|---|---|"]
    for base in LIBRARY_ORDER:
        req = ", ".join("[`%s`](%s.md)" % (LIBRARY_TITLES[r], r) for r in requires[base] if r in LIBRARY_TITLES) or "-"
        L.append("| [`%s.lua`](%s.md) | %s | %s |" % (LIBRARY_TITLES[base], base, LIBRARY_SUMMARY[base], req))
    L.append("")
    write(os.path.join(DOCS, "libraries", "index.md"), L)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    lua_dir = sys.argv[1]
    engine_page(lua_dir)
    for base in sorted(LIBRARY_TITLES):
        if os.path.exists(os.path.join(lua_dir, base + ".d.lua")):
            library_page(lua_dir, base)
    library_index(lua_dir)
    print("wrote luafunctions.md, the libraries index and %d library pages under %s" % (len(LIBRARY_TITLES), DOCS))


if __name__ == "__main__":
    main()
