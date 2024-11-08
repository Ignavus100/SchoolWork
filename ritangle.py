val = 0
i = 0
ritangle = list("RITANGLE")
triangle = list("TRIANGLE")
while val < 100001:
    val += i + 1
    if val % 90==0:
        if ritangle[int((val/90)%8)] == triangle[i%8]:
            print(val)

    
    i += 1



    

