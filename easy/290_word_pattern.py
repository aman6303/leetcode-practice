class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        value = 1
        dict1 = {}
        pattern1 = []
        for char in pattern:

            if char not in dict1.keys():
                dict1[char] = dict1.get(char, value)
                value += 1
            pattern1.append(dict1[char])

        pattern2 = []
        dict2 = {}
        value = 1
        for word in s.split():

            if word not in dict2.keys():
                dict2[word] = dict2.get(word, value)
                value += 1
            pattern2.append(dict2[word])

        if pattern1 == pattern2:
            return True
        return False


Solution().wordPattern(pattern="abba", s="dog cat cat dog")
