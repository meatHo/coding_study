#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1325                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1325                           #+#        #+#      #+#     #
#    Solved: 2026/03/22 23:01:52 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n,m=map(int,sys.stdin.readline().rstrip().split())
dir=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    dir[b].append(a)

res=[0]*(n+1)

for root in range(1,n+1):
    visited=[-1]*(n+1)
    visited[root]+=1
    dq = deque()
    dq.append(root)
    ans=0
    while dq:
        cur=dq.popleft()
        for i in dir[cur]:
            if visited[i]==-1:
                dq.append(i)
                visited[i]+=1
                ans+=1
    res[root]=ans

maxval=max(res)
for i in range(1,n+1):
    if res[i]==maxval:
        print(i,end=" ")


#//////////////////////////////////밑에는 append가 반대인 로직임. 이럴 경우 나를 해킹할 수 있는 애한테 +1을 하는거임
import sys
from collections import deque

input = sys.stdin.readline

# N: 노드 개수, M: 에지 개수
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                # 신규 노드 인덱스의 정답 리스트값을 증가
                answer[i] += 1 
                queue.append(i)

# 에지 정보 입력 받기
for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

# 모든 노드에서 BFS 실행
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    BFS(i)

# 최댓값 찾기
maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, answer[i])

# 최댓값을 가진 노드들 출력
for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ')