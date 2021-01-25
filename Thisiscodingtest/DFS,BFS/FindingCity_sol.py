#이것이 코딩테스트다
#Chapter13-15: DFS/BFS 기출 특정 거리의 도시 찾기 답안 해설
#https://www.acmicpc.net/problem/18352

#별도의 방문 노드를 저장하는 visited 배열을 사용하지 않고 처음의 최단 거리를 -1로 초기화

from collections import deque

n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화 
distance=[-1]*(n+1)
distance[x]=0 #처음 출발 노드는 0

#너비 우선 탐색 실행
q = deque()
q.append(x)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1: #방문하지 않은 노드
            distance[next_node] = distance[now]+1
            q.append(next_node)

#최단 거리가 K인 도시 번호 오름차순으로 출력
check = False #최단 거리가 K인 도시가 존재하는지 확인
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True

if check==False:
    print(-1)

