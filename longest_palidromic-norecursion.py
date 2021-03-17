"""
This code finds the longest palindromic substring.
The complxity of the algorithm O(n^3) and space complexity is O(1)

written by: Arjang Fahim
Last update: 3/10/2021
"""

def longest_palindromic(s):

    max_len = 0
    str_temp = ""
    
    k = len(s)
    for i in range(k, 0, -1):
        for j in range(len(s) - i + 1):
            str_temp = s[j:j+i]
            rem = len(str_temp) % 2
            if rem == 0:
                mid = int(len(str_temp) / 2) - 1
            else:
                mid = int(len(str_temp) / 2)

            l = 0
            t = len(str_temp) - 1
            while l <= mid and t >= mid and str_temp[l] == str_temp[t]:
                l = l + 1
                t = t - 1

            if l-1 == mid:
                return str_temp
    return ""

s = "aa"
longest_pal = longest_palindromic(s)
print(longest_pal)


