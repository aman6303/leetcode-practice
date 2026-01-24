class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 not in str1:
            return ""

        if str