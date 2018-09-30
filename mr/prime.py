"""
Primality Check
"""

from random import randint


def isprime(n):
    """
    If given number is prime, this function return true.
    """
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    s, d = _represent_format(n - 1)
    print(s, d)
    testing = randint(2, n - 2)
    print(testing)
    if _first_condition(testing, n, d) and _second_condition(testing, n, s, d):
        return False
    return True


def _first_condition(testing, mod, d):
    return (testing**d) % mod != 1


def _second_condition(testing, mod, s, d):
    for i in range(s):
        if testing**((2**i) * d) % mod == mod - 1:
            return False
    return True


def _represent_format(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    return count, n


if __name__ == '__main__':
    print(isprime(9))
    print(isprime(73))
    print(isprime(99923))
