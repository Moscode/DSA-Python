class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) <= 0 or len(t) <= 0):
            return False
        else:
            if (len(s) == len(t)):
                s_hashmap = {}
                t_hashmap = {}
                for i in range(len(s)):
                    s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
                    t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1
                for j in s_hashmap:
                    if s_hashmap.get(j, 0) != t_hashmap.get(j, 0):
                        return False
                return True
            else:
                return False
   

    """
    Untested idea: ASCII should be useful in solving this problem too
    """
    
    """
    What I learnt while searching for solution:
    
    ascii() function escapes the non-ASCII character while the print function print does         not escape this value.
    
    ord() takes char and return Dec while chr() takes Dec and return char
    """
        
        
    """
    Sorted then compare the two
    return sorted(s) == sorted(t)
    """
        
    """
    Note the edge cases needed to be handled with get method
    if (len(s) == len(t)):
        s_hashmap = {}
        t_hashmap = {}
        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1
            for j in s_hashmap:
                if s_hashmap.get(j, 0) != t_hashmap.get(j, 0):
                    return False
            return True
    """
        