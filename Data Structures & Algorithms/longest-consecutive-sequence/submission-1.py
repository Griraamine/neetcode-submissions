class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_len = 1 
        tawa = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                tawa += 1 
                if max_len < tawa:
                    max_len = tawa
            else:
                tawa = 1

        return max_len