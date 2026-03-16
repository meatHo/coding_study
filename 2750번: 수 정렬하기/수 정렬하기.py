#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2750                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatHo <boj.kr/u/meatHo>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2750                           #+#        #+#      #+#     #
#    Solved: 2026/03/11 22:56:34 by meatHo        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import *
import sys

input = int(sys.stdin.readline().strip())
arr = []
for i in range(input):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
for i in range(input):
    print(arr[i])