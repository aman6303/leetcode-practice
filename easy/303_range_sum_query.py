class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums  # string the array

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.arr[left : right + 1])  # calculating sum and returning it


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(0, 2))
