class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # dict1 = {}
        # for char in s:
        #     dict1[char] = dict1.get(char, 0) + 1

        # dict2 = {}
        # for char in t:
        #     dict2[char] = dict2.get(char, 0) + 1

        # if dict1 == dict2:
        #     return True
        # return False

        # method 2

        alphabets = [0] * 26

        for char in s:
            index = ord(char) - 97
            alphabets[index] += 1

        for char in t:
            index = ord(char) - 97
            alphabets[index] -= 1

        # if len(alphabets) == alphabets.count(0):
        if all(i == 0 for i in alphabets):
            return True
        return False


Solution().isAnagram(s="anagram", t="nagaram")
