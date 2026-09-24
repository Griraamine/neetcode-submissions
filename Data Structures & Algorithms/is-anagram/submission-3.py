class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        
        
        seen = [0] * 26

        for i in range(len(s)):
            seen[ord(s[i]) - ord('a')] += 1
            seen[ord(t[i]) - ord('a')] -= 1

        return all(value == 0 for value in seen)

        