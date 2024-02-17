import math

num = int(input())
ans = 0

max = math.sqrt(num)

if max ** 2 == num:
    print(int(max))
else:
    max = int(max)
    for temp in range(1, max+1):
        if temp ** 2 < num:
            ans = temp
    print(f"The largest square has side length {ans}.")