class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        u = sum(weights)
        res = u
        
        def canCap(cap):
            newcap = cap
            day = 1
            for weight in weights:
                if newcap - weight < 0:
                    day += 1
                    newcap = cap
                newcap -= weight
            return day <= days

        while l <= u:
            cap = int((l + u) // 2)
            if canCap(cap):
                res = min(res, cap)
                u = cap - 1
            else:
                l = cap + 1
            
        return res
        