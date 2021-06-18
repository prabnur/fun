from sys import argv
from datetime import datetime
import random
import pyperclip

def distort(word):
  distorted = ""
  now = datetime.now()
  seed = (now.time().hour * 3600) + (now.time().minute * 60) + now.time().second
  random.seed(seed)
  for i in range(len(word)):
    letter = word[i]
    if random.random() < 0.5:
      distorted += letter.lower()
    else:
      distorted += letter.upper()
  return distorted

phrase = " ".join(argv[1:])
distorted = distort(phrase)
print(distorted)
pyperclip.copy(distorted)
