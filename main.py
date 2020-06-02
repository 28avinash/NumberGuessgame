import random

def Clue(number):
    if(number%2==0):
        return "Let's have a clue Number is Even"
    else:
        return "Let's have a clue Number is Odd "

def Score(chances):
    if(chances==2):
        return "Your Score is 30"
    elif(chances==1):
        return "Your Score is 20"
    else:
        return "Your Score is 10"


def Game():
    computer_guess = random.randint(1, 10)
    chances = 3
    guess="Wrong"
    print("\nLets Play Number Guess And See Who is Genius")
    print("You or Computer")
    Name = input("Enter Your Name:")
    print("Computer Has Guessed the number \n Now Your Turn")
    while(chances>0):

        chances = chances - 1
        user_guess = int(input("\nEnter your guess Number Between 1 to 10 : "))

        if (user_guess == computer_guess):
            print("\nCongratulation {}, You are Genius !!".format(Name))
            break
        elif (user_guess > computer_guess):
            if (chances == 0):
                print("\nYour Are Out Of Chances , Sorry You Loss !! Computer Guessed {}".format(computer_guess))
            else:
                print(
                    "\nYour Guess Larger Than Computer Guess \n Let's Try Again \n{} Chances Remaining.. ".format(chances))
        else:
            if (chances == 0):
                print("\nYour Are Out Of Chances , Sorry You Loss !! Computer Guessed {}".format(computer_guess))
            else:
                print("\nYour Guess Smaller Than Computer Guess \n Let's Try Again \n{} Chances Remaining.. ".format(chances))
        if(chances==2):
            print(Clue(computer_guess))
    print(Score(chances))

def main():
    Game()
    while True:
        another_game = input("\nDo you wish to play again?(Yes/No): ")
        if another_game == "Yes":
            Game()
        else:
            break
main()