class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        for i in range(len(num)):
            for j in range(len(num)):
                if j==i:
                    continue
                if num[i]+ num[j] == target:
                    return [i, j]
                
print(Solution().twoSum([2,7,11,15],9))
