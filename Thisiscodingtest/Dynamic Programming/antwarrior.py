#개미 전사 문제 (chapter8-03)

n = int(input())
a = list(map(int,input().split()))
k = len(a)
d = [0]*(101)
#i번째 칸을 약탈했을 때의 최대값을 d[i]에 저장
d[1] = a[0]
d[2] = max(d[1],a[1])

#다이나믹 프로그래밍(bottom up)
#점화식 a(i) = max(a(i-1), a(i-2)+i의 값)

for i in range(3,k+1):
    d[i] = max(d[i-1],d[i-2]+a[i-1])

print(d[k])
