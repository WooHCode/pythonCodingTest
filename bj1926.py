"""
1. 아이디어
- 2중for문을 돌면서 값이1 && BFS
- BFS를 돌면서 그림 개수 +1, 최대값을 갱신
2. 시간복잡도
- BFS = O(V+E)
- V = M * N
- E = 4 * V
- V + E = M * N + 4V = V + 4V = 5V = 5*M*N
- BFS = O(5V) = 5*500*500 = 750000 < 200,000,000 -> 가능
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt +=1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)