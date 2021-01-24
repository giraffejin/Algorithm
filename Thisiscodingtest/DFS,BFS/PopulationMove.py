# 이것이 코딩테스트다
# Chapter12-21: DFS/BFS 기출 인구 이동
# https://www.acmicpc.net/problem/16234

# 백준 사이트에서 채점하는 경우 80%구간에서 시간 초과 발생

from collections import deque
n,l,r = map(int,input().split()) #국경선을 여는 기준:l이상 r이하

#인구 정보
land =[]
for i in range(n):
    land.append(list(map(int,input().split())))

#방문 국가인지 확인하기 위한 정보
visited = [[False] * (n) for _ in range(n)]

#인접한 나라 간의 국경선은 정사각형 형태로 존재
dx = [-1,1,0,0]  #상하좌우
dy = [0,0,-1,1]

#국경선을 열고 연합을 구성하는 함수(BFS를 활용)
def union(x,y):
    q =deque()
    nations =[] #연합에 속하는 국가의 위치
    q.append((x,y))#출발점을 큐에 삽입
    nations.append((x,y))
    visited[x][y] = True #해당 출발점은 방문 노드에 추가
    count = 1 #연합에 포함되는 국가의 수
    population =land[x][y] #인구 수
    while q:
        x,y = q.popleft()
        for i in range(4): #인접합 국가들 중 국경선을 열 수 있는 경우가 있는지 확인
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<n and ny<n and nx>=0 and ny>=0 and not visited[nx][ny]:
                if abs(land[x][y]-land[nx][ny])>=l and abs(land[x][y]-land[nx][ny])<=r:
                        q.append((nx,ny)) #큐에 인접한 노드 추가
                        visited[nx][ny]=True
                        count+=1 #연합에 추가
                        nations.append((nx,ny))
                        population+=land[nx][ny] #연합에 포함되는 인구 수 증가

    answer = (nations,count,population)
    return answer

#연합 국가에 따라 값 변환
def move(answer):
    nations, count, population = answer
    for nation in nations:
        a,b = nation[0],nation[1]
        land[a][b] = int(population//count)

#인구 이동 실행
def simulate():
    #인구 이동이 가능한 연합 수
    group = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                answer = union(i,j) #현재 위치에서 국경선에 따라 이동할 수 있는 경우 탐색
                if answer[1]!=1: #연합에 여러 국가가 묶이는 경우
                    move(answer) #그에 따라 값 변경
                    group+=1

    return group

#인구 이동이 필요하지 않을 때까지 이동 (묶이는 group수가 0이면 더이상 이동 불가)
results = -1
result = -1
while results!=0:
    results = simulate()
    visited = [[False] * (n) for _ in range(n)]
    result+=1

print(result)


                    




