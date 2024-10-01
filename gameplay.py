import Map as m
import Menu
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


def main():
    print("\nWelcome to the Mysterious Castle Adventure!\n")
    defaultState()
    menu()


main()