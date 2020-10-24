#! /usr/bin/python
import sys
import random
filenum=sys.argv[1]
termnum=sys.argv[2]
def generateTime(index,num):
	filename=""
	if index<10:
		filename="Term-0"+str(index)
	else:
		filename="Term-"+str(index)
	f=open(filename,"w")
	for i in range(num):
		f.write(str(random.randint(0,10000))+'\n')
	f.close()

for i in range(1,int(filenum)+1):
	generateTime(i,int(termnum))