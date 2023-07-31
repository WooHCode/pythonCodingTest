"""
1. 아이디어
- 2중 for문을 돌면서 1이면 bfs
- bfs를 돌면서 1이고 방문하지 않았다면 cnt +1
2. 시간복잡도
- BFS = O(V+E)
- V = N * M = 100 * 100 = 10000
- E = 4V = 400
- BFS = 10400 -> 2억보다 작음, BFS가능
3. 자료구조
- 방문여부 체크 : bool[][]
- 이어져있는 노드 체크 : int
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(start_y, start_x):
    q = deque([(start_y, start_x, 1)])  # 시작 위치와 거리를 함께 큐에 넣어줍니다.
    chk[start_y][start_x] = True

    while q:
        y, x, distance = q.popleft()

        if y == N-1 and x == M-1:
            return distance  # 목적지에 도착했을 때, 거리를 반환합니다.

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and not chk[ny][nx] and maze[ny][nx] == 1:
                chk[ny][nx] = True
                q.append((ny, nx, distance + 1))  # 다음 위치로 이동하면서 거리를 1 증가시킵니다.

    return -1  # 도착지점에 도달하지 못한 경우 -1을 반환합니다.

print(bfs(0, 0))  # 시작 위치인 (0, 0)에서 출발하여 목적지인 (N-1, M-1)로 가는 최단 거리를 출력합니다.
