#!/usr/bin/env Python3

import re


fasta_file = open("Python_06.fasta", "r")
contents = fasta_file.read()
#print (contents)


# Using pattern matching, find all the header lines
#found = re.findall (r">.*", contents)

group1 = [""]
group2 = [""]

for i in fasta_file:
    
    print (i)
    #if line.startswith(">"):
     #   print (line)
      #  found = re.search (r"(\w*\|\w*\|\w*\|.*\|\w*) (.*)", line)        
       # group1 = found.group(1)
        #group2 = found.group(2)

        #print (group1)
        #print (group2)


#print  ("group1", group1, "group2", group2)
 
        
