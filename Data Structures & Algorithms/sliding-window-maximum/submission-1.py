class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #max heap so leftmost is greatest
        res = []
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: #remove smaller numbers from q than current
                q.pop()
            q.append(r)

            if l > q[0]: #if greatest number is out of window remove it from the queue
                q.popleft()
            
            if (r + 1) >= k: # if window size >= k, increment left and add current greatest
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res