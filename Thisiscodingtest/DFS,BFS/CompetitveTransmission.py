# 이것이 코딩테스트다
# Chapter12-17: DFS/BFS 기출 경쟁적 전염
#https://www.acmicpc.net/problem/18405

#BFS를 활용하여 문제를 해결하고 낮은 번호부터 증식하기 위해 큐에는 낮은 바이러스의 번호부터 삽입한다

from collections import deque 
n,k = map(int,input().split())
#시험관 바이러스 정보
tube=[]
for i in range(n):
    tube.append(list(map(int,input().split())))

s,tx,ty = map(int,input().split()) #x,y로 받지 않는 이유는 아래 DFS를 실행할때 x,y로 값이 덮어씌워지는 것 방지
#방향 벡터
dx =[-1,1,0,0]
dy=[0,0,-1,1]

#바이러스가 존재하는 위치 정보
virus=[]
for i in range(n):
    for j in range(n):
        if tube[i][j]!=0: #바이러스가 있다면
            virus.append((tube[i][j],0,i,j))

#바이러스 번호를 오름차순으로 정렬(낮은 번호의 바이러스부터 전염되기 위해)
virus.sort()

#BFS를 실행할 큐에 바이러스 정보 삽입
q = deque(virus)
while q:
    num,time,x,y = q.popleft()
    if time==s: #s초가 경과했다면
        break

    for i in range(4): #상하좌우에 대하여
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if tube[nx][ny]==0: #바이러스가 존재하지 않는다면
                tube[nx][ny] = num #해당 번호의 바이러스로 증식
                q.append((num,time+1,nx,ny))

#s초 후 tx,ty에 존재하는 바이러스의 번호
print(tube[tx-1][ty-1]) #(1,1)이 시작점이기 때문에
        





