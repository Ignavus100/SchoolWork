List = []
intager = int(input("factor number: "))
def nextPrime(prev):
    prime = False
    i = prev + 1
    if isPrime(i):
        return i 
def isPrime(intager):
    flag = False
    if intager == 0 or intager == 1:
        return False
    elif intager > 1:
        for i in range(2, int(intager)):
            if (intager % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True
def main(intager):
    prime = 2
    if isPrime(intager):
        List.append(int(intager))
        print(List)
        exit()
    else:
        while intager % prime != 0:
            prime = nextPrime(prime)
    List.append(int(prime))
    intager = intager / prime
    main(intager)
main(intager)