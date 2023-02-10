with open("handshake.dat", "r") as file:
    sets = file.readline()
    temps = []
    for datanum in range(int(sets)):
        values = file.readline()
        for value in range(int(values)):
            data = file.readline().strip()
            temps.append(data.replace(" : ", " ").replace(", ", " ").split())
        print(temps)
        temps.clear()