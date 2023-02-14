file = open("handshake.dat", "r")

sick = ["Employee_A"]
healthy = []

for i in range(int(file.readline())):
    for f in range(int(file.readline())):
        line = file.readline()
        first_index = line.index(" ")
        healthy.append(line[:first_index].strip())
        healthy.append(line[first_index+3:].strip())
    print(healthy)
    healthy.clear()
