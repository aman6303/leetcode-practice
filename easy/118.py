class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1, numRows + 1):
            curr_arr = []
            for j in range(1, i + 1):
                curr_arr.append(i - 1)
            ans.append(curr_arr)
        return ans

        # i = 0

        # while i < numRows:
        #     j = 0
        #     while j < i:
        #         print(i, j)
        #         j += 1
        #     i += 1


print(Solution().generate(5))

# 1
# 11
# 121
# 1331
# 14641
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

# i = 4, j = 0   1
# i = 4, j = 1   4
# i = 4, j = 2   6
# i = 4, j = 3   4
# i = 4, j = 4   1

# Not solved yet
