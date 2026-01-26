class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # method 1 - brute force (time limit exceeded)
        # avg = []

        # for i in range(len(nums)-(k-1)):
        #     curr_sum = 0
        #     for j in range(i,i+k):
        #         curr_sum += nums[j]
            
        #     curr_avg = curr_sum / k
        #     avg.append(curr_avg)

        # return max(avg)