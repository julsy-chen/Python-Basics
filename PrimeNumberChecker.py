import math
 
num = int(input())
max = int(math.sqrt(num))
bool = False
temp = 1

for temp in range(2, max+1):
    if num % temp == 0:
        bool = True

if bool == True:
    print("Not Prime")
else:
    print("Prime")