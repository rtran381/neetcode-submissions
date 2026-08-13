class Solution:
    def trap(self, height: List[int]) -> int:
        preMax = [0]
        sufMax = [0]


        left, right = 0, len(height) - 1


        maxPre, maxSuf = height[left], height[right]
        for i in range(1 ,len(height)):
            preMax.append(maxPre)
            if height[i] > maxPre:
                maxPre = height[i]
        
        for i in range(len(height) - 2 , -1 , -1):
            sufMax.insert(0,maxSuf)
            if height[i] > maxSuf:
                maxSuf = height[i]

        total = 0
        for i in range(0,len(height)):
            total += max(min(preMax[i], sufMax[i]) - height[i], 0)
        
        print(sufMax)
        print(preMax)
        return total