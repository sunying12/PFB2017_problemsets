#!/usr/bin/env python3
import sys

count = int(sys.argv[1])

# if/else statement
if count > 0:
	# prints out something 
	message = "is a positive number"
	print (count , message)
	if count > 50:
	# print out
		biggermessage = "is bigger than 50"
		print (count, biggermessage)
		if count%3 == 0: 
			# print out
			divisible = "this is divisible by 3"
			print (count, divisible)
		else: 
			# print out
			notdivisible = "this is not divisible by 3" 
			print (count, notdivisible) 
	else: 
		smallermessage = "is smaller than 50"
		print (count, smallermessage)
		if count %2 == 0:
			# print out 
			evenmessage = "is an even number"
			print (count, evenmessage)
		else: 
			oddmessage = "is an odd number"
			print (count, oddmessage)
else: 
	message = "is a negative number"
	print (count, message)
