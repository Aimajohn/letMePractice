class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        chosen  = 0
        counter = 0
        for row in matrix:
            if target > row[-1]:
                continue
            return target in row
            
