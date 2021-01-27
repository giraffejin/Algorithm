# 이것이 코딩테스트다
# Chapter15-29: 이진 탐색 기출 공유기 설치 답안 해설
# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline
n,c = map(int,input().split())
homes =[]
#집 위치 정보 받기
for i in range(n):
    homes.append(int(input()))

homes.sort() #이진 탐색을 위해 집의 위치를 정렬

start = homes[1]-homes[0] 
end =  homes[-1]-homes[0]
result = 0

while start<=end:
    mid = (start+end)//2 #mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    count = 1
    home = homes[0]
    
    #해당 간격으로 공유기를 설치해본다
    for i in range(1,n):
        if homes[i]>=home+mid:
            count+=1
            home = homes[i]

    if count>=c: #c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid+1
        result = mid #최적의 결과를 저장
        
    else: #c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid-1

print(result)

        




