# Rolling a Dice against a DC

from random import randrange

dice_roll = randrange(1,21)
print(f"You roller {dice_roll}.")

difficulty = int(input("Set a difficulty: "))

if dice_roll >= difficulty:
    print("You were successful.")
else:
    print("You failed.")