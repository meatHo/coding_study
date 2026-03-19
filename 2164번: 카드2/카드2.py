#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2164                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2164                           #+#        #+#      #+#     #
#    Solved: 2026/03/19 00:12:02 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import *

n=int(sys.stdin.readline().rstrip())

mydq = deque()
for i in range(1,n+1):
    mydq.appendleft(i)

while len(mydq)>1:
    mydq.pop()
    mydq.appendleft(mydq.pop())
print(mydq.pop())