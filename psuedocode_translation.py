value = int(input("enter a 2 digit intager: "))
operation = input("calculate additive or multiplicative persistence (a or b)").lower()
i = 0
while value > 9:
    if operation == "a":
        value = (value % 10) + (value // 10)
    else:
        value = (value % 10) * (value // 10)
    i += 1
print("the persistence is: " + str(i))