# 이것이 코딩테스트다
# Chapter16-31: 다이나믹 프로그래밍 기출 금광

t = int(input()) #테스트 케이스 갯수

#채굴 함수
def mining(a,n,m):
    d=[[0]*m for _ in range(n)]
    for i in range(n):
        d[i][0] = a[i][0] #dp테이블의 초기값 설정

    for j in range(1,m):
        for i in range(0, n):
            if i-1>=0:
                d[i][j] = max(d[i-1][j-1]+a[i][j], d[i][j]) #왼쪽 위에서 값이 올때
            if i>=0:
                d[i][j] = max(d[i][j-1]+a[i][j],d[i][j]) #왼쪽에서 올때
            if i+1<n:
                d[i][j] = max(d[i+1][j-1]+a[i][j], d[i][j]) #왼쪽 아래에서 올 때

    result = 0
    for i in range(n):
        result = max(result,d[i][m-1])

    return result

results=[]
for i in range(t): #테스트 케이스 입력 받기
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    a = []
    for i in range(n): #금광 위치 정보 받기
        x = i * m
        a.append(array[x:x + m])

    results.append((mining(a,n,m)))

#테스트 케이스 마다 금의 최대 크기 출력
for i in results:
    print(i)


