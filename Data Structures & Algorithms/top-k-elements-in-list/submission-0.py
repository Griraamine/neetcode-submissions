from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums :
            seen[num] += 1

       # {number : its_concurrency}

        idk = [[] for _ in range(len(nums) + 1)]


        [0 , 1 , 2 , 3 , 4, 5, 6]
        [[],[1],[2],[3],[],[],[],]
        for key in (seen.keys()):
            idk[seen[key]].append(key)


        return [num for freq in range(len(idk)-1,0,-1) for num in idk[freq]][:k]           




 

        



        