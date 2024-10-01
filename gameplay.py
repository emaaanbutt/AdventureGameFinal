import Map as m
import Menu
import json
import random

WHITE_BG = "\033[47m"
RESET = "\033[0m"

character = "Warrior"
color = Menu.DEFAULT
room = "Entrance_Hall"
current_room = m.gameState['rooms'][room]
inventory = []


def gameplay():
    global room
    global current_room
    global inventory

    print("Welcome,"+WHITE_BG+color+f"{character}!"+RESET+" You've just stepped into the Mysterious Castle—where secrets lurk in every shadow "
          "and puzzles await your cleverness. \nGet ready for a wild adventure filled with surprises and maybe a monster or two!\n")

    print(WHITE_BG+color+f"{character}!"+RESET+f" you are in the {room}.")
    print(current_room['Description'])

    while True:
        command = input("\nEnter command : ").lower()

        if command == "quit":
            print("Exiting game...")
            break
        elif command == "look":
            look()
        elif command[0:2] == "go":
            move(command[3:])
        elif command[0:7] == "examine":
            examine(command[8:])
        elif command[0:12] == "solve puzzle" or command[0:12] == "solve riddle":
            displayPuzzle()
        elif command == "interact" and room == 'Servant_Quarters':
            if m.interactWithBodyless():
                displayPuzzle()
        elif command == "interact" and room == "Hidden_Chamber":
            m.interactWithDragon()
        elif command[0:9] == "inventory":
            displayInventory()
        elif command[0:4] == "take":
            item = command[5:]
            takeItem(current_room, item)
        elif command[0:4] == "drop":
            item = command[5:]
            dropItem(current_room, item)
        elif command[0:3] == "use":
            item = command[4:]
            if command[-3:] == 'key':
                useKey(item)
            else:
                useItem(item)
        elif command == "save":
            print("Saving game...\n")
            save_game()
        elif command == "load":
            room, inventory, m.gameState = load_game()
            gameplay()
        elif command == "help":
            Menu.help()
        elif command[0:3] == "use":
            item = command[4:]
            useItem(item)
        else:
            print("Invalid command.")


def move(command):
    global current_room
    global room
    availableMovements = current_room['Movements']
    found = False
    for i in range(len(availableMovements)):
        if command.lower() == availableMovements[i].lower():
            prev_room = room
            room = current_room['Exits'][i].split('(')[0]
            current_room = m.gameState['rooms'][room]
            if not current_room['Locked']:
                print(WHITE_BG+color+f"{character}!"+RESET+f", you have entered the {room}. ")
                print(current_room['Description'])
                found = True
                if room == "Final_Exit":
                    print("\nGame Over...")
                    loadDefaultGame()
                    menu()
            else:
                if current_room['Locked']:
                    required_key = current_room['Unlocked_By'][0]  # this will check if the room is locked and will open by a specific key
                    print(f"The door to the {room} is locked. You need to find the {required_key} hidden in another part of the castle to unlock it.")
                    room = prev_room
                    break

    else:
        if not found:
            print("You attempt to move forward, but there's no way through, "+WHITE_BG+color+f"{character}!"+RESET+" You need to reconsider your direction.")

def look():
    print(current_room['Description'])
    print("\nThe collectable items present in this room are : ")
    for item in current_room['Items']:
        print(item)
    displayExits()

def examine(command):
    item = command.lower()
    if item in current_room['Items'] or item in inventory:
        print(m.ExaminableItems[item])
    elif item in current_room.keys():
        print(current_room[item])
    else:
        print(f"{item} is not examinable.")


def displayExits():
    print("\nThe exits are : ")
    for i in current_room['Exits']:
        print(i)


def displayPuzzle():
    if all(p['Solved'] for p in current_room['Puzzle'].values()):
        print("It seems like you have already solved this puzzle. Move ahead...")
        return
    else:
        print(current_room['Puzzle_Help'])
        for key, value in current_room['Puzzle'].items():
            riddle = current_room['Puzzle'][key]
            if not riddle['Solved']:
                print(riddle['Riddle'])
                solvePuzzle(key)
            elif riddle['Solved']:
                continue

        if all(p['Solved'] for p in current_room['Puzzle'].values()):
            reward = current_room['Puzzle Reward'][0]
            print("\nWell done "+WHITE_BG+color+f"{character}!"+RESET+f" The puzzle clicks into place, and a \"{reward}\" appears before you, "
                  "cold and shimmering in the dim light.")
            current_room['Items'].append(reward.lower())


def solvePuzzle(key):
    global inventory
    while True:
        riddle = current_room['Puzzle'][key]
        answer = input("Enter your answer (type 'back' to go back): ").lower()
        if answer == "back":
            gameplay()
        elif answer in riddle['Answer'].lower():
            riddle['Solved'] = True
            return True
        elif answer[0:3] == "use":
            if answer[4:] in inventory:
                print(m.Items[answer[4:]]['Use'])
                riddle['Solved'] = True
            else:
                print(f"{answer[4:]} not found in inventory. Type \"back\" to go back.")
        else:
            denials = [
                '\nYour answer echoes through the castle halls, but the silence that follows tells you it wasn\'t the right one.Try again.',
                '\nA shadow flickers across the room, as if the castle itself is shaking its head. Rethink your answer and try once more!',
                '\nThe walls seem to sigh in disappointment as your answer fades away. Think carefully and try again!',
                '\nYour answer falls flat like a castle ghost\'s joke—no laughs here! Dust yourself off and give it another whirl!']
            message = random.choice(denials)
            print(message)

# inventory methods:
def displayInventory():
    if len(inventory) == 0:
        print("There is nothing in your inventory")
    else:
        print("The items in your inventory are: ")
        print(inventory)


def useKey(item):
    global current_room
    global inventory
    global room
    rooms = m.gameState['rooms']

    if len(inventory) == 0:
        print("There is nothing in your inventory")
        return

    if item in inventory:
        if item in m.keys.keys():
            c_room = m.keys[item]['c_room']
            if m.keys[item]['prev_room'] == room:
                if rooms[c_room]['Locked']:
                    if rooms[c_room]['Unlocked_By'][0] == item:
                        rooms[c_room]['Locked'] = False
                        print(WHITE_BG+color+f"{character}!"+RESET+f" you have used the {item} to unlock the door to the {c_room}.")
                    else:
                        print(f"The {item} does not matches with the key to unlock {c_room}.")
                else:
                    print(f"The {c_room} is already unlocked. Move ahead...")
            else:
                print(f"The {item}  cannot be used to unlock {c_room}")
        else:
            print(f"The {item} does not exist.")
    else:
        print(f"This {item} is not present in your inventory.")


def useItem(item):
    if item in m.Items.keys():
        if m.Items[item]['Room'] == room:
            print(m.Items[item]['Use'])
        else:
            print(WHITE_BG+color+f"{character}!"+RESET+f" This {item} seems to have lost its purpose in this place—try using it somewhere else!")
    else:
        print(WHITE_BG+color+f"{character}!"+RESET+f" This {item} cannot be used at all. Try something else.")


def takeItem(curr_room, item):
    if item in curr_room["Items"]:
        inventory.append(item)
        print(f"The {item} has been added to the inventory.")
        curr_room['Items'].remove(item)
    elif item in inventory:
        print(f"The {item} is already present in the inventory.")
    else:
        print(f"The {item} cannot be taken.")


def dropItem(curr_room, item):
    if item in inventory:
        curr_room['Items'].append(item)
        inventory.remove(item)  # this line will remove the item from the inventory
        print(f"You have dropped the item into the {room}")
    else:
        print(f"The {item} is not present in the inventory.")



def save_game():
    with open('savefile.txt', 'w') as file:
        file.write(f"Room: {room}\n")
        file.write(f"{inventory}\n")

    with open('gameState.json', 'w') as file:
        json.dump(m.gameState, file)

    print("Game saved successfully.")


def load_game():
    global room, inventory
    lineCounter = 0
    try:
        with open('savefile.txt', 'r') as file:
            for line in file:
                if lineCounter == 0:
                    room = line.strip()[6:]
                elif lineCounter == 1:
                    inventory = line.strip()
                lineCounter += 1

        with open('gameState.json', 'r') as file:
            m.gameState = json.load(file)

        return room, inventory, m.gameState

    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        gameplay()


def defaultState():
    with open('defaultState.json', 'w') as file:
        json.dump(m.gameState, file)


def loadDefaultGame():
    with open('defaultState.json', 'r') as file:
        m.gameState = json.load(file)


def menu():
    print("\n1. Start the Adventure")
    print("2. Customize Your Character")
    print("3. Read the Backstory")
    print("4. Instructions")
    print("5. Load previous game")
    print("6. Exit Game\n")
    choice = int(input("Enter your choice : "))

    global character, color
    global room, inventory

    if choice == 1:
        gameplay()
    elif choice == 2:
        character, color = Menu.customizeCharacter()
        menu()
    elif choice == 3:
        Menu.backstory()
        menu()
    elif choice == 4:
        Menu.instructions()
        menu()
    elif choice == 5:
        room, inventory, m.gameState = load_game()
        gameplay()
    elif choice == 6:
        print("Exiting game....")
        return 0
    else:
        print("Invalid choice.")
        menu()


def main():
    print("\nWelcome to the Mysterious Castle Adventure!\n")
    defaultState()
    menu()


main()