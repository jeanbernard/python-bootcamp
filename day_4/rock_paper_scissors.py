rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import sys

options = [rock, paper, scissors]
p1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
cpu =  random.randint(0, 2)

if p1 > 2:
    print("You typed an invalid number, you lose!")
    sys.exit(0)

p1_opt = options[p1]
cpu_opt = options[cpu]

print(f"Player chose: {p1_opt}")
print(f"Computer chose: {cpu_opt}")

draw = p1_opt == cpu_opt
if draw:
    print("Tie!")
else:
    if p1_opt == rock and cpu_opt == scissors:
        print("You win!")
    elif p1_opt == scissors and cpu_opt == paper:
        print("You win!")
    elif p1_opt == paper and cpu_opt == rock:
        print("You win!")
    else:
        print("You lose!")
