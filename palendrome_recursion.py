"""
This function recursively returns true if a given string is a palindrome.
Otherwise false.

written by: Arjang Fahim
Last update: 1/29/2021

Inputs: s: a string 
		l: a string denotes the last character in a string
		r: a string denotes the last character in a string
"""

def palen(s, l, r):
	if l != r:
		return False

	if s == "":
		return True

	l = s[0]
	r = s[len(s)-1]
	
	if len(s) > 2:
		s = s[1:len(s)-1]
	else:
		s = ""

	return palen(s, l, r)


s = "899"
l = s[0]
r = s[len(s)-1]

print(palen(s, l, r))

