import Map as m
import Menu








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