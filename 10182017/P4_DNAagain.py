#!/usr/bin/env Python3

list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for a,i in enumerate(list):
    leng = len(i)
    string = "{}\t{}\t{}\n"
    # 1, 4, sequence
    new_string = string.format(a,leng,i)
    print (new_string)






# tuple list
#fancy_length = [(len(i),i) for i in list]
