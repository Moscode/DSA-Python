class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        return hashmap.values()
        
        
        
        
        """
        First Attempt solution
        
        solution = []
        for i in range(len(strs)):
            temp = []
            anagram = "".join(sorted(strs[i]))
            for j in range(len(strs)):
                j = j + 1
                if j == len(strs):
                    break
                anagram_2 = "".join(sorted(strs[j]))
                if (anagram == anagram_2):
                    if i > 0:
                        if not (strs[i] in solution[i - 1]):
                            temp.append(strs[j])
                    elif i == 0:
                        temp.append(strs[j])
                else:
                    continue
            solution.append(temp)
        return solution
        """