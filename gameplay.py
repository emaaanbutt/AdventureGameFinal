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


def main():
    print("\nWelcome to the Mysterious Castle Adventure!\n")
    defaultState()
    menu()


main()