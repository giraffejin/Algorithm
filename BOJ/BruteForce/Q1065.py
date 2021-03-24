# 한수 (백준 - 브루트포스 유형)
# https://www.acmicpc.net/problem/1065
# 각 자리수가 등차수열을 이루는 수의 갯수

n = int(input())
count = 0 #한 수의 갯수 세기

for i in range(1,n+1):
    if i<=99: #한 자리수와 두 자리 수는 모두 등차수열 구성
        count+=1

    elif i<1000: # 세 자리 수인 경우 등차인지 확인
        i1 = i//100
        i2 = (i%100)//10
        i3 = i%10
        if (i1+i3)==2*i2:
            count+=1

print(count)