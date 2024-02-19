import math

num = int(input())
max = int(math.sqrt(num))
temp = 1;

for temp in range(1, max+1):
    if num % temp == 0:
        print(int(temp))
        print(int(num / temp))