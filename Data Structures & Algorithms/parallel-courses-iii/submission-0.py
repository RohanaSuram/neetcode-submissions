from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        dp = time[:]

        for a, b in relations:
            graph[a-1].append(b-1)
            indegree[b-1] += 1
        q = deque(i for i in range(n) if indegree[i] == 0)
        while q:
            u = q.popleft()
            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return max(dp)
        