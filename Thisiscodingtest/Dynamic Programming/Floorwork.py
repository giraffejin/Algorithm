#바닥 공사 문제 (chapter8-04)

n = int(input())
#dp테이블 초기화
d = [0]*1001

#다이나믹 프로그래밍 진행
d[1]=1
d[2]=3

for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2]*2) % 796796

print(d[n])