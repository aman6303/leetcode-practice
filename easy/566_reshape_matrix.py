# 566. Reshape the Matrix

# Hint
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        shapeofmat = len(mat) * len(mat[0])  # calculating the shape of matrix

        if shapeofmat != r * c:
            return mat

        flatarr = []
        for row in mat:  # flatten the array
            flatarr.extend(row)

        ans = []

        sizearr = r * c
        while sizearr > 0:  # reshaping the arr
            finalrow = []
            for j in range(c):
                finalrow.append(flatarr[-sizearr])
                sizearr -= 1

            ans.append(finalrow)

        return ans


# print(Solution().matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4))
print(Solution().matrixReshape(mat=[[1, 2], [3, 4]], r=4, c=1))
