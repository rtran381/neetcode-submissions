class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = 0
            
        while top < bottom and left < right:
            for c in range(left,right):
                res.append(matrix[top][c])
            top += 1
            for r in range(top, bottom):
                res.append(matrix[r][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][c])
            bottom -= 1

            for r in range(bottom - 1, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
        return res
