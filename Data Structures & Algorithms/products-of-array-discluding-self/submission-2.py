class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n    # left[i] = i 左边所有数的乘积
        right = [1] * n   # right[i] = i 右边所有数的乘积

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [left[i] * right[i] for i in range(n)]
            

                

            
        