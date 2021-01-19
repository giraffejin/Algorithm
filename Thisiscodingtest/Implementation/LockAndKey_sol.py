#구현 기출 문제 - 자물쇠와 열쇠 (chapter12-10) 답안 해설

#자물쇠의 크기와 열쇠의 크기가 20x20보다 작기때문에 완전 탐색을 이용하여 열쇠를 이동이나 회전시켜서 자물쇠에 끼워보는 작업을 전부 시도
#완전 탐색을 수월하게 하기 위해 자물쇠 리스트의 크기를 3배 이상으로 변경하여 활용함
#새로 만든 자물쇠 리스트의 정중앙에 기존의 자물쇠를 위치한다

#2차원 리스트 90도 회전하는 함수
def rotate(a):
    n = len(a)
    m = len(a[0])
    result =[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
    return result

#자물쇠가 풀리는지 확인하는 함수(자물쇠에 해당하는 부분이 모두 1로 채워져 있는지 확인)
#자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length,2*lock_length):
        for k in range(lock_length,2*lock_length):
            if new_lock[i][k]==1:
                return True

    return False

def solution(key,lock):
    n = len(lock)
    m = len(key)
    #자물쇠의 크기를 기존 3배로 변환
    new_lock = [[0]*(3*n) for _ in range(3*n)]
    #확대한 자물쇠의 중앙에 원래 자물쇠를 위치하기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    
    #회전이 가능한 4가지의 방향에 대해 확인
    for rotation in range(4):
        #key를 회전
        rotate(key)
        for i in range(2*n):
            for j in range(2*n):
                #자물쇠에 열쇠를 넣어 값 구하기(자물쇠에 열쇠를 끼워 넣기)
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b] += key[a][b]

                #자물쇠의 합이 1인지 확인(새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사)
                if check(new_lock)==True:
                    return True

                #자물쇠를 다시 빼기
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b]-=key[a][b]
    return False

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key,lock))



