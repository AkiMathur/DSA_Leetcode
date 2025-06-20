class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        count = 0
                
        for j in range(1,len(nums)):
            if nums[i] == nums[j] and count < 1:
                i += 1
                count += 1
            elif nums[i] != nums[j]:
                count = 0
                i += 1
            nums[i] = nums[j]
        return i + 1