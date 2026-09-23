from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first initialize the dict that will hold the {num : appearance_num}
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # now initialize array that will hold the 
        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()


        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res




