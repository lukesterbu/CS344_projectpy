#!/usr/bin/env python3

import random

# Returns a list of 10 random letters
def randomString():
	i = 0
	word = []
	while i < 10:
		letters = "abcdefghijklmnopqrstuvwxyz"
		word.append(random.choice(letters))
		i = i + 1
	return word
# EOFunction

# Creates a file called fileName. Calls 
# randomString() and writes the 
# returned value to the file specified by
# fileName. Then prints the first line of
# the file to the console.
def writeToFile(fileName):
	with open(fileName, "w+") as f:
		f.write(''.join(randomString()) + '\n')
	f.close()
	with open(fileName) as f:
		print(f.readline(), end = "")
	f.close()
# EOFunction

# Prints out 2 random numbers and their
# product.
def getNumbers():
	a = random.randint(1, 42)
	b = random.randint(1, 42)
	c = a * b
	print(a)
	print(b)
	print(c)
# EOFunction

writeToFile("charmander")
writeToFile("squirtle")
writeToFile("bulbasaur")

getNumbers()
