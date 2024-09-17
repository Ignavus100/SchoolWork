def main():
    startBase = int(input("beginning base: "))
    endBase = int(input("end base: "))
    endUnitsint = [10, 11, 12, 13, 14, 15]
    endUnitsLetter = ["A", "B", "C", "D", "E", "F"]
    num = input("number: ").upper()
    numb = 0
    num = list(num)
    for i in range(len(num)):
        if num[i] not in "1234567890":
            num[i] = endUnitsint[endUnitsLetter.index(num[i])]
    for i in range(len(num)):
        num[i] = int(num[i])
        numb += num[i]*(startBase**(len(num)-(i+1)))
        print(numb)
    conversion = []
    while numb > 0:
        conversion.append(numb % endBase)
        numb = numb // endBase
    for i in range(len(conversion)):
        if conversion[i]>9:
            conversion[i] = endUnitsLetter[i]
        conversion[i] = str(conversion[i])
    conversion.reverse()
    print(conversion)
main()