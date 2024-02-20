input = int(input())
answer = 0
maxFactor = 0

for num in range(1, input + 1):
    totalFactor = 0
    
    for divider in range(1, num + 1):
        if num % divider == 0:
            totalFactor += 1

    if totalFactor > maxFactor:
        maxFactor = totalFactor
        answer = num

print(answer)