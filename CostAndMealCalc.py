product = float(input())
taxNum = int(input())
taxPercent = float(1 + taxNum / 100)

totalCost = product * taxPercent
print(totalCost)