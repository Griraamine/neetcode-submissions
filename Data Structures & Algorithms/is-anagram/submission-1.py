from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        
        
        seen = defaultdict(int)
        nah = defaultdict(int)


        for i in range(len(s)):
            seen[s[i]] += 1
            nah[t[i]] += 1

        return nah == seen
