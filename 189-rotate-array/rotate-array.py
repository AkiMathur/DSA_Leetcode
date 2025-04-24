class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k !=0:
            reverse = [0] * n

            for i in range(n):
                reverse[(i+k)%n] = nums[i]

            for i in range(n):
                nums[i] = reverse[i]
