#이것이 코딩테스트다
#Chapter12-13: 구현 기출 치킨 배달
#https://www.acmicpc.net/problem/15686
#해당 코드로 구현시 타임 아웃은 발생하지 않으나 수행시간이 길다

from itertools import combinations
n,m = map(int,input().split())
home =[] #집의 위치
chicken=[]#치킨집의 위치
INF = 1e9 #초기값은 무한대로
#도시의 정보
for i in range(n):
    city = list(map(int,input().split()))
    for j in range(n):
        if city[j]==1:
            home.append((i,j))
        elif city[j]==2:
            chicken.append((i,j))

#치킨집이 최대 m개일때 가능한 조합
comb = list(combinations(chicken,m))
result = INF
for case in comb: #가능한 모든 치킨집의 조합에 대하여
    city_distance = 0 #초기의 도시의 치킨 거리를 0
    for h in home: #각 집에 대한 치킨 거리 구하기
        home_distance = INF
        for c in case: #조합의 개별 치킨집까지의 거리 계산
            distance = abs(h[0]-c[0]) + abs(h[1]-c[1])
            home_distance = min(home_distance,distance)

        city_distance+=home_distance

    result = min(result,city_distance)

print(result)

