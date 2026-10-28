class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        totalAppearances = {}
        for num in nums:
            totalAppearances[num] = totalAppearances.get(num, 0) + 1
        
        sorted_nums = sorted(totalAppearances, key=totalAppearances.get, reverse=True)
        return sorted_nums[:k]
        


        