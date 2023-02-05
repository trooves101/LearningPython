string = "Hello Testing"  # Define variable
while len(string):  # While loop with the condition being when the string is empty.
    print(string)
    string = string[:len(string) - 1]  # Removes the last letter from the string
