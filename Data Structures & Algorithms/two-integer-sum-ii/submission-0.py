class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 1
        end = len(numbers)
        while numbers[start - 1] + numbers[end - 1] != target:
            if numbers[start - 1] + numbers[end - 1] > target:
                end -= 1
            else:
                start += 1
        return [start,end]