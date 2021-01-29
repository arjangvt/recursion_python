"""
This function recursively computes the factorial of an integer

written by: Arjang Fahim
Last update: 1/29/2021

Input: n: an integer value
		
"""



def fact(n):
	if n == 1 or n == 0:
		return 1

	result = n * fact(n-1)
	return result

n = 3
print(fact(n))

