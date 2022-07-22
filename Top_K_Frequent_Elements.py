class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for word in nums:
            if word in hashmap:
                hashmap[word] = hashmap.get(word) + 1
            else:
                hashmap[word] = 1
        solution = dict(sorted(hashmap.items(), key = lambda item: item[1]))
        final_solution = solution.keys()
        return list(final_solution)[-k:]