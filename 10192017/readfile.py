#!/usr/bin/env Python3

# open and read content

Dream_file = open("Python_05.txt", "r")
Dream_contents = Dream_file.read()



# Upper case each line
Upper_contents = Dream_contents.upper()


# print each line to STDOUT
#print (Upper_contents)

# write contents to a new file called "Python_05_uc.txt"

writing_file = open("Python_05_uc.txt" , "w")
writing_file.write(str(Upper_contents) + "\n")
writing_file.close()
print ("Write to file Python_05_uc.txt")
