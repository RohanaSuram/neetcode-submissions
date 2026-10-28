class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = sorted(s)
        tarr = sorted(t)
        if sarr == tarr:
            return True
        else:
            return False
        