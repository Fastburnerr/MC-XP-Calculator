<img width="1069" height="576" alt="image(1)" src="https://github.com/user-attachments/assets/b2a8a535-ea4e-49a5-8e76-a898cff9fbfc" />
# MC-XP-Calculator

A CLI tool to calculate the time to obtain an XP level given a mob, average rate of killing the mob, starting level, and the goal level. The time is given in a format of days, hours, minutes, seconds. Full release set to work with Minecraft Java Edition up to version 1.21.11.

Valid Passive Mobs: armadillo, axolotl, bee, camel, camel husk, cat, chicken, cod, cow, dolphin, donkey, fox, frog, glow squid, goat, happy ghast, horse, llama, mooshroom, mule, nautilus, ocelot, panda, parrot, pig, polar bear, pufferfish, rabbit, salmon, sheep, tropical fish, turtle, wolf, zombie horse, zombie nautilus

Valid Hostile Mobs: baby drowned, baby husk, baby zombie, baby zombie villager, baby zombified piglin, bogged, blaze, breeze, cave spider, chicken jockey, creaking, creeper, drowned, elder guardian, ender dragon, enderman, endermite, evoker, giant, ghast, guardian, hoglin, husk, illusioner, large magma cube, large slime, medium magma cube, medium slime, parched, phantom, piglin, piglin brute, pillager, ravager, respawned ender dragon, shulker, silverfish, skeleton, small magma cube, small slime, spider, stray, vex, vindicator, warden, witch, wither, wither skeleton, zombie, zombie villager, zoglin, zombified piglin

Constraints:
  -The input for mob name will be normalised in such a way that it will remove spaces (" "), dashes ("-"), and underscores ("_") before going through the computation. The normalised input must then match the name within the included data set, otherwise the user will be asked to input again.
  -The input for average kill rate must be a non-zero positive integer, otherwise the user will be asked to input again.
  -The input for starting level must be a non-negative integer, otherwise the user will be asked to input again.
  -The input for goal level must be a greater integer than the starting level, and because the starting level cannot be a negative integer, neither can the goal level. If fail then user will be asked to try again

Disclaimers:
  -The calulated result is an estimation of the time it will take to level up from starting level to ending level.
  -Some mob XP rates within the data set are based on the average amount of XP they drop. Actual drop amounts may vary.
