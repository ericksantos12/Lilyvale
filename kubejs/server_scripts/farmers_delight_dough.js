if (Platform.isLoaded("farmersdelight")) {
    ServerEvents.recipes(event => {
        event.replaceOutput({ id: "farmersdelight:wheat_dough_from_water" }, "farmersdelight:wheat_dough", "create:dough")
        event.replaceOutput({ id: "farmersdelight:wheat_dough_from_eggs" }, "farmersdelight:wheat_dough", "create:dough")
        event.replaceInput({ id: "create:crafting/appliances/slime_ball" }, "create:dough", "#forge:dough")
    })
}
