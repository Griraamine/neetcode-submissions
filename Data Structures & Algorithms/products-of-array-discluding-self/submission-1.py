from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        front = []
        back = []
        pos = 1
        neg = 1 
        for i in range(len(nums)):
            pos *= nums[i]
            front.append(pos)
            neg *= nums[len(nums) - i -1 ]
            back.append(neg)
        result = []
        for i in range(1,len(nums)-1):
            result.append(front[i-1]*back[len(nums) - i - 2])
        
        return [back[len(nums)-2]] + result + [front[len(nums)-2]]

        