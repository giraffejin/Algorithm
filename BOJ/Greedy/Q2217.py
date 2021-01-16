#로프 (백준 - 그리디 유형)
import sys
input = sys.stdin.readline

#로프의 수
n = int(input())
#각 로프의 버틸 수 있는 최대 중량
rope =[]
for i in range(n):
    rope.append(int(input()))

#오름차순으로 정렬
rope.sort()

#최대 중량 값 비교
limit =[]
for i in range(n):
    limit.append((n-i)*rope[i])

print(max(limit))