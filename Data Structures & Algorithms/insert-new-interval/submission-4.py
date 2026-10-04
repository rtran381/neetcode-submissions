class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        if i >= len(intervals):
            res.append(newInterval)
            return res

        if intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            res += intervals[i:]
            return res

        while i < len(intervals):
            if newInterval[1] >= intervals[i][0]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                res.append(newInterval)
                res += intervals[i:]
                return res

            i += 1
        res.append(newInterval)
        return res