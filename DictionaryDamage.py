import time

i = True  # creates a boolean variable


def damage(weapon):  # defines a function which has a dictionary associated with weapon damage.
    stats = {
        "Halberd": 126,
        "Sword": 68,
        "Hammer": 214
    }
    return stats[weapon]  # when the function is called with a parameter it'll return this.


while i:  # loops while "i" is true
    usr1 = input("Give a weapon name.\n")  # prompts the user with that question allowing a user input
    print("The " + usr1 + " does " + str(damage(usr1)) + " damage.")  # prints the damage using the dictionary
    time.sleep(5)
    usr2 = input("Do you want to continue getting the stats Yes or No?\n")
    if usr2 in ("n", "no", "No", "N"):  # if the user input is "no" then it runs this
        i = False # makes i false so the while loop stops running
