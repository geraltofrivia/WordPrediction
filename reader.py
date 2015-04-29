'''This file aims to create a dictionary out of a corpus. This can later be pushed onto the Redis DB for future purposes
Python 2.7'''

import os


corpus_dir =  os.path.join(os.path.dirname(__file__),'corpus')
myfile = open(os.path.join(corpus_dir,'a.txt'), "r")

for word in  myfile.read().split():
	if str.isalpha(word.strip()):
		print word

		