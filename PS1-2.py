"""Assume 's' is a string of lower case characters. Write a program that
prints the number of times the string 'bob' occurs in 's'
"""
bobcount = 0
"""Cycle through series of three letters to check for 'bob'"""
for char in range(len(s)-2):
    if (
        s[char]   == 'b' and
        s[char+1] == 'o' and
        s[char+2] == 'b'
    ):
        vnum += 1
print("Number of bob occurs is: " + str(bobcount))