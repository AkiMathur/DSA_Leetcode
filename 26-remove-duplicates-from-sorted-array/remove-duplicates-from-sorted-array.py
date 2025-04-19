class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        i = 0
        while i < len(nums):
            if nums[i] != last:
                last = nums[i]
                i+=1
            else:
                nums.pop(i)
            