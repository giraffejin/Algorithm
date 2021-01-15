#회의실 배정 (백준 - 그리디 유형)

import sys
input = sys.stdin.readline
n = int(input())
time =[] #회의 시간 정보를 담을 리스트
meeting = 0 #전체 가능한 회의 최대 개수

#회의 정보 입력 받기
for i in range(n):
    start,end = map(int,input().split())
    time.append((start,end))

#시작 시간이 작은 순서대로 정렬
time.sort(key= lambda x:x[0])
#끝나는 시간이 작은 순서대로 정렬
time.sort(key=lambda x:x[1])

#회의가 끝나는 시간이 시작 시간보다 작으면 회의 가능
end = 0
for i in range(n):
    start = time[i][0]
    if start>=end:
        meeting+=1
        end = time[i][1]

print(meeting)
