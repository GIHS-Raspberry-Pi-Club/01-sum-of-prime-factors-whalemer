#!/usr/bin/env python3

import math

# "Try to write your function without using trial division!"
# oops

def pf_sum(n):
    factors = []
    while n%2 == 0:  
        factors.append(2)
        n = n/2
    for i in range(3,math.floor(math.sqrt(n))+1,2):
        while n%i == 0:
            factors.append(i)
            n = n/i
    if n>2:
        factors.append(int(n))

    return reduce(lambda a,b: a+b, factors)

