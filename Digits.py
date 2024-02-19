digits = []
maxLengthList = 4
A = False

while len(digits) < maxLengthList:
    digit = int(input())
    digits.append(digit)

if digits[0] == 8 or digits[0] == 9:
    if digits[1] == digits[2]:
        if digits[3] == 8 or digits[3] == 9:
            A = True

if A == True:
    print("ignore")
else:
    print("answer")