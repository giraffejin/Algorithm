#ATM (백준 - 그리디 유형)

#사람의 수
n = int(input())
#각자 돈을 인출하는데 걸리는 시간
time = list(map(int,input().split()))
result = 0 #전체 소요 시간

#인출시간을 오름차순으로 정렬하여 인출하는데 적은 시간이 걸리는 사람부터 우선적으로 실행
time.sort()
for i in range(n):
    result += (n-i)*time[i]

print(result)