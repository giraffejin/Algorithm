#이것이 코딩테스트다
#Chapter12-11: 구현 기출 뱀 답안 해설
#기존에 작성한 코드와 비교하여 수행 시간이 훨씬 단축됨

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
data = [[0] * (n + 1) for _ in range(n + 1)]  #맵 정보
info =[] #방향 회전 정보

#맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for i in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽 보고 있으므로 (동,남,서,북)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 회전 함수
def turn(direction,c):
    if c=='L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1, 1  #뱀의 머리 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y+ dy[direction]
        #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx and nx<=n and ny<=n and ny>=1 and data[nx][ny]!=2:
            #사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py]=0
            #사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx,ny))
                
        #벽이나 뱀의 몸통과 부딪히면
        else:
            time+=1
            break
        x,y = nx,ny #다음 위치로 머리를 이동
        time+=1
        if index<l and time==info[index][0]: #회전할 시간인 경우 회전
            direction = turn(direction,info[index][1])
            index+=1

    return time

print(simulate())


