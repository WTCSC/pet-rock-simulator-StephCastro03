def naming():
    name = input("What would you like to name your pet rock?")
    return name
def show_stats(name,rock):
    print(f"great choice your rocks name is {name}")
    print(f"Hunger:{rock['Hunger']}/10")
    print(f"Happiness:{rock['Happiness']}/10")

def main():

    rock = { 
        "Hunger" : 5,
        "Happiness" : 5,
        }
    
    print("Welcome to the Pet Rock Simulator!")

    name = naming()

while True:
    show_stats(name, rock)
    if rock ["Hunger"] >= 10:
        print(f"{name} got too hungry and rolled away to find food")
        print("Game Over")
        break 
    if rock["Happiness"] <= 0:
        print(f"{name} got to sad and left you for a owner who is more fun.")
        print("Game Over")
        break 
    print("What do you want to do with your Rock?")
    print(" 1. Feed the rock")
    print(" 2. Play with the rock")
    print(" 3. Do nothing")
    print(" 4. Quit the game")

    choice = input("Your choice: ")

    if choice == "1":
        rock["Hunger"] -= 2
        rock["Happiness"] += 1
        print(f"You fed {name}. Your rocks normally don't eat but your rock enjoyed the food.")
    elif choice == "2":
         rock["Hunger"] += 1
         rock["Happiness"] += 2
         print(f"You played with {name}. The rock looks slighly more excited!")
    elif choice == "3":
        rock["Hunger"] += 2
        rock["Happiness"] -= 2
        print(f"You ignored {name}. The rock looks very very lonely.")
    elif choice == "4":
        print(f"You decided to stop caring for {name}. Goodbye!")
        print("Game Over")
        break
    else:
        print(f"{name} tilts slightly. Your rock doesn't understand the choice you made.")
    
    rock["Hunger"] += 1
    rock["Happiness"] -= 1

    if rock["Hunger "] < 0:
        rock["Hunger "] = 0
    if rock["Happiness"] > 10:
        rock["Happiness"] = 10

if __name__ == "__main__":
    main()