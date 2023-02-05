fruitbowl = []
storage = input("How much storage does your fruit bowl have?")


def remove():  # creates a function that removes something from the list
    usr1 = input("Which fruit would you like removed?")
    if fruitbowl.index(usr1) == -1:  # checks if the user input is actually in the list
        return "Please enter a valid fruit."
        remove()
    else:
        fruitbowl.remove(usr1)  # removes it from the list
        return fruitbowl


def add():  # function that adds/appends the fruit the user inputs
    usr2 = input("Which fruit would you like to add?")
    fruitbowl.append(usr2)
    return fruitbowl


def fcount():  # function that counts the amount of fruit the user inputs
    usr3 = input("Which fruit would you like to count?")
    return fruitbowl.count(usr3)


while storage != str(len(fruitbowl)):  # while loop that continues until storage == length
    usr4 = input("Would you like to remove, add, or count a fruit?")
    if usr4 == "remove":
        print(remove())
    elif usr4 == "add":
        print(add())
    elif usr4 == "count":
        print(fcount())