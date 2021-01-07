#숫자 카드 게임(chapter3-03)

N,M = map(int,input().split())
card = []

for _ in range(N):
    card.append(list(map(int, input().split())))

answer =[]
for i in range(N):
    card[i].sort()
    answer.append(card[i][0])

print(max(answer))

result = 0
for i in range(N):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)