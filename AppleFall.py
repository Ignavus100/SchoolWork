planets = int(input("number of planets"))
planetFacts = []
value = []
for i in range(planets):
    planetFacts[i] = input("planet", str(i)).split()
    value[i] = int(planetFacts[i][0])/(0.5 * int(planetFacts[i][1]) * int(planetFacts[i][1]))
print(value.max())