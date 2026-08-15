class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        def heapify(length: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < length and nums[left] > nums[largest]:
                largest = left
                
            if right < length and nums[right] > nums[largest]:
                largest = right
                
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(length, largest)
        
        # Build max heap (in-place)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
            
        # Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Swap max element to the end
            heapify(i, 0)                        # Heapify root with reduced size
            
        return nums