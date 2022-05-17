import time
import random

# Varibles
player_name = ""
difficulty_level = ""
hardcore_mode = False
health = 1
max_health = 1
default_enemy_health = 1
number_of_rooms = 0
rooms_remaining = 0
traps_cleared = 0
traps_failed = 0
enemies_fought = 0

# Inventory stuff
rps_analyzer = False
max_health_potion = 0
health_potion = 0

#Functions
def intro():
  print("\nWalking through a small forest, you fell into")
  print("a trap and stumbled down a hole!")
  time.sleep(2)
  # cool ascii text made with https://www.ascii-art-generator.org/
  print("""
============================================================
 _____    _    _   _   _    _____   ______    ____    _   _ 
|  __ \  | |  | | | \ | |  / ____| |  ____|  / __ \  | \ | |
| |  | | | |  | | |  \| | | |  __  | |__    | |  | | |  \| |
| |  | | | |  | | | . ` | | | |_ | |  __|   | |  | | | . ` |
| |__| | | |__| | | |\  | | |__| | | |____  | |__| | | |\  |
|_____/   \____/  |_| \_|  \_____| |______|  \____/  |_| \_|
                                                            
       ______   _____    _____   _    _   _______   _ 
      |  ____| |_   _|  / ____| | |  | | |__   __| | |
      | |__      | |   | |  __  | |__| |    | |    | |
      |  __|     | |   | | |_ | |  __  |    | |    | |
      | |       _| |_  | |__| | | |  | |    | |    |_|
      |_|      |_____|  \_____| |_|  |_|    |_|    (_)
      
============================================================""")
  time.sleep(1)
  print("\t\t\t  A cool text-based adventure game")
  time.sleep(1)
  print("\n============================================")
  print("Welcome to Dungeon Fight! A text-based")
  print("adventure game where you will have to")
  print("progress through multiple rooms in order to")
  print("escape the dungeon.")
  print("============================================")

def enter_name():
  global player_name
  player_name = input("\nTo begin, enter your name here: ")

def set_difficulty():
  global difficulty_level
  global hardcore_mode
  hardcore_mode = False
  # Sets the difficulty level
  while True:
    print("\nEnter a difficulty level.")
    difficulty_level = input("Type in 'easy', 'normal', 'hard', or 'hardcore'. ").lower()
    if difficulty_level == "easy" or difficulty_level == "e":
      difficulty_level = "easy"
      print("\nEasy mode it is!")
      break
    elif difficulty_level == "normal" or difficulty_level == "n":
      difficulty_level = "normal"
      print("\nNormal mode it is!")
      break
    elif difficulty_level == "hard" or difficulty_level == "h":
      difficulty_level = "hard"
      print("\nHard mode it is! Good Luck!")
      break
    elif difficulty_level == "hardcore" or difficulty_level == "hc":
      hardcore_mode = True
      difficulty_level = "hard"
      print("\nHard mode it is!")
      print("You have chosen hardcore, everything will be much harder. \nGood Luck.")
      break
    else:
      continue

def preload_game():
  # Load global variables.
  global health
  global default_enemy_health
  global number_of_rooms
  global rooms_remaining
  global max_health
  if difficulty_level == "easy":
    max_health = 50
    default_enemy_health = 10
    number_of_rooms = 10
  elif difficulty_level == "normal":
    max_health = 30
    default_enemy_health = 15
    number_of_rooms = 15
  elif difficulty_level == "hard":
    max_health = 20
    default_enemy_health = 20
    number_of_rooms = 20

  if hardcore_mode == True:
    max_health = 100

  health = max_health
  rooms_remaining = number_of_rooms + 1
  input("\nYou have selected " + difficulty_level + " mode.\nThere will be " + str(number_of_rooms) + " rooms in this dungeon. \nPress enter to continue.")

def game_cycle():
  global rooms_remaining
  while rooms_remaining > 0:
    rooms_remaining -= 1
    print("\n" + str(rooms_remaining) + "/" + str(number_of_rooms) + " rooms remaining.\n")
    if health <= 0:
      break
    elif rooms_remaining == 1:
      boss_intro()
      continue
    elif rooms_remaining == 0:
      break
    while True:
      response = input("Enter 'menu' or press enter to continue. ")
      if response == "menu":
        menu()
      else:
        break
    print("\nYou proceed into another room...")
    time.sleep(1)
    get_event()

def game():
  input("Press enter to start!")
  intro()
  enter_name()
  set_difficulty()
  preload_game()
  game_cycle()
  print(game_over())
  retry()

def retry():
  time.sleep(1)
  print("Would you like to play again?")
  retry = ""
  while True:
    retry = input("Enter 'Yes' or 'No': ").lower()
    if retry == "yes":
      game()
      return False
    elif retry == "no":
      print("\nGoodbye!")
      return False

def menu():
  global health
  global health_potion
  global max_health_potion

  while True:
    print("\n\t\t\t\t\tMenu")
    print("============================================")
    menu_response = input("\nEnter 'stats', inventory', or 'exit': ")
    if menu_response == "stats":
      print("\n\t\t\t\tPlayer Stats")
      print("============================================\n")
      print("Name: " + player_name)
      get_hp()
      print(str(rooms_remaining) + "/" + str(number_of_rooms) + " rooms remaining.")
      print("Difficulty: " + str(difficulty_level))
      print("Hardcore mode: " + str(hardcore_mode))
      print("Opponents fought: " + str(enemies_fought))
      print("Traps cleared: " + str(traps_cleared))
      print("Traps failed: " + str(traps_failed))
    elif menu_response == "inventory":
      print("\n\t\t\t  Player Inventory")
      print("============================================\n")
      if rps_analyzer == False and health_potion == 0 and max_health_potion == 0:
        print("A barren wasteland...")
      else:
        if rps_analyzer == True:
          print("Rock Paper Scissors predictor")
        if health_potion > 0:
          print(str(health_potion) + "x health_potion")
        if max_health_potion > 0:
          print(str(max_health_potion) + "x max_health_potion")
        print("")
      if max_health_potion > 0 or health_potion > 0:
        item_use = input("""Enter a potion to use or press enter to continue. """).lower()

        if item_use == "health_potion":
          if health_potion > 0:
            print("\nYou drink the healing potion and\ngain some health back!\n")
            if difficulty_level == "easy":
              health += 15
            elif difficulty_level == "normal":
              health += 10
            elif difficulty_level == "hard":
              health += 8
              health_potion -= 1
            if health > max_health:
              health = max_health
            get_hp()
          else:
            print("You dont have this!\n")

        elif item_use == "max_health_potion":
          if max_health_potion > 0:
            print("You drink the healing potion and\ngain all your health back!\n")
            health = max_health
            max_health_potion -= 1
            get_hp()
          else:
            print("You don't have this!\n")
    else:
      break

def get_event():
  event = random.randrange(5)
  if event == 0:
    rock_paper_scissors()
  elif event == 1:
    guess_my_number()
  elif event == 2:
    supply_room()
  elif event == 3:
    print("\nEmpty room...")
    time.sleep(1)
  elif event == 4:
    quick_type_game()

def game_over():
  print("\n\t\t\t\t Game Over!")
  print("============================================")
  if health > 0:
    return "Congratulations, you made it out alive!"
  else:
    return "\nYou Died."

def print_scores(player_score, enemy_score):
    print("\nPlayer score: " + str(player_score))
    print("Enemy score: " + str(enemy_score))
    get_hp()

def get_hp():
  print("Player HP: " + str(health) + "/" + str(max_health) + " (" + str(round((health/max_health*100), 2)) + "%)")

def supply_room():
  global health
  global max_health
  global rps_analyzer
  global health_potion
  global max_health_potion

  print("\n\t\t\t   A supply room!")
  print("============================================")
  time.sleep(1)
  print("You stumble upon a supply room!")
  time.sleep(1)
  print("You scour around and you find...")
  time.sleep(1)

  supply_item = random.randint(1,3)

  if supply_item == 1:
    print("\nA healing potion!\n")
    if hardcore_mode == False:
      print("Health potion added to inventory.")
      health_potion += 1
    elif hardcore_mode == True:
      time.sleep(1)
      print("Unforunately, as you pick up the potion")
      print("it appears that the cork is on too")
      print("tight... who superglued this thing!?\n")
      time.sleep(2)
      print("Potion discarded.")
      time.sleep(1)

  elif supply_item == 2:
    print("\nA max healing potion!\n")
    if hardcore_mode == False:
      print("Max health potion added to inventory.")
      max_health_potion += 1
    elif hardcore_mode == True:
      time.sleep(1)
      print("Unforunately, as you pick up the potion")
      print("it appears that the cork is on too")
      print("tight... who superglued this thing!?\n")
      time.sleep(2)
      print("Potion discarded.")
      time.sleep(1)

  elif supply_item == 3:
    rps_analyzer = True
    print("\nA rock paper scissors predictor!\n")
    time.sleep(1)
    print("This will be handy...")
    time.sleep(2)

def rock_paper_scissors():
  # Probably very inefficient coding.
  # Rest in piece cyclomatic complexity.
  global health
  global enemies_fought
  global rps_analyzer
  rps_player_input = 0
  rps_enemy_input = 0
  rps_player_score = 0
  rps_enemy_score = 0

  print("\nEnemy Fight!")
  time.sleep(1)
  print("\n\t\t\tRock Paper Scissors!")
  print("""============================================
You stumble across an enemy.
He is reluctlent to fight you physically,
but he will challange you to a game of 
rock paper scissors!
============================================""")

  time.sleep(2)
  if difficulty_level == "easy":
    rps_difficulty = 1
  elif difficulty_level == "normal":
    rps_difficulty = 2
  elif difficulty_level == "hard":
    rps_difficulty = 3

  print("\n\t\t\t\t   Rules:")
  print("============================================")
  print("On " + str(difficulty_level) + " difficulty, you have to win by " + str(rps_difficulty) + ".")
  print("\nHowever, if you losing by 2, you will\nlose HP every round you are losing by 2.")
  print("""\nThere is a 'safety net' in this game so if
you are a certain amount of points behind
the enemy, additional points will not be
added towards the enemy.""")
  if hardcore_mode == True:
    print("\nWarning: In hardcore mode, there is no cap")
    print("on how much the enemy is winning by. So it")
    print("will be easier to lose when the enemy is")
    print("winning by more than 3 points.")
  print("============================================")
  time.sleep(2)
  input("\nPress enter to continue.")

  while (rps_enemy_score + rps_difficulty) > rps_player_score and health > 0:
    print("\n============================================")
    print_scores(rps_player_score, rps_enemy_score)

    try: 
      # 1 is rock
      # 2 is paper
      # 3 is scissors
      """
      Very inefficient coding, might change later
      """
      rps_enemy_input = int(random.randint(1, 3))

      # Predicts enemy movement provided if player
      # has the rps analyzer.
      if rps_analyzer == True:
        print("\nThe rock paper scissors predictor")
        print("predicts the enemy will draw...")
        if rps_enemy_input == 1:
          print("Rock!")
        elif rps_enemy_input == 2:
          print("Paper!")
        elif rps_enemy_input == 3:
          print("Scissors!")

      rps_player_input = int(input("\nType in 1 for rock, 2 for paper, or 3 for scissors: "))

      if rps_player_input == 1 and rps_enemy_input == 2:
        print("\nYou choose rock, I choose paper!")
        print("Paper beats rock!")
        print("Enemy gets a point!")
        rps_enemy_score += rps_enemy_score_comparator(rps_player_score, rps_enemy_score)
      elif rps_player_input == 2 and rps_enemy_input == 1:
        print("\nYou choose paper, I choose rock!")
        print("Paper beats rock!")
        print("\nPlayer gets a point!")
        rps_player_score += 1
      elif rps_player_input == 2 and rps_enemy_input == 3:
        print("\nYou choose paper, I choose scissors!")
        print("Scissors beats paper!")
        print("\nEnemy gets a point!")
        rps_enemy_score += rps_enemy_score_comparator(rps_player_score, rps_enemy_score)
      elif rps_player_input == 3 and rps_enemy_input == 2:
        print("\nYou choose scissors, I choose paper!")
        print("Scissors beats paper!")
        print("\nPlayer gets a point!")
        rps_player_score += 1
      elif rps_player_input == 3 and rps_enemy_input == 1:
        print("\nYou choose scissors, I choose rock!")
        print("Rock beats scissors!")
        print("\nEnemy gets a point!")
        rps_enemy_score += rps_enemy_score_comparator(rps_player_score, rps_enemy_score)
      elif rps_player_input == 1 and rps_enemy_input == 3:
        print("\nYou choose rock, I choose scissors!")
        print("Rock beats scissors!")
        print("\nPlayer gets a point!")
        rps_player_score += 1
      elif rps_player_input == rps_enemy_input:
        print("\nTie!")

      if rps_enemy_score >= (rps_player_score + 2):
        health -= 1

    except ValueError:
     print("Please type in a number!")

  print_scores(rps_player_score, rps_enemy_score)

  if health <= 0:
    print("""\nAs you are about to lift up your
arms to play another round, you feel
faint. Eyesight blurring, darkness
setting in, you suddenly collaspe!
It seems as though as he is too strong.""")
  else:
    enemies_fought += 1
    print("""\nDrat! I never knew you were that good at 
Rock Paper Scissors!
Hmmph... You may proceed.""") 

    if rps_analyzer == True:
      print("\nUnforunately, your rock paper scissors")
      print("predictor has broke.")
      rps_analyzer = False

def rps_enemy_score_comparator(player, enemy):
  # Used to prevent dumb rng in rock paper scissors from screwing over the player.
  if difficulty_level == "hard":
    if hardcore_mode == True:
      return 1
    else:
      if enemy >= (player + 3):
        return 0
      else:
        return 1
  else: 
    if enemy >= (player + 2):
      return 0
    else:
      return 1

def guess_my_number():
  global health
  global enemies_fought
  guess = 0

  print("\nEnemy Fight!")
  time.sleep(1)
  print("\n\t\t\t  Guess My Number!")
  print("""============================================
You stumble across an opponent.
The gatekeeper of rooms, only one who 
guesses her number may pass...
============================================""")
  time.sleep(2)
  if difficulty_level == "easy":
    tries = 5
    low_range = 1
    high_range = 10
  elif difficulty_level == "normal":
    tries = 5
    low_range = 1
    high_range = 50
  elif difficulty_level == "hard":
    if hardcore_mode == True:
      tries = 10
      low_range = 1
      high_range = 1000
    else:
      tries = 7
      low_range = 1
      high_range = 100

  print("\n\t\t\t\t   Rules:")
  print("============================================")
  print("In " + str(difficulty_level) + " difficulty, you have guess my") 
  print("number within " + str(tries) + " tries, Otherwise, you will")
  print("start to lose HP. My number will range from")
  print(str(low_range) +  " to " + str(high_range) + ".")
  print("============================================")
  time.sleep(2)
  input("\nPress enter to continue.")
  print("\nLet us begin!")

  number = int(random.randint(low_range, high_range))
  while guess != number:
    if tries >= 0:
      print("\nTries remaining: " + str(tries))
    else:
      print("\nTries exceeded: " + str(tries * -1))
      
    get_hp()

    try:
      guess = int(input("Enter an integer between " + str(low_range) + " and " + str(high_range) + ": "))
      if guess == number:
        break
      else:
        if guess < number:
          print("\nHigher...")
        else:
          print("\nLower...")
      time.sleep(0.5)
      tries -= 1
      if tries < 0:
        health -= 1
      if health <= 0:
        break
    except ValueError:
      print("\nPlease type in an integer!")

  if health <= 0:
    print("""\nAs you are about to open your
mouth to guess another number, you feel
faint. Eyesight blurring, darkness
setting in, you suddenly collaspe!
It seems as though as she is too strong.""")
    time.sleep(5)
  else:
    enemies_fought += 1
    print("""\nYou finally guessed my number! Hope that
wasn't too painful. Fine, you may proceed.""")
  time.sleep(2)

def quick_type_game():
  global health
  global traps_cleared
  global traps_failed

  print("\nA Trap!")
  time.sleep(1)
  print("\n\t\t\t\tQuick, Type!")
  print("""============================================
You stumbled upon a trap!
You must type a word quickly in order to\nescape!
Remember: You only have one try!
============================================""")
  time.sleep(1)
  input("\nPress enter to start.")

  if difficulty_level == "easy":
    seconds = 5
  elif difficulty_level == "normal":
    seconds = 4
  elif difficulty_level == "hard":
    if hardcore_mode == True:
      seconds = 20
    else:
      seconds = 3

  word_chooser = random.randrange(3)
  if hardcore_mode == True:
    if word_chooser == 0:
      word = "pneumonoultramicroscopicsilicovolcanoconiosis"
    elif word_chooser == 1:
      word = "supercalifragilisticexpialidocious"
    elif word_chooser == 2:
      word = "incomprehensibilities"
  else:  
    if word_chooser == 0:
      word = "python"
    elif word_chooser == 1:
      word = "dungeon"
    elif word_chooser == 2:
      word = "fight"

  print("Type the following word in " + str(seconds) + " seconds!\n")
  print(word)
  print("\nType the word down below and enter it!")
  time.sleep(seconds)
  guess = str(input("").lower())

  """Due to current limitations of how this game is ran, if the player does not
  enter in anything when the time runs out, it will glitch a little depending on
  what the player has entered. They could also cheat by waiting until the time
  runs out, then type in the word. May be fixed if I figure it out."""

  if guess == word:
    traps_cleared += 1
    print("Congrats! You have escaped the trap\nwithout a scratch!")
  else:
    traps_failed =+ 1
    health -= 10
    print("You have failed to type in the")
    print("word correctly.")
    if health > 0:
      print("\nYou managed to escape the trap, but you\ntook some damage while escaping.")
    elif health <= 0 or hardcore_mode == True:
      print("\nUnfortunately, you did not make it out\nalive.")

def boss_intro():
  while True:
    response = input("Enter 'menu' or press enter to continue. ")
    if response == "menu":
      menu()
    else:
      break
  print("\nYou proceed into another room...")
  print("\nYou stumble upon a large door...")
  time.sleep(2)
  print("You enter a dark room...")
  time.sleep(2)
  if difficulty_level == "easy":
    print("\nThe room is empty...?")
    time.sleep(1)
    print("You see a note on the ground.")
    time.sleep(1)
    print("You pick it up and read:")
    time.sleep(1)
    print("============================================\n")
    print("BOSS: Sorry " + player_name + ",")
    print("I had to run some errands, come back here")
    print("when you are not in easy mode.")
    print("\n============================================")
    time.sleep(2)
    input("\nPress enter to continue.")
  else:
    print("You see a figure in the background...")
    time.sleep(2)
    print("The torches on the wall suddendly lights up!")
    time.sleep(2)
    print("The boss stands there menacingly...")
    time.sleep(2)
    boss_fight()

def print_boss(condition = "normal"):
  # Tool used: https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/
  # Base image used: https://commons.wikimedia.org/w/index.php?curid=46192204
  # Benny "the kid" Paret in fighting pose before his death.jpeg, Creative Commons
  print("""============================================""")
  if condition == "normal":
    print("""                                 
     ,&@@@@@@@/                         
   ,%&&&@@@@@@@@,                           
   /*,....,//(&@@                          
   ,..  ....,/&@,.                          
   ,/O ,./O,,##&@.                       
   .,.,<..,.,/@@@@*,       .                
     /,___.,(&@@%*.....*/*. .               
    */(*.*#&&@&*,.....**,,,*/*              
  .**,.*/@@@@(,.....,*,......**/*,          
  ,,.,**,,/##**,,....,**,,...#//##%#%%      
  .,,/,..*/#%@@*,,,,..,*/#%@@&&(**#(#&&%    
   */(*.*&%%@@@(*,,,,,*#@@(*/,&#*//@@@@@(   
  .*.*%%&&&&@@@%(/***/#&&/(/%#,#@@@@@@@@@@. 
  */.../%   &%&@@&%###/**/#%@@&*((&@@@@@@@@@
  */((.&,    &#@&%/,,***,,*#%%#.    /#@@@@@@
 ,(####%%    ,%%&&#**,,,   .         *&@@@@&
  *#&&%%#       .              *(           
   .(%*        .      .,(#&&   #%%#         
            %&&&%@&%%&%@@@@&#   (@@.        
           %@@%&&&@@@@@@@@@@@@   *@@        
          /&&&&&&@&@@@@@@@@@@@&*  &@/                                 
      """)
  elif condition == "low":
    print("""                                
     ,&@@@@@@@/                         
   ,%&&&@@@@@@@@,                           
   /*,....,//(&@@                          
   ,..  ....,/&@,.                          
   ,/> ,./<,,##&@.                       
   .,.,<..,.,/@@@@*,       .                
     /,___.,(&@@%*.....*/*. .               
    */(*.*#&&@&*,.....**,,,*/*              
  .**,.*/@@@@(,.....,*,......**/*,          
  ,,.,**,,/##**,,....,**,,...#//##%#%%      
  .,,/,..*/#%@@*,,,,..,*/#%@@&&(**#(#&&%    
   */(*.*&%%@@@(*,,,,,*#@@(*/,&#*//@@@@@(   
  .*.*%%&&&&@@@%(/***/#&&/(/%#,#@@@@@@@@@@. 
  */.../%   &%&@@&%###/**/#%@@&*((&@@@@@@@@@
  */((.&,    &#@&%/,,***,,*#%%#.    /#@@@@@@
 ,(####%%    ,%%&&#**,,,   .         *&@@@@&
  *#&&%%#       .              *(           
   .(%*        .      .,(#&&   #%%#         
            %&&&%@&%%&%@@@@&#   (@@.        
           %@@%&&&@@@@@@@@@@@@   *@@        
          /&&&&&&@&@@@@@@@@@@@&*  &@/                                 
            """)
  print("""============================================\n""")

def boss_hp(health, max):
  print("BOSS HP: " + str(health) + "/" + str(max) + " (" + str(round((health/max*100), 2)) + "%)")

def boss_fight():
  global health
  repeat = True
  time.sleep(1)
  print("\n\t\t\t\tBoss Fight")
  print_boss()

  boss_max = (default_enemy_health * 3)
  boss_health = boss_max
  boss_hp(boss_health, boss_max)
  print("Note: Press enter key to advance dialogue.")
  input("BOSS: So we finally meet " + player_name + ".")
  input("BOSS: If you want to leave this place, you'll\nhave to go through me first.")
  input("\nPress enter to continue")

  while boss_health/boss_max > 0 and health > 0:
    if boss_health/boss_max <= 0.5 and repeat == True:
      input("\nBOSS: Grr... I never knew you were that strong...")
      input("BOSS: Guess I will have to fight towards the bitter\nend.")
      input("\nPress enter to continue.")
      repeat = False
    
    if boss_health/boss_max <= 0.5:
      print_boss("low")
      print("BOSS: Why do I hear boss music?\n")
    else:
      print_boss()
      print("*Boss music plays*\n")

    get_hp()
    boss_hp(boss_health, boss_max)
      # 1 is attack
      # 2 is defend
      # 3 is counter
    boss_input = random.randint(1, 3)
    player_input = str(input("\nType in 1 to attack, 2 to defend, 3 to counter, or 'menu': "))
    print("")
    if player_input == "1":
      if boss_input == 1:
        print("You both attack at the same time!")
        print("Player and BOSS lose 2 HP!")
        health -= 2
        boss_health -= 2
      elif boss_input == 2:
        print("You attack and the BOSS defends!")
        print("BOSS loses 1 HP!")
        boss_health -= 1
      elif boss_input == 3:
        print("You attack and BOSS counters!")
        print("Player loses 3 HP!")
        health -= 3
    elif player_input == "2":
      if boss_input == 1:
        print("You defend and BOSS attacks!")
        print("Player loses 1 HP!")
        health -= 1
      elif boss_input == 2:
        print("You both defend at the same time!")
        print("Nothing happens.")
      elif boss_input == 3:
        print("You defend and BOSS counters!")
        print("BOSS loses 2 HP!")
        boss_health -= 2
    elif player_input == "3":
      if boss_input == 1:
        print("You counter and BOSS attacks!")
        print("BOSS loses 3 HP")
        boss_health -= 3
      elif boss_input == 2:
        print("You counter and BOSS defends!")
        print("Player loses 2 HP!")
        health -= 2
      elif boss_input == 3:
        print("You and BOSS counter at the same time!")
        time.sleep(1)
        print("The counters generate an explosion!")
        time.sleep(1)
        print("Player and BOSS lose 5 HP!")
        boss_health -= 5
        health -= 5
    elif player_input == "menu":
      menu()

    else:
      print("\nChoose a valid option!")

    time.sleep(1)
    print("")
    get_hp()
    boss_hp(boss_health, boss_max)

  if boss_health <= 0 and health <= 0:
    input("BOSS: Heh, at least this fight isnt in vain.")
    input("You and BOSS died.")
    input("Press enter to continue. ")
  elif boss_health <= 0:
    time.sleep(2)
    input("BOSS: Wow, you are strong, " + player_name + ".")
    input("BOSS: I guess... this is it...")
    input("BOSS faints.")
    input("Press enter to continue. ")
  elif health <= 0:
    input("You feel your eyesight blur, in pain from\ninjuries.")
    input("BOSS: Heh, guess you were no match\nfor me after all!")

game()
