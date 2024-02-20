import math

num = int(input())
max = int(math.sqrt(num))
temp = max
sum = 1

for temp in range(max, 1, -1):
    if num % temp == 0:
        sum += temp
        sum += num / temp

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
