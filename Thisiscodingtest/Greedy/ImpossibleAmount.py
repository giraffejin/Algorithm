#그리디 기출 - 만들 수 없는 금액 (chapter11-04)

n = int(input())
coins = list(map(int,input().split()))
#화폐단위를 먼저 정렬
coins.sort()

result = 1 #만들 수 없는 최소값

#정렬된 화폐의 값을 하나씩 더해가며 만들 수 없는 최소값을 갱신
for coin in coins:
    if result<coin:
        break
    result +=coin

print(result)