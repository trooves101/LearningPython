fruitbowl = []
storage = int(input("How much storage does your fruit bowl have?"))


def remove():  # creates a function that removes something from the list
    usr1 = input("Which fruit would you like removed?")
    try:
        fruitbowl.remove(usr1)
        return fruitbowl
    except ValueError:
        return "Please enter a valid fruit."


def add():  # function that adds/appends the fruit the user inputs
    usr2 = input("Which fruit would you like to add?")
    fruitbowl.append(usr2)
    return fruitbowl


def fcount():  # function that counts the amount of fruit the user inputs
    usr3 = input("Which fruit would you like to count?")
    return fruitbowl.count(usr3)


actions = {  # creates a dictionary to store da functions
    "remove": remove,
    "add": add,
    "count": fcount
}

while storage != len(fruitbowl):  # while loop that continues until storage == length
    usr4 = input("Would you like to remove, add, or count a fruit?")
    if usr4 in actions:  # checks if the input is in the actions dictionary
        print(actions[usr4]())
    else:
        print("Invalid input, enter 'remove', 'add', or 'count'.")
