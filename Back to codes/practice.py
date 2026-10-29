import sys


def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)


values = list(map(int, sys.stdin.buffer.read().split()))
n = values[0]
numbers = values[1:1 + n]

print(sum_even_numbers(numbers))