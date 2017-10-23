#!/usr/bin/env Python3

FastQ = open("Python_05.fasta", "r")
#print (contents)

# count the number of lines and the number of characters per line


# total number of lines
count =0
character =0
sum_lines = []
for i, line in enumerate(FastQ):
    line = line.rstrip()
    count +=1
    lenline = len(line)
    sum_lines.append(lenline)
    print ("this is", i , "and length", lenline)
    for a in line:
        character +=1
        

   

# total number of characters




print ( "this is the total number of lines", count)
print ( "this is the total number of characters", character)
print ( "The average line length is", sum(sum_lines)/count)
