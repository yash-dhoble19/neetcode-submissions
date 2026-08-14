class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

    # answer stores left products
        answer = [1] * n

    # Build left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

    # Running right product
        right = 1

    # Combine left and right products
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right* nums[i]

        return answer
