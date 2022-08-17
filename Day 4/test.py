# Rock Paper Sciccors 
# Rock 1
# Paper 2
# Sciccors 3 
# Rock beats Sciccors, sciscors beat paper, paper beats rock

# 1 vs 3 = 1, 3 vs 2 = 3, 1 vs 2 = 2
# 3! = 3*2*1
import random

ask_rps = int(input("Rock Paper Sciscors or Choose between 1 2 3?"))

program_choice = random.randint(1,3)

while (ask_rps == program_choice):
  print("I choose "+str(program_choice))
  print("It's draw, pick again!")
  ask_rps = int(input("Rock Paper Sciscors or Choose between 1 2 3?"))
  program_choice = random.randint(1,3)

if (ask_rps + program_choice == 4):
  if (ask_rps == 1):
    print("You pick rock you win")
  else:
    print("I pick Rock, I win")

if (ask_rps + program_choice == 5):
  if (ask_rps == 3):
    print("You pick Sciccors you win")
  else:
    print("I pick Sciccors, I win")

if (ask_rps + program_choice == 3):
  if (ask_rps == 2):
    print("You pick Paper you win")
  else:
    print("I pick Paper, I win")