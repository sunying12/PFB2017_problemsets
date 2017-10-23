#!/usr/bin/env Python

from math import sqrt

file = open("pfb.fastq", "r")


linenumber=0
entrylist = []
sequence = []
qualityscore = []

sumsequence =[]
totalsequence =0
sumquality = []
totalquality =0

for line in file:
	line = line.strip()
	linenumber+=1
	if linenumber %4 ==1: 
		#print ("this is the entry name")
		entrylist.append(line)
	if linenumber %4 ==2: 
		sequence.append(line)
		sumsequence.append(len(line))
		totalsequence +=1
		#print ("this is the sequence", len(line))
	if linenumber %3 ==0: 
		print ("this is a plus sign")
	if linenumber %4 ==0:
		#print ("this is the quality score")
		qualityscore.append(line)
		sumquality.append(len(line))
		totalquality +=1
#print (entrylist)
#print (sequence)
#print (qualityscore)

print ("this is the sum of the sequences",sum(sumsequence))
print ("this is the total number of sequences",totalsequence)
#print (linenumber/4)
# calculate the mean of sequence lengths

print ("this is the mean of the sequences" , sum(sumsequence)/totalsequence)

# calculate the standard deviation of sequence lengths

list = sumsequence.copy()
mean = sum(list)/len(list)

# This is another way to do it
#for x in list:
	#sum = (x -mean)
	#print (sum)
	#differences.append(sum)
	#print (differences)
	#print (x)
differences = [x-mean for x in list]

#print (differences)
sq_difference = [d**2 for d in differences]

ssd = sum(sq_difference)

print ("the standard deviation of the sequence is",ssd)

# to calculate the mean of the quality scores

#print(qualityscore)
#print(sumquality)
#print(totalquality)

qlist = sumquality.copy()

print (qlist)

qmean = sum(qlist)/len(qlist)
qdifferences = [x -mean for x in list]
qsq_differences = [d**2 for d in qdifferences]
qssd = sum(qsq_differences)
print ("the standard deviation of the quality is", qssd)


