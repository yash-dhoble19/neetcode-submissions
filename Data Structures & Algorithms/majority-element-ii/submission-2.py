class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h= {}
        new = []
        for i in range(len(nums)):
            h[nums[i]] = 1 + h.get(nums[i], 0)
        print(h)
        for key in h :  
            if h[key] > len(nums)/3:
                new.append(key)   
        return new

        