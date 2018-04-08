class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S==T: return 0
        nr = len(routes)
        routes = [set(_) for _ in routes]
        cross = [[False]*nr for _ in range(nr)]
        for i in range(nr):
            for j in range(i, nr):
                if i==j:
                    cross[i][j] = True
                else:
                    c = (len(routes[i]&routes[j])>0)
                    cross[i][j] = cross[j][i] = c
        dic = collections.defaultdict(set)
        for r in range(len(routes)):
            for i in routes[r]:
                dic[i].add(r)
        q = list(dic[S])
        dest = dic[T]
        visited = dic[S]
        cnt = 0
        while q:
            cnt += 1
            new_q = []
            for idx in q:
                if idx in dest:
                    return cnt
                for new_idx in range(nr):
                    if cross[idx][new_idx] and new_idx not in visited:
                        visited.add(new_idx)
                        new_q.append(new_idx)
            q = new_q
        return -1