#
# decipher.py (c) Luis Hoderlein
#
# BUILT: Apr 21, 2016
#
# This program can brute force Cesarian ciphers
# It gives you all possible outputs, meaning you still have to chose the output you want
#

# imports
import string

# adds padding to make output inline
def pad(num):
	if num < 10:
		return "0"+str(num)
	else:
		return str(num)

# declare vars + ask for input
raw_txt = raw_input("Enter ciphertext: ")
raw_int = []
txt = ""
spaces = []
periods = []
excl = []

# make all lower case (necessary)
raw_txt = raw_txt.lower()

# log spaces + remove them
for i in range(0, len(raw_txt)):
	if raw_txt[i] != " ":
		txt = txt + raw_txt[i]
	else:
		spaces.append(i);

# log periods and remove them
raw_txt = txt
txt = ""
for i in range(0,len(raw_txt)):
	if raw_txt[i] != ".":
		txt = txt + raw_txt[i]
	else:
		periods.append(i);

# log exclamation marks and remove them
raw_txt = txt
txt = ""
for i in range(0,len(raw_txt)):
	if raw_txt[i] != "!":
		txt = txt + raw_txt[i]
	else:
		excl.append(i);

# turn chars into ints
for i in range(0, len(txt)):
	try:
		raw_int.append(26 + int(float(txt[i])))
	except ValueError:
		raw_int.append(string.lowercase.index(txt[i]))

# loop through every possible solution (36 of them), using i has cipher number
# and print all possible solution + add the spaces, exclamtion marks, perdiods, question marks again
# to prevent some weird bug, possible int has to be reassigned every time
for i in range(0, 36):
	possible_int = []
	for j in range(0, len(raw_int)):
		possible_int.append(raw_int[j])
	possible_txt = ''
	for j in range(0, len(possible_int)):
		possible_int[j] = possible_int[j]+i
		if possible_int[j] >= 36:
			possible_int[j] = possible_int[j] - 36
		if possible_int[j] < 26:
			possible_txt = possible_txt + string.lowercase[possible_int[j]]
		else:
			possible_txt = possible_txt + str((possible_int[j] - 26))
	del possible_int
	for j in range(0, len(spaces)):
		possible_txt = possible_txt[:spaces[j]] + " " +possible_txt[spaces[j]:]
	for j in range(0, len(periods)):
		possible_txt = possible_txt[:periods[j]] + "." +possible_txt[periods[j]:]
	for j in range(0, len(excl)):
		possible_txt = possible_txt[:excl[j]] + "!" +possible_txt[excl[j]:]	
	print "Solution "+pad(i)+" is: "+possible_txt
