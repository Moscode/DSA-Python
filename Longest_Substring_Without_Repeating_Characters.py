class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        What I learnt:
        1. Failed this task alot of times because of different edge cases that I could not come up             with
        2. Understood difference between .discard and .remove method on set
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            seen = set()
            f_pointer = 0
            s_pointer = 0
            longest = 0
            while s_pointer < len(s):
                if s[s_pointer] not in seen:
                    seen.add(s[s_pointer])
                    s_pointer += 1
                else:
                    while s[s_pointer] in seen:
                        seen.discard(s[f_pointer])
                        f_pointer += 1
                longest = max(longest, (s_pointer - f_pointer))
            return longest
        
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        sub_array = []
        start = 0
        longest = 0
        while start < len(s):
            if s[start] in sub_array:
                longest = max(longest, len(sub_array))
                sub_array.clear()
            else:
                sub_array.append(s[start])
                longest = max(longest, len(sub_array))
                start += 1
        print(sub_array)
                
        return longest
        """