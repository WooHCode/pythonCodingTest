"""
1. 아이디어
- 1부터 N까지 하나를 우선 선택하고
- 다음 1부터 N까지 선택할 때 이미 선택하지 않은 경우 선택
- M개를 선택했을 경우 프린트
2. 시간복잡도
- 중복이 가능할 경우 N^N -> 8까지 가능
- 중복이 불가능 할 경우 N!  -> 10까지 가능
3. 자료구조
- 방문 여부 확인 배열 : bool[][]
- 선택한 값 저장 배열: int[]
"""

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
chk = [False] * (N+1)
rs = []

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
recur(0)