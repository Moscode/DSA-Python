class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in nums]
        postfix = [1 for i in nums]
        
        #prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        #postfix
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
            
        return [prefix[i] * postfix[i] for i in range(len(nums))]