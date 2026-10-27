class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        rightsum = total
        leftsum = 0
        rightsum = 0
        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum

            if leftsum == rightsum:
                return i
            leftsum += nums[i]

        return -1