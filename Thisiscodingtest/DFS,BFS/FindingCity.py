#이것이 코딩테스트다
#Chapter12-15: DFS/BFS 기출 특정 거리의 도시 찾기
#https://www.acmicpc.net/problem/18352

#모든 간선의 길이가 동일하므로 BFS를 활용하여 최단 거리 값을 계산

import sys
from collections import deque

input = sys.stdin.readline
n,m,k,x = map(int,input().split())

#graph정보 구성
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] *(n+1)
#최단 거리 값을 포함할 리스트
count=[0]*(n+1)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    count[start]=0 #출발도시에서 출발도시로의 최단 거리는 0
    while queue:
        v = queue.popleft()
        #아직 방문하지 않은 인접한 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count[i] = count[v]+1
                visited[i] =True
    return count #최단 경로 거리를 계산

count = bfs(graph,x,visited)

for i in range(1,n+1):
    if count[i]==k:
        print(i, end=' ')

if count.count(k)==0: #최단 거리가 K인 도시가 존재하지 않는 경우
    print(-1)




