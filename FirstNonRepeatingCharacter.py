def nonrepeatingCharacter( s):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Iterate through the string to populate the dictionary
    for char in s:
        if char in char_count:
            char_count[char] += 1
            print(char_count)
        else:
            char_count[char] = 1

    # Iterate through the string again to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None or a default value
    return None

result = nonrepeatingCharacter("hello")
print(result)  # Output: "h"