import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

x = int(input())
x += 1
while not is_prime(x):
    x += 1

print(x)
