class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        w = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1
        return w


print(Solution().removeElement([3, 2, 2, 3], 3))
