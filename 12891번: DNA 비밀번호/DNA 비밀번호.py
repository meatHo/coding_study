#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12891                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12891                          #+#        #+#      #+#     #
#    Solved: 2026/03/18 21:51:18 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *
input = sys.stdin.readline

def check(c):
    if c=='A':
        return 0
    elif c=='C':
        return 1
    elif c=='G':
        return 2
    elif c=='T':
        return 3

z,p = map(int,input().rstrip().split())
mystr = input().rstrip()
a,c,g,t = map(int,input().rstrip().split())
arr = [0]*4

s=res=0
e=s+p-1

for i in range(p):
    arr[check(mystr[i])] +=1

while True:
    if arr[0]>=a and arr[1]>=c and arr[2]>=g and arr[3]>=t:
        res+=1
    # print(f"a{arr[0]} c{arr[1]} g{arr[2]} t{arr[3]}")
    arr[check(mystr[s])]-=1
    s+=1
    e+=1
    if e == z:
        break
    arr[check(mystr[e])]+=1


print(res)


