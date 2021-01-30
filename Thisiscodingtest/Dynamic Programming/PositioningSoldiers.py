# 이것이 코딩테스트다
# Chapter16-34: 다이나믹 프로그래밍 기출 병사 배치하기
# https://www.acmicpc.net/problem/18353

# LIS(가장 긴 증가하는 부분 순열)의 개념을 활용하여 문제를 해결한다
# LIS를 구현하기 위해 DP를 활용
# 문제는 가장 긴 감소하는 부분 순열로 입력되는 순열을 뒤집어 활용

n = int(input())
fight = list(map(int,input().split()))
fight.reverse()
d =[1]*(n) #dp테이블 초기화

for i in range(1,n):
    for j in range(i):
        if fight[j]<fight[i]:
            d[i] = max(d[i],d[j]+1)

#열외를 시켜야 하는 병사의 수
print(n-max(d))