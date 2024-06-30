from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for x in range(m):
          for y in range(n):
            if matrix[x][y] == 0:
              zeros.append((x,y))
        for x,y in zeros:
          matrix[x][:]=[0] * n
          for x_array in range(m):
            matrix[x_array][y] = 0
    
s = Solution()
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

s.setZeroes(matrix)
print(matrix)
