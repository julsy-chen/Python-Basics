input1 = input()
input2 = input()

if input1 == input2:
    print("Tie Game.")
elif input1 == "Rock":
    if input2 == "Scissors":
        print("Player 1 Wins.")
    else:
        print("Player 2 Wins.")
elif input1 == "Scissors":
    if input2 == "Paper":
        print("Player 1 Wins.")
    else: 
        print("Player 2 Wins.")
else:
    if input2 == "Rock":
        print("Player 1 Wins.")
    else:
        print("Player 2 Wins.")
