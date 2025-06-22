# Snake Water Gun Game

import random

print('''
Welcome to Snake Water Gun Game!!

RULES:
    - Snake (s) drinks Water → Snake wins
    - Water (w) damages Gun → Water wins
    - Gun (g) kills Snake → Gun wins
    - Same choices → It's a draw
      
OPTIONS:
    - Snake  → Press 's'
    - Water  → Press 'w'
    - Gun    → Press 'g'

Let the battle begin!
''')

userDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

user = input("Enter your choice (s/w/g): ").lower()

if user not in userDict:
    print("Invalid choice. Please enter 's', 'w', or 'g'.")
else:
    choice = userDict[user]
    computer = random.choice(list(userDict.values()))

    print(f"You chose: {reverseDict[choice]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Alternate for switch case in python is match-case
    match(choice, computer):
        case (1, -1) | (-1, 0) | (0, 1):
            print("You Win")
        case (-1, 1) | (0, -1) | (1, 0):
            print("Computer Wins")
        case _ if choice == computer:
            print("Its a Draw")