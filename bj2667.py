"""
1. 아이디어
- 2중 for문을 돌면서 값이 1이고 방문 x, dfs
- dfs를 통해 찾은 값을 저장 후 정렬해서 출력
2. 시간복잡도
- DFS = O(V+E)
- V = N^2
- E = N^2 * 4
- V+E = 25^ + 25^ * 4 < 2억, DFS가능
3. 자료구조
- 지도 : int[][]
- 방문확인 : bool[][]
- 결과값 : int[]
"""

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [([False] * n) for _ in range(n)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)

result.sort()
print(len(result))

for i in result:
    print(i)