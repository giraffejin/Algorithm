#부품 찾기 문제 (chapter7-02) 계수 정렬을 이용한 답안 해설

n = int(input())
count = [0]*1000001

for i in input().split():
    count[int(i)] +=1
m = int(input())
b = list(map(int,input().split()))

for i in b:
    if(count[i]==1):
        print('yes', end=' ')
    else:
        print('no', end=' ')