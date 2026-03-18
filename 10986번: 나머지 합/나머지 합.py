#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10986                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10986                          #+#        #+#      #+#     #
#    Solved: 2026/03/17 23:54:59 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().rsplit()))
remainder=[0]*m
temp = 0
answer = 0
for i in arr:
    temp+=i
    num = temp%m
    if num == 0:
        answer+=1
    remainder[num]+=1

for i in remainder:
    if i>1:
        answer+=i*(i-1)//2
print(answer)
