import random
"""puseudo code: 1.Create a random number 
2. input a number3 using while loop to check the number is equal or not equal for sixtimes,"""
def guess_game():
    """
    We will create a "Guess the Number" game via Pair Programming
Game rules:
The computer will think of a random number from 1 to 50, and ask you to guess it.
After each guess, the computer will tell you whether your guess is too high or too low.
You have only 6 tries to guess the number correctly."""

    a=random.randint(1,50)
    print ("Welcome to the Game: Guess the number")
    Game_rules="The computer will think of a random number from 1 to 50, and ask you to guess it.After each guess, the computer will tell you whether your guess is too high or too low.You have only 6 tries to guess the number correctly."
    print(f"{Game_rules}")
    b=int(input("please enter a numb from 1 to 50"))
    iteration=0
    while iteration<6:
        if a==b:
            print("GOOD JOB! YOU Are Right")
            break
        elif a<b:
            print("your guess is too high")     
        elif a>b:
            print("your guess is too low")
        b=int(input("please enter another number"))
        iteration=iteration+1
    if iteration==6:
        print(f"Unfortunately your guesses are all wrong the random number is:{a:f}")
        print("please try again later")

guess_game()
