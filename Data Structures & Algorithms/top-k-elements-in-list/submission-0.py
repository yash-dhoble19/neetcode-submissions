class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = 1 + h.get(nums[i],0)

        # h1= dict(sorted(h.items(), key=lambda item: item[1]))
        h1 = sorted(h, key= h.get, reverse = True )
        return h1[:k]
