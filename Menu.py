# Text colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
DEFAULT = "\033[39m"

def customizeCharacter():
    myCharacter = input("Welcome, adventurer! What shall we call you? Your name will echo through the halls of the castle! Choose wisely: ")
    print("As you prepare for your journey, it's time to choose your class! Will you be a :")
    print("1. 'Warrior', skilled in combat and strength")
    print("2. A 'Mage' with the power of arcane spells")
    print("3. An 'Archer' who strikes from the shadows with unmatched precision")

    while True:
        try:
            myClass = int(input("Enter your choice: "))
            if myClass in [1, 2, 3]:
                break
            else:
                print("Please choose a valid option: 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    myColor = DEFAULT
    print("Every hero has a signature color! What color will represent your spirit? ")
    print("1. BLACK")
    print("2. RED")
    print("3. GREEN")
    print("4. YELLOW")
    print("5. BLUE")
    print("6. MAGENTA")
    print("7. CYAN")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                if choice == 1:
                    myColor = BRIGHT_BLACK
                elif choice == 2:
                    myColor = BRIGHT_RED
                elif choice == 3:
                    myColor = BRIGHT_GREEN
                elif choice == 4:
                    myColor = BRIGHT_YELLOW
                elif choice == 5:
                    myColor = BRIGHT_BLUE
                elif choice == 6:
                    myColor = BRIGHT_MAGENTA
                elif choice == 7:
                    myColor = BRIGHT_CYAN

                break
            else:
                print("Please choose a valid option: 1-7")
        except ValueError:
            print("Invalid input. Please enter a number (1-7).")


    print(f"\nYou are good to go, {myCharacter} .")
    return myCharacter, myColor

def backstory():
    print('\nOnce a grand stronghold of a noble family, the castle became a place of sorrow ',
    'after a dark betrayal sealed its fate. A powerful curse engulfed \nthe castle, trapping ',
    'the spirits of its former inhabitants within its walls and preventing anyone from entering ',
    'or leaving. Legends \nwhisper of hidden treasures and ancient artifacts scattered throughout '
    'the castle, each guarded by intricate puzzles designed to test the brave. ')
    print("\nAs you step into this forsaken realm, a heavy silence envelops you. Your mission is clear: explore the ",
    "various rooms of the castle, solve the \nenigmatic challenges that protect the secrets of ",
    "the past, and unravel the mystery behind the betrayal. With each puzzle you conquer, \nyou ",
    "draw closer to breaking the curse and freeing the tormented souls. Only through \nyour courage, ",
    "wit, and determination can you uncover the truth and escape the castle’s grasp.\n")

def instructions():
    print("Game Instructions")
    print("Welcome to The Mysterious Castle Adventure! Your goal is to navigate through ",
    "the haunted castle, solve puzzles, and ultimately \nescape its grasp. You’ll explore various "
    "rooms, uncover secrets, and confront challenges that stand in your way.")
    print("\nObjective: Your mission is to find a way out of the castle by exploring its rooms, ",
    "collecting items, and solving intricate puzzles.\nOnly by piecing together the history of the ",
    "castle and its past inhabitants can you hope to break the curse that binds it.")
    help()
    print('\nTips:')
    print('-Pay attention to your surroundings; clues may be hidden in descriptions.')
    print('-Items you collect may be vital for solving puzzles')

def help():
    print("Available Commands")
    print('Movement: "go [direction]" (e.g., "go north", "go south")')
    print('"look" - Redisplay current room description')
    print('"inventory" - Show player\'s inventory')
    print('"take [item]" - Pick up an item')
    print('"drop [item]" - Drop an item')
    print('"use [item]" - Use an item in the current room')
    print('"examine [object]" - Get more details about an object in the room')
    print('"save" - Save the current game state')
    print('"load" - Load a previously saved game')
    print('"quit" - Exit the game')
    print('"help" - Display available commands')