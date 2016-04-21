#
# decipher.py (c) Luis Hoderlein
# 
# BUILT: Apr 21, 2016
#
# This program can brute force Cesarian ciphers
# It gives you all possible outputs, meaning you still have to chose the output you want
#

import string

def pad(num):
	if num < 10:
		return "0"+str(num)
	else:
		return str(num)

raw_txt = raw_input("Enter ciphertext: ")
raw_int = []
txt = ""
spaces = []

raw_txt = raw_txt.lower()

for i in range(0, len(raw_txt)):
	if raw_txt[i] != " ":
		txt = txt + raw_txt[i]
	else:
		spaces.append(i);

for i in range(0, len(txt)):	
	raw_int.append(string.lowercase.index(txt[i]))

for i in range(0, 26):
	possible_int = []
	for j in range(0, len(raw_int)):
		possible_int.append(raw_int[j])
	possible_txt = ""
	for j in range(0, len(possible_int)):
		possible_int[j] = possible_int[j]+i
		if possible_int[j] >= 26:
			possible_int[j] = possible_int[j] - 26
		possible_txt = possible_txt + string.lowercase[possible_int[j]]
	del possible_int
	for j in range(0, len(spaces)):
		possible_txt = possible_txt[:spaces[j]] + " " +possible_txt[spaces[j]:]	
	print "Solution "+pad(i)+" is "+possible_txt
