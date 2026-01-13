class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i > target:
                    return nums.index(i)
            else:
                return len(nums)


print(Solution().searchInsert([1, 3, 5, 6], 5))
