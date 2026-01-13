class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > (len(nums) / 2):
                return i


print(Solution().majorityElement([3, 2, 3]))
