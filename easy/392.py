class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # method 1 - wrong ans
        # ans = t.find(s)
        # if ans >= 0:
        #     return True
        # return False

        matchstr = ""
        for char in t:
            if char in s:
                matchstr = matchstr + char
        # breakpoint()
        if matchstr == s:
            return True
        return False


Solution().isSubsequence(s="abc", t="ahbgdc")
