class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)
        result = [0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
            sufix [len(nums)- i-1] = sufix [len(nums)- i ]*nums[len(nums)- i] 
        for i in range(len(nums)):
            result[i] = prefix[i]*sufix[i]
        return result