import random

num = random.randint(1, 11)
while True:
    user = int(input("enter your guess: "))
    if user == num:
        print("correct")
        break
    else:
        print("right")