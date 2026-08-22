class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stack and temperatures[stack[-1]] < cur:
                rm = stack.pop()
                res[rm] = i - rm
            stack.append(i)
        return res
