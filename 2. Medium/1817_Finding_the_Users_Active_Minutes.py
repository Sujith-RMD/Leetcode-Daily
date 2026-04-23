from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for uid, t in logs:
            d[uid].add(t)
        ans = [0] * k
        for uid in d:
            uam = len(d[uid])
            if uam <= k:
                ans[uam - 1] += 1
        return ans