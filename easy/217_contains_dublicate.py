class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True


print(Solution().containsDuplicate([1, 2, 3, 1]))
