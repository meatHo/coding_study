#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11286                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11286                          #+#        #+#      #+#     #
#    Solved: 2026/03/19 22:01:40 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
from queue import *

n=int(sys.stdin.readline().rstrip())

pq = PriorityQueue()
for i in range(n):
    t=int(sys.stdin.readline().rstrip())
    if t==0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((abs(t),t))
