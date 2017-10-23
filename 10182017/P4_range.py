#!/usr/bin/env Python3

#for i in range(0,100):
 #   print (i)


#for i in range (0,101):
 #   print (i)

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

for i in range (start,end):
    if i%2 != 0:
        print (i)
