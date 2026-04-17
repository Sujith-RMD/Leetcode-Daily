class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = {}
        ans = float('inf')
        for j, v in enumerate(nums):
            if v in d:
                ans = min(ans, j - d[v])
            rev = int(str(v)[::-1])
            d[rev] = j        
        return ans if ans != float('inf') else -1