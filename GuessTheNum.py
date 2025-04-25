import random
import time

# Instruction
print("Welcome to Number Guesser!")
time.sleep(0.5)
print("The computer will choose a number and if you choose the same, You WIN")
time.sleep(2)

# Game start
print("Let's begin...")
n = int(input("select the range: "))

if (n < 3): # restriction
    time.sleep(2)
    print("there's not a lot left to guess. is it?")

#game code
else:
    Comp_num = random.randrange(1,n)
    time.sleep(2)
    print("Computer succesfully selected the number...")
    Human_num = int(input("Enter the number you think the computer choose? "))

    if (Comp_num == Human_num):
        time.sleep(2)
        print("Yay!! you WON 🎉")
    else:
        print("you choose:", Human_num)
        time.sleep(1)
        print("But comuter picked:", Comp_num)
        time.sleep(1)
        print("Better luck next time")