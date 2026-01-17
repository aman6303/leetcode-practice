# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle) # we can do it directly

        i = 0
        while len(haystack) > 0:
            if haystack.startswith(needle):
                return i
            i += 1
            haystack = haystack[1:]
        else:
            return -1
