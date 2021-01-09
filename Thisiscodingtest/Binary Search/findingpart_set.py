#부품 찾기 문제 (chapter7-02) 집합 자료형을 이용한 답안 해설

n = int(input())
#가게에 있는 전체 부품 번호를 집합 자료형에 기록
a = set(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

for i in b:
    if i in a:
        print('yes', end=' ')
    else:
        print('no', end=' ')
