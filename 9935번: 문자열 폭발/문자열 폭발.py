#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9935                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: meatho <boj.kr/u/meatho>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9935                           #+#        #+#      #+#     #
#    Solved: 2026/04/08 21:45:15 by meatho        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import *

str = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

len_bomb = len(bomb)

st = list()
for s in str:
    st.append(s)
    if len(st)>=len_bomb and st[-len_bomb:]==bomb:
        for _ in range(len_bomb):
            st.pop()

if st:
    for s in st:
        print(s, end="")
else:
    print("FRULA")
