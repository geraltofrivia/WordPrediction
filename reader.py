'''This file aims to create a dictionary out of a corpus. This can later be pushed onto the Redis DB for future purposes
Python 2.7'''

import os
import sys
import redis 	#install this by typing 'sudo pip install redis' in terminal

r=redis.StrictRedis(host="localhost",port=6379,db=0) 	#setting up the database

corpus_dir =  os.path.join(os.path.dirname(__file__),'corpus')
corpus_files = os.listdir(corpus_dir)
dictionary = {}

def search(dicta, word):
	#Tuple is of the form value, occurance
	present = False
	for item in dicta:
		if item[0] == word:
			present = True

	return present

def increment_count(list,word):
	newlist = []
	for item in list:
		if not item[0] == word:
			newlist.append(item)
		else:
			newlist.append((item[0], item[1] + 1))
	return newlist



def read_file(file_name):
	global dictionary
	myfile = open(os.path.join(corpus_dir,file_name), "r").read().split()
	#print "*********************%s******************" % file_name
	#Filter myfile to store only words
	
	for word in myfile[:]:
		if not str.isalpha(word):
			myfile.remove(word)

	if len(myfile) < 2:
		print "Error: File too short. Exiting."
		return

	for i in  range(2,len(myfile)):
		word3 = myfile[i].strip().lower()
		word2 = myfile[i-1].strip().lower()
		word1 = myfile[i-2].strip().lower()

		if not word1 in dictionary:
			dictionary_level2 = {word2:[(word3,1)]}
			dictionary[word1] = dictionary_level2
			continue

		else:
			dictionary_level2 = dictionary[word1]
			if not word2 in dictionary_level2 :
				dictionary_level2[word2] = [(word3,1)]
				continue

			else:
				if search(dictionary_level2[word2],word3):
					newlist = increment_count(dictionary_level2[word2],(word3))
					dictionary_level2[word2] = newlist
					continue
				else:
					dictionary_level2[word2].append((word3,1))
					continue

	
for file_name in corpus_files:
	read_file(file_name)

#for key in dictionary:
#	print key, ':', dictionary[key], '\n'
print len(dictionary)
hkey = "redis_dictionary"
r.hmset('hi',dictionary)

print dictionary['the']['man']
#hget(name, key)
#hset(name, key, value)