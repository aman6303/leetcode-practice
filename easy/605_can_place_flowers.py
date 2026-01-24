class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                # by doing i == 0 (we are checking if i is 0th index or not)

                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                # similarly here we are checking if i is last index or not

                # if it is last or first(0) just return True
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0  # think if [0,0,0] and n = 0 here we not be decreaing n to 1
