# 이것이 코딩테스트다
# Chapter13-19: DFS/BFS 기출 연산자 끼워 넣기 답안 해설
#https://www.acmicpc.net/problem/14888

# 모든 연산자 순열의 경우를 구하는 과정으로 깊이 우선 탐색(DFS)를 활용

n = int(input())
data = list(map(int,input().split()))
#더하기, 빼기, 곱하기, 나누기의 연산자 개수
add,sub,mul,div = map(int,input().split())

#최솟값과 최대값 초기화
max_value = -1e9
min_value = 1e9

#깊이 우선 탐색
def dfs(i,now):
    global min_value,max_value,add,sub,mul,div

    #모든 연산자를 다 수행한 경우, 최솟값과 최댓값 업데이트
    if i==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)

    else: #각 연산자에 대해 재귀적으로 수행

        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1

        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1

        if mul>0:
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1

        if div>0:
            div-=1
            dfs(i+1,int(now/data[i]))
            div+=1

dfs(1,data[0])

print(max_value)
print(min_value)
