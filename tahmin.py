import random
import time 

print("Number Guessing Game  /n Make a guess between 1 and 40 ")
guess_right = 7
random_number = random.randint(1,40)

while True:
    guess =  int(input("your guess:"))

    if (guess == random_number):
        print("questioning the number...")
        time.sleep(1)
        print("Congrats!")
        print("Number",random_number)
        break
    elif(guess < random_number):
        print("questioning the number...")
        time.sleep(1)
        guess_right -= 1
        print("please give a higher number.")
        print("guess_right:",guess_right)
    else:
        print("questioning the number...")
        time.sleep(1)
        guess_right -= 1
        print("please give a lower number.")
        print("guess_right:",guess_right)
    if (guess_right == 0 ):
        print("your guess is over. sorry.")
        print("Our number:",random_number)
        break
