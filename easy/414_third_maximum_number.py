class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # set1 = set(nums)

        # max_value = max(set1)
        # count = 0
        # for num in set1:
        #     if num < max_value:
        #         count += 1
        #         if count == 2:
        #             return num
        # return max_value

        nums = list(set(nums))  # removing duplicates

        max_value1 = max(nums)
        nums.remove(max_value1)  # as remove is affecting the original array

        if len(nums) > 0:
            max_value2 = max(nums)
            nums.remove(max_value2)
            if len(nums) > 0:
                return max(nums)
        return max_value1
