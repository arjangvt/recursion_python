"""
This function recursively returns the median of two sorted arrays

written by: Arjang Fahim
Last update: 2/17/2021

"""

def utils(i, j, arr1,arr2, merged):
	
	if i >= len(arr1):
		for k in range(j, len(arr2)):
			merged.append(arr2[k])
		return merged

	if j >= len(arr2):
		for k in range(i, len(arr1)):
			merged.append(arr1[k])
		return merged
		
	if arr1[i] <= arr2[j]:
		merged.append(arr1[i])
		i += 1
	else:
		merged.append(arr2[j])
		j += 1

	utils(i,j, arr1, arr2, merged)

	return merged




def median_sorted_array(arr1, arr2):
	merged = utils(0,0, arr1, arr2, [])
	median = 0
	arr_len = len(merged)
	rem = arr_len % 2
	if rem == 0:
		median = (merged[int((arr_len/2))-1] + merged[int((arr_len + 2)/2) -1]) / 2
	else:
		median = merged[(int((arr_len + 1)/2) -1)]

	print(merged, float(median))
    
arr1 = [1,2]
arr2 = [3,4]

median_sorted_array(arr1, arr2)
