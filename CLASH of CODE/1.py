import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = int(input())
for i in range(t):
    n, k = [int(j) for j in input().split()]
    print(k - n % k)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print("The number of students for each testcase.")
