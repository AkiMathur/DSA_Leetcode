class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        farthest = 0
        current = 0

        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])

            if current == i:
                jump += 1
                current = farthest
                if farthest >= len(nums)-1:
                    return jump
        return jump