'''This file aims to create a dictionary out of a corpus. This can later be pushed onto the Redis DB for future purposes
Python 2.7'''

import os
import redis 	#install this by typing 'sudo pip install redis' in terminal
r=redis.StrictRedis(host="localhost",port=6379,db=0) 	#setting up the database
corpus_dir =  os.path.join(os.path.dirname(__file__),'corpus')
myfile = open(os.path.join(corpus_dir,'a.txt'), "r").read().split()
dictionary = {}
current_pointer='asd'

#Filter myfile to store only words
for word in myfile:
	if not str.isalpha(word):
		myfile.remove(word)

#making 3-grams 
k=0
di={}	#dictionary to store the first second and third words in 3 gram
toCompare=[] #list to store all the 3grams
for j in range(0,len(myfile)):
	#first word
	if (j>len(myfile)-1):
		di['f']=''
	else:
		di['f']=myfile[j]
	#second word	
	if ((j+1)>(len(myfile)-1)):
		di['s']=''
	else:
		di['s']=myfile[j+1]
	#third word
	if ((j+2)>(len(myfile)-1)):
		di['t']=''
		toCompare.append(di.copy())
	else:
		di['t']=myfile[j+2]
		toCompare.append(di.copy())	#adding the dictionary of 3gram to a list

#print toCompare		#error when the code reaches EOF of corpus...if a full stop is being included at the end of the text it
					#is not considering the last word.
for element in toCompare:
	print element['f']+" "+element['s']+" "+element['t'] #can access any value of any dictionary in the list in this way 

#Main thing 

for i in  range(1,len(myfile)):
	word = myfile[i].strip().lower()
	previousword = myfile[i-1].strip().lower()

	if not previousword in dictionary:
		dictionary[previousword] = [word]

	else:
		if not word in dictionary[previousword]:	#making sure the same word is not added in the list again
			dictionary[previousword].append(word)

#print dictionary


