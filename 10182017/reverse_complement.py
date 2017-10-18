#!/usr/bin/env Python3

# Test sequence

Sequence = 'ATGCAGGGGAAACATGATTCAGGAC'  
# Complement = 'TACGTCCCCTTTGTACTAAGTCCTG'  
# Reverse Complement ='GTCCTGAATCATGTTTCCCCTGCAT'


# complement the original sequence
# replace all the letters to lowercase letters
# make everything uppercase again
complement = sequence.replace ('A', 't').replace ('T', 'a').replace ('C', 'g').replace ('G', 'c').upper()
 
# get the reverse complement
reverse = complement[::-1]
