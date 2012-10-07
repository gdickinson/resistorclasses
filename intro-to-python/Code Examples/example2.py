#!/usr/bin/python
"""Guess a secret"""

secret = "cheddar"

print("What sort of cheese am I thinking of?")
guess = raw_input()

if (guess == secret):
  print("%s is right!" % secret)
else:
  print("Nope, I wasn't thinking of %s" % guess)

print("Thanks for playing")