# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # using split
        wordlist = s.split()
        return len(wordlist[-1])

        # method 2

        count = 0
        for char in s[::-1]:
            if char == " ":
                return count
            count += 1
