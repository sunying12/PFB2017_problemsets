#!/usr/bin/env Python3

import re

NO_file =open("No.txt", "r")
contents = NO_file.read()
#print (contents)

# find all places with Nobody present
#found = re.findall("Nobody" , contents)

#print (found)

# replace Nobody with Kiwi


Kiwi = re.sub(r"Nobody" , "Kiwi", contents)

print (Kiwi)
