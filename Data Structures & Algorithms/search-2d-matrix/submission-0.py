class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search
        line = -1
        for i in range(len(matrix)):
            if matrix[i][0]<= target and matrix[i][-1] >= target:
                line = i
                break

        if line == -1:
            return False
        
        
        #bsearch with the known row
        bottom, top = 0, len(matrix[line]) -1

        while(bottom <= top):
            pos = (bottom+top) // 2
            if matrix[line][pos] > target:
                top = pos-1
            elif matrix[line][pos] < target:
                bottom = pos+1
            else:
                return True


        return False