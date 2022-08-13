class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        solution = 0
        nums_set = set(nums)
        for n in nums_set:
            if (n - 1) in nums_set:
                continue
            else:
                move_forward = 1
                while (n + move_forward) in nums_set:
                    move_forward += 1
            solution = max(solution, move_forward)
        return solution

        """
        Avoid writing nested codes because it hurt readibility.
        Clean code is achieved during planning.
        """
        """
        if len(nums) > 1:
            count = 1
            num = nums[0]
            store_count = []
            seen = []
            for i in range(len(nums)):
                see = nums[i]
                if not(see in seen):
                    seen.append(see)
                    if num + 1 in nums:
                        num += 1
                        count += 1
                        store_count.append(count)
                    else:
                        num = nums[i + 1]
                        if count > 1:
                            store_count.append(count)
            if len(store_count) > 0:
                sol = max(store_count)
                return sol
            return count
        
        elif len(nums) == 1:
            return 1
        else:
            return 0
        """ 