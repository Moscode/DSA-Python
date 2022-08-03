class Solution:
    """
    Lesson Learnt: I need to know more about built-in function
    and expected values regarding the lang I'm using
    """
    def isPalindrome(self, s: str) -> bool:
        front_pointer = 0
        end_pointer = len(s) - 1
        while(front_pointer < end_pointer):
            if not s[front_pointer].isalnum():
                front_pointer += 1
                continue
            lower_char1 = s[front_pointer].lower()
            if not s[end_pointer].isalnum():
                end_pointer -= 1
                continue
            lower_char2 = s[end_pointer].lower()
            if lower_char1 == lower_char2:
                front_pointer += 1
                end_pointer -= 1
            else:
                return False
        return True
            
        """
        store_clean_str = []
        for i in range(len(s)):
            if s[i].isalnum():
                lower_char = s[i].lower()
                store_clean_str.append(lower_char)
        """