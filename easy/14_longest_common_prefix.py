class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        element = []
        for j in range(200):
            for i in range(len(strs)):
                if i == 0:
                    element.append(strs[i][j])
                elif str[i][j] == element[i]:
                    pass


strs = ["flower", "flow", "flight"]
