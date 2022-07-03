class Solution:
    def permutation(self, nums):
        solution = []
        #Base Case
        if (len(nums) == 1):
            return [nums[:]]
        
        for index in range(len(nums)):
            num = nums.pop(0)
            permutate = permutation(nums)
        
            for perm in permutate:
                perm.append(n)
            return solution.extend(permutate)
            nums.append(n)

        return result
