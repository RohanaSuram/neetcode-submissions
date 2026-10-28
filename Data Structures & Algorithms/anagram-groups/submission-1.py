class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count for each string and save group ones w same keys so count of index's
        map1 = {}
        for str1 in strs:
            totalCount = [0] * 26
            for c in str1:
                totalCount[ord(c) - ord('a')] += 1
            if tuple(totalCount) in map1:
                map1[tuple(totalCount)].append(str1)
            else:
                map1[tuple(totalCount)] = [str1]
        res = []
        for key,val in map1.items():
            res.append(val)
        return res