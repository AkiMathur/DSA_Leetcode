class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k!=0:
            def reverse_arr(start,end):
                end -= 1
                while start<end:
                    nums[start],nums[end] = nums[end],nums[start]
                    start += 1
                    end -= 1
            reverse_arr(0,n)
            reverse_arr(0,k)
            reverse_arr(k,n)

