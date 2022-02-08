# https://www.codewars.com/kata/54d4c8b08776e4ad92000835

import math


def divisors(n):
    divs = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    divs.extend([n])
    return list(set(divs))


def isPP(n):
    divisors_n = [int(x) for x in divisors(n)]
    divisors_n.remove(n)
    divisors_n.sort()

    m = 0
    k = 2
    while k <= math.log(n, 2):
        for m in divisors_n:
            if math.pow(m, k) == n:
                return [m, k]
        k += 1
    return None
