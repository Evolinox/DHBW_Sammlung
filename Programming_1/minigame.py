# https://realpython.com/python-rock-paper-scissors/

import random

user_action = input("Enter a choice (rock, paper, scissor)")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if (user_action == computer_action):
    print(f"It's a tie! Both chose {user_action}!")
elif (user_action == "rock") and (computer_action == "paper"):
    print(f"Computer has won")