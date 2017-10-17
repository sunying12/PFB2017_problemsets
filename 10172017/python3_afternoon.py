#!/usr/bin/env python3
import sys

count = int(sys.argv[1])

# if/else statement
if count <= 30:
	# prints out a confirmation of truthe if the value is true 
	message = "is less than or equal to 30"
	print (count , message)
elif count == 30: 
	# prints out "Not TRUE" if the value is not true
	message = "Not True"
	print (count , message)
else: 
	# prints out "NOT TRUE" if the value is not true
	message = "Not True"
	print (count, message)



