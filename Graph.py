with open("graph.dat", "r") as file:
    line = file.readline()
    data = []
    for i in range(int(line)):
        line = file.readline()
        data.append(int(line))

for i in range(len(data)):
    spaces = data[i] - 2
    for x in range(data[i]-1):
        print("|" + " " * spaces + "/")
        spaces -= 1
    print("+" + "-" * data[i])