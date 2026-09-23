from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

         # number of occurance of each letter 

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] +=1

            seen[tuple(count)].append(word)


        return list(seen.values())





