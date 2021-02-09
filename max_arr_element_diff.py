"""
This code finds the maximum j-i
such that arr[j] > arr[i] 

written by: Arjang Fahim
Last update: 2/6/2021

"""

# Stack last-in-first out



def max_arr_diff(arr ,i ,j ,max):

    if j == len(arr):
        return max 

    if i != j:
        if max[0] < arr[j]-arr[i]:
            max[0] = arr[j]-arr[i]
            max[1] = j
            max[2] = i
    
    for i in range(j, len(arr)):
        max = max_arr_diff(arr, j , i+1 ,max)
    
    return max    
        
arr = [-2,7,6,3,1,1,28]
max=[]
max.append(0)
max.append(0)
max.append(0)
print(max_arr_diff(arr, 0,  0, max))