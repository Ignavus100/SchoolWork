goal = 2024
number = 1
for i in range(goal):
    total = 0
    temp = 1
    j = 0
    while total < 2024:
        total += i + j
        j += 1
    if total == 2024:
        number = number * j
print(number)