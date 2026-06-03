import random


options = ["rock", "paper", "scissors"]

user_choice = input("Choose Rock, Paper or Scissors: ").lower()

computer_choice = random.choice(options)

print("\nYour Choice:", user_choice)
print("Computer Choice:", computer_choice)

if user_choice == computer_choice:
    print("\nResult : Match Draw!")

elif user_choice == "rock" and computer_choice == "scissors":
    print("\nResult : You Win!")

elif user_choice == "paper" and computer_choice == "rock":
    print("\nResult : You Win!")

elif user_choice == "scissors" and computer_choice == "paper":
    print("\nResult : You Win!")

elif user_choice not in options:
    print("\nInvalid Choice!")

else:
    print("\nResult : Computer Wins!")
