# 이것이 코딩테스트다
# Chapter13-20: DFS/BFS 기출 감시 피하기
#https://www.acmicpc.net/problem/18428

#장애물을 설치할 수 있는 모든 조합에 대하여 학생이 감지되는지를 확인
#각 선생님들의 위치에서 상,하,좌,우로 학생을 감지하는 함수 필요

from itertools import combinations
import copy

n = int(input())
hallway = []
blank = []
teachers = []  # 선생님이 있는 위치

# 초기의 복도
for i in range(n):
    hallway.append(list(input().split()))
    for j in range(n):  # 장애물을 설치할 수 있는 빈칸 찾기
        if hallway[i][j] == 'X':
            blank.append((i, j))
        if hallway[i][j] == 'T':
            teachers.append((i, j))

# 원래 복도
original = copy.deepcopy(hallway)
# 장애물 설치 경우의 수
candidates = list(combinations(blank, 3))

# 복도에 장애물 설치하기
def build_obstacle(candidate):
    for i in candidate:
        x, y = i[0], i[1]
        hallway[x][y] = 'O'

# 감시 함수
def detection(x, y,direction):  # 특정한 방향으로 x,y에서 감시
    if direction==0: #상하좌우 순
        while x>=0:
            if hallway[x][y]=='S': #학생을 발견한 경우
                return True
            if hallway[x][y]=='O': #장애물로 막힌 경우
                return False
            x-=1 #해당 방향으로 더 나아가서 감시

    if direction==1: #상하좌우 순
        while x<n:
            if hallway[x][y]=='S':
                return True
            if hallway[x][y]=='O':
                return False
            x+=1

    if direction==2: #상하좌우 순
        while y>=0:
            if hallway[x][y]=='S':
                return True
            if hallway[x][y]=='O':
                return False
            y-=1

    if direction==3: #상하좌우 순
        while y<n:
            if hallway[x][y]=='S':
                return True
            if hallway[x][y]=='O':
                return False
            y+=1
    return False

def simulate():
    for teacher in teachers:
        x, y = teacher[0], teacher[1]
        for i in range(4):  # 상하좌우로 검사
            if detection(x,y,i):
                return True
        return False

find = False #학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 각 장애물을 설치하는 경우에 따라 적발되는 경우가 있는지 확인
for candidate in candidates:
    build_obstacle(candidate)  # 장애물을 설치
    if not simulate():
        find = True
        break

    hallway = copy.deepcopy(original)

if find:
    print('YES')
else:
    print('NO')
