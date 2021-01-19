#이것이 코딩테스트다
#Chapter12-11: 구현 기출 뱀

n = int(input()) #보드의 크기
#보드 전체를 0으로 초기화
board =[[0]*(n+1) for _ in range(n+1)] #시작점이 (1,1)이기 때문에

x,y = 1,1 #초기 출발 위치
#회전 정보를 포함하는 리스트
rotation =[]
direction = 1 #초기 출발 방향은 오른쪽

k = int(input()) #사과의 개수
for i in range(k):
    a,b = map(int,input().split())
    board[a][b]=1 #보드 판 위에 사과를 올리기

l = int(input()) #회전 방향의 개수
for i in range(l):
    t,d = input().split()
    rotation.append((t,d))
    
#북,동,남,서 로 이동
move =[(-1,0),(0,1),(1,0),(0,-1)]

#회전 함수
def rotate(d):
    global direction
    if d=='L':
        direction -=1
        if (direction==-1):
            direction=3
    if d=='D':
        direction+=1
        if(direction==4):
            direction=0

#게임이 진행되는 시간
time = 0
tail =[]
board[x][y] = 2 #뱀의 몸이 위치하는 정보를 2로 표현
i = 0
#게임을 시작
while True:

    nx = x+move[direction][0]
    ny = y+move[direction][1]
    #이동한 값이 벗어나거나 몸통을 만나면 정지
    if (nx<1 or nx>n or ny<1 or ny>n):
        time+=1
        break
    if (board[nx][ny]==2):
        time+=1
        break

    tail.append((x, y))  # 꼬리값 넣어주기
    #이동한 칸에 사과가 있는지 확인
    if (board[nx][ny]==1):
        board[nx][ny] = 0 #사과 없애기
        
    elif(board[nx][ny]!=1): #이동한 칸에 사과가 없는 경우
            a = tail[0][0]
            b = tail[0][1]
            del (tail[0])
            board[a][b] = 0 #몸통이 빠져 나갔으므로 다시 0으로

    board[nx][ny] = 2  # 이동한 칸에도 뱀의 몸이 위치
    x, y = nx, ny
    time += 1
    for i in range(l):
        if int(rotation[i][0]) ==time:
            rotate(rotation[i][1])
            i+=1

    continue

print(time)












