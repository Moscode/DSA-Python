class Solution:
    def trap(self, height: List[int]) -> int:
        """
        What I Learnt: (1) Be sure to totally understand the question.
                       (2) Always be sure that your pseudocode or solution works before
                            by using sample and workthrough, PLEASE!!!
                       (3) Variables persist throughout the code so reinitialize them
                            if you're trying to use them in another while loop
        """
      
        """Time-Complexity: O(n), Space-Complexity: O(n)"""
        """
        first_i = 0
        end_i = len(height) - 1
        max_left = [0]
        max_right = [0]
        rain_water = 0
        while first_i <= end_i:
            left = max(height[first_i], max_left[first_i])
            max_left.append(left)
            first_i += 1
            
        first_i = 0
        end_i = len(height) - 1
        while end_i >= first_i:
            right = max(height[end_i], max_right[first_i])
            max_right.insert(first_i, right)
            end_i -= 1
        
        first_i = 0
        end_i = len(height) - 1
        while first_i <= end_i:
            determinant = min(max_left[first_i], max_right[first_i])
            solution = determinant - height[first_i]
            if solution > 0:
                rain_water += solution
            first_i += 1
        return rain_water
        """
        

    """
    My first attempt before checking solution
       #____________________|
        #|___\___\___\_ _\___|
        #|   \   \   |   \   |
        #|   |   \   |   |   |
        #|   |   \   |   |   |
        
        first_i = 0
        second_i = 1
        water_size = 0
        end = len(height) - 1
        
        while second_i != end:
            determinant = height[first_i] - height[second_i]
            if determinant < 0:
                first_i = second_i
                second_i += 1
            
            else:
                water_size += determinant
                second_i += 1
        return water_size
        
    """
                