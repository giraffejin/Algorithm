#이것이 코딩테스트다
#Chapter13-16: DFS/BFS 기출 연구소 답안 해설
#https://www.acmicpc.net/problem/14502

#벽을 세워 안전 영역의 크기를 계산하는 과정과 바이러스가 사방으로 퍼지도록 하는 것을 깊이 우선 탐색(DFS)를 적용하여 구현

n,m = map(int,input().split())
data=[]
temp=[[0]*m for _ in range(n)] #벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int,input().split())))

#4가지 이동 방향에 대한 리스트
dx=[-1,0,1,0]
dy=[0,1,0,-1]

result = 0

#깊이 우선 탐색을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        #상하좌우 중에서 바이러스가 퍼질 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2 #해당 위치에 바이러스 배치하고 재귀적으로 수행
                virus(nx,ny)

#안전영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

#깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    #울타리가 3개 설치된 경우
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        #안전 영역의 최대값 계산
        result = max(result,get_score())
        return

    #빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)

