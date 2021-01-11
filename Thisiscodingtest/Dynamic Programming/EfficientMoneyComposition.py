#효율적인 화폐 구성 문제 (chapter8-05)

n,m = map(int,input().split())
#type: 화폐의 구성
type = []

#dp테이블 생성
d = [10001]*(10001)

for i in range(n):
    x = int(input())
    type.append(x)
    #초기 기준 화폐의 값은 1
    d[x]=1

for j in type:
    for i in range(j+1,m+1):
        if(d[i-j]!=10001):
            d[i] = min(d[i],d[i-j]+1)

if(d[m]==10001):
    print(-1)
else:
    print(d[m])