#!/usr/bin/env python3

# get an integer and intiate variables
n = int(input("Enter an integer: "))
b = []

# find binary value using while loop
while(n>0):
	d=n%2
	b.append(d)
	n=n//2
b.reverse()

# output the result
print("Binary Equivalent is: ")
for i in b:
	print(i,end="")
	break
