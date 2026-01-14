class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
                    return False


print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # True
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # False
