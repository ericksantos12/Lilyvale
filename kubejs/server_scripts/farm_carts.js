// Farm & Charm carts cannot be hitched to Icy's Better Horses breeds, so the
// pack leaves hauling to the horse cart gear and retires these two vehicles.
const RETIRED_FARM_CARTS = ["farm_and_charm:supply_cart", "farm_and_charm:plow"]

ServerEvents.recipes(event => {
    RETIRED_FARM_CARTS.forEach(item => event.remove({ output: item }))
})

ServerEvents.tags("item", event => {
    event.add("c:hidden_from_recipe_viewers", RETIRED_FARM_CARTS)
})
