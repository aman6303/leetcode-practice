class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # method 1 
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i

        # return -1

        # method 2 -- wrong

        # for i in range(len(s)):
        #     if s[i] not in s[(i+1):]:
        #         return i
        # return -1

        # we can do it using dict also(time improved)

        dict1 = {}
        for char in s:
            dict1[char] = dict1.get(char,0)+1

        for key in dict1.keys():
            if dict1[key] == 1:
                ans = key
                break
        else:
            return -1
        for i in range(len(s)):
            if s[i] == ans:
                return i