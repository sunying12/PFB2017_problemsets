#!/usr/bin/env Python3


fastQ = open("Python_05.wrapped.fasta", "r")


#dictionary = {}

#fastread = fastQ.read()
#faststrip = fastread.split()

#print (faststrip)
#geneID = None
#geneseq = None

#for i,str in enumerate(faststrip):

    #if i%2 == 0: 
    #    geneID = str
   # else: 
  #      geneseq = str

 #   dictionary[geneID] = geneseq


#print (dictionary)

dictionary =  {}

gene_ID = ""
genes_seq = ""


for line in fastQ:
    if line.startswith (">"): 
        genes_ID = line.rstrip().lstrip(">")

    else: 
        genes_seq = line.rstrip()


# If the statement is true then a key value pair is already in my dictionary otherwise there's no key by that name in the dictionary so we must create the key value pair
    if genes_ID in dictionary: 
        dictionary [genes_ID] += genes_seq
    else:
        dictionary [genes_ID] = genes_seq
    
print (dictionary)


if key in Dict:
    Dict[key] += value
else:
    # create the key-value pair in the Dict:
    Dict[key] = value






