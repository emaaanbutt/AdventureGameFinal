import time

gameState = {
    'rooms': {"Entrance_Hall": {
        'Description': 'As you step into the Entrance Hall, a gust of cold air greets you—either the castle is saying hello or '
                       "it’s just really, really old. \nThe torches flicker like they know something you don’t, and the shadows on the walls? "
                       'Yeah, they’re probably up to no good. \nA pile of "feathers" welcome you in the hall.',
        'Exits': ['Left_Corridor(West)', 'Right_Corridor(East)', 'Grand_Staircase(North)'],
        'Movements': ['West', 'East', 'North'],
        'Items': ['feathers'],
        'Locked': False},

        "Left_Corridor": {
            'Description': 'Entering the left corridor, you feel a chill run down your spine—what secrets lie ahead in the darkness? '
                           'Something feels wrong in this part of the castle. \nAn "anvil" is lying on the floor.',
            'Movements': ['East', 'West'],
            'Exits': ['Entrance_Hall(East)', 'Crypt(West)'],
            'Items': ['anvil'],
            'Locked': False},

        "Right_Corridor": {'Description': 'The corridor feels damp, with faded tapestries hanging along '
                                          'the stone walls. The ground beneath your feet is uneven, and the sound of clanking metal echoes \n'
                                          'faintly, coming from deeper within the castle. The passage seems to stretch into darkness. A "stone" is shining brightly among other stones.',
                           'Movements': ['West', 'East', 'South'],
                           'Exits': ['Entrance_Hall(West)', 'Armory(East)', 'Dungeon(South)'],
                           'Items': ['stone'],
                           'Locked': False},

        "Crypt": {'Description': 'You step into the cold, silent Crypt. The air is thick, and the stone '
                                 '"coffins" that line the walls look ancient, untouched for centuries. \nCarvings of strange symbols '
                                 'are etched into the stone, hinting at long-forgotten secrets. You sense something valuable might \n'
                                 'be hidden here, but it won’t reveal itself easily.',
                  'Movements': ['East', 'South'],
                  'Exits': ['Left_Corridor(East)', 'Library(South)'],
                  'Items': [],
                  'Puzzle Reward': ['golden key'],
                  'Locked': False,
                  'coffins': 'Five weathered coffins stand before you, each one guarded by a ghostly figure. An inscription above the coffins whispers:\n'
                             '"Only by solving the riddles of the guardians can you find the treasure hidden within these coffins."\n'
                             'You can choose to approach any coffin and attempt to solve the riddle posed by its guardian.',

                  'Puzzle_Help': 'If your answer is correct,the guardian will allow you to move to the next coffin, \n'
                                 'revealing its puzzle. Solve all five puzzles to reveal the treasure!\n',
                  'Puzzle': {
                      "1": {'Riddle': 'Coffin 1: Guardian: "I can be cracked, made, told, and played. What am I?"',
                            'Answer': 'A Joke jokes',
                            'Solved': False},
                      "2": {'Riddle': 'Coffin 2: Guardian: "The more you take, the more you leave behind. What am I?"',
                            'Answer': 'Footsteps footstep',
                            'Solved': False},
                      "3": {'Riddle': 'Coffin 3: Guardian: "I am a friend of time. What am I?"',
                            'Answer': 'A Clock clocks',
                            'Solved': False},
                      "4": {'Riddle': 'Coffin 4: Guardian: "I linger in dreams. What am I?"',
                            'Answer': 'A memory memories',
                            'Solved': False},
                      "5": {'Riddle': 'Coffin 5: Guardian: "I guard the past. What am I?"',
                            'Answer': 'A tombstone tombstones',
                            'Solved': False}
                  }
                  },

        "Armory": {'Description': 'Ancient suits of armor, now rusted and broken, line the walls. Broken '
                                  'weapons are strewn across the floor, and a heavy shield with an inscription \nstands upright at the '
                                  'far end. The cold metal and sharp edges tell stories of forgotten battles.'
                                  'There\'s a riddle carved onto the shield, \nwhich might unlock something valuable.',
                   'Movements': ['West', 'South'],
                   'Exits': ['Right_Corridor(West)', 'Servant_Quarters(South)'],
                   'Items': [''],
                   'Puzzle Reward': ['bronze key'],
                   'Locked': False,
                   'Puzzle_Help': 'To unlock the secrets within, you must recall the powerful words you discovered in the library. Combine the letters '
                                  'with their corresponding numbers to form \nthree 5-digit codes.'
                                  '\nA=3\nB=5\nC=2\nD=9\nE=1\nL=8\nN=6\nO=4\nR=7\nS=2\nW=0\n'
                                  'You must now enter the 5-digit codes for the three words, one at a time',
                   'Puzzle': {
                       "1": {'Riddle': 'Recall the first code... ',
                             'Answer': '58391',
                             'Solved': False},
                       "2": {'Riddle': 'Recall the second code... ',
                             'Answer': '27406',
                             'Solved': False},
                       "3": {'Riddle': 'Recall the third code...',
                             'Answer': '20479',
                             'Solved': False}
                   }
                   },

        "Grand_Staircase": {
            'Description': 'Before you lies the Grand Staircase, its imposing steps creaking beneath your feet like the '
                           'whispers of long-lost souls! Ascend if you dare, \nbut beware—the sound of your footsteps may awaken secrets '
                           'best left undisturbed! A "skull" is placed at the last step.',
            'Movements': ['South', 'North'],
            'Exits': ['Entrance_Hall(South)', 'Grand_Ballroom(North)'],
            'Items': ['skull'],
            'Locked': False},

        "Grand_Ballroom": {'Description': 'This once grand and opulent room is now faded, with tattered '
                                          'curtains and dusty chandeliers swaying slightly as if from a breeze you can’t feel. In the \ncorner '
                                          'of the room are some scattered ancient "murals". The ballroom feels eerie, as if it holds onto the memories '
                                          'of the grand parties that once took place \nhere.Something appears to be written on the "wall"',
                           'wall': '\nThe ballroom has an inscription on the wall that reads:'
                                   '\n"Only by stepping in the rhythm of the stars shall the door to the past open. Solve the puzzle to unlock its secrets."',
                           'Movements': ['South', 'North'],
                           'Exits': ['Grand_Staircase(South)', 'Tower_Room(North)'],
                           'Items': ['murals'],
                           'Puzzle Reward': ['silver key'],
                           'Locked': False,
                           'Puzzle_Help': 'You face the worn ballroom floor. Nine tiles lie before you, each engraved with a star. \n'
                                          'Step in the rhythm of the stars to get the key.\n'
                                          '1 | 2 | 3\n'
                                          '---------\n'
                                          '4 | 5 | 6\n'
                                          '---------\n'
                                          '7 | 8 | 9\n'
                                          'Enter coordinates like "1,1" or "2,3" (Hint: 5 coordinates make a pattern)\n',
                           'Puzzle': {
                               "1": {'Riddle': 'Where will you step first?',
                                     'Answer': "1,1 1,3 3,1 3,3 2,2",
                                     'Solved': False},
                               "2": {'Riddle': 'Where will you step next?',
                                     'Answer': "1,1 1,3 3,1 3,3 2,2",
                                     'Solved': False},
                               "3": {'Riddle': 'Where will you step next?',
                                     'Answer': "1,1 1,3 3,1 3,3 2,2",
                                     'Solved': False},
                               "4": {'Riddle': 'Where will you step next?',
                                     'Answer': "1,1 1,3 3,1 3,3 2,2",
                                     'Solved': False},
                               "5": {'Riddle': 'Where will you step next?',
                                     'Answer': "1,1 1,3 3,1 3,3 2,2",
                                     'Solved': False}
                           }},

        "Servant_Quarters": {
            'Description': 'As you enter the dimly lit servant quarters, you see an old "lamp" lying on the floor. '
                           'A faint voice echoes from a dark corner.\nYou approach and notice a shadowy figure with no body, just a floating head — '
                           'his name is "Bodyless." Enter "interact" to interact with this creature.',
            'Movements': ['North', 'West'],
            'Exits': ['Armory(North)', 'Dungeon(West)'],
            'Items': ['lamp'],
            'Locked': True,
            'Unlocked_By': ['bronze key'],
            'Puzzle Reward': ['castle map'],
            'Puzzle_Help': 'BODYLESS:\n"Nothing in this castle comes for free, especially not from me. You must prove your wit to earn '
                           'the key. Solve this, and the prize is yours. \nFail, and you’ll remain here, wondering what could have been. (Bodyless gives a wicked laugh)"\n',
            'Puzzle': {
                "0": {'Riddle': 'Listen closely, adventurer:\n'
                                'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?',
                      'Answer': 'an echo a echo echoes',
                      'Solved': False}
            }},

        "Dungeon": {
            'Description': 'As you descend into the dungeon, a chill envelops you, and the air is thick with an earthy smell. '
                           'The flickering torches cast dancing shadows along the stone walls. \nA "goblet" is placed in a corner wardrobe. '
                           'Ahead, you see a dimly lit chamber where five pressure plates are arranged in a line, each etched with a '
                           'different symbol. \nMaybe some sort of puzzle...',
            'Movements': ['East', 'South', 'West'],
            'Exits': ['Servant_Quarters(East)', 'Hidden_Chamber(South)'],
            'Items': ['goblet'],
            'Puzzle_Reward': ['blood moon key'],
            'Locked': True,
            'Unlocked_By': ['cell key'],
            'Puzzle_Help': 'In the center of the chamber lie five pressure plates, each marked with a distinct symbol: '
                           '\nan anvil, \na feather, \na stone, \na goblet, and a \nskull. \nYou notice a nearby inscription that reads:'
                           '"\nPlace the mentioned items upon the plates to unlock the secrets of the dungeon."\n'
                           'These items maybe present in different rooms across the castle. (Eg type "use anvil" to use anvil)',
            'Puzzle': {
                "1": {'Riddle': 'Anvil (Heavy)',
                      'Answer': True,
                      'Solved': False},
                "2": {'Riddle': 'Feather (Light)',
                      'Answer': True,
                      'Solved': False},
                "3": {'Riddle': 'Stone (Medium)',
                      'Answer': True,
                      'Solved': False},
                "4": {'Riddle': 'Goblet (Medium)',
                      'Answer': True,
                      'Solved': False},
                "5": {'Riddle': 'Skull (Heavy)',
                      'Answer': True,
                      'Solved': False},

            }},

        "Library": {'Description': 'Rows of ancient, dust-covered books line the shelves. The room smells '
                                   'of old paper and knowledge long forgotten. A small ladder leans against one of the \nshelves, and a '
                                   'particular "book" looks out of place, almost as if it has been moved recently.',
                    'Movements': ['North'],
                    'Exits': ['Crypt(North)'],
                    'Items': ['book'],
                    'Locked': True,
                    'Unlocked_By': ['golden key']},

        "Tower_Room": {'Description': 'The highest point of the castle, the Tower Room is small but '
                                      'offers a breathtaking view of the surrounding lands through a large, old "telescope". Dusty scrolls \n'
                                      'and strange "artifacts" are scattered about the room, and you sense that something important is '
                                      'hidden here.',
                       'telescope': 'The telescope is old and covered in a thick layer of dust. Wiping it clean, you notice the lens is still '
                                    'intact, though a bit cloudy from years of neglect. \nIt seems to point toward something beyond the castle walls, but it\'s'
                                    'hard to make out clearly.',
                       'artifacts': 'The artifacts are strange and foreign. One is a small, intricately carved stone that catches your eye. \n'
                                    'When you pick it up, a hidden mechanism clicks, and the stone shifts in your hand. Looks like some sort of puzzle to you.',
                       'Movements': ['South'],
                       'Exits': ['Grand_Ballroom(South)'],
                       'Items': [],
                       'Puzzle Reward': ['cell key'],
                       'Locked': True,
                       'Unlocked_By': ['silver key'],
                       'Puzzle_Help': 'The carved stone seems to be part of a hidden mechanism. If you rotate it correctly, something might happen.',
                       'Puzzle': {"1": {'Riddle': 'Rotate the stone (Type rotate) ',
                                        'Answer': 'rotate rotates',
                                        'Solved': False},
                                  "2": {'Riddle': 'Still no luck.. maybe rotate the stone again?',
                                        'Answer': 'rotate rotates',
                                        'Solved': False},
                                  "3": {'Riddle': 'I think you are getting closer. Try to rotate it again.',
                                        'Answer': 'rotate rotates',
                                        'Solved': False},
                                  "4": {'Riddle': 'Many have given up before you.. Want to give it another try?',
                                        'Answer': 'rotate rotates',
                                        'Solved': False}}},

        "Hidden_Chamber": {
            'Description': 'The hidden chamber contains a sleeping "dragon" that guards the key. To retrieve it, you must engage '
                           'the dragon in a mental duel rather than a physical fight. \nThe dragon challenges you with a task, which  '
                           'will test different skills like logic, memory, and quick thinking. Failing to accomplish any task will have \nserious consequences '
                           'and you might loose all your progress. (Type "interact" to interact with the dragon)',
            'Movements': ['North', 'South'],
            'Exits': ['Dungeon(North)', 'Final_Exit(South)'],
            'Items': [],
            'Locked': True,
            'Unlocked_By': ['blood moon key'],
            'Puzzle_Reward': ['eternity key']},

        "Final_Exit": {
            'Description': 'As you turn the key and the ancient door creaks open, a wave of fresh air rushes in. You’ve triumphed over darkness and deception. '
                           'With each step into the light, \nyou carry the stories of the castle and the promise of new adventures ahead.',
            'Locked': True,
            'Unlocked_By': ['eternity key'],
            'Items': [],
            'Movements': ['North'],
            'Exits': ['Hidden_Chamber(North)']}}
}

keys = {'golden key': {'prev_room': 'Crypt',
                       'c_room': 'Library'},

        'silver key': {'prev_room': 'Grand_Ballroom',
                       'c_room': 'Tower_Room'},

        'cell key': {'prev_room': 'Servant_Quarters',
                     'c_room': 'Dungeon'},

        'blood moon key': {'prev_room': 'Dungeon',
                           'c_room': 'Hidden_Chamber'},

        'eternity key': {'prev_room': 'Hidden_Chamber',
                         'c_room': 'Final_exit'},

        'bronze key': {'prev_room': 'Armory',
                        'c_room': 'Servant_Quarters'}

                         }

ExaminableItems = {

    'feathers': 'These feathers might be useful in future. You might want to keep it in your inventory.',
    'anvil': 'This anvil might be useful in future. You might want to keep it in your inventory.',
    'stone': 'This stone might be useful in future. You might want to keep it in your inventory.',
    'skull': 'This skull might be useful in future. You might want to keep it in your inventory.',
    'lamp': 'The glass of the lamp is broken, but it might work.',
    'murals': 'The ancient murals depict a forgotten ritual—the Dance of the Stars, where those seeking the castle\'s secrets '
              'must move in a perfect "cross", \naligning their steps with the celestial path to unlock hidden power.',
    'goblet': 'This goblet might be useful in future. You might want to keep it in your inventory.',
    'book': 'You carefully pull a dusty tome from the shelf and open it to reveal pages filled with intricate symbols '
            'and strange codes. As you scan the text, three powerful words stand out, \neach glowing faintly as if infused with magic:\n'
            '\nBLADE\nCROWN\nSWORD\n\nHmm.. You sense that these words hold the key to unlocking the mysteries of the Armory. '
            'Will you decipher their secrets?'

}

Items = {
    'feathers': {
        'Use': 'You place the feathers on the plate with the feather symbol. The plate sinks slightly into the floor with '
               'a soft click. It seems you’ve chosen wisely, but the puzzle isn’t complete yet.',
        'Room': 'Dungeon'},
    'anvil': {
        'Use': 'The weight of the anvil causes the plate to sink heavily into the ground with a loud thud. The air feels tense, '
               'as if the dungeon is waiting for more.',
        'Room': 'Dungeon'},
    'stone': {
        'Use': 'You place the stone on the plate marked with its symbol. The plate shifts slightly downward with a dull grinding '
               'sound. You sense you’re on the right path, but the puzzle remains incomplete.',
        'Room': 'Dungeon'},
    'goblet': {
        'Use': 'As you place the goblet on the corresponding plate, it lowers smoothly into the floor with a metallic clink. '
               'The tension in the air grows, as though something important is about to happen.',
        'Room': 'Dungeon'},
    'skull': {
        'Use': 'As you place the skull onto the last plate, it sinks down with a heavy thud. The room falls eerily silent for a '
               'moment before a soft click echoes through the chamber. Suddenly, from a hidden compartment in the wall, something '
               'shiny catches your eye',
        'Room': 'Dungeon'},
    'lamp': {
        'Use': 'You light the old lamp, and a warm, flickering glow spreads through the room, illuminating its ancient secrets.',
        'Room': 'any'},
    'castle map': {
        'Use': "                                _________\n"
               "                               |  Tower  |\n"
               "                               |  Room   |\n"
               "                               |___   ___|\n"
               "                                   |  | \n"
               "                                ___|  |__\n"
               "                               |  Grand  |\n"
               "                               |Ball Room|\n"
               "                               |___   ___|\n"
               "                                   |  | <----- Grand Staircase\n"
               "       _________                ___|  |__                __________\n"
               "      |  Crypt  | _ _ _ _ _ _ _| Entrance| _ _ _ _ _ _ _|   Armory |\n"
               "      |           Left Corridor    Hall    Right Corridor          |\n"
               "      |___   ___|  - - - - - - |_________| - - - - - - -|____   ___|\n"
               "          |  |                                               |  |  \n"
               "       ___|  |___                          _________     ____|  |___\n"
               "      | Library  |                        |         | _ _| Servant  |\n"
               "      |          |                        | Dungeon  _ _ _ Quarters |\n"
               "      |__________|                        |___   ___|    |__________|\n"
               "                                              |  | \n"
               "                                         _____|  |______ \n"
               "                                         |              |\n"
               "                                         |Hidden Chamber|\n"
               "                                         |              |\n"
               "                                         |_____    _____|\n"
               "                                         ______|   |_____\n"
               "                                         |  Final Exit   |\n",
        'Room': 'any'}
}


def interactWithDragon():
    symbols = ['*', '#', '!', '$', '@', '^', '^', '@', '$', '!', '#', '*']
    print(
        "DRAGON:\nMortal, you dare disturb my slumber in search of the key? Very well. But only those with a mind sharper than my claws may "
        "proceed. Your trial begins now.")
    print(
        "\nThe dragon breathes a stream of shimmering symbols into the air. These symbols will pulse and shift before your eyes, burning themselves "
        "into your \nmind for just a few fleeting moments. Then, as quickly as they appear, they will vanish, leaving only faint after-images in the darkness.")
    print(
        "\nPress 'ready' when you are ready to view the symbols. (Hint: Remember well, for what is forgotten is forever lost. )")
    command = input("Enter command: ").lower()
    if command == "ready":
        sequence = ' '.join(symbols)
        print(sequence)
        time.sleep(10)
        clear_screen()

        print("Now, tell me… what did you see?", end=" ")
        lives = 3
        for i in range(3):
            print(f"{lives} tries remaining.")
            answer = input("Enter the sequence (include spaces): ")
            if answer == sequence:
                reward = gameState['rooms']['Hidden_Chamber']['Puzzle_Reward'][0]
                print(
                    'DRAGON:\n"At last, a worthy soul. Your resolve and cunning have brought you here, beyond the reach of most."')
                print(
                    "The dragon’s eyes glow with a hint of respect as the chamber’s heat cools.The dragon exhales a plume of smoke, revealing the "
                    f"{reward}.")
                gameState['rooms']['Hidden_Chamber']['Items'].append(reward)
                print(
                    'DRAGON:\n"This is your passage to freedom. Go now, and let the castle\'s secrets rest... for now."')

                break
            elif i == 0:
                print("DRAGON:\n\"Foolish mortal, your memory fails you. The heat rises, and my patience wears thin.\""
                      "\nThe ground trembles beneath you as the dragon’s anger stirs.")
                lives -= 1
            elif i == 1:
                print(
                    "DRAGON:\n\"Still, you falter! My fury burns brighter. One more misstep and your journey will end here.\""
                    "\nThe walls quake violently, and the chamber swelters as flames lick the edges of the room.")
                lives -= 1
            elif i == 2:
                print("DRAGON:\n\"You have squandered your chances! Now, feel my wrath!\""
                      "\nA deafening roar shakes the room. The chamber plunges into darkness")
                lives -= 1
        else:
            print(
                'DRAGON:\n"Pathetic! You have failed me for the last time. Return to the start and come back only if you dare."')
            print("\n\nGAME OVER!!!")


def clear_screen():
    print("\n" * 50)


def interactWithBodyless():
    print(
        "BODYLESS:\nAh, I see you’ve wandered far into the castle. Few have found me, and fewer have left with their minds intact. "
        "\nTell me, adventurer, are you one who seeks answers or more puzzles to tangle your thoughts?")
    print('\n(Option 1): "I seek answers. Tell me who you are and what you want."'
          '\n(Option 2): "I enjoy a good challenge. What puzzle do you have for me?"')

    while True:
        choice = input("Choose your option : ").lower()
        if choice in "option 1":
            print(
                'BODYLESS:\nAnswers? Oh, answers, I have many. I was once a servant of this castle. But long ago, I angered the wrong master, '
                'and my body was taken as punishment. \nNow, I remain only as this... a whisper in the shadows. He sighs.')
            print(
                'But since you want answers, listen closely. Somewhere in this room lies a key. But only those who are sharp of mind may claim it.')
            print('\n(Option 1): "Tell me the riddle. I\'m ready."'
                  '\n(Option 2): "This is nonsense! I don\'t have time for games.')
            while True:
                c1 = input("Enter your choice : ").lower()
                if c1 in "option 1":
                    return True
                elif c1 in "option 2":
                    print("Ah! You stupid, useless creature. I hope you remain stuck within thee walls forever.")
                    return True
                else:
                    print("Invalid option")

        elif choice in "option 2":
            print(
                'BODYLESS:\nA challenge, is it? Very well, I respect your taste for riddles. My body is gone, but my mind remains '
                'sharp. Let me see if yours is too. \nYou want a reward, don’t you? You seek something that unlocks more than just doors.')
            print('Bodyless grins mischievously.')
            print('\n(Option 1): "Yes, give me the riddle!"'
                  '\n(Option 2): "You speak in riddles. Just tell me where the key is!"')
            while True:
                c2 = input("Enter your choice : ").lower()
                if c2 in 'option 1':
                    return True
                elif c2 in "option 2":
                    print("Ah! You impatient creature.")
                    return True
                else:
                    print("Invalid option")

        else:
            print("Invalid option")
