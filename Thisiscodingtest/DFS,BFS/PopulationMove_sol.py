# 이것이 코딩테스트다
# Chapter12-21: DFS/BFS 기출 인구 이동 답안 해설
# https://www.acmicpc.net/problem/16234

# 백준 사이트에서 채점하는 경우 80%구간에서 시간 초과 발생
# index 값을 통해 연합의 정보를 활용하여 visited 배열을 별도로 사용하지 않는다

from collections import deque
import sys
input = sys.stdin.readline
n,l,r = map(int,input().split())

#전체 나라의 정보 입력 받기
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy=[0,-1,0,1]
result = 0

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 정산
def process(x,y,index):
    #(x,y)의 위치와 연결된 연합 정보를 담는 리스트
    united=[]
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index #현재 연합의 정보 할당
    summary = graph[x][y] #현재 연합의 전체 인구 수
    count = 1 #현재 연합의 국가 수

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #바로 옆에 있는 나라를 확인하여
            if nx<n and ny<n and nx>=0 and ny>=0 and union[nx][ny]==-1:
                #옆에 있는 나라와 인구 차이가 L명 이상, R명 이하
                if l<=abs(graph[nx][ny] - graph[x][y]) <=r:
                    q.append((nx,ny))
                    #연합에 추가
                    union[nx][ny]=index
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx,ny))
    #연합 국가끼리 인구를 분배
    for i,j in united:
        graph[i][j] = summary//count

total_count = 0

#더이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union =[[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1: #아직 처리되지 않은 나라이면
                process(i,j,index)
                index+=1
    #모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    total_count+=1

print(total_count)
