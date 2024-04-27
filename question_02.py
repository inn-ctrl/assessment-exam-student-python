"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""

def count_unique_chars(string_1, string_2):
    #combine
    strings =string_1 + string_2
    #remove spaces
    nospacestring = strings.replace(" ", "")
    #make into a list
    combined = list(nospacestring)
    #Find unique chars
    unique = set(combined)
    #find length
    length = len(unique)
    return length