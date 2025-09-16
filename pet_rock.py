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
    
    show_stats(name,rock)

if __name__ == "__main__":
    main()