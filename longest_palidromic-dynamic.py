"""
This code finds the longest palindromic substring, using dynamic programming
The complxity of the algorithm O(n^2) and space complexity is O(n^2)\

written by: Arjang Fahim
Last update: 3/16/2021

"""

def longest_palindromic(s):

    start = 0
    n = len(s)
            
    max_length = 1

    table = [[0 for x in range(n)] for y in range(n)]

    # set the diagonal to true
    for i in range(n):
        table[i][i] = 1

    # palidromes with the size of 2    
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = 1
            start = i
            max_length = 2

    k = 3
    for k in range(k, n+1):
        for i in range(n-k+1):

            # The upper index of a sub string with the length k starting from i
            j = i + k - 1

            if table[i+1][j-1] == 1 and s[i] == s[j]:
                table[i][j] = 1

                if k > max_length:
                    #print("inside", i, k)
                    start = i
                    max_length = k
    
    
    
    return s[start: start+ max_length]

s = "cbbd"
longest_pal = longest_palindromic(s)
print(longest_pal)


