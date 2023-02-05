num = int(input("Give any whole number: "))  # input() gets the input

if num < 0:  # checks if the number is less than zero (negative)
    print("Your number is negative")
elif num % 2 == 0:  # gets the remainder of the number to check if it's positive
    print("Your number is even")
elif num % 2 != 0:  # repeats the previous statement but for odd
    print("Your number is odd")
