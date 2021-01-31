"""
This function recursively returns all possible combinations of r elements in
a given array size n
Note that the elements are not allowed to be repeated

written by: Arjang Fahim
Last update: 1/29/2021

Inputs: arr: input array of integers
		s_index: starting index of the array
		r: the length of the combinations
		arr_temp: a temptorary array of integers to hold the results
		depth: an integer variable can be used for watching the depth of the recursion
"""

def all_combination(arr, s_idx, r, arr_temp, depth):

	if (len(arr_temp) == r):
		print(arr_temp)
		return
		
	for j in range(s_idx, len(arr)):
		arr_temp.append(arr[j])
		s_idx = s_idx+1
		all_combination(arr, s_idx, r, arr_temp, 0)
		
		arr_temp.pop()
	return 

arr = [1, 2, 3, 4, 5]
r = 2
s_idx = 0

arr_temp = []

depth = 0
all_combination(arr, s_idx, r, arr_temp, depth)


