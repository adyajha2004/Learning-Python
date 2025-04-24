import random

# Instruction
print("Welcome to Number Guesser! \nThe computer will choose a number and if you choose the same, You WIN")
n = int(input("select the range: "))

if (n < 3): # restriction
    print("there's not a lot left to guess. is it?")

#game code
else:
    Comp_num = random.randrange(1,n)
    print("Computer succesfully selected the number...")
    Human_num = int(input("Enter the number you think the computer choose? \n"))

    if (Comp_num == Human_num):
        print("Yay!! you WON 🎉")
    else:
        print("the comuter picked:", Comp_num)
        print("but you choose:", Human_num)
        print("Better luck next time")