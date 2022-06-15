# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def primes(n):
    j = 1
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            print(j, p)
            j += 1
            if j == 10002:
                break
            for i in range(p, n + 1, p):
                sieve[i] = False


print(primes(200000))
