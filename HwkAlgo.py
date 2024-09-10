X = int(input("Enter an intager greater than one: "))
Product = 1
Factor = 0
while Product < X:
    Factor += 1
    Product = Product * Factor
if X == Product:
    Product = 1
    for i in range(Factor):
        Product = Product * i
        print(i + 1)
else:
    print("no result")