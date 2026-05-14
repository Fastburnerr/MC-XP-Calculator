"""

 Minecraft XP Calculator

 Description: A CLI tool to calculate the time to obtain an XP level given a mob,
              average rate of killing the mob, starting level, and the goal level.
              The time is given in a format of days, hours, minutes, seconds.

 Valid Passive Mobs: armadillo, axolotl, bee, camel, camel husk, cat, chicken, cod, cow, dolphin, donkey, fox, frog, glow squid, goat, happy ghast, horse, llama, mooshroom, mule, nautilus, ocelot, panda, parrot, pig, polar bear, pufferfish, rabbit, salmon, sheep, tropical fish, turtle, wolf, zombie horse, zombie nautilus
 Valid Hostile Mobs: baby drowned, baby husk, baby zombie, baby zombie villager, baby zombified piglin, bogged, blaze, breeze, cave spider, chicken jockey, creaking, creeper, drowned, elder guardian, ender dragon, enderman, endermite, evoker, giant, ghast, guardian, hoglin, husk, illusioner, large magma cube, large slime, medium magma cube, medium slime, parched, phantom, piglin, piglin brute, pillager, ravager, respawned ender dragon, shulker, silverfish, skeleton, small magma cube, small slime, spider, stray, vex, vindicator, warden, witch, wither, wither skeleton, zombie, zombie villager, zoglin, zombified piglin
 
 Constraints: -The input for mob name will be normalised in such a way that it will
               remove spaces (" "), dashes ("-"), and underscores ("_") before going
               through the computation. The normalised input must then match the
               name within the included data set, otherwise the user will be asked
               to input again.
              -The input for average kill rate must be a non-zero positive integer,
               otherwise the user will be asked to input again.
              -The input for starting level must be a non-negative integer, otherwise
               the user will be asked to input again.
              -The input for goal level must be a greater integer than the starting
               level, and because the starting level cannot be a negative integer,
               neither can the goal level. If fail then user will be asked to try again
 
 Disclaimers: -The calulated result is an estimation of the time it will take to level
               up from starting level to ending level.
              -Some mob XP rates within the data set are based on the average amount
               of XP they drop. Actual drop amounts may vary.

"""
#Data Table
mobs_xp_table = {
  #Passive Mobs
  "axolotl": 1, "armadillo": 2, "bee": 2, "camel": 2, "camelhusk": 2, "cat": 2, "chicken": 2, "cod": 2, "cow": 2, "dolphin": 2, "donkey": 2, "fox": 2, "frog": 2, "glowsquid": 2, "goat": 2, "happyghast": 2, "horse": 2, "llama": 2, "mooshroom": 2, "mule": 2, "nautilus": 2, "ocelot": 2, "panda": 2, "parrot": 2, "pig": 2, "polarbear": 2, "pufferfish": 2, "rabbit": 2, "salmon": 2, "sheep": 2, "tropicalfish": 2, "turtle": 2, "wolf": 2, "zombiehorse": 2, "zombienautilus": 2,

  # Hostile Mobs
  "smallmagmacube": 1, "smallslime": 1, "mediummagmacube": 2, "mediumslime": 2, "endermite": 3, "largemagmacube": 4, "largeslime": 4, "bogged": 5, "cavespider": 5, "creeper": 5, "drowned": 5, "enderman": 5, "giant": 5, "ghast": 5, "hoglin": 5, "husk": 5, "illusioner": 5, "parched": 5, "phantom": 5, "piglin": 5, "pillager": 5, "shulker": 5, "silverfish": 5, "skeleton": 5, "spider": 5, "stray": 5, "vex": 5, "vindicator": 5, "warden": 5, "witch": 5, "witherskeleton": 5, "zombie": 5, "zombievillager": 5, "zoglin": 5, "zombifiedpiglin": 5, "blaze": 10, "breeze": 10, "chickenjockey": 10, "elderguardian": 10, "evoker": 10, "guardian": 10, "babydrowned": 12, "babyhusk": 12, "babyzombie": 12, "babyzombievillager": 12, "babyzombifiedpiglin": 12, "piglinbrute": 20,  "ravager": 20, "creaking": 22, "wither": 50, "respawnedenderdragon": 500, "enderdragon": 12000
  }

loadAtt = 1

# Initialization
def __init__():
  if callable(load) and callable(convertLevelToXP) and callable(normalizeString) and callable(convertToTime) and callable(retryFunction):
    print("Tool loaded after attempt " + str(loadAtt) + "!\n")
    load()
  else:
    if loadAtt <= 5:
      print("Attempt " + str(loadAtt) + " failed! Reattempting to load...\n")
      __init__()
    else:
      print("Failed to load. Terminating the program...")
      exit()

# Main Function
def load():
  mobName = normalizeString(str(input("Enter Mob Name: ")).strip().lower())
  while mobName not in mobs_xp_table:
    mobName = normalizeString(input("Mob not found in database. Try again: "))
  killRate = input("Enter Average Kills Per Second: ")
  while not killRate.isdigit() or int(killRate) <= 0:
    killRate = input("Kill rate must be a positive integer. Try again: ")
  startLevel = input("Enter Starting Level: ")
  while not startLevel.isdigit() or int(startLevel) < 0:
    startLevel = input("Starting level must be a non-negative integer. Try again: ")
  goalLevel = input("Enter Goal Level: ")
  while int(goalLevel) <= int(startLevel):
    goalLevel = input("Goal level must be greater than starting level. Try again: ")

  calculate(str(mobName), int(killRate), int(startLevel), int(goalLevel))
  retryFunction()

# Helper Functions
def convertLevelToXP(level: int):
  if level <= 16:
    return (level * level) + 6 * level
  elif level <= 31:
    return (2.5 * level * level) - (40.5 * level) + 360
  else:
    return (4.5 * level * level) - (162.5 * level) + 2220

def normalizeString(string: str):
  result = string.replace(" ", "").replace("_", "").replace("-", "")
  return result

def convertToTime(seconds: float):
  totalTime = ""
  days = int(seconds // 86400)
  if days > 0:
    totalTime += f"{days} day{'s' if days != 1 else ''}, "
    seconds -= days * 86400
  hours = int(seconds // 3600)
  if hours > 0:
    totalTime += f"{hours} hour{'s' if hours != 1 else ''}, "
    seconds -= hours * 3600
  minutes = int(seconds // 60)
  if minutes > 0:
    totalTime += f"{minutes} minute{'s' if minutes != 1 else ''}, "
    seconds -= minutes * 60
  seconds = int(seconds)
  if seconds > 0:
    totalTime += f"{seconds} second{'s' if seconds != 1 else ''}"
  return totalTime.strip(", ")

def calculate(mob: str, rate: int, starting: int, goal: int):
  print("\nIt will take approximately " + convertToTime(float((convertLevelToXP(goal) - convertLevelToXP(starting)) / (mobs_xp_table[mob] * rate))) + ".\n")

# Restart Contingency
def retryFunction():
  retry = input("Do you want to perform another calculation? (y/n): ").strip().lower()
  if retry == "y":
    load()
  else:
    print("\nTerminating the program.")
    exit()

# Execution
__init__()