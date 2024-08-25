planets = int(input("number of planets"))
planetFacts = []
value = []
for i in range(planets):
    planetFacts.append(input("planet " + str(i+ 1)).split())
    value.append(float(planetFacts[i][0])/(0.5 * float(planetFacts[i][1]) * float(planetFacts[i][1])))
    
print(value.index(max(value)) + 1)