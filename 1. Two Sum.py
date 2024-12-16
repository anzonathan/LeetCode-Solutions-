#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum == target:
                ind = [i,i+1]
                return ind

