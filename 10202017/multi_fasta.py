#!/usr/bin/env Python3

# take from user input and calculate nucleotype composition for each sequence
# use datastructure to kep count
# Print each sequence name and it's composition in this format


import sys
import re

input = sys.argv[1]

#print (input)

file = open(input, "r")

#contents = file.read ()

#print (contents)

#seqName\tA_count\tT_count\tG_count\tC_count

dictionary = {}
Key = ""
Value = ""
NuKey = ""
NuValue = ""

for line in file: 

# set up dictionary
    i = line.rstrip()
    if i.startswith(">"):
        Key = i
               
    else:
        Value = i

# append to dictionary
    if Key in dictionary:
        dictionary[Key] += Value
    else: 
        dictionary[Key] = Value

# build a dictionary
dictionary[Key] = Value


#print (dictionary)

genes = {}

for ge in dictionary:
    genes[ge] = {'A': len(re.findall(r"A",dictionary[ge])), "T": len(re.findall(r"T",dictionary[ge])), 'C': len(re.findall(r"C",dictionary[ge])), 'G': len(re.findall(r"G",dictionary[ge])) }   










#print (len(dictionary.keys())) 

#for sequence in dictionary.values(): 
    # calculate the nucleotide composition for each sequence
 #   Apat = len(re.findall(r"A", sequence))
 #   Cpat = len(re.findall(r"C", sequence))
 #   Gpat = len(re.findall(r"G", sequence))
 #   Tpat = len(re.findall(r"T", sequence))
 #   NuKey = ['A', 'C', 'G', 'T']
 #   Nudic [NuKey] = 
