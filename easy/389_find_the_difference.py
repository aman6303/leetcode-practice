class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        # t_set = set(t)
        # s_set = set(s)
        # ans = t_set.difference(s_set)
        # return ans.pop()  -wrong ans

        method 2 - correct but slow
        t_list = [char for char in t]
        for char in s:
            t_list.remove(char)

        return t_list[0]

        # # method 3 - fails when s='a' and t='aa'

        # for char in t:
        #     if char not in s:
        #         return char