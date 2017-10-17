#!/usr/bin/env python3
import sys

count = sys.argv[1]

# if/else statement
if bool(count) == True:
	# prints out a confirmation of truth if the value is true 
	message = "Great job, it is indeed true"
	print (count , message)
elif bool(count) != True: 
	# prints out "Not TRUE" if the value is not true
	message = "Not True, try again"
	print (count , message)
else: 
	# something else
	message = "Error?"
	print (count, message)



