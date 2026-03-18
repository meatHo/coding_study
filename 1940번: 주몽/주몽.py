#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1940                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1940                           #+#        #+#      #+#     #
#    Solved: 2026/03/18 14:03:48 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
jip = set(arr)
res = 0
for i in range(n):
    if m-arr[i] in jip and m-arr[i]!=arr[i]: # m=10 이고 5이면 같은거임.
        res+=1
print(res//2)

#========================================


import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
s=sum=res = 0
e=n-1

while s<e:
    sum = arr[s]+arr[e]
    if sum > m:
        e-=1
    elif sum < m:
        s+=1
    else:
        res+=1
        e-=1
        s+=1
print(res)

#========================================
import sys
from collections import *

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
res = 0
visited = set()

for x in arr:
    target = m - x
    if target in visited:
        res += 1
    else:
        visited.add(x) # 아직 짝을 못 찾았으면 방문 목록에 추가

print(res) # 이 방식은 중복이 없으므로 바로 출력