class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def calculate_prod(mylist):
            # if set(mylist) == {-1,1}:
            #     neg_ones = mylist.count(-1)
            #     if neg_ones % 2 == 0:
            #         return 1
            #     return -1
            ans = 1
            for i in mylist:
                ans *= i
            return ans

        final_ans = []
        for i in range(len(nums)):
            result = calculate_prod(nums[0:i] + nums[i + 1 :])
            final_ans.append(result)  # -- time limit exceded

        return final_ans
