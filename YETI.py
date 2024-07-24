string = input("string: ")
numbers = ""
letters = ""
for i in range(len(string)):
    if string[i] in "1234567890":
        numbers += string[i]
    else:
        letters += string[i]
print(letters)
print(numbers)