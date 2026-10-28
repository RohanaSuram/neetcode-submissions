class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, value in enumerate(nums):
            difference = target - value
            if difference not in map:
                map[value] = i
            else:
                return[map[difference], i]
        