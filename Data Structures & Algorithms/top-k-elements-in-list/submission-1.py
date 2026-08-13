class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        n = len(nums) + 1
        buckets = [[] for _ in range(n)] # make a bucket for each element

        for num in nums: #count num freq
            count[num] = 1 + count.get(num,0) 
        for num, cnt in count.items(): #add num to corresponding freq bucket
            buckets[cnt].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1): #go backwards from n
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
