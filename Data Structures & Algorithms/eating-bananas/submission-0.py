
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_needed(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left



