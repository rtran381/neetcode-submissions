class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        for i, height in enumerate(heights + [0]):
            while stack and  height < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    w = (i - stack[-1] - 1)
                else:
                    w = i
                best = max(h * w, best)
            stack.append(i)
        return best