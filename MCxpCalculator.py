"""

 Minecraft XP Calculator

 Description: A CLI tool to calculate the time to obtain an XP level given a mob,
              average rate of killing the mob, starting level, and the goal level.
              The time is given in a format of days, hours, minutes, seconds.

"""
#Data Table
mobs_xp_table = {
  #Passive Mobs
  "axolotl": 1, "armadillo": 2, "bee": 2, "camel": 2, "camelhusk": 2, "cat": 2, "chicken": 2, "cod": 2, "cow": 2, "dolphin": 2, "donkey": 2, "fox": 2, "frog": 2, "glowsquid": 2, "goat": 2, "happyghast": 2, "horse": 2, "llama": 2, "mooshroom": 2, "mule": 2, "nautilus": 2, "ocelot": 2, "panda": 2, "parrot": 2, "pig": 2, "polarbear": 2, "pufferfish": 2, "rabbit": 2, "salmon": 2, "sheep": 2, "traderllama": 2, "tropicalfish": 2, "turtle": 2, "wolf": 2, "zombiehorse": 2, "zombienautilus": 2,

  # Hostile Mobs
  "smallmagmacube": 1, "smallslime": 1, "mediummagmacube": 2, "mediumslime": 2, "endermite": 3, "largemagmacube": 4, "largeslime": 4, "bogged": 5, "cavespider": 5, "creeper": 5, "drowned": 5, "enderman": 5, "giant": 5, "ghast": 5, "hoglin": 5, "husk": 5, "illusioner": 5, "parched": 5, "phantom": 5, "piglin": 5, "pillager": 5, "shulker": 5, "silverfish": 5, "skeleton": 5, "spider": 5, "stray": 5, "vex": 5, "vindicator": 5, "warden": 5, "witch": 5, "witherskeleton": 5, "zombie": 5, "zombievillager": 5, "zoglin": 5, "zombifiedpiglin": 5, "blaze": 10, "breeze": 10, "chickenjockey": 10, "elderguardian": 10, "evoker": 10, "guardian": 10, "babydrowned": 12, "babyhusk": 12, "babyzombie": 12, "babyzombievillager": 12, "babyzombifiedpiglin": 12, "ravager": 20, "piglinbrute": 20, "creaking": 22, "wither": 50, "respawnedenderdragon": 500, "enderdragon": 12000
  }

# Initialization
def init():
  print("Tool Loaded!\n")
  load()

# Main Function
def load():
  mobName = normalizeMobName(str(input("Enter Mob Name: ")).strip().lower())
  if mobName not in mobs_xp_table:
    print("Mob not found in database. Please check the name and try again.\n")
    retryFunction()
  killRate = input("Enter Average Kills Per Second: ")
  if not killRate.isdigit() or int(killRate) <= 0:
    print("Kill rate must be a positive integer.\n")
    retryFunction()
  startLevel = input("Enter Starting Level: ")
  if not startLevel.isdigit() or int(startLevel) < 0:
    print("Starting level must be a non-negative integer.\n")
    retryFunction()
  goalLevel = input("Enter Goal Level: ")
  if not goalLevel.isdigit() or int(goalLevel) < 0:
    print("Goal level must be a non-negative integer.\n")
    retryFunction()
  elif int(goalLevel) <= int(startLevel):
    print("Goal level must be greater than starting level.\n")
    retryFunction()

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

def normalizeMobName(mob: str):
  norm = mob.replace(" ", "").replace("_", "").replace("-", "")
  return norm

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
  print("\nIt will take " + convertToTime(float((convertLevelToXP(goal) - convertLevelToXP(starting)) / (mobs_xp_table[mob] * rate))) + "\n")

# Restart Contingency
def retryFunction():
  retry = input("Do you want to perform another calculation? (y/n): ").strip().lower()
  if retry == "y":
    load()
  else:
    print("\nTerminating the program.")
    exit()

# Execution
init()