#1로 만들기 문제 (chapter8-02)

x = int(input())
#결과를 저장하기 위한 dp테이블
d = [0]*30001

#bottomup 방식으로 구현
for i in range(2,x+1):
    d[i] = d[i-1]+1
    if(i%2==0):
        d[i] = min(d[i],d[i//2]+1)
    if(i%3==0):
        d[i] = min(d[i],d[i//3]+1)
    if(i%5==0):
        d[i] = min(d[i],d[i//5]+1)

print(d[x])




