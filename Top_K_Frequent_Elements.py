class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        (1) Learnt how to sort a dictionary using values or keys
        (2) learnt that even though dictionary keys return a list it can't still be slice 
        because it is still diction until when list method is used on it
        (3) Understanding how to use slice with negative values better
        """
        hashmap = {}
        for word in nums:
            if word in hashmap:
                hashmap[word] = hashmap.get(word) + 1
            else:
                hashmap[word] = 1
        solution = dict(sorted(hashmap.items(), key = lambda item: item[1]))
        final_solution = solution.keys()
        return list(final_solution)[-k:]