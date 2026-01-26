class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counts = []
        for i in set(arr):
            counts.append(arr.count(i))

        if len(counts) == len(set(counts)):
            return True
        return False
