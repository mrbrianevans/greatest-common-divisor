import random
from datetime import datetime


def euclid(x, y):
    m = max(x, y)
    n = min(x, y)
    if n == 0:
        return m
    r = m % n
    m = n
    n = r
    return euclid(m, n)


def primary_school_method(x, y):
    x_prime_factors = list()
    y_prime_factors = list()

    j = 2
    while x > 1:
        if x % j == 0:
            x /= j
            x_prime_factors.append(j)
        else:
            j += 1

    j = 2
    while y > 1:
        if y % j == 0:
            y /= j
            y_prime_factors.append(j)
        else:
            j += 1

    greatest_common_divisor = 1
    for factor in x_prime_factors:
        if factor in y_prime_factors:
            greatest_common_divisor *= factor
            y_prime_factors.remove(factor)
    return greatest_common_divisor


def consecutive_integers(x, y):
    common_factors = list()
    for i in range(1, min(x, y)+1):
        if x % i == 0 and y % i == 0 or i == 1:
            common_factors.append(i)
    return max(common_factors)


def speedtest(function, iterations=1000):
    begin = datetime.now().timestamp()
    for x in range(1, iterations):
        for y in range(1, iterations):
            function(x, y)
    finish = datetime.now().timestamp()
    return finish - begin


def accuracy_test(functions, iterations=100):
    for i in range(1, iterations):
        x = random.randrange(1000)
        y = random.randrange(1000)
        answer = functions[0](x, y)
        for function in functions:
            assert function(x, y) == answer


if __name__ == "__main__":
    accuracy_test([euclid, primary_school_method, consecutive_integers])
    print("Euclid:", speedtest(euclid, 1000), 'seconds')
    print("Middle-school method:", speedtest(primary_school_method, 1000), 'seconds')
    print("Consecutive Integers:", speedtest(consecutive_integers, 1000), 'seconds')
