# 이것이 코딩테스트다
# Chapter16-33: 다이나믹 프로그래밍 기출 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input()) #상담 할 수 있는 기간
time =[] #상담에 걸리는 시간
price = [] #상담할 때 받을 수 있는 금액

for i in range(n):
    t,p = map(int,input().split())
    time.append(t)
    price.append(p)

d=[0]*(n+1) #dp테이블 초기화
result = 0

for i in range(n-1,-1,-1):
    if (i+time[i])<=n: #상담이 가능하다면
        d[i] = max(price[i]+d[i+time[i]], result) #최고 이익을 계산한다
        result = d[i]
    else:
        d[i] = result

print(result)
