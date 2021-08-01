"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""


def sum_min(numbers):

    return sum(numbers.pop(numbers.index(min(numbers))) for _ in range(2))


def sum_min2(numbers):

    return sum(sorted(numbers)[:2])


print(sum_min([19, 5, 42, 2, 77]))
print(sum_min2([19, 5, 42, 2, 77]))
