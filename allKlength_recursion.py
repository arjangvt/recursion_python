"""
This function recursively returns all k-mers(strings with the length k)
that can be generated from a given set (all combinations).

written by: Arjang Fahim
Last update: 1/29/2021

Inputs: s: a set object
		k: an integer that holds length of strings
		k_mer: a string that is generated on each recursive call
		depth: an integer that holds the depth of recursion
"""

def find_all_k_length(s, k ,k_mer,  depth):

	if len(k_mer) == k:
		print(k_mer)
		return
	
	for char in s:
		k_mer = k_mer + char
		
		# can be used for debugging purpose
		depth = depth + 1
		find_all_k_length(s, k,  final, k_mer, depth)
		depth = depth - 1
		k_mer = k_mer[0:len(k_mer)-1]
	return 

s = set(['a', 'b'])
k = 5
k_mer = ""
depth = 0
find_all_k_length(s, k, k_mer, depth)


