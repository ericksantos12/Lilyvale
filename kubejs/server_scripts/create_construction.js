ServerEvents.recipes(event => {
    if (!Platform.isLoaded("create")) return

    event.remove({ output: "create:andesite_casing" })
    event.remove({ output: "create:copper_casing" })
    event.remove({ output: "create:brass_casing" })

    event.shapeless(Item.of("create:andesite_casing", 2), ["create:andesite_alloy", "#minecraft:logs"])
        .id("kubejs:construction/andesite_casing")
    event.shapeless(Item.of("create:copper_casing", 2), ["create:copper_sheet", "#minecraft:logs"])
        .id("kubejs:construction/copper_casing")
    event.shapeless(Item.of("create:brass_casing", 2), ["create:brass_sheet", "#minecraft:logs"])
        .id("kubejs:construction/brass_casing")
})
