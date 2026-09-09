class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        from collections import deque

class Solution(object):

    def bfs(self, src, adj, n):
        dist = [-1] * n
        q = deque([src])
        dist[src] = 0

        while q:
            node = q.popleft()

            for nei in adj[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    q.append(nei)

        return dist

    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dx = self.bfs(x, adj, n)
        dy = self.bfs(y, adj, n)
        dz = self.bfs(z, adj, n)

        ans = 0

        for i in range(n):
            d = sorted([dx[i], dy[i], dz[i]])

            if d[0] * d[0] + d[1] * d[1] == d[2] * d[2]:
                ans += 1

        return ans