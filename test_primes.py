#!/usr/bin/env python3

import primes

def test_primes():
    assert primes.eratosthenes(5) == [2,3]
    g = primes.gen_eratosthenes()
    assert [next(g) for _ in range(3)] == [2,3,5]
    
