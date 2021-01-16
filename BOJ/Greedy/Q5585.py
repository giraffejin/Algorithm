#거스름돈 (백준 - 그리디 유형)

#타로가 지불할 돈
cost = int(input())
#잔돈
n = 1000-cost

#화폐의 종류
coins = [500,100,50,10,5,1]
i = 0
result = 0

while n>0:
    result += (n//coins[i])
    n = n % coins[i]
    i+=1

print(result)