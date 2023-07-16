import random

# Define the rooms and their connections
rooms = {
    "Entrance Hall": {"North": "Library", "East": "Kitchen"},
    "Library": {"South": "Entrance Hall", "West": "Secret Passage"},
    "Kitchen": {"West": "Entrance Hall"},
    "Secret Passage": {"East": "Library", "North": "Treasure Room"},
    "Treasure Room": {"South": "Secret Passage"},
}

# Define items and their locations
items = {
    "key": "Kitchen",
    "torch": "Entrance Hall",
}

# Define the game state
player_location = "Entrance Hall"
inventory = []

def print_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("You are carrying:")
        for item in inventory:
            print(f"- {item}")

def move(direction):
    global player_location
    if direction in rooms[player_location]:
        player_location = rooms[player_location][direction]
        print(f"You move to the {player_location}.")
    else:
        print("You can't go that way.")

def get_item(item):
    if item in items and items[item] == player_location:
        inventory.append(item)
        print(f"You pick up the {item}.")
    else:
        print("There is no such item here.")

def check_for_win():
    return player_location == "Treasure Room" and "key" in inventory

def main():
    print("Welcome to Adventure Quest!")
    print("Your objective is to find the hidden treasure.")
    print("Use 'go [direction]' to move and 'get [item]' to pick up items.")

    while True:
        print("\n----------------------------------")
        print(f"You are in the {player_location}.")
        print_inventory()

        if check_for_win():
            print("Congratulations! You found the hidden treasure. You win!")
            break

        action = input("What will you do? ").lower().split()

        if action[0] == "go":
            if len(action) > 1:
                move(action[1].capitalize())
            else:
                print("Please specify a direction.")
        elif action[0] == "get":
            if len(action) > 1:
                get_item(action[1].lower())
            else:
                print("Please specify an item.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

