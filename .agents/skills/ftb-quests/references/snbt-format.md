# SNBT Format Reference

SNBT (Stringified NBT) is the human-readable text format used by FTB Quests for all configuration files.

## Syntax Rules

### Objects
```snbt
{
	key: value
	another_key: "string value"
	nested: {
		inner_key: 42
	}
}
```

- Fields are **newline-separated** — NO commas between top-level fields
- Inline objects on one line use commas: `{ key: "a", key2: "b" }`
- Keys are unquoted unless they contain special characters

### Strings
- Simple strings can be unquoted: `type: item`
- Strings with spaces or special chars must be quoted: `command: "/tp @p ~ ~5 ~"`
- Always use double quotes: `"hello world"`

### Numbers
| Suffix | Type | Example |
|--------|------|---------|
| (none) | int | `42` |
| `L` | long | `128L` |
| `d` | double | `0.5d` |
| `f` | float | `1.0f` |

### Booleans
```snbt
enabled: true
disabled: false
```

### Arrays
Entries are newline-separated (no commas):
```snbt
my_list: [
	"item1"
	"item2"
]
```

### Nested Array of Objects
```snbt
quests: [
	{
		id: "ABC123DEF4567890"
		type: "item"
	}
	{
		id: "1234567890ABCDEF"
		type: "checkmark"
	}
]
```

## ID Format

All FTB Quests IDs are **16-character uppercase hexadecimal strings** using ONLY characters `0-9` and `A-F`:
```
7942A6A571A4C5EB    ← VALID
58920EE9A298549B    ← VALID
C1D2E3F4G5H6C7D8   ← INVALID (contains G and H)
```

## Item Object Format (1.21+)

### Simple Item
```snbt
item: { id: "minecraft:diamond" }
```

### Item with Count
```snbt
item: { count: 16, id: "minecraft:diamond" }
```

### Item with Components
```snbt
item: {
	count: 1
	id: "mymod:special_item"
	components: {
		"minecraft:custom_data": { myKey: "myValue" }
	}
}
```

### Missing Item Placeholder
```snbt
item: {
	count: 1
	id: "ftbquests:missing_item"
	components: { "ftbquests:missing_item": "original_mod:item_id" }
}
```

### Custom Icon (PNG)
```snbt
icon: {
	components: { "ftbquests:icon": "mymod:textures/gui/icon.png" }
	id: "ftbquests:custom_icon"
}
```

## Localization File Format

The `lang/*.snbt` file has **unquoted keys** with colon-space (`: `) separator — NOT JSON:

```snbt
{
	chapter.784A70C90F6F5A49.title: "Getting Started"
	chapter_group.485E071B353FF153.title: "Tutorial"
	quest.7942A6A571A4C5EB.title: "Collect Diamonds"
	quest.7942A6A571A4C5EB.quest_subtitle: "Sparkly!"
	quest.7942A6A571A4C5EB.quest_desc: ["Line 1", "&4Red line", "Line 3"]
	task.58920EE9A298549B.title: "Custom task label"
}
```

### Color Codes
Use `&` prefix: `&0`-`&9`, `&a`-`&f` for colors. `&l` bold, `&n` underline, `&o` italic, `&m` strikethrough, `&r` reset.

Example: `"&4&lWARNING: &rThis quest is dangerous!"`

### Page Breaks
A description line containing exactly `{@pagebreak}` splits the description into pages. The quest window shows one page at a time with arrows to move between them. The editor's page-break button inserts the same line. Confirmed in FTB Quests 2001.4.22 (`Quest.PAGEBREAK_CODE`, `ViewQuestPanel.addPageBreak`).

```snbt
description: [
	"First page: what this quest is about."
	"{@pagebreak}"
	"&3&lSecond page title"
	"Details that would make the first page too long."
]
```

Use page breaks when a description runs past one screen: a long build guide, a materials list, controls. Start each page with a short colored heading so the reader knows where they are, and end the first page with a line saying what the next pages cover. Keep the line on its own; text on the same line is not treated as a break. In the 1.21+ lang format, put `"{@pagebreak}"` as its own element of the `quest_desc` array.

### Images in Descriptions
A line of the form `{image:namespace:path/to/texture.png width:80 height:100 align:center}` draws a texture inside the description (`width`/`height` in GUI pixels; `align` is `left`, `center` or `right`; `fit:true` scales to the panel). The texture must be in a loaded resource pack; in a KubeJS pack, put it under `kubejs/assets/<namespace>/textures/...`.
