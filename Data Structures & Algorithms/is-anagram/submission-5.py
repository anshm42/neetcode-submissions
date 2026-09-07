class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countt = {}
        counts = {}

        for i in range(len(s)):
            countt[t[i]] = countt.get(t[i], 0) + 1
            counts[s[i]] = counts.get(s[i], 0) + 1
        
        return countt == counts