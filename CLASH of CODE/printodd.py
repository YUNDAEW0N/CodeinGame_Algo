import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
stack=[]

while (n>=1):
    if n%2==0:
        n=n-1
    
    stack.append(n)
    n=n-2

while stack:
    a=stack.pop()
    print(a)




