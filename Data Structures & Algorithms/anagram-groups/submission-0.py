class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = {}
        for value in strs:
            key = "".join(sorted(value))
            if key not in total:
                total[key] = []
            total[key].append(value)
        return list(total.values())