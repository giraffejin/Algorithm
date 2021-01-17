#수 정렬하기 (백준 - 구현 유형)

import sys
input = sys.stdin.readline

n = int(input())
num = list(int(input())for i in range(n))
num.sort()

for i in num:
    print(i)