class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return res
            
            if total > target or i >= len(nums):
                return

            #choice 1 including a number
            curr.append(nums[i])
            dfs(i, total + nums[i])

            #choice 2 excluding a number
            curr.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res


        