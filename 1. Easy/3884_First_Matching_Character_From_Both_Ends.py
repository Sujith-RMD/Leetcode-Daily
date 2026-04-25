class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            j=n-i-1
            if s[i]==s[j]:
                return i
        return -1