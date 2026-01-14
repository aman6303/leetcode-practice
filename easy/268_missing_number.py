class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # brute force approach
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


print(Solution().missingNumber([3, 0, 1]))  # 2
print(Solution().missingNumber([0, 1]))  # 2
