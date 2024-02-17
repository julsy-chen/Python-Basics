winCounter = 0
game = 0

while game < 6:
    currentGame = input()
    if currentGame == "W":
        winCounter += 1
    game += 1
#end of while loop
    
if winCounter > 4: 
    print("1")
elif winCounter > 2:
    print("2")
elif winCounter > 0:
    print("3")
else:
    print("-1")