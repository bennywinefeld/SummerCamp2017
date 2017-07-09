from random import choice
play = "y"
while (play == "y"):
    your_choice = input("Please select rock, paper, or scissors: ").lower()
    comp_choice = choice(["rock", "paper", "scissors"])
    print("The computer has selected " + comp_choice)
    if (your_choice[0]+comp_choice[0] in ["rr","pp","ss"]):
        print("It's a tie")
    elif (your_choice[0]+comp_choice[0] in ["rs","sp","pr"]):
        print("Congrats, you win!")
    else:
        print("Sorry, you lose!")
    play = input("Would you like to continue playing? yes/no ").lower()[0]
print("Ok, goodbye")