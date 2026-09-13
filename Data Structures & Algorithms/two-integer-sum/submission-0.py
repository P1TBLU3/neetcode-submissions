class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dif:
                return [dif[complement],i]
            
            dif[nums[i]] = i