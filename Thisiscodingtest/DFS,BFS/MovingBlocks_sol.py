# 이것이 코딩테스트다
# Chapter 13-22: DFS/BFS 기출 블록 이동하기 답안 해설
# https://programmers.co.kr/learn/courses/30/lessons/60063

#간선의 비용이 모두 1로 동일하므로 BFS를 이용해 최적의 해를 구할 수 있다
#위치 정보를 튜플로 관리하고 로봇의 상태를 집합 자료형으로 관리한다

from collections import deque

def get_nex_pos(pos,board):
    next_pos=[] #반환 결과(이동 가능한 위치들)
    pos = list(pos) #현재 위치 정보를 리스트로 변환(집합->리스트)
    pos1_x,pos1_y,pos2_x,pos2_y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    #상하좌우로 이동하는 경우에 대해서 처리
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
        #이동하고자 하는 두 칸이 모두 비어있다면
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
            next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
    
    #현재 로봇이 가로로 놓여 있는 경우
    if pos1_x ==pos2_x:
        for i in [-1,1]: #위쪽으로 회전하거나 아래쪽으로 회전
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: #위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x +i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x +i, pos2_y)})
    
    #현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 위쪽으로 회전하거나 아래쪽으로 회전
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:  # 왼쪽 혹은 오른쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    #현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    #맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board =[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]

    #너비 우선 탐색 실행
    q = deque()
    visited=[]
    pos = {(1,1),(1,2)} #시작 위치 설정
    q.append((pos,0))
    visited.append(pos)
    while q:
        pos,cost = q.popleft()
        #(n,n)위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n,n) in pos:
            return cost
        #현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_nex_pos(pos,new_board):
            #아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)

    return 0
