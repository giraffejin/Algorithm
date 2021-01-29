# 이것이 코딩테스트다
# Chapter16-32: 다이나믹 프로그래밍 기출 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline
n = int(input()) #삼각형의 크기
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))


for i in range(1,n):
    for j in range(i+1):
        if j-1<0: 
            left = 0
        else: #왼쪽 대각선에서 올 수 있는 값이 있는 경우
            left = dp[i-1][j-1]

        if j>=i:
            right = 0
        else:
            right = dp[i-1][j] #오른쪽 대각선에서 올 수 있는 값이 있는 경우
        dp[i][j] = dp[i][j] + max(left,right) #합이 최대가 되는 값 저장

#최대가 되는 경로에 있는 수의 합
result = max(dp[n-1])
print(result)
