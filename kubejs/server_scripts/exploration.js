ServerEvents.recipes(event => {
    event.shaped("minecraft:bundle", [
        "S",
        "L"
    ], {
        S: "minecraft:string",
        L: "minecraft:leather"
    }).id("kubejs:exploration/bundle")
})

ServerEvents.loaded(event => {
    if (event.server.persistentData.lilyvaleInsomniaDisabled) return

    event.server.runCommandSilent("gamerule doInsomnia false")
    event.server.persistentData.lilyvaleInsomniaDisabled = true
})
