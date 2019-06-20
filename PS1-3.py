"""Assume s is a string of lower case characters. Write a program that 
prints the longest substring of s in which the letters occur in 
alphabetical order. In the case of ties, print the substring that 
appears first.
"""
working = s[0]
longest = s[0]
"""Build strings where characters appear in alphabetical order"""
for char in range(1, len(s)):
    if s[char] >= working[-1]:
        working += s[char]
        if len(working) > len(longest):
            longest = working
    else:
        if len(working) > len(longest):
            longest = working
        working = s[char]
print("Longest substring in alphabetical order is: " + longest)