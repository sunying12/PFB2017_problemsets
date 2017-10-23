#!/usr/bin/env Python3

sequence = "GGCTAGCATTTAGGCGATAGAGAATTTTNNNNNNNNNNNNNNNNN"

quality = "DDHHIIIIIIIIHII&&&&&&&&&&&"

FILE= []
qC= []
for i in sequence:
    Stt = "N"
    if i.endswith(Stt):
        K=i[:-1]
    else: 
        #FILE += i
        FILE.append(i)
#print (FILE)
#print (sequence)


for q in quality:
    if (ord(q)-33) >20:
        #print ("stuff", q)
        qC.append(q)
#print (qC)


index =0

for index in range (len(sequence)):

    if sequence[index] != "N":

        if quality[index] 

(ord(q)-33) >20: 
quality =(sequence[index])




new_sequence = sequence[:index]
new_quality = quality[:index]
