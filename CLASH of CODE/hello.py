import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if len(a) > 0:
    print("*" * (len(a) + 4))
    print("* " + a + " *")
    print("*" * (len(a) + 4))
else:
    print("***")
    print("*  *")
    print("***")