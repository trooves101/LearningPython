file = open("interview.dat", "r")

ApplicantSets = []
first_index = 0

for i in range(int(file.readline())):  # Runs for however many the .dat said to
    Applicants = {}  # Creates a dictionary to store each person
    ApplicantSets.append(Applicants)  # Appends applicants for whenever it loops
    amt = int(file.readline())
    for x in range(amt):  # Runs for however many the file says
        name, score = file.readline().split(" ", 1)  # splits the first " "
        name = name.strip()
        score = list(map(str.strip, score.split(" ")))  # Splits into map
        Applicants[name] = score

for sets in ApplicantSets:  # runs for amount of dictionaries in the list
    for name, score in sets.items():  # runs for however much data is in the dictionary
        total = int(score[0]) + int(score[1]) + int(score[2])  # score is the 3 integers which are what the people ot on their interviews
        score = total
        ApplicantSets[first_index][name] = score
    ApplicantSets[first_index] = sorted(ApplicantSets[first_index], key=ApplicantSets[first_index].get)  # sorts the dictionary from least to greatest
    ApplicantSets[first_index].reverse()
    print(", ".join(ApplicantSets[first_index]))
    first_index += 1
