// CABIN 1.20.1 railway casing tweak; other Create train recipes remain vanilla.
ServerEvents.recipes(event => {
    if (!Platform.isLoaded("create")) return

    event.remove({ output: "create:railway_casing" })
    event.shapeless(Item.of("create:railway_casing", 2), ["create:golden_sheet", "minecraft:deepslate"])
        .id("kubejs:trains/railway_casing")
})
