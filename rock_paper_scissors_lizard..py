import random
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

options = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}

player_options = int(input("Enter a number between 1 and 5: "))
if player_options not in options: # use not in instead of !=
    print("Invalid! Choose again!")

computer_options = random.randint(1,5)

print(f"You chose: {options[player_options]}")
print(f"CPU chose: {options[player_options]}")

if player_options == computer_options:
  print("Its a tie")
elif (player_options == 1 and computer_options == 3) or \
       (player_options == 2 and computer_options == 1) or \
       (player_options == 3 and computer_options == 2) or \
       (player_options == 4 and computer_options == 1):
   print("The player won!")
else:
   print("The computer won!")