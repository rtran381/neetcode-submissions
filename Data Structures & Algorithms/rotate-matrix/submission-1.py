class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        x, y = 1, 0
        while y < len(matrix):
            while x < len(matrix):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
                x += 1
            y += 1
            x = y + 1