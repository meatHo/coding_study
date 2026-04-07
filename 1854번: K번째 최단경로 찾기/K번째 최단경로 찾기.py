#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1854                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1854                           #+#        #+#      #+#     #
#    Solved: 2026/04/06 23:55:41 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
import heapq

n,m,k = map(int,sys.stdin.readline().split())

dir = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    dir[a].append((b,c))

weight=[[]for _ in range(n+1)]#음수로 저장 maxheap
heapq.heappush(weight[1],0)
hq = []
heapq.heappush(hq,(0,1))
# heapq는 [0]에 대해서만 최소 보장. 나머지는 순서대로 있을 확률 없음.

while hq:
    cur_weight, cur = heapq.heappop(hq)

    for to, to_weight in dir[cur]:
        # print(cur)
        next_weight = cur_weight+to_weight

        if len(weight[to])<k:
            heapq.heappush(weight[to],-next_weight)
            heapq.heappush(hq,(next_weight,to))
        
        elif next_weight<-weight[to][0]:
            heapq.heappop(weight[to])
            heapq.heappush(weight[to],-next_weight)
            heapq.heappush(hq,(next_weight,to))

for i in range(1,n+1):
    # print(weight[i])
    if len(weight[i])<k:
        print(-1)
    else:
        print(-weight[i][0])