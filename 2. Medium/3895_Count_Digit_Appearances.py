class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            while i!=0:
                if i%10==digit:
                    c+=1
                i//=10
        return c