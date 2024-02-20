loop = True
sum = 0
counter = 0

while loop:
    userInput = input()

    # use EXIT to exit program
    if userInput.lower() == "exit":
        loop = False
        break
    else:
        num = int(userInput)
        if 0 <= num <= 100:
            sum += num
            counter += 1

avg = sum / counter
print(avg)