class Solution:
    """
    What I learnt:
    Fancy feature should only be used if neccessary e.g enumerate
    Pay close attention to details
    set cannot be indexed
    Validate the requirements of what you need a data structure for before selecting one
    Learnt that because I used set thinking about distinct value instead of indexing
    """
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return nums
        sub = {}
        for i, val in enumerate(nums):
            if val in sub:
                return [sub[val], i]
            conjugate = target - val
            sub[conjugate] = i
    
    """
    time: O(n^2) and space: O(n)
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j):
                    sum_num = nums[i] + nums[j]
                    if (sum_num == target):
                        return [i, j]
    """           

b = Solution()
print(b.twoSum([2,7,11,15], 17))