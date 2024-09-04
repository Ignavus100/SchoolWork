List = []
intager = int(input("factor number: "))
def nextPrime(prev):
    i = prev + 1
    while not(isPrime(i)):
        i+=1
    return i
def isPrime(num):
    num = int(num)
    if num > 1:
  
    # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
def main(intager, List):
    if isPrime(intager):
        List.append(int(intager))
        List.sort()
        for i in range(len(List)):
            if i == len(List)-1:
                print(List[i])
            else:
                print(List[i], "x", end=" ")
        exit()
    prime = 2
    if not(isPrime(intager)):
        while intager % prime != 0:
            prime = nextPrime(prime)
    List.append(int(prime))
    intager = intager / prime
    main(intager, List)    
main(intager, List)