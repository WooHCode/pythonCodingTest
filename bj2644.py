"""
1. 아이디어
- 첫번째에 노드 수가 정해짐
- 두번째에 노드의 번호가 주어짐(7,3이면 7에서 3까지)
- 세번째에는 간선의 수가 정해짐
- 네번째부터는 연결정보가 주어짐
-노드 번호부터 시작해서 하나씩 뽑아서 bfs, 방문하지않았으면 +1
2. 시간복잡도
- BFS = O(V+E)
- V : 100 * 100
- E : 4V = 4 * 100 * 100
- 2억미만, BFS가능
3. 자료구조
- 방문여부 : bool[]
- bfs = deque[(start,0)]- 시작점, 촌수 형태로 저장
"""

import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
start, end = map(int, input().split())
d = int(input())
G = [[] for _ in range(V+1)]

def bfs():
    q = deque([(start, 0)])  # 큐에 튜플 형태로 (노드, 촌수)를 저장합니다.
    chk = [False] * (V+1)
    chk[start] = True
    while q:
        node, cnt = q.popleft()
        if node == end:  # 끝 노드에 도달하면 촌수를 출력하고 종료합니다.
            print(cnt)
            return
        for next_node in G[node]:  # 현재 노드와 연결된 모든 노드를 확인합니다.
            if not chk[next_node]:  # 방문하지 않은 노드라면 큐에 넣고 방문 표시를 합니다.
                chk[next_node] = True
                q.append((next_node, cnt+1))

    # 끝 노드에 도달하지 못한 경우, 촌수가 없으므로 -1을 출력합니다.
    print(-1)

for _ in range(d):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

bfs()
