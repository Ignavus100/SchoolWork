a = 2024
c = 2025
b = 1
total = 0
while b<c:
    b = (c**2 - a**2)**0.5
    if b == b//1:
        total += 1
        print(a, b, c, total)
    c += 1
