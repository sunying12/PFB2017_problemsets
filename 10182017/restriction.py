#!/usr/bin/env Python3

dna="GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

# Figure out how many of them there are
fecori= dna.count('GAATTC')

# find the start position of a  EcoR1 site GAATTC
# use locate and report
start= dna.find('GAATTC')
# find found it at 395
first_fragment = dna[0:396]
second_fragment = dna[396:]

# the python number is 395 so the actual location starts at the 396 position
first_position = "0:396"
second_position = "396:842"


first_length =len(first_fragment)
second_length =len(second_fragment)

# Find the location of this site (first and last nucleotides)
# extract the restriction fragments- print each fragment along with its position in the whole DNA sequence and its length
# use string formatting to format your print statement

# Fragment\tPosition\tlength
#GAATTC\t395\t6
string1 = " First fragment:{}\tPosition:{}\tlength:{}"
string2 = " Second fragment:{}\tPosition:{}\tlength:{}"
firststring = string1.format(first_fragment, first_position, first_length)
secondstring = string2.format(second_fragment, second_position, second_length)
print (firststring)
print (secondstring)

