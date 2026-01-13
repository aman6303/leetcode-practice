class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                print(i)
                for j in nums[i:]:
                    if j != 0:
                        nums[i], j = j, nums[i]


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums=[0, 1, 0, 3, 12])6
print(nums)
