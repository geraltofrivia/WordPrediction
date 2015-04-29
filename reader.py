'''This file aims to create a dictionary out of a corpus. This can later be pushed onto the Redis DB for future purposes
Python 2.7'''

import os

corpus_dir =  os.path.join(os.path.dirname(__file__),'corpus')
myfile = open(os.path.join(corpus_dir,'a.txt'), "r").read().split()
dictionary = {}

#Filter myfile to store only words
for word in myfile:
	if not str.isalpha(word):
		myfile.remove(word)


#Main thing
for i in  range(1,len(myfile)):
	word = myfile[i].strip().lower()
	previousword = myfile[i-1].strip().lower()

	if not previousword in dictionary:
		dictionary[previousword] = [word]
	else:
		dictionary[previousword].append(word)

print dictionary


