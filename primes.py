#!/usr/bin/env python3
import sys

def eratosthenes(n):
    primes = {i:True for i in range(2,n)}
    for i in range(2,n):
        if primes[i] == True:
            for j in range(2*i, n, i):
                primes[j] = False
#     my_list = []
#     for prime in primes.keys():
#         if primes[prime] == True:
#             my_list.append(prime)
#            |------^
    return [prime for prime, is_prime in primes.items() if is_prime]

def hello_world():
    print("hello world!")

def gen_eratosthenes():
    def is_prime(pot_prime, l):
        prime_bool = True
        for p in l:
            if pot_prime % p == 0:
                return False
        return True
    
    primes = []
    pot_prime = 2
    while True:
        primes.append(pot_prime)
        yield pot_prime
        pot_prime += 1
        while not is_prime(pot_prime, primes):
            pot_prime += 1

def main():
    args = sys.argv
    n = int(args[1])
    print(eratosthenes(n))
#     print(gen_eratosthenes(n))

if __name__ == '__main__':
    main()