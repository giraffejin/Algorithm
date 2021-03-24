# 날짜 계산(백준 - 구현 유형)
# https://www.acmicpc.net/problem/1476

e,s,m = map(int,input().split())
year =1

while True:
    if (year-e)%15 ==0 and (year-s)%28==0 and (year-m)%19==0:
        break
    else:
        year+=1

print(year)