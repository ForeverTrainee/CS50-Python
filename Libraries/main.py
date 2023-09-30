#import random
#If we import whole library like #import random, we use random.randint(...)
# or random.choice(["Heads","Tails"])
from random import choice
from random import randint
from random import shuffle
import statistics
import sys
import cowsay
import requests
import json
#If we use from random impot choice/randint we use just randint/choice without random.



number = randint(1,100)
coin= choice(["Heads","Tails"])
cards = ["Ace","King","Queen","Jack"]
shuffle(cards)
#print(number)
#print(coin)
#for card in cards:
    #print(card)


print(statistics.mean([1,2,3]))


if len(sys.argv) < 1:
    sys.exit("Too few arguemnts")
elif len(sys.argv) > 1:
    sys.exit("Too many arguments")

cowsay.kitty("Hello World") #installed via pip, imported cowsay library

response = requests.get("https://ipapi.co/json/")
output = response.json()
print(json.dumps(response.json()))
for result in output:
    print(f"{result} : {output[result]}")