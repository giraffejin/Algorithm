#전보 (chapter9-03)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for i in range(n+1)]
distance =[INF]*(n+1)

#그래프 정보를 입력받음
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

#다익스트라 알고리즘 수행
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    #큐가 비어있지 않다면
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

#c지점을 시작점으로 다익스트라 알고리즘 실행
dijkstra(c)

#메세지를 받는 도시의 총 개수와 총 걸리는 시간 구하기
count = 0
spendtime = 0
for i in range(1,n+1):
    if (distance[i]!=INF):
        count +=1
        spendtime = max(spendtime,distance[i])

#출발지점의 개수는 count에서 제외, 거리가 INF는 아니지만 0이므로
count = count-1
print(count,spendtime)



