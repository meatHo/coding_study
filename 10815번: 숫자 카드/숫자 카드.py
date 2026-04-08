#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10815                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10815                          #+#        #+#      #+#     #
#    Solved: 2026/04/08 23:27:00 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
temp = map(int,sys.stdin.readline().split())

card = defaultdict(int)
for c in temp:
    card[c]+=1

m = int(sys.stdin.readline().rstrip())
whether = map(int,sys.stdin.readline().split())

for w in whether:
    if card[w]==0:
        print(0, end=" ")
    else:
        print(1, end=" ")

