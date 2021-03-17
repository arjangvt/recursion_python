"""
This code finds the longest palindromic substring using recursion.

written by: Arjang Fahim
Last update: 3/5/2021
"""

def longest_palindromic(s, i, j, sub_str, max_len, lp):

    
    if i+1 == len(s):
        print("len")
        return

    if sub_str == sub_str[::-1]:
        if len(sub_str) > max_len:
            max_len = len(sub_str)
            lp = sub_str 

    if j < len(s) and (j+1-i > max_len):
        lp = longest_palindromic(s, i, j + 1, sub_str + s[j], max_len, lp)
    elif j == len(s) and i+1 < len(s):
        lp = longest_palindromic(s, i + 1, i + 2 , s[i+1], max_len, lp)
    
    
    return lp

def util(s):
    return (longest_palindromic(s, 0 , 0, "", 0, ""))
    
s = "ada"
longest_pal = util(s)
print(longest_pal)


