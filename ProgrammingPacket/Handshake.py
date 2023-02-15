file = open("handshake.dat", "r")

sick = []
companies = []
for x in range(int(file.readline())):
    employees = {}
    companies.append(employees)
    amt = int(file.readline())
    for i in range(amt):
        shaker, shakees = file.readline().split(':')
        shaker = shaker.strip()
        shakees = list(map(str.strip, shakees.split(',')))
        employees[shaker] = shakees
    sick = employees


for company in companies:
    for shaker, shakees in company.items():
        print(sick)