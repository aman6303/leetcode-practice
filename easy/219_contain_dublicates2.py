class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # method 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] == nums[j]:
        #             if abs(i-j) <= k:
        #                 return True
        #             return False
        #  wrong ans

        # initial check
        if len(nums) == len(set(nums)):
            return False

        # method 2
        for i in range(len(nums)):
            if nums[i] in nums[i + 1 :]:
                index = nums[i + 1 :].index(nums[i])
                final_index = index + (i + 1)
                if abs(i - final_index) <= k:
                    return True

        return False

        # try 3
        # for num in set(nums):
        #     first_index = nums.index(num)

        #     if num in nums[first_index+1:]:
        #         index = nums[first_index+1:].index(num)
        #         final_index = index + (first_index+1)
        #         if abs(first_index-final_index) <=k:
        #             return True

        # return False -- still time limit exceded

        # try 4 - time exceded
        # potential_ans = []
        # for num in set(nums):
        #     if nums.count(num) >= 2:
        #         potential_ans.append(num)

        # for num in potential_ans:
        #     first_index = nums.index(num)

        #     if num in nums[first_index+1:]:
        #         index = nums[first_index+1:].index(num)
        #         final_index = index + (first_index+1)
        #         if abs(first_index-final_index) <=k:
        #             return True

        # return False


print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # True
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # False
