class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        else:
            num = ""
            for digit in digits:
                num = num + str(digit)
            ans = int(num) + 1
            result = []
            for digit in str(ans):
                result.append(int(digit))
            return result


print(Solution().plusOne([9]))
