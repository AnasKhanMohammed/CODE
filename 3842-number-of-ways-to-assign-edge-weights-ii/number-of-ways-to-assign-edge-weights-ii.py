class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        stack = [1]

        while stack:
            node = stack.pop()

            for nei in adj[node]:
                if nei != parent[node]:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    stack.append(nei)

        LOG = n.bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]

        up[0] = parent[:]

        for j in range(1, LOG):
            for node in range(1, n + 1):
                up[j][node] = up[j - 1][up[j - 1][node]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)
            distance = depth[u] + depth[v] - 2 * depth[ancestor]

            if distance == 0:
                ans.append(0)
            else:
                ans.append(pow(2, distance - 1, MOD))

        return ans