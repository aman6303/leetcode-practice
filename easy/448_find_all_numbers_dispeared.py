class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # brute force -time exceded
        # ans = []
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         ans.append(i)

        # ans = []
        # for i in range(1,len(nums)+1):
        #     if i not in set(nums):
        #         ans.append(i)

        # using set appproach

        set1 = set(i for i in range(1, len(nums) + 1))
        set2 = set(nums)

        ans = list(set1 - set2)

        return ans
