num = int(input())
prevTerm = 0
temp = 0
sum = 1

for num in range(1, num):
    temp = sum
    sum += prevTerm
    prevTerm = temp

print(sum)