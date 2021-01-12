#미래 도시 문제 (chapter9-02)

n,m = map(int,input().split())
INF = 1e9
#모든 노드에서 각 지점까지의 거리를 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 오는 값은 0으로
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for i in range(m):
    a,b = map(int,input().split())
    #도로에 대해 양방향으로 이동 가능하기 때문에
    graph[a][b]=1
    graph[b][a]=1

#플로이드 워셜 알고리즘 수행
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

#거쳐갈 노드 k와 도착할 노드 x
x,k = map(int,input().split())

#결과 출력
if graph[1][k]+graph[k][x] >=INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])

