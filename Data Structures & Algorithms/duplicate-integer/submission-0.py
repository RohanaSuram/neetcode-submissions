class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for letter in nums:
            if letter in seen:
                return True
            else:
                seen.add(letter)
        return False