def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_prime_sums(target):
    primes = get_primes_up_to(target)
    results = []
    i, j = 0, len(primes) - 1
    while i <= j:
        if primes[i] + primes[j] == target:
            results.append((primes[i], primes[j]))
            i += 1
            j -= 1
        elif primes[i] + primes[j] < target:
            i += 1
        else:
            j -= 1
    return results
target_number = int(input("Enter an integer: "))
prime_pairs = find_prime_sums(target_number)

if prime_pairs:
    for pair in prime_pairs:
        print(f"{pair[0]} + {pair[1]} = {target_number}")
else:
    print("No prime pairs sum up to the given number.")
