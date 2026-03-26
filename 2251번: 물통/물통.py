#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2251                           #+#        #+#      #+#     #
#    Solved: 2026/03/23 02:10:24 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
#  DFS
import sys
from collections import *

def dfs(a,b):#a가 b에게 붓는 것 8, 0, 2 일 떄 a->b로 이동 로직
    # 1 4 5
    # 5 4 1
    if visited[a][b]:
        return

    visited[a][b]=True

    maxa=maxk[0]
    maxb=maxk[1]
    maxc=maxk[2]
    c=maxc-b-a

    if a == 0 :
        res.add(c)
    
    # 아니 여기 if문을 쓸 이유가 없지 않나? 그냥 각각 a에서 전송할 떄 b에서 전송할 떄 c에서 전송할 때 걍 무지성으로 돌리면 되잖아
    # visited만 하고 걍 돌리면 되지 않나? -> min으로
    water = 0
    
    # a->b
    water = min(a, maxb-b)
    dfs(a-water,b+water)
    # a->c
    water = min(a, maxc-c)
    dfs(a-water,b)
    # b->a
    water = min(b, maxa-a)
    dfs(a+water,b-water)
    # b->c
    water = min(b, maxc-c)
    dfs(a,b-water)
    # c->a
    water = min(c, maxa-a)
    dfs(a+water,b)
    # c->b
    water = min(c, maxb-b)
    dfs(a,b+water)




sys.setrecursionlimit(10*9)

maxk=list(map(int,sys.stdin.readline().rstrip().split()))
visited=[[False for _ in range(201)] for _ in range(201)]

# 5 4 1

res=set()
dfs(0,0)

temp = list(res)
temp.sort()
for i in temp:
    print(i, end=" ")



# BFS

import sys
from collections import *

maxa,maxb,maxc = map(int,sys.stdin.readline().rstrip().split())

dq = deque()

total = maxc

visited=[[False for _ in range(201)] for _ in range(201)]
dq.append((0,0)) # 튜플

res = set()

while dq:
    t=dq.popleft()
    cura=t[0]
    curb=t[1]

    if visited[cura][curb]:
        continue
    
    visited[cura][curb]=True
    curc=total-cura-curb

    if cura==0:
        res.add(curc)
    
    # a->b
    water = min(maxb-curb,cura)
    dq.append((cura-water,curb+water))
    # a->c
    water = min(maxc-curc,cura)
    dq.append((cura-water,curb))
    # b->a
    water = min(curb,maxa-cura)
    dq.append((cura+water,curb-water))
    # b->c
    water = min(curb,maxc-curc)
    dq.append((cura,curb-water))
    # c->a
    water = min(curc,maxa-cura)
    dq.append((cura+water,curb))
    # c->b
    water = min(curc,maxb-curb)
    dq.append((cura,curb+water))

temp=list(res)
temp.sort()
for i in temp:
    print(i, end=' ')