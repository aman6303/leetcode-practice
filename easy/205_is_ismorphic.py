class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        value = 1
        dict1 = {}
        pattern = []
        for char in s:

            if char not in dict1.keys():
                dict1[char] = dict1.get(char, value)
                value += 1
            pattern.append(dict1[char])

        pattern2 = []
        dict2 = {}
        value = 1
        for char in t:

            if char not in dict2.keys():
                dict2[char] = dict2.get(char, value)
                value += 1
            pattern2.append(dict2[char])
        breakpoint()
        if pattern == pattern2:
            return True
        return False


Solution().isIsomorphic("foo", "bar")
