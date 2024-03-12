import random

def flip_coin():
  return random.choice(["Heads", "Tails"])

total_heads = 0
total_tails = 0
tails = 0
heads = 0

Plr1 = str(input("Player 1 Face: "))

if "heads" in Plr1.lower():
   heads = 1
if "tails" in Plr1.lower():
   tails = 1

if Plr1 == "heads":
    tails = 2
if Plr1 == "tails":
    heads = 2


for i in range(1):
  if (flip_coin() == "Heads"):
    total_heads += 1
  else:
    total_tails += 1

if total_heads == 1:
  print("Player " + str(heads) + " Won it landed heads!") 
if total_tails == 1:
    print("Player " + str(tails) + " Won it landed tails!") 

input("Press Enter to exit")