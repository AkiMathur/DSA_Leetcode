class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 1  # Points to where the next valid element goes
        count = 1  # Number of times the current number has been seen

        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1  # New number
            
            if count <= 2:
                nums[i] = nums[j]
                i += 1
        
        return i
                
