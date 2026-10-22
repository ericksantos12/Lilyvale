ServerEvents.recipes(event => {
    if (!Platform.isLoaded("create")) return

    event.remove({ id: "create:crushing/obsidian" })
    event.custom({
        type: "create:crushing",
        ingredients: [{ item: "minecraft:obsidian" }],
        processingTime: 500,
        results: [{ item: "create:powdered_obsidian" }]
    }).id("kubejs:processing/obsidian_crushing")

    event.remove({ id: "create:splashing/gravel" })
    event.custom({
        type: "create:splashing",
        ingredients: [{ item: "minecraft:gravel" }],
        results: [
            { item: "minecraft:iron_nugget", count: 2, chance: 0.125 },
            { item: "minecraft:flint", chance: 0.25 }
        ]
    }).id("kubejs:processing/gravel_washing")

    event.remove({ id: "create:splashing/red_sand" })
    event.custom({
        type: "create:splashing",
        ingredients: [{ item: "minecraft:red_sand" }],
        results: [
            { item: "minecraft:gold_nugget", count: 2, chance: 0.125 },
            { item: "minecraft:dead_bush", chance: 0.05 }
        ]
    }).id("kubejs:processing/red_sand_washing")
})
