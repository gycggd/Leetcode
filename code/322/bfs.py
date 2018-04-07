class Solution:
    ret = sys.maxsize
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        q = [0]
        cnt =  0
        visited = {0}
        while q:
            cnt += 1
            new_q = []
            for v in q:
                for c in coins:
                    new_v = v + c
                    if new_v == amount: return cnt
                    elif new_v > amount: continue
                    elif new_v not in visited:
                        visited.add(new_v)
                        new_q.append(new_v)
            q = new_q
        return -1