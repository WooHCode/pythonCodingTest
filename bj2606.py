"""
1. 아이디어
- 2중 for문을 돌면서 1을만나면 bfs
- bfs를 돌면서 방문하지않았고, 1을 만나면 count +1
2. 시간복잡도
- BFS = O(V+E)
- V : 100 * 100
- E : 4 * 100 * 100
- V+E = 2억보다 작음, BFS가능
3. 자료구조
- 방문여부 : bool[][]
- 타겟 : q
- 감염된 노드 수 : int
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
G = [[] for _ in ' '* (n+1)]


rs = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs():
    global rs
    q = deque([1])
    chk = [False]*(n+1)
    chk[1] = True
    while q:
        t= q.popleft()
        for node in G[t]:
            if not chk[node]:
                chk[node] = True
                rs +=1
                q.append(node)

for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

bfs()
print(rs)