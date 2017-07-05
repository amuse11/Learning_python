import random

print ("Pick a side of the coin. Heads or Tails?")
input_coin = input()
input_coin = input_coin.lower()
coin = random.choice(["heads", "tails"])

if input_coin == coin:
    print ("You picked the right side!")
else:
    print ("Sadly, that is not the right side!")
