def ValidISBN10(num):
    num = list(num)
    check = num.pop(-1)
    for i in range(len(num)):
        num[i] = int(num[i])
    val = 0
    for i in range(len(num)):
        val += num[i] * ((len(num)+1)-i)
    calcCheck = 11 - (val % 11)
    if calcCheck == 10:
        calcCheck = "X"
    elif calcCheck == 11:
        calcCheck = 0
    if str(calcCheck) == check:
        return True
    else:
        return False
    

def ValidISBN13(num):
    num = list(str(num))
    for i in range(len(num)):
        num[i] = int(num[i])
    check = num.pop(-1)
    val = 0
    odd = (len(num) % 2 == 1)
    for i in range(len(num)):
        if odd:
            if i % 2 == 0:
                val += num[i] * 3
            else:
                val += num[i]
        
        else:
            if i % 2 == 0:
                val += num[i]
            else:
                val += num[i] * 3
    
    calcCheck = 10-(val % 10)
    if calcCheck == 10:
        calcCheck = 0
    if check == calcCheck:
        return True
    else: 
        return False

def ValidUPC(num):
    num = list(num)
    for i in range(len(num)):
        num[i] = int(num[i])
    check = num.pop(-1)
    odd = (len(num) % 2 == 1)
    val = 0
    if odd:
        for i in range(len(num)):
            if i % 2 == 0:
                val += num[i]
        val = val * 3
        for i in range(len(num)):
            if i % 2 == 1:
                val += num[i]
        calcCheck = 10 - (val%10)
        if calcCheck == 10:
            calcCheck = 0
    else:
        for i in range(len(num)):
            if i % 2 == 1:
                val += num[i]
        val = val * 3
        for i in range(len(num)):
            if i % 2 == 0:
                val += num[i]
        calcCheck = 10 - (val%10)
        if calcCheck == 10:
            calcCheck = 0
    if calcCheck == check:
        return True
    else:
        return False

print(ValidISBN10("1841462012"))
print(ValidISBN13(9781861978768))
print(ValidUPC("0974213606"))