from main import power, factorial, permutation, combination

def test_power():
    assert power(2, 3) == 8

def test_factorial():
    assert factorial(5) == 120

def test_permutation():
    assert permutation(5, 2) == 20

def test_combination():
    assert combination(5, 2) == 10

test_power()
test_factorial()
test_permutation()
test_combination()
