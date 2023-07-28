"""
1. 아이디어
- 입력받은 노드와 간선 데이터로 map을 만들어준다.
- 입력받은 간선에 대한 데이터로 map에 append해준다.
- map을 2중 for문을 돌면서 1을 만나면 bfs, dfs를 진행한다.
- bfs를 돌면서 1을 만나면 해당
2. 시간복잡도
-bfs, dfs = 11000 - 가능
3. 자료구조
- map : int[][]
- 방문확인 : bool[][]
- 결과 : dfs => int[]
        bfs => int[]
"""

import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    stk = [V]
    visit = [False]*(N+1)
    while stk:
        cur = stk.pop()
        if visit[cur]: continue
        visit[cur] = True
        print(cur, end=" ")
        stk.extend(G[cur][::-1])
    print()

def bfs():
    Q = deque([V])
    visit = [0]*(N+1)
    while Q:
        cur = Q.popleft()
        if visit[cur]: continue
        visit[cur] = True
        print(cur, end=" ")
        Q.extend(G[cur])

N, M, V = map(int, input().split())
G = [[] for _ in ' '*(N+1)]
for _ in ' '*M:
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
G = list(map(sorted, G))
dfs()
bfs()

