class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity: O(n), space complexity: O(1) since the question ignore the output/res space
        pref = 1
        postfix = 1
        res = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
        """
        
        
        """
        time complexity: O(n), space complexity: O(n)
        prefix = [1 for i in nums]
        postfix = [1 for i in nums]
        
        #prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        #postfix
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
            
        return [prefix[i] * postfix[i] for i in range(len(nums))]
        """