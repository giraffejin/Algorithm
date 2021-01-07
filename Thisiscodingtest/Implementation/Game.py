#게임 개발 문제 (chapter4-03)

n,m = map(int,input().split())
x,y,direction = map(int,input().split())

d = [[0]*m for _ in range(n)]

d[x][y]=1

#지도의 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#븍, 동, 남, 서
move = [(-1,0),(0,1),(1,0),(0,-1)]


#왼쪽으로 회전
def left():
    global direction #함수 밖에서 정의된 것을 함수 내에서 사용하기 위해
    direction -= 1
    if(direction==-1):
        direction = 3

count = 1
turn = 0 #북, 동, 남, 서 4가지 방향의 경우의 수

while True:
    #처음에 왼쪽 방향 회전
    left()
    
    #처음에 현재 방향 기준으로 왼쪽 방향부터 차례대로 갈 곳 정하기
    nx = x + move[direction][0]
    ny = y + move[direction][1]
    
    #회전하고 가보지 않은 칸이 있으면 이동 -> 지도 상에서 육지이고, 가보지 않은 경우
    if(d[nx][ny]==0 and array[nx][ny]==0):
        d[nx][ny]=1
        x,y = nx,ny
        count +=1
        turn = 0
        continue
     #회전한 이후 이미 가본 칸 또는 바다로 되어 있는 칸
    else:
        turn +=1

    #네 방향 모두 갈 수 없는 경우
    if turn ==4:
        nx = x - move[direction][0]
        ny = y - move[direction][1]
        if(array[nx][ny]==1):
            break
        else:
            x,y = nx,ny
        turn = 0

print(count)




