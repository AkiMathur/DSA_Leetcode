class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Two pointer
        i = 0 #Unique

        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i +=1
                nums[i] = nums[j]
        return i + 1
            