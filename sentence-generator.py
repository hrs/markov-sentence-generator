#!/usr/bin/python

import re
import random
import sys

mapping = {}
tempM = {}
starts = []
markovLength = 1

def fixCaps (word):
    if word.isupper () and word != "I":
        word = word.lower ()
    elif word [0].isupper ():
        word = word.lower().capitalize ()
    else:
        word = word.lower()
    return word

def toHash (lst):
    return tuple (lst)

def wordlist (filename):
    f = open (filename, 'r')
    lines = f.readlines ()
    wordlist = []
    for line in lines:
        wordlist.extend ([fixCaps (w) for w in re.findall (r"[\w']+|[.,!?;]", line)])
    return wordlist

def addItemToTempM (history, word):
	global tempM
	while len (history) > 0:
		first = toHash (history)
		if first in tempM:
			if word in tempM [first]:
				tempM [first][word] += 1.0
			else:
				tempM [first][word] = 1.0
		else:
			tempM [first] = {}
			tempM [first][word] = 1.0
		history = history [1:]

def buildMapping (wordlist):
	global tempM
	global markovLength
	starts.append (wordlist [0])
	for i in range (1, len (wordlist) - 1):
		if i <= markovLength:
			history = wordlist [: i + 1]
		else:
			history = wordlist [i - markovLength + 1 : i + 1]
		follow = wordlist [i + 1]
		# if the last elt was a period, add the next word to the start list
		if history [len (history) - 1] == "." and (follow not in ".,!?;"):
			starts.append (follow)
		addItemToTempM (history, follow)
	# Normalize the values in tempM, put them into mapping
	for first, followset in tempM.iteritems ():
		total = sum ([i for i in followset.values ()])
		mapping [first] = dict ([(k, v / total) for k, v in followset.iteritems ()])

def next (prevList):
	sum = 0.0
	retval = ""
	index = random.random ()
	while (toHash (prevList) not in mapping):
		prevList.pop (0)
	for k, v in mapping [toHash (prevList)].iteritems ():
		sum += v
		if (sum >= index and retval == ""):
			retval = k
	return retval

def genSentence ():
	global markovLength
	curr = random.choice (starts)
	sent = curr.capitalize ()
	prevList = [curr]
	while (curr not in "."):
		curr = next (prevList)
		prevList.append (curr)
		if len (prevList) > markovLength:
			prevList.pop (0)
		if (curr not in ".,!?;"):
			sent += " "
		sent += curr
#		if (curr in ";!?"):
#		sent += "\n"
	return sent

def main ():
	if len (sys.argv) < 2:
		sys.stderr.write ('Usage: sys.argv [0] text_source [chain_length=1]\n')
		sys.exit (1)
	filename = sys.argv [1]
	global markovLength
	if len (sys.argv) == 3:
		markovLength = int (sys.argv [2])
	buildMapping (wordlist (filename))
	print genSentence ()

if __name__ == "__main__":
	main()
