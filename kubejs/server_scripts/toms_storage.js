/*
 * Tom's Simple Storage recipes rebuilt around Create components.
 * Andesite tier needs only a crafting table; electron tube, brass and
 * precision mechanism tiers follow Create progression. No Nether items.
 */

ServerEvents.recipes(event => {
    if (!Platform.isLoaded("toms_storage") || !Platform.isLoaded("create")) return

    const replaced = [
        "inventory_connector",
        "storage_terminal",
        "inventory_cable_connector",
        "level_emitter",
        "inventory_cable_connector_filtered",
        "tag_item_filter",
        "poly_item_filter",
        "crafting_terminal",
        "wireless_terminal"
    ]
    replaced.forEach(id => event.remove({ id: `toms_storage:${id}` }))

    // Andesite tier: crafting table only
    event.shaped("toms_storage:ts.inventory_connector", [
        " A ",
        "CKC",
        " A "
    ], {
        A: "create:andesite_alloy",
        C: "#forge:chests/wooden",
        K: "create:andesite_casing"
    }).id("kubejs:toms_storage/inventory_connector")

    event.shaped("toms_storage:ts.storage_terminal", [
        " G ",
        "RKR",
        " A "
    ], {
        G: "#forge:glass",
        R: "minecraft:redstone",
        K: "create:andesite_casing",
        A: "create:andesite_alloy"
    }).id("kubejs:toms_storage/storage_terminal")

    event.shapeless("toms_storage:ts.inventory_cable_connector", [
        "toms_storage:ts.inventory_cable",
        "create:andesite_casing",
        "create:andesite_alloy"
    ]).id("kubejs:toms_storage/inventory_cable_connector")

    // Electron tube tier
    event.shaped("toms_storage:ts.level_emitter", [
        " T ",
        "ACA",
        " E "
    ], {
        T: "minecraft:redstone_torch",
        A: "create:andesite_alloy",
        C: "toms_storage:ts.inventory_cable",
        E: "create:electron_tube"
    }).id("kubejs:toms_storage/level_emitter")

    event.shapeless("toms_storage:ts.inventory_cable_connector_filtered", [
        "toms_storage:ts.inventory_cable_connector",
        "create:electron_tube",
        "minecraft:paper"
    ]).id("kubejs:toms_storage/inventory_cable_connector_filtered")

    event.shapeless("toms_storage:ts.tag_item_filter", [
        "toms_storage:ts.item_filter",
        "create:electron_tube",
        "minecraft:name_tag"
    ]).id("kubejs:toms_storage/tag_item_filter")

    // Brass tier
    event.shapeless("toms_storage:ts.polymorphic_item_filter", [
        "toms_storage:ts.item_filter",
        "create:electron_tube",
        "create:brass_ingot"
    ]).id("kubejs:toms_storage/poly_item_filter")

    event.shaped("toms_storage:ts.crafting_terminal", [
        "WBW",
        " T ",
        " B "
    ], {
        W: "minecraft:crafting_table",
        B: "create:brass_ingot",
        T: "toms_storage:ts.storage_terminal"
    }).id("kubejs:toms_storage/crafting_terminal")

    // Precision mechanism tier
    event.shaped("toms_storage:ts.wireless_terminal", [
        " L ",
        "BTB",
        " M "
    ], {
        L: "create:redstone_link",
        B: "create:brass_ingot",
        T: "toms_storage:ts.storage_terminal",
        M: "create:precision_mechanism"
    }).id("kubejs:toms_storage/wireless_terminal")
})
