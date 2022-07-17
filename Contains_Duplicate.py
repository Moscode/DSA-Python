class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()
        for element in nums:
            if element in checker:
                return True
            else:
                checker.add(element)
        return False
        
        
        
        
        """
        Best solution: it is using an hash table which has a very good look up
        h = {}
        
        for i in nums:
            if i in h:
                return True
            else:
                h[i] = 1
        
        return False
        """
        
        
        
        """
        //This is leveraging on property of set
        
         if len(nums)==len(set(nums)):
            return False
        else:
            return True
        """
        
        
        
        
        """
        //Worked but not effient because of append and for loop
        
        checker = []
        for element in nums:
            if element in checker:
                return True
            else:
                checker.append(element)
        return False
        """