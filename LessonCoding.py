number = int(input("enter an intager greater than 1: "))
x = 2
count = 0
while number > 1:
    multi = False
    while(number % x) == 0:
        if not multi:
            print(x)
        count += 1
        multi = True
        number = number // x
    x += 1
print(count)