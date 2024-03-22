def power(base, exponent):
    return base ** exponent

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def permutation(n, r):
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i
    return numerator

def combination(n, r):
    numerator = 1
    denominator = 1
    for i in range(n, n-r, -1):
        numerator *= i
    for i in range(1, r+1):
        denominator *= i
    return numerator // denominator
