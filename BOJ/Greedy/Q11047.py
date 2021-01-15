#동전 O (백준 - 그리디 유형)

n,k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

#큰 동전부터 사용하기 위해 내림차순으로 정렬
coins.sort(reverse=True)

#전체 필요한 동전의 개수
result = 0

#단위가 큰 동전으로 나누어가며 실행
for coin in coins:
        result+= k//coin
        k = k%coin

print(result)