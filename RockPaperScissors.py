import random

print("-----------Welcome to Rock Paper Scissors--------")

User_score = 0
Computer_score = 0
ties = 0

name = input("Enter Your name here: ")
print("""
Winning Rules:
1. Paper vs Rock --> Paper
2. Rock vs Scissors --> Rock
3. Scissors vs Paper --> Scissors""")
print()
print("""Choice are:
      1. Rock
      2. Paper
      3. Scissors""")

while True:
    choice =int(input("Enter your choice from 1-3: "))

    print()
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        User_choice = "Rock"
    elif choice == 2:
        User_choice ="Paper"
    else:
        User_choice = "Scissors"

    print("The User's choice is", User_choice)
    print("Now it is Computer's turn")

    computer = random.randint(1,3)

    if computer == 1:
        computer_choice = "Rock"
    elif computer == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissores"

    print("The Computer's choice is ",computer_choice)

    if ((User_choice == "Paper" and computer_choice == "Rock") or(User_choice == "Rock" and computer_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif ((User_choice == "Scissors" and computer_choice == "Rock") or(User_choice == "Rock" and computer_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"
    elif (User_choice == computer_choice):
        print("It is a tie")
        result = "Tie" 
    else: 
        print("Scissors wins")
        result = "Scissors"

    if result == "Tie":
        ties += 1
    elif result == User_choice:
        print("User wins")
        User_score += 1
    else:
        print("Computer wins")
        Computer_score += 1

    print("Scores are")
    print(name,"'s score is",User_score)
    print("Computer's score is",Computer_score)
    print("ties are",ties)

    repeat = input("Do you want to play again? ")
    if repeat == "No" or repeat == "No":
        break 
print("Game Over!")
print('Thanks for Game!') 