class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pass
        skill.sort()
        left = 0
        n = len(skill)
        right = n - 1
        target = skill[left] + skill[right]
        answer = 0

        for i in range(n//2):
            if skill[left] + skill[right] != target:
                return -1
            answer += skill[left] * skill[right]
            left += 1
            right -= 1
        return answer
            
