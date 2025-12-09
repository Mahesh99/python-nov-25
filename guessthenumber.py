import random

def guess_the_number():
    r=random.randint(1,101)
    turns=0
    while True:
        u_inp=int(input("Guess the number b/w 1 and 100:"))
        turns+=1
        if r>u_inp:
            print("Number is greater")
        elif r < u_inp:
            print("Number is smaller")
        else:
            print("You guessed right!")
            print(f"You took {turns} turns to guess it right")
            break



guess_the_number()
