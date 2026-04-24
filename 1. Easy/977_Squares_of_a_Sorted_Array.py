class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        left = 0
        right = len(nums) - 1
        l = []
        while left <= right:
            if nums[left] > nums[right]:
                l.append(nums[left])
                left += 1
            else:
                l.append(nums[right])
                right -= 1
        return l[::-1] 