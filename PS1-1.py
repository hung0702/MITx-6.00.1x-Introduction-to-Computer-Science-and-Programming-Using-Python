"""
Assume 's' is a string of lower case characters. Write a program that
counts up the number of vowels contained in the string 's'
"""
vowels = 0
"""Cycle through characters of 's' and count the number of vowels"""
for char in range(len(s)):
    if (
        s[char] == 'a' or 
        s[char] == 'e' or 
        s[char] == 'i' or
        s[char] == 'o' or
        s[char] == 'u'
    ):
        vowels += 1
print("Number of vowels: " + str(vowels))
