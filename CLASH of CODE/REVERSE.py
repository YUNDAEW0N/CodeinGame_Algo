#The game mode is REVERSE: 
#You do not have access to the statement. You have to guess what to do by observing the following set of tests:

import sys
import math
from collections import Counter
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b = int(input())
c = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


answer=[]
answer.append(a)
answer.append(b)
answer.append(c)
# 등장 횟수 세기
counter = Counter(answer)

# 가장 많이 등장하는 숫자 찾기
most_common_numbers = counter.most_common()

# 등장 횟수가 다 같은지 확인
counts = [count for _, count in most_common_numbers]
if len(set(counts)) == 1:
    print("no solution")
else:
    most_common_number = most_common_numbers[0][0]
    print(most_common_number)

stack=[]