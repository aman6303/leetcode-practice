class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        ans = []

        set1 = set(nums1)
        set2 = set(nums2)
        list1 = set1.difference(set2)
        ans.append(list(list1))
        list2 = set2.difference(set1)
        ans.append(list(list2))

        return ans
