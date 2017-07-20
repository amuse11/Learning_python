import random

while True:
    print("Pick a side of the coin. Heads or Tails? Type 'End' when you wish to stop.")
    input_coin = input()
    input_coin = input_coin.lower()
    coin = random.choice(["heads", "tails"])
    if input_coin == coin:
        print ("The side is " + (coin))
        print ("You picked the right side!")
        continue
    elif input_coin != coin and input_coin != "end":
        print ("The side is " + (coin))
        print ("Sadly, that is not the right side!")
        continue
    elif input_coin == "end":
        print ("The program has ended")
        break
