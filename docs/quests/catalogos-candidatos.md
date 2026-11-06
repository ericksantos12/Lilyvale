# Lilyvale — catálogos candidatos e versões de referência

**Anexo de planejamento; não é arquivo de quests.** Complementa `planejamento.md`.

As listas abaixo são sementes para a auditoria, não um conjunto de objetivos já aprovado. Foram extraídas estaticamente dos JARs resolvidos no lockfile. Receita presente no JAR não prova que ela esteja carregada; arquivos condicionais, compat, registros via código, loot e scripts podem mudar o resultado.

## 1. Versões dos 49 mods do escopo

| Mod solicitado | Arquivo resolvido inspecionado |
| --- | --- |
| Sophisticated Backpacks | `sophisticatedbackpacks-1.20.1-3.26.14.2226.jar` |
| Sophisticated Storage | `sophisticatedstorage-1.20.1-1.5.7.2195.jar` |
| Tom's Simple Storage | `toms_storage-1.20-1.7.1.jar` |
| Gliders | `gliders-forge-1.2.0.jar` |
| Camerapture | `Camerapture-1.10.12+mc1.20.1-forge.jar` |
| Comforts | `comforts-forge-6.4.0+1.20.1.jar` |
| Nature's Compass | `NaturesCompass-1.20.1-1.12.0-forge.jar` |
| Carry On | `carryon-forge-1.20.1-2.1.2.7.jar` |
| Farmer's Delight | `FarmersDelight-1.20.1-1.3.4.jar` |
| Farmer's Respite | `farmersrespite-1.20.1-2.1.2.jar` |
| Ocean's Delight | `oceansdelight-1.0.2-1.20.jar` |
| Veggies Delight | `VeggiesDelight-1.20.1-1.9.3.jar` |
| Vintage Delight | `vintagedelight-0.1.6.jar` |
| [Let's Do] Farm & Charm | `letsdo-farm_and_charm-forge-1.0.14.jar` |
| [Let's Do] Meadow | `letsdo-meadow-forge-1.3.25.jar` |
| [Let's Do] Vinery | `letsdo-vinery-forge-1.4.41.jar` |
| [Let's Do] Bakery | `letsdo-bakery-forge-1.1.15.jar` |
| Harvest with Ease | `harvest-with-ease-forge-1.20.1-9.4.0.jar` |
| Tide | `tide-forge-1.20.1-2.1.1-hotfix.jar` |
| Create | `create-1.20.1-6.0.8.jar` |
| Create Contraption Terminals | `createcontraptionterminals-1.20-1.2.0.jar` |
| Create: Steam 'n' Rails | `Steam_Rails-1.7.3+forge-mc1.20.1.jar` |
| Create Railways Navigator | `createrailwaysnavigator-forge-1.20.1-beta-0.10.0-C6.jar` |
| Regions Unexplored | `RegionsUnexploredForge-0.5.6+1.20.1.jar` |
| Better Archeology | `betterarcheology-1.2.1-1.20.1.jar` |
| Via Romana | `via_romana-2.2.3+1.20.1-forge.jar` |
| Lootr | `lootr-forge-1.20-0.7.35.90.jar` |
| The Aether | `aether-1.20.1-1.5.2-neoforge.jar` |
| Deeper and Darker | `deeperdarker-forge-1.20.1-1.3.3.jar` |
| Ad Astra | `ad_astra-forge-1.20.1-1.15.21.jar` |
| Overgeared | `overgeared-forge-1.20.1-1.6.36.jar` |
| Advanced Netherite | `advancednetherite-forge-2.1.3-1.20.1.jar` |
| Critters and Companions | `crittersandcompanions-forge-1.20.1-2.7.1.jar` |
| Naturalist | `naturalist-2.0.9-forge-1.20.1.jar` |
| Icy's Better Horses | `icys-better-horses-2.1.8-forge-1.20.1.jar` |
| Hamsters Plus Lite | `hamsters-forge-1.0.3-1.20.1.jar` |
| Immersive Melodies | `immersive_melodies-0.8.0+1.20.1-forge.jar` |
| Chipped | `chipped-forge-1.20.1-3.0.7.jar` |
| Another Furniture | `another_furniture-forge-1.20.1-3.0.4.jar` |
| Amendments | `amendments-1.20-2.2.6.jar` |
| Construction Sticks | `ConstructionSticks-1.20.1-1.2.7.jar` |
| Display Delight | `displaydelight-1.7.0.jar` |
| Perfect Plushies | `perfectplushies-forge-1.20.1-1.13.3.jar` |
| Chimes | `Chimes-v2.1.1-1.20.1-Forge.jar` |
| Cluttered | `cluttered-[Forge]-3.0.3-1.20.1.jar` |
| Dusty Decorations | `DustyDecorations_1.20.1Forge_V1.13.jar` |
| End Remastered | `endrem_forge-5.3.3-R-1.20.1.jar` |
| Endercon | `endercon-1.0.2 [Forge-Neoforge].jar` |
| True Ending | `tru.e-ending-v1.1.0c.jar` |

## 2. Critério de expansão em quests

- Cada identidade aprovada vira uma folha C independente, sem consumo. As listas não devem virar uma task conjunta de entrega.
- Para produtos culinários, confirmar que são alimentos/bebidas finais; esta triagem não é consulta ao registro FoodProperties.
- Uma folha pode aceitar aliases de apresentação, como fatia e bolo, mas não deve contar os dois como receitas diferentes sem justificativa.
- A coluna técnica serve à implementação futura; texto visível deve ser traduzido ao português e mencionar EMI quando orientar receita.
- Uma lista de itens existentes não comprova sua obtenção inicial. Pelúcias, artefatos e drops raros exigem auditoria adicional.
- Números são contagens de candidatos neste snapshot, não compromisso com a quantidade final de quests.

## 3. Rótulos de Vinery — VC04

Resultados de `vinery:wine_fermentation`. Ignorar idade e NBT cosmético na coleção comum; confirmar receita carregada e fonte dos ingredientes. Sucos e intermediários ficam na trilha de aprendizado, não nesta lista de rótulos.

**26 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `vinery:aegis_wine` | Aegis Wine |
| `vinery:apple_cider` | Cider |
| `vinery:apple_wine` | Apple Wine |
| `vinery:bolvar_wine` | Bolvar Wine |
| `vinery:bottle_mojang_noir` | A Bottle of 'Mojang Noir' |
| `vinery:chenet_wine` | Chenet Wine |
| `vinery:cherry_wine` | Cherry Wine |
| `vinery:chorus_wine` | Chorus Wine |
| `vinery:clark_wine` | Clark Wine |
| `vinery:creepers_crush` | A Bottle of 'Creepers Crush' |
| `vinery:cristel_wine` | Cristel Wine |
| `vinery:eiswein` | Eiswein |
| `vinery:glowing_wine` | Sun-kissed Wine |
| `vinery:jellie_wine` | Jellie Wine |
| `vinery:jo_special_mixture` | Jo's Special Mixture |
| `vinery:kelp_cider` | Kelp Cider |
| `vinery:lilitu_wine` | Miss Lilitus Wine |
| `vinery:magnetic_wine` | Magnetic Wine |
| `vinery:mead` | Mead |
| `vinery:mellohi_wine` | Mellohi Wine |
| `vinery:noir_wine` | Noir Wine |
| `vinery:red_wine` | Red Wine |
| `vinery:solaris_wine` | Solaris Wine |
| `vinery:stal_wine` | Stal Wine |
| `vinery:strad_wine` | Strad Wine |
| `vinery:villagers_fright` | A Bottle of 'Villagers Fright' |

## 4. Queijos de Meadow — VC03

Resultados do tipo `meadow:cheese`. Resolver equivalência roda/fatia antes de criar o filtro. Ingredientes de regiões ou situações especiais são opcionais.

**7 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `meadow:amethyst_cheese_block` | Amethyst Cheese Wheel |
| `meadow:buffalo_cheese_block` | Buffalo Cheese Wheel |
| `meadow:cheese_block` | Cheese Wheel |
| `meadow:goat_cheese_block` | Goat Cheese Wheel |
| `meadow:grain_cheese_block` | Grain Cheese Wheel |
| `meadow:sheep_cheese_block` | Sheep Cheese Wheel |
| `meadow:warped_cheese_block` | Warped Cheese Wheel |

## 5. Produtos culinários candidatos — Farmer's Delight

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**44 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `farmersdelight:apple_cider` | Apple Cider |
| `farmersdelight:apple_pie` | Apple Pie |
| `farmersdelight:bacon_and_eggs` | Bacon and Eggs |
| `farmersdelight:bacon_sandwich` | Bacon Sandwich |
| `farmersdelight:baked_cod_stew` | Baked Cod Stew |
| `farmersdelight:beef_patty` | Beef Patty |
| `farmersdelight:beef_stew` | Beef Stew |
| `farmersdelight:chicken_sandwich` | Chicken Sandwich |
| `farmersdelight:chicken_soup` | Chicken Soup |
| `farmersdelight:chocolate_pie` | Chocolate Pie |
| `farmersdelight:cod_roll` | Cod Roll |
| `farmersdelight:cooked_rice` | Cooked Rice |
| `farmersdelight:dumplings` | Dumplings |
| `farmersdelight:egg_sandwich` | Egg Sandwich |
| `farmersdelight:fish_stew` | Fish Stew |
| `farmersdelight:fried_rice` | Fried Rice |
| `farmersdelight:fruit_salad` | Fruit Salad |
| `farmersdelight:gleaming_salad_block` | Gleaming Salad |
| `farmersdelight:glow_berry_custard` | Glow Berry Custard |
| `farmersdelight:hamburger` | Hamburger |
| `farmersdelight:honey_cookie` | Honey Cookie |
| `farmersdelight:honey_glazed_ham_block` | Honey Glazed Ham |
| `farmersdelight:kelp_roll` | Kelp Roll |
| `farmersdelight:melon_juice` | Melon Juice |
| `farmersdelight:melon_popsicle` | Melon Popsicle |
| `farmersdelight:mixed_salad` | Mixed Salad |
| `farmersdelight:mushroom_rice` | Mushroom Rice |
| `farmersdelight:nether_salad` | Nether Salad |
| `farmersdelight:noodle_soup` | Noodle Soup |
| `farmersdelight:onion_soup` | Onion Soup |
| `farmersdelight:pasta_with_meatballs` | Pasta with Meatballs |
| `farmersdelight:pasta_with_mutton_chop` | Pasta with Mutton Chop |
| `farmersdelight:pie_crust` | Pie Crust |
| `farmersdelight:pumpkin_soup` | Pumpkin Soup |
| `farmersdelight:ratatouille` | Ratatouille |
| `farmersdelight:roast_chicken_block` | Roast Chicken |
| `farmersdelight:salmon_roll` | Salmon Roll |
| `farmersdelight:shepherds_pie_block` | Shepherd's Pie |
| `farmersdelight:squid_ink_pasta` | Squid Ink Pasta |
| `farmersdelight:stuffed_potato` | Stuffed Potato |
| `farmersdelight:stuffed_pumpkin_block` | Stuffed Pumpkin |
| `farmersdelight:sweet_berry_cheesecake` | Sweet Berry Cheesecake |
| `farmersdelight:sweet_berry_cookie` | Sweet Berry Cookie |
| `farmersdelight:vegetable_soup` | Vegetable Soup |

## 6. Produtos culinários candidatos — Farmer's Respite

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**11 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `farmersrespite:blazing_chili` | Blazing Chili |
| `farmersrespite:coffee` | Coffee |
| `farmersrespite:coffee_beans` | Coffee Beans |
| `farmersrespite:coffee_cake` | Coffee Cake |
| `farmersrespite:green_tea_cookie` | Green Tea Cookie |
| `farmersrespite:long_apple_cider` | Apple Cider |
| `farmersrespite:long_coffee` | Coffee |
| `farmersrespite:rose_hip_pie` | Rose Hip Pie |
| `farmersrespite:strong_apple_cider` | Apple Cider |
| `farmersrespite:strong_coffee` | Coffee |
| `farmersrespite:strong_melon_juice` | Melon Juice |

## 7. Produtos culinários candidatos — Ocean's Delight

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**2 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `oceansdelight:seagrass_salad` | Seagrass Salad |
| `oceansdelight:stuffed_cod` | Stuffed Cod |

## 8. Produtos culinários candidatos — Veggies Delight

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**26 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `veggiesdelight:broccoli_salad` | Broccoli Salad |
| `veggiesdelight:broccoli_soup` | Broccoli Soup |
| `veggiesdelight:cacciatore` | Cacciatore |
| `veggiesdelight:carrot_cake` | Carrot Cake |
| `veggiesdelight:carrot_juice` | Carrot Juice |
| `veggiesdelight:cauliflower_kuku` | Cauliflower Kuku |
| `veggiesdelight:cauliflower_soup` | Cauliflower Soup |
| `veggiesdelight:cesar_salad` | Cesar Salad |
| `veggiesdelight:dandelion_juice` | Dandelion Juice |
| `veggiesdelight:fish_and_chips` | Fish And Chips |
| `veggiesdelight:garlic_chicken_stew` | Garlic Chicken Stew |
| `veggiesdelight:garlic_stuffed_mushrooms` | Garlic Stuffed Mushrooms |
| `veggiesdelight:pasta_with_broccoli` | Pasta With Broccoli |
| `veggiesdelight:roasted_vegetables` | Roasted Vegetables |
| `veggiesdelight:shakshouka` | Shakshouka |
| `veggiesdelight:stuffed_bellpeppers_block` | Stuffed Bell Peppers |
| `veggiesdelight:stuffed_zucchini_boat` | Stuffed Zucchini Boat |
| `veggiesdelight:stuffed_zucchinis` | Stuffed Zucchinis |
| `veggiesdelight:sweet_potato_cupcake` | Sweet Potato Cupcake |
| `veggiesdelight:sweet_potato_pancakes` | Sweet Potato Pancakes |
| `veggiesdelight:sweet_potato_pie` | Sweet Potato Pie |
| `veggiesdelight:turnip_beef_stew` | Turnip Beef Stew |
| `veggiesdelight:turnip_cake` | Turnip Cake |
| `veggiesdelight:turnip_salad` | Turnip Salad |
| `veggiesdelight:vegetarian_burger` | Vegetarian Burger |
| `veggiesdelight:zucchini_sandwich` | Zucchini Sandwich |

## 9. Produtos culinários candidatos — Vintage Delight

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**25 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `vintagedelight:century_egg` | Century Egg |
| `vintagedelight:cheese_burger` | Cheese Burger |
| `vintagedelight:cheese_pasta` | Cheese Pasta |
| `vintagedelight:cucumber_salad` | Cucumber Salad |
| `vintagedelight:deluxe_burger` | Deluxe Burger |
| `vintagedelight:gearo_berry_jam_bottle` | Gearo Berry Jam Bottle |
| `vintagedelight:ghostly_chili` | Ghostly Chili |
| `vintagedelight:glow_berry_jam_bottle` | Glow Berry Jam Bottle |
| `vintagedelight:kimchi` | Kimchi |
| `vintagedelight:oatmeal` | Oatmeal |
| `vintagedelight:oatmeal_cookie` | Oatmeal Cookie |
| `vintagedelight:overnight_oats` | Overnight Oats |
| `vintagedelight:pad_thai` | Pad Thai |
| `vintagedelight:pepper_jam_bottle` | Pepper Jam Bottle |
| `vintagedelight:pepper_jam_mason_jar` | Pepper Jam Mason Jar |
| `vintagedelight:pickle` | Pickle |
| `vintagedelight:pickle_soup` | Pickle Soup |
| `vintagedelight:pickled_beetroot` | Pickled Beetroot |
| `vintagedelight:pickled_egg` | Pickled Egg |
| `vintagedelight:pickled_onion` | Pickled Onion |
| `vintagedelight:pickled_pepper` | Pickled Pepper |
| `vintagedelight:pickled_pitcher_pod` | Pickled Pitcher Pod |
| `vintagedelight:stuffed_burrito` | Stuffed Burrito |
| `vintagedelight:surstromming` | Surstromming |
| `vintagedelight:sweet_berry_jam_bottle` | Sweet Berry Jam Bottle |

## 10. Produtos culinários candidatos — [Let's Do] Farm & Charm

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**17 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `farm_and_charm:bacon_with_eggs` | Bacon with Eggs |
| `farm_and_charm:barley_soup` | Barley Soup |
| `farm_and_charm:beef_patty_with_vegetables` | Beef Patty with Vegetables |
| `farm_and_charm:farmer_salad` | Farmer Salad |
| `farm_and_charm:farmers_breakfast` | Farmers Breakfast |
| `farm_and_charm:grandmothers_strawberry_cake` | Grandmothers Strawberry Cake |
| `farm_and_charm:lamb_with_corn` | Lamb with Corn |
| `farm_and_charm:oat_pancake` | Oat Pancake |
| `farm_and_charm:oatmeal_with_strawberries` | Oatmeal with Strawberries |
| `farm_and_charm:onion_soup` | Onion Soup |
| `farm_and_charm:pasta_with_onion_sauce` | Pasta with Onion Sauce |
| `farm_and_charm:potato_soup` | Potato Soup |
| `farm_and_charm:potato_with_roast_meat` | Potato With Roast Meat |
| `farm_and_charm:sausage_with_oat_patty` | Sausage with Oat Patty |
| `farm_and_charm:simple_tomato_soup` | Simple Tomato Soup |
| `farm_and_charm:stuffed_chicken` | Stuffed Chicken |
| `farm_and_charm:stuffed_rabbit` | Stuffed Rabbit |

## 11. Produtos culinários candidatos — [Let's Do] Bakery

Triagem por saídas de receita do namespace próprio e nome funcional. **Não é lista completa nem aprovação de comestibilidade.** Incluir pratos de crafting e das máquinas; remover ingredientes, formas duplicadas e compat desativada. Conferir alimentos que esta busca por nomes não reconheceu. Bebidas de Vintage Delight representadas como `minecraft:potion`/NBT não estão nesta triagem e exigem auditoria específica.

**23 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `bakery:apple_cupcake` | Apple Cupcake |
| `bakery:apple_jam` | Apple Jam |
| `bakery:cake_display` | Cake Display |
| `bakery:cake_stand` | Cake Stand |
| `bakery:chocolate_cake` | Chocolate Cake |
| `bakery:chocolate_gateau` | Chocolate Gateau |
| `bakery:chocolate_glazed_cookie` | Chocolate Glazed Cookie |
| `bakery:chocolate_jam` | Chocolate Spread |
| `bakery:chocolate_truffle` | Chocolate Truffle |
| `bakery:cupcake_display` | Cupcake Display |
| `bakery:glowberry_jam` | Glowberry Jam |
| `bakery:jam_roll` | Jam Roll |
| `bakery:pudding` | Pudding |
| `bakery:sandwich` | Sandwich |
| `bakery:strawberry_cake` | Strawberry Cake |
| `bakery:strawberry_cupcake` | Strawberry Cupcake |
| `bakery:strawberry_glazed_cookie` | Strawberry Glazed Cookie |
| `bakery:strawberry_jam` | Strawberry Jam |
| `bakery:sweetberry_cake` | Sweetberry Cake |
| `bakery:sweetberry_cupcake` | Sweetberry Cupcake |
| `bakery:sweetberry_glazed_cookie` | Sweetberry Glazed Cookie |
| `bakery:sweetberry_jam` | Sweetberry Jam |
| `bakery:vegetable_sandwich` | Vegetable Sandwich |

## 12. Olhos de End Remastered — JE01

Uma folha por olho encontrado. A lista de 16 não vira exigência de 16 para entrar no End. Verificar regras de portal distintas, configuração e rastreamento histórico antes de criar agregações.

**16 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `endrem:black_eye` | Black Eye |
| `endrem:cold_eye` | Cold Eye |
| `endrem:corrupted_eye` | Corrupted Eye |
| `endrem:cryptic_eye` | Cryptic Eye |
| `endrem:cursed_eye` | Cursed Eye |
| `endrem:evil_eye` | Evil Eye |
| `endrem:exotic_eye` | Exotic Eye |
| `endrem:guardian_eye` | Guardian Eye |
| `endrem:lost_eye` | Lost Eye |
| `endrem:magical_eye` | Magical Eye |
| `endrem:nether_eye` | Nether Eye |
| `endrem:old_eye` | Old Eye |
| `endrem:rogue_eye` | Rogue Eye |
| `endrem:undead_eye` | Undead Eye |
| `endrem:witch_eye` | Witch Eye |
| `endrem:wither_eye` | Wither Eye |

## 13. Raças candidatas — CC02

As identidades referem-se às entidades; os ovos só serviram para localizar os registros de raça no snapshot. **Não usar ovos como objetivo de survival.** Escolher observação ou doma como contrato consistente, e confirmar IDs no registro em runtime.

**15 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `icys-better-horses:american_paint_horse` | American Paint Horse |
| `icys-better-horses:andalusian_horse` | Andalusian Horse |
| `icys-better-horses:appaloosa_horse` | Appaloosa Horse |
| `icys-better-horses:arabian_horse` | Arabian Horse |
| `icys-better-horses:belgian_horse` | Belgian Draft |
| `icys-better-horses:clydesdale_horse` | Clydesdale |
| `icys-better-horses:friesian_horse` | Friesian Horse |
| `icys-better-horses:haflinger_horse` | Haflinger |
| `icys-better-horses:icelandic_horse` | Icelandic Horse |
| `icys-better-horses:morgan_horse` | Morgan Horse |
| `icys-better-horses:mustang_horse` | Mustang Horse |
| `icys-better-horses:percheron_horse` | Percheron Horse |
| `icys-better-horses:quarter_horse` | Quarter Horse |
| `icys-better-horses:shire_horse` | Shire Horse |
| `icys-better-horses:thoroughbred_horse` | Thoroughbred Horse |

## 14. Instrumentos existentes — CC03

Preservar as 11 quests e IDs existentes. Um instrumento por folha, independentes, sem consumo ou comparação de NBT.

**11 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `immersive_melodies:bagpipe` | Bagpipe |
| `immersive_melodies:didgeridoo` | Didgeridoo |
| `immersive_melodies:ender_bass` | Ender Bass |
| `immersive_melodies:flute` | Flute |
| `immersive_melodies:handpan` | Handpan |
| `immersive_melodies:lute` | Lute |
| `immersive_melodies:piano` | Piano |
| `immersive_melodies:tiny_drum` | Tiny Drum |
| `immersive_melodies:triangle` | Triangle |
| `immersive_melodies:trumpet` | Trumpet |
| `immersive_melodies:vielle` | Vielle |

## 15. Fósseis candidatos — MF02

Uma entrada por conjunto de fóssil; cabeça e corpo não devem inflar a coleção como fósseis diferentes. Artefatos identificados têm condições/NBT próprios e não foram inventariados como variantes finais aqui.

**7 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `betterarcheology:chicken_fossil` | Chicken-Fossil |
| `betterarcheology:creeper_fossil` | Creeper-Fossil |
| `betterarcheology:guardian_fossil` | Guardian-Fossil |
| `betterarcheology:ocelot_fossil` | Ocelot-Fossil |
| `betterarcheology:sheep_fossil` | Sheep-Fossil |
| `betterarcheology:villager_fossil` | Villager-Fossil |
| `betterarcheology:wolf_fossil` | Wolf-Fossil |

## 16. Pelúcias existentes, ainda não aprovadas — LR03

**HOLD: fonte inicial de survival ainda não auditada por identidade.** Tradução e loot de quebrar uma pelúcia existente não provam que o jogador consegue obtê-la. Filtrar conteúdo de autor, restrito ou raro após conferir comerciante/registro/config. Não prometer completar esta lista sem essa auditoria.

**47 candidatos distintos.**

| Identidade candidata | Nome de referência |
| --- | --- |
| `perfectplushies:aye_aye_plushie` | Aye Aye Plushie |
| `perfectplushies:bear_plushie` | Bear Plushie |
| `perfectplushies:brown_rabbit_plushie` | Brown Rabbit Plushie |
| `perfectplushies:capybara_plushie` | Capybara Plushie |
| `perfectplushies:cat_plushie` | Cat Plushie |
| `perfectplushies:daniel_plushie` | Daniel Plushie |
| `perfectplushies:doe_plushie` | Doe Plushie |
| `perfectplushies:dog_plushie` | Dog Plushie |
| `perfectplushies:dolphin_plushie` | Dolphin Plushie |
| `perfectplushies:duck_plushie` | Duck Plushie |
| `perfectplushies:dumbo_blob_plushie` | Dumbo Blob Plushie |
| `perfectplushies:elephant_plushie` | Elephant Plushie |
| `perfectplushies:fennec_fox_plushie` | Fennec Fox Plushie |
| `perfectplushies:frog_plushie` | Frog Plushie |
| `perfectplushies:gamerpotion_plushie` | GamerPotion Plushie |
| `perfectplushies:gamerpotion_plushie_rare` | GamerPotion Plushie |
| `perfectplushies:geode_plushie` | Geode Plushie |
| `perfectplushies:goose_plushie` | Goose Plushie |
| `perfectplushies:hedgehog_plushie` | Hedgehog Plushie |
| `perfectplushies:hippo_plushie` | Hippo Plushie |
| `perfectplushies:hummingbird_plushie` | Hummingbird Plushie |
| `perfectplushies:joosh_plushie` | Joosh Plushie |
| `perfectplushies:june_plushie` | June Plushie |
| `perfectplushies:koala_plushie` | Koala Plushie |
| `perfectplushies:lion_cub_plushie` | Lion Cub Plushie |
| `perfectplushies:monkey_plushie` | Monkey Plushie |
| `perfectplushies:mouse_plushie` | Mouse Plushie |
| `perfectplushies:nyf_plushie` | Nyf Plushie |
| `perfectplushies:panda_plushie` | Panda Plushie |
| `perfectplushies:quokka_plushie` | Quokka Plushie |
| `perfectplushies:raccoon_plushie` | Raccoon Plushie |
| `perfectplushies:red_fox_plushie` | Red Fox Plushie |
| `perfectplushies:red_panda_plushie` | Red Panda Plushie |
| `perfectplushies:red_ruffed_lemur_plushie` | Red Ruffed Lemur Plushie |
| `perfectplushies:reindeer_plushie` | Reindeer Plushie |
| `perfectplushies:robin_plushie` | Robin Plushie |
| `perfectplushies:rocris_plushie` | RoCris Plushie |
| `perfectplushies:rubber_duck_plushie` | Rubber Duck Plushie |
| `perfectplushies:seal_plushie` | Seal Plushie |
| `perfectplushies:silk_plushie` | Silk Plushie |
| `perfectplushies:sirjain_plushie` | SirJain Plushie |
| `perfectplushies:sirjain_plushie_rare` | SirJain Plushie |
| `perfectplushies:sizableshrimp_plushie` | SizableShrimp Plushie |
| `perfectplushies:snow_fox_plushie` | Snow Fox Plushie |
| `perfectplushies:tslat_plushie` | Tslat Plushie |
| `perfectplushies:turtle_plushie` | Turtle Plushie |
| `perfectplushies:white_rabbit_plushie` | White Rabbit Plushie |

## Registros que ficam no sistema original

- Tide: usar Fishing Journal; não gerar um álbum FTB paralelo de todos os peixes.
- Chipped: escolher projetos/paletas; não gerar uma folha por textura.
- Regions Unexplored: agrupar paisagens com alternativas; não todos os biomas.
- Storage/Backpacks/Tom's: mapear as 210 quests existentes, sem duplicar objetivos/recompensas.
- Fauna de Naturalist/Critters/Hamsters: o catálogo final depende de registro de entidades, comportamento e possibilidade real de encontro, não de receitas de itens.

## Lista de conferência antes de aprovar um candidato

1. O item/entidade existe no registro carregado desta versão?
2. Tem fonte inicial válida no survival deste pack, não só no criativo?
3. A receita não depende de integração ausente nem foi removida por script?
4. É resultado final/identidade relevante, não apresentação duplicada ou ingrediente?
5. O filtro reconhece aliases necessários sem aceitar um item genérico demais?
6. O texto distingue descoberta de fabricação/captura/domesticação?
7. A folha é independente, sem consumo e sem gate para outros estilos de jogo?
8. Sua recompensa não conclui outra folha nem repete recompensas de um ID migrado?

