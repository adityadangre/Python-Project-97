import random

randomnumber = random.randint(1, 9)
chance = 5
hintCount = 3
name = input("Enter your Name: ")

print(f"Hello {name}!!! Welcome you to the Guessing Number Game.")
print(
    """Rules for the game:
    1. You will get 5 chances for correct guess.
    2. If your guess is right then you will win the game.
    3. If you get all the 5 guess as wrong, you will lose the Game.
    4. For a wrong guess, you can get a hint.
    5. There will be only 3 hints for help.
    6. If you want the hint, press on Y or if you don't want, press on N."""
)

while chance > 0: 
    guess = int(input("Enter your guess: "))

    if(randomnumber != guess):
        chance = chance - 1

        if(chance > 0):
            print("Try Again!!!")

            if(hintCount>0):
                hint = input("If you want hint, press Y else, press N: ")

                if(hint.upper()=='Y'):
                    hintCount=hintCount-1

                    if(guess>randomnumber):
                        print("Hint : Enter some small number than that of your guessed number.")

                    else:
                        print("Hint : Enter some large number than that of your guessed number.")

    elif(randomnumber == guess):
        chance = 0
        print('Congratulations!!! Your guess is correct...')
    
if(chance == 0):
    if(randomnumber != guess):
        print(f"Oops!!! The correct number was {randomnumber}. Good luck next time...")
