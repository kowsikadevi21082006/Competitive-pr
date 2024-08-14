

def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist= dict(lambda: float("inf"))
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = (queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w] = edge_len + path_len
                    (queue, (edge_len + path_len, w))

    return dist

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        N = len(original)
        M = len(source)
        G = dict(list)
        
        ss = set()

        for i in range(N):
            G[original[i]].append((changed[i],cost[i]))
            ss.add(original[i])

        
        DG = {} 

        for let in ss:
            dist = dijkstra(G,let)
            DG[let] = dist

        res = 0

        # @cache
        def dp(i):
            if i == M:
                return 0
            
            r= float('inf')
            
            if source[i] == target[i]:
                r = min(r, dp(i+1))
            
            
            for pos in ss:
                
                lp = len(pos)

                spos =source[i:i+lp]
                dpos = target[i:i+lp]

                if spos == pos and DG[spos][dpos] != float('inf'):

                    r = min(r, dp(i+lp) + DG[spos][dpos] )

            return r
        
        rrr = dp(0)
        
        return rrr if rrr != float('inf') else -1
        