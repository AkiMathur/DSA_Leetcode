class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        major = nums.count(nums[0])
        temp = nums[0]
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i = j
                count = nums.count(nums[i])
                if count > major:
                    major = count
                    temp = nums[i]
        return temp