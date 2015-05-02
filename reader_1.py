'''This file aims to create a dictionary out of a corpus. This can later be pushed onto the Redis DB for future purposes
Python 2.7'''

import os
import redis 	#install this by typing 'sudo pip install redis' in terminal
r=redis.StrictRedis(host="localhost",port=6379,db=0) 	#setting up the database
corpus_dir =  os.path.join(os.path.dirname(__file__),'corpus')
myfile = open(os.path.join(corpus_dir,'a.txt'), "r").read().split()
dictionary = {}

#Filter myfile to store only words
for word in myfile:
	if not str.isalpha(word):
		myfile.remove(word)


#Main thing 
k=0
for i in  range(1,len(myfile)):
	word = myfile[i].strip().lower()
	previousword = myfile[i-1].strip().lower()

	if not previousword in dictionary:
		dictionary[previousword] = [word]
		r.set(previousword,'')	#added to the database with empty key
		print 'added to redis is the word '+r.get(previousword)

	else:
		dictionary[previousword].append(word)
		r.set(previousword,word)	#added values to the same key, if exists
		print 'appended to redis is the word '+r.get(previousword) #just to check

print dictionary


